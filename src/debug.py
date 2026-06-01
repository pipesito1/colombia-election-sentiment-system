import pandas as pd

df = pd.read_csv("data/news_colombia.csv")

print("🔍 Buscando 'abelardo'...\n")

found = False

for text in df["text"]:
    if "abelardo" in text.lower():
        print(text)
        found = True

if not found:
    print("❌ No hay menciones de Abelardo en los datos")