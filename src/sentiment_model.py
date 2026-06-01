import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

from src.preprocessing import clean_text

# cargar datos
df = pd.read_csv("data/Twitter_Data.csv")

# mapear etiquetas
df["sentiment"] = df["category"].map({
    -1: "negative",
     0: "neutral",
     1: "positive"
})

# limpiar datos
df = df.dropna(subset=["sentiment"])
df = df.dropna(subset=["clean_text"])
df = df.rename(columns={"clean_text": "text"})

# aplicar limpieza
df["clean"] = df["text"].apply(clean_text)

# features y target
X = df["clean"]
y = df["sentiment"]

# 🔥 NUEVO: mejor vectorización
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2)
)

X_vec = vectorizer.fit_transform(X)

# split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 🔥 EVALUACIÓN (ESTO ES LO IMPORTANTE)
y_pred = model.predict(X_test)

print("\n📊 Evaluación del modelo:\n")
print(classification_report(y_test, y_pred))

# guardar modelo
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\n✅ Modelo entrenado y guardado")