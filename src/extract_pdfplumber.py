# Import the pdfplumber library
import pdfplumber
import regex as re

# Function to extract text from each page of a PDF file
def text_from_pdf_with_pdfplumber1(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[16:]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'^alterações.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^alterado.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'pág.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'versão à data.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^rectificado.*$', '', full_text, flags=re.MULTILINE | re.IGNORECASE)
                full_text = re.sub(r'^código penal - cp|legislação consolidada$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    # Return the full extracted text
    return full_text

def text_from_pdf_with_pdfplumber2(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[16:]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'^alterações.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^alterado.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'pág.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'versão à data.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^rectificado.*$', '', full_text, flags=re.MULTILINE | re.IGNORECASE)
                full_text = re.sub(r'^código de processo penal - cpp|legislação consolidada$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    # Return the full extracted text
    full_text = re.sub(r'nessa conformidade, o crime sexual praticado contra menor', '', full_text)
    return full_text

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage  
pdf_path = '../Original Files/Codigo_Processo_Penal.pdf'
output_file = '../TXT Files/pdfplumber_codigo_processual_penal.txt'
extracted_text = text_from_pdf_with_pdfplumber2(pdf_path)
write_to_file(extracted_text, output_file)