"""
The file to execute the QA system in the browser using FastAPI.
"""
import os
import pickle


from dotenv import load_dotenv
import faiss
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from loguru import logger

load_dotenv()

if __name__ == "__main__":
    logger.info("Loading the document loader...")
    document_loader = TextLoader('data/state_of_the_union.txt')
    text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    docs = document_loader.load_and_split(text_splitter=text_splitter)
    
    #Create a vector store from the documents and save it to disk
    embedding = OpenAIEmbeddings()
    store = FAISS.from_documents(docs, embedding)

    faiss.write_index(store.index, "docs.index")
    store.index = None
    with open("faiss_store.pkl", "wb") as f:
        pickle.dump(store, f)
