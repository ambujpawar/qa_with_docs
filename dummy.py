"""
The dummy file to check if the vectorizer and loading similar documentation works.
"""

import pickle

from dotenv import load_dotenv
import faiss
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

load_dotenv()


if __name__ == "__main__":
    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)
    store.index = faiss.read_index("docs.index")
    
    qa_chain = ConversationalRetrievalChain.from_llm(
                    llm=ChatOpenAI(temperature=0),
                    retriever = store.as_retriever(),
                    return_source_documents=True,
                    )
    chat_history = []

    while True:
        query = input("Query: ")
        print(f"Query: {query}")
        result = qa_chain({"question": query, "chat_history": chat_history})
        print(f"Answer: {result['answer']}")
        chat_history.append((query, result["answer"]))

