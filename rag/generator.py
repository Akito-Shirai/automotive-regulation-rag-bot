from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

def get_answer(retriever, query: str):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
    docs = retriever.get_relevant_documents(query)
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=query)
