# Chatbot with PDF Integration

This project demonstrates how to build a chatbot using **Streamlit**, **LangChain**, and **OpenAI API** to allow users to upload a PDF and interact with the content via a chatbot. The chatbot uses **FAISS** for vector search and answers questions based on the uploaded PDF content.

## Features
- Upload PDF files and extract the text.
- Automatically split large PDFs into manageable chunks for processing.
- Use OpenAI's GPT-3.5 model to answer questions based on the contents of the PDF.
- Display chat responses using **Streamlit** for an interactive user interface.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/justnapinn/chatbot.git
cd chatbot
```
### 2. Create a virtual environment and install dependencies:

2.1 Create a virtual environment for the project using the following command:
```bash
python -m venv .venv
```
2.2 Activate the Virtual Environment
- On Windows:
```bash
.venv\Scripts\activate
```
- On macOS/Linux:
```bash
source .venv/bin/activate
```
2.3 Install Dependencies
```bash
pip install -r requirements.txt
```


### 3. Setup OpenAI API Key:
You need to create an API key on the OpenAI platform and set it in your environment.

Option 1: Create a .env file in the root of your project and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-api-key
```

Option 2: Alternatively, you can directly replace "insert-your-api-key-here" in the code with your actual OpenAI API key (not recommended for public repositories):
```bash
OPENAI_API_KEY = "your-api-key"
```

### 4. Running the app
- Make sure the virtual environment is activated.

- Run the Streamlit app:

```bash
streamlit run app.py
```

### How It Works

- Text Extraction: The uploaded PDF is parsed using the PyPDF2 library, and the text is extracted.

- Text Chunking: The extracted text is split into chunks using the RecursiveCharacterTextSplitter to facilitate better handling of large PDFs.

- Embedding Generation: OpenAIEmbeddings is used to generate embeddings for the text chunks.

- FAISS Vector Store: The generated embeddings are stored in a FAISS vector store for similarity search.

Question Answering: The user can ask questions, and the most relevant chunks are retrieved using FAISS similarity search, then passed to ChatOpenAI to generate responses based on the PDF's content.

