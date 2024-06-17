# DataMining - LawTalk Project

The LawTalk Project consists of developing a chatbot using Ollama LLM's and the integration of RAG to create a chatbot that analyses and answers practical cases regarding crimes utilizing the Portuguese Penal Code and the Portuguese Processual Penal Code.

## Team Members

- **PG50380** - Francisco Claudino
- **PG50633** - Mariana Marques
- **PG53597** - Afonso Bessa
- **PG54780** - Eduardo Henriques

## Index of Contents:

#### `docs`: Contains both presentations and the article of this project

#### `Embeddings`: Contains the vector embeddings of the LLM Models. One subdirectory is present for each of our most used models, as well as a generic one for other models

#### `Final PDF Files`: Contains the result of the translation and conversion of the processed TXT files back to the PDF format. All files fed to the model are in English

#### `Images`: Contains the images used in the web application of the project. Also contains the standart font used for TXT to PDF conversion

#### `Original Files`: Contains the original PDF files for the Portuguese Penal and Processual Penal Code

#### `PDF Files`: Contains the result of the division of the Portuguese Penal Code and the Portuguese Processual Penal Code ready for PreProcessement



### `src`: Contains the Source Code of the Project

- **`app.py`**: Contains the core chatbot implementation using Ollama LLM's.
- **`divide_codigo_penal.py`**: Contains the script to divide the PDF File that contains the Portuguese Penal Code in many smaller PDF files.
- **`divide_codigo_processual_penal.py`**: Contains the script to divide the PDF File that contains the Portuguese Processual Penal Code in many smaller PDF files.
- **`divide_direito_processual_penal.py`**: Contains the script to divide the PDF File that contains the Notes from the Law Course from the University of Porto in many smaller PDF files.
- **`document_loader.py`**: Contains the script for loading the PDF Files to the database.
- **`evaluate.csv`**: Contains the Test Dataset for the evaluation of the LLM Models.
- **`evaluate.ipynb`**: Contains the Jupyter Notebook for evaluating the LLM Models.
- **`extract_pdfplumber.py`**: Contains the code for extracting raw text from PDF files using PDFPlumber.
- **`format_and_translate.py`**: Contains the script for applying indentation and structural modification to a TXT File, as well as to translate the TXT Files and convert it to a PDF File.
- **`format.py`**: Contains the script for applying indentation and structural modification to a TXT file.
- **`llm.py`**: Contains the prompts and the chain build with the RAG Framework.
- **`models.py`**: Contains code that verifies and downloads the LLM Models if not present in the local machine.
- **`process_single_files.py`**: Contains the script to process the PDF Files that contain Legal Cases and their Resolution into many smaller TXT Files.
- **`py2pdf.py`**: Contains the code for extracting raw text from PDF Files using Py2PDF.
- **`requirements.txt`**: Contains the tools necessary to run the project.
- **`stats.csv`**: Contains the results of the evaluation for each LLM Model.
- **`stats.py`**: Contains the script to display the results of the evaluation in charts at a Web Base Application.
- **`streamlit.py`**: Main script to run the chatbot on a Web Based Application.
- **`tesseract.py`**: Contains the code for extracting raw text from PDF Files using Tesseract.
- **`translate.py`**: Contains the code to translate a TXT file to English from Portuguese using the Google Translate library.Afterwards, converts the raw text into a PDF file.
- **`txt_to_pdf.py`**: Script to convert a TXT File to a PDF File.

#### `TXT Files`: Contains the files in TXT format extracted from the Original Files

#### `TXT Files Processed`: Contains the files in TXT format after they have been properly formatted(indentation, newlines and structural modifications)

## Running the Application

### Requirements:

- **Ollama service running:** Run **'ollama start'** and **'ollama pull <model_name>'** to download the desired model(s).
- **Python: 3.11.8**
- **Required modules:** Run 'pip install -r requirements.txt'

### Running the app:

- **W/ Streamlit:** In the 'src' directory, run 'streamlit run streamlit.py <args>'
- **In Terminal:** In the 'src' directory, run 'python3 app.py <args>'

### Arguments:

- **-m <model_name>:** Decide the name of the model(e.g. "-m 'llama2'")
- **-p <path_directory>:** Customize the path where the files used by the model is(e.g. "-p '../New_Folder'")
- **-r:** Decide if the embeddings will be reloaded into the database