from http.client import responses

import streamlit as st
from PyPDF2 import PdfReader
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY = "your-api-key"
#Upload PDF files
st.header("My First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking question",type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() #Concatenate text from all pages into a single string in the text variable.
        #st.write(text)

#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators = "\n",
        chunk_size = 1000,
        chunk_overlap = 150,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)


    #generationg embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    #creating vector store -> FAISS
    """
    - embeddings (Openai)
    - initizling_FAISS
    - Store chunks and embeddings
    """

    vector_store = FAISS.from_texts(chunks,embeddings)

    # get user question
    user_question = st.text_input("Type your question here")

    #Similarity search
    if user_question:
        """
        A = user_question -> user_question
        B = vector_DB -> vector_store
        """
        match = vector_store.similarity_search(user_question)
        #st.write(match)

        #define LLM
        llm = ChatOpenAI(
            openai_api_key = OPENAI_API_KEY,
            temparature = 0,
            max_tokens = 1000,
            model_name = "gpt-3.5-turbo"
        )

        #output results
        #chain -> take the question, get relevent document, pass it to the LLM, generate the output
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents = match, question = user_question)
        st.write(response)




