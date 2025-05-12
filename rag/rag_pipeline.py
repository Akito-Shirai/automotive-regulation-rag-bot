from rag.document_loader import load_documents
from rag.retriever import create_retriever
from rag.generator import get_answer

def run_pipeline(query: str, doc_path: str):
    docs = load_documents(doc_path)
    retriever = create_retriever(docs)
    answer = get_answer(retriever, query)
    return answer
