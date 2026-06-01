import joblib
from src.preprocessing import clean_text

#cargar modelo y vectorizador
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict(text):
    clean = clean_text(text)
    X = vectorizer.transform([clean])

    prediction = model.predict(X)[0]
    proba = model.predict_proba(X).max()

    # 🔥 REGLAS INTELIGENTES
    text_lower = clean.lower()

    negative_keywords = ["crisis", "denuncia", "corrupción", "ataque", "problema"]
    positive_keywords = ["avance", "logro", "éxito", "mejora", "crecimiento"]

    if any(word in text_lower for word in negative_keywords):
        prediction = "negative"
    elif any(word in text_lower for word in positive_keywords):
        prediction = "positive"

    return {
        "sentiment": prediction,
        "confidence": float(proba)
    }