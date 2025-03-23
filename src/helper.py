from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

def pdf_loader(data_dir):
    loader = DirectoryLoader(data_dir,glob="*.pdf",loader_cls=PyPDFLoader)
    doc = loader.load()
    return doc

def text_split(extreacted_text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap = 20)
    chunks = text_splitter.split_documents(extreacted_text)
    return chunks

#Download the Embeddings from Hugging Face
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings
