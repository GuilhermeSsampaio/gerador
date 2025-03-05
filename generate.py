import os
import datetime
from docx2pdf import convert
import format_docx as doc_format

def add_file_to_doc(doc, dir_name, file_path, add_page_break=True):
    """Adiciona o conteúdo de um arquivo ao documento."""
    if add_page_break:
        doc_format.add_page_break(doc)
    
    relative_path = os.path.splitext(os.path.relpath(file_path, dir_name))[0].replace(os.sep, '.')
    prefix_doc = "diretório.arquivo : "
    title_text = prefix_doc + relative_path
    
    # Adiciona o título do arquivo (em negrito)
    doc_format.add_subtitle(doc, title_text)
    
    # Adiciona uma linha em branco
    doc_format.add_empty_paragraph(doc)
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            # Adiciona o conteúdo do arquivo
            doc_format.add_paragraph_text(doc, file.read())
    except Exception as e:
        error_msg = f"Erro ao ler o arquivo: {file_path}\n{str(e)}"
        doc_format.add_paragraph_text(doc, error_msg)

def generate_document(base_dir, output_filename, include_dirs, include_env=True):
    """Gera a documentação para os diretórios especificados."""
    # Cria um novo documento com formatação padrão
    doc = doc_format.create_document()
    
    # Adiciona o título principal
    title = "Linguagem de Programação III - Entrega 1 - Guilherme Silva Sampaio"
    doc_format.add_title(doc, title)
    
    # Adiciona uma linha em branco após o título
    doc_format.add_empty_paragraph(doc)
    
    # Coleta todos os arquivos a serem incluídos
    files_list = []
    for root, dirs, files in os.walk(base_dir):
        if "node_modules" in root:
            continue
        relative_path = os.path.relpath(root, base_dir)
        if any(relative_path.startswith(d) for d in include_dirs):
            for file in files:
                if file.endswith(".env") and not include_env:
                    continue
                file_path = os.path.join(root, file)
                files_list.append((root, file_path))
    
    files_list.sort(key=lambda x: x[1])
    
    # Adiciona cada arquivo ao documento
    first_file = True
    for root, file_path in files_list:
        if first_file:
            add_file_to_doc(doc, base_dir, file_path, add_page_break=False)
            first_file = False
        else:
            add_file_to_doc(doc, base_dir, file_path)
    
    # Adiciona a página de assinatura
    doc_format.add_page_break(doc)
    date_str = datetime.datetime.now().strftime("%d/%m/%Y")
    doc_format.add_paragraph_text(doc, f"Dourados, {date_str} -- (Assinatura)")
    
    # Cria diretório de saída se não existir
    output_dir = "arquivos-entrega"
    os.makedirs(output_dir, exist_ok=True)
    
    # Salvar arquivos no diretório de saída
    docx_path = os.path.join(output_dir, output_filename + ".docx")
    pdf_path = os.path.join(output_dir, output_filename + ".pdf")
    
    # Salva o documento DOCX
    doc_format.save_document(doc, docx_path)
    
    # Converte para PDF
    convert(docx_path, pdf_path)