import re
import unicodedata

def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = remove_accents(text)  # 🔥 clave

    # eliminar URLs
    text = re.sub(r"http\S+", "", text)

    # mantener letras y espacios
    text = re.sub(r"[^a-zñ\s]", "", text)

    # limpiar espacios
    text = re.sub(r"\s+", " ", text).strip()

    return text