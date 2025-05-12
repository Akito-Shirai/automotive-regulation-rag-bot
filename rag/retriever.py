from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()

def create_retriever(docs):
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="./chroma_db")
    retriever = db.as_retriever(search_kwargs={"k": 3})
    return retriever
