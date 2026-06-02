# 🇨🇴 Colombia Election Sentiment System

An end-to-end data science project that analyzes political sentiment in Colombia using real-time news data, Natural Language Processing (NLP), and interactive dashboards.

---

## 🚀 Overview

This project collects political news from major Colombian media sources, processes the text using NLP models, and generates insights about public sentiment toward political candidates.

The system transforms raw news data into actionable insights through:

- 📥 Data collection (RSS scraping)
- 🧠 Sentiment analysis (Transformer-based model)
- 📊 Data processing & feature engineering
- 📈 Interactive dashboard visualization (Streamlit)

---

## 🔍 Key Features

- Real-time news extraction from multiple sources
- Candidate mention detection using keyword matching
- Sentiment classification (positive, neutral, negative)
- Confidence scoring for predictions
- Sentiment distribution analysis
- Temporal sentiment trends
- Candidate ranking based on perception score
- Interactive dashboard with filters

---

## 🧠 Methodology

1. **Data Collection**
   - Scrapes RSS feeds from Colombian news outlets

2. **Text Preprocessing**
   - Cleaning and normalization of text

3. **Candidate Detection**
   - Keyword-based matching

4. **Sentiment Analysis**
   - Transformer-based NLP model

5. **Scoring System**
   - Positive = +1  
   - Neutral = 0  
   - Negative = -1  

---

## 📊 Dashboard

The project includes an interactive Streamlit dashboard that allows:

- Sentiment distribution by candidate  
- Sentiment trends over time  
- Candidate ranking  
- Dynamic filtering  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- Streamlit  
- Transformers (Hugging Face)  
- BeautifulSoup  
- Matplotlib  

---

## 📂 Project Structure

colombia-election-sentiment-system/
│
├── data/
├── models/
├── src/
│ ├── data_collection.py
│ ├── analysis.py
│ ├── inference_transformer.py
│ └── preprocessing.py
│
├── dashboard.py
├── api/
├── notebooks/
├── requirements.txt
└── README.md


---

## ⚙️ How to Run

### 1. Clone repository

```bash
git clone https://github.com/pipesito1/colombia-election-sentiment-system.git
cd colombia-election-sentiment-system

```

## Create environment

python -m venv venv
venv\Scripts\activate   # Windows

## Install dependencies

pip install -r requirements.txt

## Run pipeline

python src/data_collection.py
python -m src.analysis

##  Launch dashboard
streamlit run dashboard.py
