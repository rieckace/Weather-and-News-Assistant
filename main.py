import os
import requests
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# LLM from Groq
llm = ChatOpenAI(
    model="llama3-8b-8192",
    openai_api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

# HuggingFace Embeddings example (not used directly here)
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

st.set_page_config(page_title="🌦️ Weather & News Assistant", layout="centered")
st.title("🌤️ Weather and 📰 News Assistant")

# --- Weather API ---
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url)
    if res.status_code != 200:
        return f"❌ Could not fetch weather for {city}."
    data = res.json()
    description = data['weather'][0]['description'].capitalize()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    return f"🌡️ {temp}°C, {description}, 💧 Humidity: {humidity}%"

# --- News API ---
def fetch_top_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    res = requests.get(url)
    if res.status_code != 200:
        return []
    return res.json().get("articles", [])[:5]

# --- LLM Explanation ---
def generate_llm_response(prompt):
    response = llm.predict(prompt)
    return response

# --- Streamlit UI ---
city = st.text_input("Enter your city name for weather:")

if city:
    st.subheader(f"📍 Weather in {city}")
    weather = fetch_weather(city)
    st.markdown(weather)

    explanation = generate_llm_response(f"Explain this weather to a regular person: {weather}")
    st.info(explanation)

st.subheader("📰 Top Trending News")
news = fetch_top_news()
for i, article in enumerate(news, 1):
    title = article.get("title", "No title")
    url = article.get("url", "")
    st.markdown(f"{i}. [{title}]({url})")

summary_prompt = "Summarize today's top 5 news headlines in simple terms:\n"
for a in news:
    summary_prompt += f"- {a.get('title', '')}\n"

if news:
    st.subheader("🧠 Summary of News")
    summary = generate_llm_response(summary_prompt)
    st.success(summary)
