import os 
import argparse
import shutil
from llama_index.readers.file.pymu_pdf.base import PyMuPDFReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Document, StorageContext, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from llama_index.embeddings.huggingface import HuggingFaceEmbedding



# You'll also need to encode other things like BM-25 and NER.

CHROMA_PATH = "src/data/chroma"
DATA_Source = "src/data/data_source/test.pdf"

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()

    if args.reset:
        print("Resetting database database ✨✨✨")
        clear_database()

    documents = load_documents()
    chunks = split_documents(documents)
    add_to_database(chunks)

def load_documents():

    loader = PyMuPDFReader()
    return loader.load(DATA_Source)

def split_documents(documents: list[Document]):

    text_parser = SentenceSplitter(
        chunk_size = 600,
        chunk_overlap= 100,
    )
    return text_parser.split_text(documents)

def add_to_database(chunks: list[Document]):

    db = chromadb.PersistentClient(path=CHROMA_PATH)
    chroma_collection = db.get_or_create_collection("chroma_db")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # define embedding model
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    index = VectorStoreIndex.from_documents(
        chunks,
        storage_context=storage_context,
        embedding_model=embed_model,
    )


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


if __name__ == "__main__":
    main()