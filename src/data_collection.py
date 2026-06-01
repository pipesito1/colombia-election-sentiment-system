import requests
import pandas as pd
from bs4 import BeautifulSoup

urls = [
    "https://www.eltiempo.com/rss/politica.xml",
    "https://www.semana.com/rss/politica/",
    "https://www.portafolio.co/rss/politica",
    "https://www.bluradio.com/rss/politica.xml",
    "https://www.rcnradio.com/rss/politica.xml",
    "https://www.lafm.com.co/rss/politica"
]

news = []

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "xml")

        for item in soup.find_all("item"):
            news.append({
                "text": item.title.text,
                "date": item.pubDate.text if item.pubDate else None,
                "source": url
            })

    except Exception as e:
        print(f"❌ Error con {url}: {e}")
        continue

df = pd.DataFrame(news)

# 🔥 eliminar duplicados
df = df.drop_duplicates(subset=["text"])

df.to_csv("data/news_colombia.csv", index=False)

print("✅ Noticias guardadas")
print(df.head())