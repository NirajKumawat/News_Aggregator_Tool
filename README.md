# 📰 The News Aggregator Tool

A smart tool that lets you extract and understand content from multiple news articles — powered by AI.

Paste up to 3 article URLs, and this app will:
- Fetch the article content
- Split it into chunks for processing
- Build a searchable vector database
- Let you ask questions about the articles
- Respond with answers and sources, using Google's Gemini AI

---

## 🚀 How to Run It Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/the-news-aggregator-tool.git
cd the-news-aggregator-tool
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### 4. Set up your environment variables

Create a `.env` file in the project root and add your API key:

```
GOOGLE_API_KEY=your_google_api_key
```

> 💡 Replace `your_google_api_key` with your Gemini API key.

### 5. Run the app

```bash
streamlit run app.py
```

---

## 💡 What You Can Do

Once the app is running:
- Paste links to news articles (up to 3)
- Let the tool process and store the content
- Ask questions like:
  - "What is this article about?"
  - "What are the key takeaways?"
  - "Who is being discussed?"
- Get smart answers and article sources

---

## 🧠 Tech Stack

- **Streamlit** for the UI
- **LangChain** to connect everything
- **Google Gemini** for answering questions
- **HuggingFace Embeddings** + **FAISS** for search
- **UnstructuredURLLoader** to load web content

---

## 📁 File Structure

```
.
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies
├── .env                    # Your API keys (not pushed to GitHub)
├── faiss_store_gemini.pkl  # Auto-generated vector store
└── README.md               # This file
```

---

## 📌 Notes

- Make sure article URLs are public (no paywalls).
- Answers are based on Gemini AI; output may vary.
- The FAISS database is re-created each time you process URLs.

---

## ✨ Future Ideas

- Upload PDF or DOC files
- Save previous sessions
- Add article summarization
- Language translation support

---

## 📄 License

This project is open-source under the MIT License.

---

## 🙌 Built for learning, research, and exploration.
