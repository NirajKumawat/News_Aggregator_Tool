import os
import pickle
import time
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="NewsAI", layout="wide", page_icon="🧠")

# -------------------- UI Layout --------------------
st.title("📰 The News Aggregator Tool")
st.markdown("**Effortlessly extract insights from news articles using AI.**")

st.divider()

col1, col2 = st.columns([1, 2])

# Sidebar-style Left Column for URLs
with col1:
    st.subheader("🔗 Article URLs")
    st.markdown("*Paste up to 3 news article URLs below:*")
    urls = []
    for i in range(3):
        url = st.text_input(f"URL {i+1}", key=f"url_input_{i}")
        urls.append(url.strip())

    process_url_clicked = st.button("🚀 Process URLs")

# Right Column for Output and QA
with col2:
    file_path = "faiss_store_gemini.pkl"
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.9, max_tokens=500)

    if process_url_clicked:
        with st.spinner("🔄 Loading and processing URLs..."):
            loader = UnstructuredURLLoader(urls=urls)
            data = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                separators=["\n\n", "\n", ".", ","],
                chunk_size=1000
            )
            docs = splitter.split_documents(data)

            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectorstore = FAISS.from_documents(docs, embeddings)

            with open(file_path, "wb") as f:
                pickle.dump(vectorstore, f)

            st.success("✅ Articles processed and vector database created!")

    st.markdown("### 💬 Ask Questions About the Articles")
    query = st.text_input("Type your question here...", key="qa_input")

    if query:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                vectorstore = pickle.load(f)

            chain = RetrievalQAWithSourcesChain.from_llm(
                llm=llm,
                retriever=vectorstore.as_retriever()
            )

            with st.spinner("Thinking..."):
                result = chain({"question": query}, return_only_outputs=True)

            st.markdown("#### 🧠 Answer")
            st.markdown(f"<div class='answer-box'>{result['answer']}</div>", unsafe_allow_html=True)

            sources = result.get("sources", "")
            if sources:
                st.markdown("#### 📚 Sources")
                for src in sources.split("\n"):
                    if src.strip():
                        st.markdown(f"- {src}")

st.divider()
st.caption("© 2025 News_Aggregator_Tool | Built using Streamlit & LangChain")
