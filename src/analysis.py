import pandas as pd
from src.inference_transformer import predict
from src.preprocessing import clean_text
import matplotlib.pyplot as plt

# =========================
# 🎯 CANDIDATOS
# =========================

candidates = {
    "cepeda": ["cepeda", "ivan cepeda"],
    "paloma": ["paloma", "paloma valencia"],
    "abelardo": ["abelardo", "espriella", "de la espriella"]
}

# =========================
# 🔍 CONTEXTO
# =========================

keywords_context = ["eleccion", "voto", "candidato", "campana", "encuesta"]

# =========================
# 📥 DATA
# =========================

df = pd.read_csv("data/news_colombia.csv")

results = []

# =========================
# 🧠 ANÁLISIS
# =========================

for _, row in df.iterrows():
    text = row["text"]
    date = row.get("date", None)
    source = row.get("source", "unknown")

    text_clean = clean_text(text)

    # filtro longitud
    if len(text_clean.split()) < 5:
        continue

    # filtro inteligente
    if not any(word in text_clean for word in keywords_context) and \
       not any(word in text_clean for words in candidates.values() for word in words):
        continue

    for candidate, keywords in candidates.items():
        if any(f" {word} " in f" {text_clean} " for word in keywords):

            # 🔥 usar texto limpio
            pred = predict(text_clean)

            results.append({
                "candidate": candidate,
                "text": text,
                "date": date,
                "source": source,
                "sentiment": pred["sentiment"],
                "confidence": pred["confidence"]
            })

# =========================
# 📊 DATAFRAME FINAL
# =========================

df_results = pd.DataFrame(results)

if df_results.empty:
    print("⚠️ No hay menciones de candidatos en las noticias actuales")
    exit()

df_results.to_csv("data/candidate_sentiment.csv", index=False)

# =========================
# 📊 RESUMEN GENERAL
# =========================

summary = df_results.groupby("candidate")["sentiment"] \
    .value_counts(normalize=True).unstack().fillna(0)

summary.plot(kind="bar", figsize=(8,5))
plt.title("Distribución de Sentimiento por Candidato")
plt.xlabel("Candidato")
plt.ylabel("Proporción")
plt.xticks(rotation=0)
plt.legend(title="Sentimiento")
plt.show()

# =========================
# 📈 EVOLUCIÓN TEMPORAL
# =========================

df_results["date"] = pd.to_datetime(df_results["date"], errors="coerce")

timeline = (
    df_results.groupby(["date", "candidate"])["sentiment"]
    .value_counts(normalize=True)
    .unstack()
    .fillna(0)
    .reset_index()
)

# 🔥 ordenar por fecha (clave)
timeline = timeline.sort_values("date")

print("\n📈 Evolución temporal:\n")
print(timeline.head())

# =========================
# 🧠 SCORE (UNA SOLA MÉTRICA)
# =========================

sentiment_map = {
    "positive": 1,
    "neutral": 0,
    "negative": -1
}

df_results["sentiment_score"] = df_results["sentiment"].map(sentiment_map)

favorability = df_results.groupby("candidate")["sentiment_score"] \
    .mean().sort_values(ascending=False)

print("\n📊 Índice de favorabilidad:\n")
print(favorability)

# =========================
# 🔥 TOP NOTICIAS
# =========================

print("\n🔥 NOTICIAS MÁS INFLUYENTES:\n")

top_news = df_results.sort_values("confidence", ascending=False).head(5)

print(top_news[["candidate", "text", "sentiment", "confidence"]])

# =========================
# 📉 TENDENCIA POR CANDIDATO
# =========================

for candidate in df_results["candidate"].unique():
    subset = df_results[df_results["candidate"] == candidate]

    trend = subset.groupby("date")["sentiment"] \
        .value_counts(normalize=True).unstack().fillna(0)

    trend = trend.sort_index()

    trend.plot(title=f"Evolución sentimiento - {candidate}")
    plt.show()

# =========================
# 🧠 INSIGHTS AUTOMÁTICOS
# =========================

print("\n🧠 INSIGHTS AUTOMÁTICOS:\n")

for candidate, score in favorability.items():

    if score > 0.2:
        print(f"📈 {candidate} tiene percepción POSITIVA en medios")
    elif score < -0.2:
        print(f"📉 {candidate} tiene percepción NEGATIVA en medios")
    else:
        print(f"➖ {candidate} tiene percepción NEUTRAL en medios")

# =========================
# 📊 PRINT FINAL
# =========================

print("\n📊 Resumen:\n")
print(summary)