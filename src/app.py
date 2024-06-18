from langchain_community.llms import Ollama
from langchain.evaluation import load_evaluator
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from models import check_if_model_is_available
from document_loader import load_documents
import argparse
import sys
import pandas as pd
import openai
from llm import getChatChain

TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def load_documents_into_database(llm_model_name:str, model_name: str, documents_path: str, reload: bool) -> Chroma:
    """
    Loads documents from the specified directory into the Chroma database
    after splitting the text into chunks.

    Returns:
        Chroma: The Chroma database with loaded documents.
    """
    # Diretoria genérica para outros modelos, e específica para os 3 modelos que vamos testar
    # print(llm_model_name)
    if llm_model_name in ["llama2","zephyr","mistral"]:
        directory = "../Embeddings/Embeddings_" + llm_model_name
    else:
        directory = "../Embeddings/Embeddings"
        
    print("Loading documents")
    raw_documents = load_documents(documents_path)
    documents = TEXT_SPLITTER.split_documents(raw_documents)

    # Write
    if reload:
        print("Creating embeddings and loading documents into Chroma")
        db = Chroma.from_documents(
            documents=documents,
            embedding=OllamaEmbeddings(model=model_name),
            persist_directory=directory
        )
    else:
        # Read
        db = Chroma(persist_directory=directory, embedding_function=OllamaEmbeddings(model=model_name))
    
    return db

# Modelo do OpenAI com custom Embeddings para comparacoes
openai.api_key = ''
def generate_gpt_chat(prompt):
    response = openai.Completion.create(
      model="gpt-3.5-turbo",
      organization="org-ZabQCXoLTtRLYzgxcp5uSRma",
    )
    return response.choices[0].text.strip()


def main(llm_model_name: str, embedding_model_name: str, documents_path: str) -> None:
    
    if llm_model_name == "gpt":
        while True:
            try:
                user_input = input("\n\nPlease enter your question (or type 'exit' to end): ")
                if user_input.lower() == "exit":
                    break
                print(generate_gpt_chat(user_input))
            except KeyboardInterrupt:
                break
        exit()
    
    # Check to see if the models available, if not attempt to pull them
    try:
        check_if_model_is_available(llm_model_name)
        check_if_model_is_available(embedding_model_name)
    except Exception as e:
        print(e)
        sys.exit()

    # Creating database form documents
    try:
        db = load_documents_into_database(llm_model_name, embedding_model_name, documents_path,True)
    except FileNotFoundError as e:
        print(e)
        sys.exit()

    # Initialize LLM and chat chain
    llm = Ollama(model=llm_model_name)
    chat = getChatChain(llm, db)

    # Start the conversation loop
    while True:
        try:
            user_input = input("\n\nPlease enter your question (or type 'exit' to end): ")
            if user_input.lower() == "exit":
                break

            chat(user_input)
        except KeyboardInterrupt:
            break

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run local LLM with RAG with Ollama.")
    parser.add_argument(
        "-m",
        "--model",
        default="mistral",
        help="The name of the LLM model to use.",
    )
    parser.add_argument(
        "-e",
        "--embedding_model",
        default="nomic-embed-text",
        help="The name of the embedding model to use.",
    )
    parser.add_argument(
        "-p",
        "--path",
        default="../Final PDF Files",
        help="The path to the directory containing documents to load.",
    )
    parser.add_argument(
        "-r",
        "--reload",
        action="store_true",
        default=False,
        help="If provided, Embeddings will be reloaded. Otherwise(default), they are read from the Vector Database.",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    main(args.model, args.embedding_model, args.path)
