import os 
import argparse
import shutil

from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Document, StorageContext, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader
from llama_index.core.schema import TextNode



# You'll also need to encode other things like BM-25 and NER.

CHROMA_PATH = "src/data/chroma"
DATA_Source = "src/data/data_source"

def load_documents():

    # Reads all the documents in the data source
    doc = SimpleDirectoryReader(DATA_Source).load_data()
    return doc

def split_documents_into_TextNodes(documents: list[Document]):
    text_parser = SentenceSplitter(
        chunk_size=600,
        chunk_overlap=0
    )

    text_chunks = []
    # maintain relationship with source doc index, 
    # to help inject doc metadata i
    doc_idxs = []

    # Splitting documents
    for doc_idx, page in enumerate(documents):

        page_text = page.get_text()
        chunks = text_parser.split_text(page_text)
        text_chunks.extend(chunks)
        doc_idxs.extend([doc_idx] * len(chunks))
    

    # Converting split nodes into TextNodes
    nodes = []
    for idx, text_chunk in enumerate(text_chunks):
        node = TextNode(
            text=text_chunk,
        )
        nodes.append(node)
        src_doc = documents[doc_idxs[idx]]
        node.metadata = src_doc.metadata

    # print(nodes[0].__dict__)
    return nodes


def add_to_database(nodes: list[TextNode]):

    db = chromadb.PersistentClient(path=CHROMA_PATH)
    chroma_collection = db.get_or_create_collection("chroma_db")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # define embedding model
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    print(f"Nodes: {len(nodes)}")
    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context,
        embedding_model=embed_model,
    )


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()

    if args.reset:
        print("Resetting database ✨✨✨")
        clear_database()

    documents = load_documents()
    nodes = split_documents_into_TextNodes(documents)
    add_to_database(nodes)