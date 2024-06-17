import time
import translators as ts
from deep_translator import GoogleTranslator
import streamlit as st
import argparse
import base64
from streamlit.components.v1 import html
from models import check_if_model_is_available
from document_loader import load_documents
from llm import getChatChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def load_documents_into_database(llm_model_name:str, model_name: str, documents_path: str) -> Chroma:
    print("Loading documents")
    raw_documents = load_documents(documents_path)
    documents = TEXT_SPLITTER.split_documents(raw_documents)

    if llm_model_name in ["llama2","zephyr","mistral"]:
        directory = "../Embeddings_" + llm_model_name
    else:
        directory = "../Embeddings"
    
    print("Creating embeddings and loading documents into Chroma")
    db = Chroma.from_documents(
        documents,
        OllamaEmbeddings(model=model_name),
        persist_directory=directory
        
    )
    return db

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run local LLM with RAG with Ollama.")
    parser.add_argument(
        "-r",
        "--reload",
        action="store_true",
        default=False,
        help="If provided, Embeddings will be reloaded. Otherwise(default), they are read from the Vector Database.",
    )
    return parser.parse_args()

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_image(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
        .stApp{
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
        }
        [data-testid="stBottom"] > div {
            background: transparent;
        }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)

    input_style = """
    <style>
    input[type="text"] {
        background-color: transparent;
        color: #a19eae;  // This changes the text color inside the input box
    }
    div[data-baseweb="base-input"] {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)
    return

def setup():
    st.set_page_config(page_title='LawTalk', page_icon="📊", initial_sidebar_state="expanded", layout='wide')
    st.sidebar.image("../Images/lawtalk_logo.png")

def main(reload: bool):
    setup()
    set_background_image("../Images/background.png")
    st.sidebar.header("Settings")
    reload_embedings = st.sidebar.checkbox("Reload Embeddings",True)
    llm_model_name = st.sidebar.selectbox("LLM Model Name", ["mistral","llama2","zephyr"],1)
    embedding_model_name = "nomic-embed-text"
    documents_path = "../Final PDF Files"   

    # Check to see if the models available, if not attempt to pull them
    try:
        check_if_model_is_available(llm_model_name)
        check_if_model_is_available(embedding_model_name)
    except Exception as e:
        st.error(e)
        st.stop()

    if reload_embedings:
        try:
            db = load_documents_into_database(llm_model_name, embedding_model_name, documents_path)
        except FileNotFoundError as e:
            st.error(e)
            st.stop()
    else:
        db = Chroma(persist_directory=documents_path, embedding_function=OllamaEmbeddings(model=llm_model_name))

    llm = Ollama(model=llm_model_name)
    chat = getChatChain(llm, db)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Envia Mensagem ao LawTalk"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            start_time = time.time() 
            response = chat(prompt)
            translated_result = (ts.translate_text(response, translator="google", to_language='pt'))
            st.write(translated_result)
            end_time = time.time()
            elapsed_time = end_time - start_time
            #st.write(f"Elapsed time: {round(elapsed_time,2)} seconds")  # Display elapsed time
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    args = parse_arguments()
    main(args.reload)