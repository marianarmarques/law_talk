## Setup :
1. Create a virtual environment in python.
2. Install the required Python packages by running `pip install -r requirements.txt` on your virtual environment.

## Running the Project

**Note:** The first time you run the project, it will download the necessary models from Ollama for the LLM and embeddings. This is a one-time setup process and may take some time depending on your internet connection.

1. Ensure your virtual environment is activated.
2. Run the main script with `python app.py -m <model_name> -p <path_to_documents> - r <reload_embeddings>` to specify a model, the path to documents and if you want the vector embeddings to be processed oe not. If no model is specified, it defaults to [mistral](https://ollama.com/library/mistral). If no path is specified, it defaults to `Codigo_Penal_Divided`. If no information about the reload of the embeddings is specified, it defaults to True and it will reload the embeddings.
3. Optionally, you can specify the embedding model to use with `-e <embedding_model_name>`. If not specified, it defaults to [nomic-embed-text](https://ollama.com/library/nomic-embed-text).
4. To run the web application simply run `streamlit run streamlit.py`.

## Technologies Used

- [Langchain](https://github.com/langchain/langchain): A Python library for working with Large Language Model
- [Ollama](https://ollama.ai/): A platform for running Large Language models locally.
- [Chroma](https://docs.trychroma.com/): A vector database for storing and retrieving embeddings.
- [PDFPlumber](https://pypi.org/project/PyPDF2/](https://pypi.org/project/pdfplumber/0.1.2/)): A Python library for reading and manipulating PDF files.
