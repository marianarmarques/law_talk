from divide_codigo_penal import divide_pdf, convert_pdfs_to_txt
from extract_pdfplumber import text_from_pdf_with_pdfplumber2, write_to_file
from translate import text_to_pdf
from format import format_text
import os, re
from pathlib import Path

page_ranges_codigo_penal = [(0, 12), (13, 18), (18, 29), (29, 32), (32, 39), (39, 70), (70,72), (72,76), (76,91), (91,104), (104,116,), 
               (116,120), (120,143), (143,169)]

page_ranges_codigo_processual_penal = [(0, 15), (16, 26), (26, 39), (40, 42), (42, 47), (47, 53), (53,62), (62,71), (71,88), (88,97), (97,113), 
               (113,116), (116,136), (136,142), (142,164), (164,170), (170,180), (181,194), (195,202), (202,220)]

if __name__ == "__main__":
    # Iterar pelos pfds originais e dividir em secções
    
    # Codigo Penal
    divide_pdf("../Original Files/Codigo_Penal.pdf", page_ranges_codigo_penal)

    # Codigo Processual Penal
    divide_pdf("../Original Files/Codigo_Processual_Penal.pdf", page_ranges_codigo_processual_penal)
    
    # PDF to TXT
    file_num = 0
    print("Conversion")
    convert_pdfs_to_txt("../PDF Files")
    # Formatting
    print("Formatting")
    file_num = 0
    for filename in os.listdir('../TXT Files'):
        print(file_num)
        file_num+=1
        with open(f'../TXT Files/{filename}', 'r', encoding='utf-8') as file:
            text = file.read()
            formatted_text = format_text(text)
            with open(f'../TXT Files Processed/{filename}', 'w', encoding='utf-8') as file:
                file.write(formatted_text)
    # Translatting ++ TXT to PDF
    print("Translation")
    file_num = 0
    for filename in os.listdir('../TXT Files Processed'):
        print(file_num)
        file_num += 1
        txt_path = f'../TXT Files Processed/{filename}'
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
            pdf_dir = f'../Final PDF Files/{filename.replace(".txt", ".pdf")}'
            text_to_pdf(txt_path, pdf_dir)