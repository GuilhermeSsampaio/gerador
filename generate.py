import os
import datetime
from docx2pdf import convert
import format_docx as doc_format
from sub_listagem import exportOrderCorrect


name = input("Digite o nome completo do aluno: ")

def add_file_to_doc(doc, dir_name, file_path, add_page_break=True):
    """Adiciona o conteúdo de um arquivo ao documento."""
    if add_page_break:
        doc_format.add_page_break(doc)
    
    relative_path = os.path.splitext(os.path.relpath(file_path, dir_name))[0].replace(os.sep, '.')
    title_text = f"diretório.arquivo : {relative_path}"
    
    doc_format.add_subtitle(doc, title_text)
    doc_format.add_empty_paragraph(doc)
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            doc_format.add_paragraph_text(doc, file.read())
    except Exception as e:
        error_msg = f"Erro ao ler o arquivo: {file_path}\n{str(e)}"
        doc_format.add_paragraph_text(doc, error_msg)

def collect_files(base_dir, include_dirs, include_env):
    """Coleta todos os arquivos, priorizando os dentro de subpastas mais profundas."""
    all_files = []
    
    # Diretórios que devem ser ignorados
    exclude_dirs = [
        'node_modules',
        'imagens',
        '.git',
        '.vscode',
        '__pycache__',
        'venv',
        'dist',
        'build',
        '.next'
    ]
    
    # Arquivos que devem ser ignorados
    exclude_files = [
        '.DS_Store',
        '.env.local',
        '.env.example',
        'ormconfig.ts',
        'tsconfig.json',
        'package.json',
        '.env.development',
        '.gitignore',
        'package-lock.json',
        'yarn.lock'
    ]
    
    for root, dirs, files in os.walk(base_dir):
        # Modificar a lista dirs em tempo real para pular diretórios excluídos
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        relative_path = os.path.relpath(root, base_dir)
        if any(relative_path.startswith(d) for d in include_dirs) or relative_path == ".":
            for file in files:
                # Verificar se o arquivo não está na lista de exclusão
                if file in exclude_files:
                    continue
                
                # Verificar a condição do arquivo .env
                if file.endswith(".env") and not include_env:
                    continue
                
                file_path = os.path.join(root, file)
                # Calcular o nível de profundidade (quantidade de diretórios)
                depth = len(relative_path.split(os.sep)) if relative_path != "." else 0
                all_files.append((depth, relative_path, file, file_path))
    
    # Ordenar primeiro por profundidade (decrescente), depois pelo caminho
    return [(root, file_path) for depth, rel_path, file, file_path in 
            sorted(all_files, key=lambda x: (-x[0], x[1], x[2]))]

def generate_document(base_dir, output_filename, include_dirs, include_env=True):
    """Gera a documentação para os diretórios especificados."""
    doc = doc_format.create_document()
    
    title = "Linguagem de Programação III - Entrega 1 - " + name
    doc_format.add_title(doc, title)
    doc_format.add_empty_paragraph(doc)
    
    files_list = collect_files(base_dir, include_dirs, include_env)
    
    first_file = True
    for root, file_path in files_list:
        add_file_to_doc(doc, base_dir, file_path, add_page_break=not first_file)
        first_file = False
    
    doc_format.add_page_break(doc)
    date_str = datetime.datetime.now().strftime("%d/%m/%Y")
    doc_format.add_paragraph_text(doc, f"Dourados, {date_str} -- (Assinatura)")
    
    output_dir = "arquivos-entrega"
    os.makedirs(output_dir, exist_ok=True)
    
    docx_path = os.path.join(output_dir, f"{output_filename}.docx")
    pdf_path = os.path.join(output_dir, f"{output_filename}.pdf")
    
    doc_format.save_document(doc, docx_path)
    convert(docx_path, pdf_path)
