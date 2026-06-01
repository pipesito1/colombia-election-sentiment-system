from transformers import pipeline

#modelo en español
classifier = pipeline("sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment"
            )

def predict(text):
    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    # 🔥 convertir estrellas a sentimiento
    if "1" in label or "2" in label:
        sentiment = "negative"
    elif "3" in label:
        sentiment = "neutral"
    else:
        sentiment = "positive"

    return {
        "sentiment": sentiment,
        "confidence": float(score)
    }