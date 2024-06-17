def format_text(text):
    # Split the text into lines
    lines = text.split('\n')

    # Initialize variables
    formatted_lines = []
    indent_level = 0
    apply_next_line = False

    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) > 0:
            
            if apply_next_line:
                indented_line = '    ' * indent_level + stripped_line
                formatted_lines.append(indented_line)
                apply_next_line = False
                continue
            
            # Determine the indentation level based on the content
            if stripped_line.startswith('título'):
                indent_level = 0
                apply_next_line = True
            elif stripped_line.startswith('capítulo'):
                indent_level = 1
                apply_next_line = True
            elif stripped_line.startswith('secção'):
                indent_level = 2
                apply_next_line = True
            elif stripped_line.startswith('artigo'):
                indent_level = 3
                apply_next_line = True
            elif stripped_line[0].isdigit():
                indent_level = 4
            elif stripped_line.startswith('a)') or stripped_line.startswith('b)') or stripped_line.startswith('c)') or stripped_line.startswith('d)') or stripped_line.startswith('e)') or stripped_line.startswith('f)') or stripped_line.startswith('g)') or stripped_line.startswith('h)') or stripped_line.startswith('i)') or stripped_line.startswith('ii)') or stripped_line.startswith('iii)') or stripped_line.startswith('iv)'):
                indent_level = 5
            else:
                indent_level = 0

            # Apply the indentation
            indented_line = '    ' * indent_level + stripped_line
            formatted_lines.append(indented_line)
        else:
            # Add an empty line
            formatted_lines.append('')
    
    # Join the lines back into a single string
    formatted_text = '\n'.join(formatted_lines)
    
    return formatted_text

if __name__ == "__main__":
    # Read the text from the input file
    
    with open('../TXT Files/Codigo_Processual_Penal_Divided_Parte_19.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Format the text
    formatted_text = format_text(text)

    # Write the formatted text to a new file
    with open("../TXT Files Processed/Codigo_Processual_Penal_Divided_Parte_19.txt", 'w', encoding='utf-8') as file:
        file.write(formatted_text)

    print("Text formatting complete. Check the 'Formatted_Codigo_Processual_Penal_Divided_Parte_19.txt' file.")