# RAG-based FAQ Bot for Automotive Regulations

## 🧠 Overview

This project is a Proof-of-Concept (PoC) for a chatbot that uses Retrieval-Augmented Generation (RAG) to answer questions about automotive regulations.

## 🚀 Features

- PDF-based document ingestion and chunking
- Vector store using Chroma DB
- Question answering using OpenAI via LangChain
- Simple Streamlit UI for interaction

## 📁 Project Structure

```
rag_faq_bot/
├── app/                 # Streamlit frontend
├── api/                 # (Optional) FastAPI backend
├── rag/                 # RAG logic modules
├── data/                # Regulation PDF documents
├── notebooks/           # Experiments
├── docs/                # Documentation assets
├── requirements.txt     # Python dependencies
├── .env                 # API Keys and environment variables
└── README.md
```

## 📂 Note on Data Folder

Please add your own regulation-related PDF documents to the `data/` directory.
These files are **not included in version control** and must be added manually.

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

## 🔑 Environment

Create a `.env` file:

```
OPENAI_API_KEY=your-api-key
```

## ▶️ Run

```bash
streamlit run app/main.py
```

## 🧠 Sample Query

> "The brake pedal feels soft when pressed. What regulation might apply?"

## 🧑‍💻 Author

Akito Shirai | Generative AI Engineer | Based in Tochigi, Japan
