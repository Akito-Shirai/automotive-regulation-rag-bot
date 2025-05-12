import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(file_path: str):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        raise FileNotFoundError(f"Invalid or empty file: {file_path}")

    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(docs)
