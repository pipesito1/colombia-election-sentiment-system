import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sentimiento Político", layout="wide")

st.title("📊 Análisis de Sentimiento Político en Colombia")

df = pd.read_csv("data/candidate_sentiment.csv")

# =========================
# 🧠 SCORE
# =========================
sentiment_map = {"positive": 1, "neutral": 0, "negative": -1}
df["score"] = df["sentiment"].map(sentiment_map)

# =========================
# 📌 KPIs GENERALES
# =========================
st.subheader("📌 Resumen general")

col1, col2, col3 = st.columns(3)

col1.metric("Total registros", len(df))
col2.metric("Candidatos", df["candidate"].nunique())
col3.metric("Confianza promedio", round(df["confidence"].mean(), 2))

# =========================
# 🏆 RANKING + GANADOR
# =========================
st.subheader("🏆 Ranking de percepción")

ranking = df.groupby("candidate")["score"].mean().sort_values(ascending=False)

# 🔥 GANADOR (WOW FACTOR)
winner = ranking.index[0]
st.success(f"🏆 Candidato con mejor percepción: {winner}")

col1, col2, col3 = st.columns(3)

for i, (candidate, value) in enumerate(ranking.items()):
    if i == 0:
        col1.metric(f"🥇 {candidate}", f"{value:.2f}")
    elif i == 1:
        col2.metric(f"🥈 {candidate}", f"{value:.2f}")
    elif i == 2:
        col3.metric(f"🥉 {candidate}", f"{value:.2f}")

# =========================
# 🧠 INSIGHTS AUTOMÁTICOS
# =========================
st.subheader("🧠 Insights automáticos")

for candidate, score in ranking.items():
    if score > 0.2:
        st.write(f"📈 {candidate} tiene percepción positiva en medios")
    elif score < -0.2:
        st.write(f"📉 {candidate} tiene percepción negativa")
    else:
        st.write(f"➖ {candidate} tiene percepción neutral")

# =========================
# 🎯 FILTRO GLOBAL
# =========================
st.subheader("🎯 Filtrar")

candidate_selected = st.radio(
    "Selecciona candidato",
    ["Todos"] + list(df["candidate"].unique())
)

if candidate_selected != "Todos":
    df = df[df["candidate"] == candidate_selected]

# =========================
# 📊 DISTRIBUCIÓN
# =========================
st.subheader("📊 Distribución de sentimiento")

summary = df.groupby("candidate")["sentiment"].value_counts(normalize=True).unstack().fillna(0)

st.bar_chart(summary, use_container_width=True)

# =========================
# 📈 EVOLUCIÓN
# =========================
st.subheader("📈 Evolución temporal")

df["date"] = pd.to_datetime(df["date"], errors="coerce")

trend = df.groupby("date")["sentiment"].value_counts(normalize=True).unstack().fillna(0)

trend = trend.sort_index()

st.line_chart(trend, use_container_width=True)

# =========================
# 🔥 TOP NOTICIAS
# =========================
st.subheader("🔥 Noticias más influyentes")

top_news = df.sort_values("confidence", ascending=False).head(5)

st.dataframe(top_news[["candidate", "text", "sentiment", "confidence"]])

# =========================
# 📋 DATOS
# =========================
st.subheader("📋 Datos")

st.dataframe(df)