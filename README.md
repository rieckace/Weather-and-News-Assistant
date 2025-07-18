
# 🌤️📰 News & Weather Assistant

This assistant gives you:
- Real-time **weather updates** based on city input.
- The latest **top news headlines** (India).
- **LLM-powered summaries** using Groq API + HuggingFace models.

---

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [OpenWeather API](https://openweathermap.org/) — Weather data
- [NewsAPI](https://newsapi.org/) — Trending news
- [Groq API](https://console.groq.com/docs) — LLM (LLaMA3)
- 🤗 [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — for vectorization

---

## 📁 Project Structure
<img width="559" height="244" alt="image" src="https://github.com/user-attachments/assets/145c6a10-65ab-432e-9d0b-71f53cfedebb" />

---

## ✅ Features

- 🔍 Search any **city** for real-time weather.   
- 📢 Shows **5 top trending Indian news headlines**.   
- 🧠 Uses **Groq + HuggingFace** to summarize and explain results clearly.    

---

## 🚀 Run Locally

1. **Clone the repository**:  
git clone https://github.com/rieckace/news-weather-assistant.git    
cd news-weather-assistant

---
### Install dependencies:  
pip install -r requirements.txt  

---
Setup environment:
---
 .env.example   
**Add your API keys in .env:**    

GROQ_API_KEY=your_groq_api_key  
WEATHER_API_KEY=your_openweather_key   
NEWS_API_KEY=your_newsapi_key   

---
## Run the Streamlit app:  
streamlit run assistant_app.py 

---

🧪 Sample Output  
---
✅ Weather: Clear sky, 30°C in Mumbai  

✅ LLM Summary: "Today’s weather in Mumbai will feel warm with gentle wind..."   

✅ News: 5 headline summaries using LLM embeddings   

---
📦 Dependencies
---
txt  
streamlit  
requests  
python-dotenv  
transformers  
torch  
sentence-transformers  
groq  

---

Made with ❤️ using Groq LLMs and 🤗 HuggingFace.
=======

