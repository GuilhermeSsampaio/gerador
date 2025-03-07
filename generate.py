import os
import datetime
from docx2pdf import convert
import format_docx as doc_format
from sub_listagem import exportOrderCorrect
from functools import cmp_to_key  # Importa a ferramenta para usar comparação customizada

name = input("Digite o nome completo do aluno: ")
entrega = input("Digite o número da entrega: ")

def add_file_to_doc(doc, dir_name, file_path, add_page_break=True):
    """Adiciona o conteúdo de um arquivo ao documento."""
    if add_page_break:
        doc_format.add_page_break(doc)
    
    relative_path = os.path.splitext(os.path.relpath(file_path, dir_name))[0].replace(os.sep, '.')
    title_text = f"diretório.arquivo : {relative_path}"
    
    doc_format.add_subtitle(doc, title_text)
    doc_format.add_empty_paragraph(doc)
    
    try:
        # Verifica se o arquivo é uma imagem
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Usa caminho absoluto para imagens
            absolute_path = os.path.abspath(file_path)
            print(f"Processando imagem: {absolute_path}")
            
            # Tenta adicionar a imagem com tamanho reduzido para evitar problemas
            success = doc_format.add_image(doc, absolute_path, width=3.5)
            
            if success:
                print(f"Imagem adicionada com sucesso: {os.path.basename(absolute_path)}")
            else:
                print(f"Falha ao adicionar imagem: {os.path.basename(absolute_path)}")
            
        else:
            # Para arquivos de texto
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    doc_format.add_paragraph_text(doc, content)
                    print(f"Arquivo de texto adicionado: {os.path.basename(file_path)}")
            except UnicodeDecodeError:
                # Se falhar ao abrir como texto, pode ser um arquivo binário
                doc_format.add_paragraph_text(doc, f"[Arquivo binário não exibido: {os.path.basename(file_path)}]")
                print(f"Arquivo binário ignorado: {os.path.basename(file_path)}")
    except Exception as e:
        error_msg = f"Erro ao processar o arquivo: {file_path}\n{str(e)}"
        doc_format.add_paragraph_text(doc, error_msg)
        print(f"ERRO GERAL: {error_msg}")
        
def collect_files(base_dir, include_dirs, include_env):
    """Coleta todos os arquivos, mantendo o agrupamento dos arquivos da mesma subpasta."""
    all_files = []
    
    # Diretórios que devem ser ignorados
    exclude_dirs = [
        'node_modules',
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
    
    # Adicionar verificação explícita para o diretório de imagens
    images_dir = 'imagens'
    if images_dir not in include_dirs and os.path.exists(os.path.join(base_dir, images_dir)):
        include_dirs.append(images_dir)
        print(f"Diretório de imagens '{images_dir}' adicionado automaticamente")
    
    for root, dirs, files in os.walk(base_dir):
        # Modifica a lista dirs em tempo real para pular diretórios excluídos
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        relative_path = os.path.relpath(root, base_dir)
        if any(relative_path.startswith(d) for d in include_dirs) or relative_path == ".":
            for file in files:
                if file in exclude_files:
                    continue
                if file.endswith(".env") and not include_env:
                    continue
                
                file_path = os.path.join(root, file)
                depth = len(relative_path.split(os.sep)) if relative_path != "." else 0
                all_files.append((depth, relative_path, file, file_path))
    
    # Função comparadora personalizada para manter agrupados os arquivos da mesma hierarquia
    def compare_items(item1, item2):
        r1 = item1[1]  # relative_path do primeiro item
        r2 = item2[1]  # relative_path do segundo item
        
        # Se ambos estão no mesmo diretório, ordena pelo nome do arquivo
        if r1 == r2:
            return -1 if item1[2] < item2[2] else (1 if item1[2] > item2[2] else 0)
        
        # Tratar arquivos do diretório base: se um arquivo estiver no base_dir ("."),
        # queremos que ele apareça depois de arquivos que estejam em subpastas.
        if r1 == "." and r2 != ".":
            return 1
        if r2 == "." and r1 != ".":
            return -1
        
        # Se um dos diretórios for prefixo do outro, o que tiver maior profundidade (subpasta) vem primeiro.
        if r1.startswith(r2 + os.sep):
            return -1  # item1 está em uma subpasta de item2
        if r2.startswith(r1 + os.sep):
            return 1   # item2 está em uma subpasta de item1
        
        # Se não houver relação de prefixo, ordena lexicograficamente
        return -1 if r1 < r2 else 1 if r1 > r2 else 0

    # Ordena usando a função comparadora personalizada
    all_files_sorted = sorted(all_files, key=cmp_to_key(compare_items))
    
    return [(root, file_path) for depth, rel_path, file, file_path in all_files_sorted]

def generate_document(base_dir, output_filename, include_dirs, include_env=True):
    """Gera a documentação para os diretórios especificados."""
    doc = doc_format.create_document()
    
    title = "Linguagem de Programação III - Entrega "+entrega + " - "  + name
    doc_format.add_title(doc, title)
    doc_format.add_empty_paragraph(doc)
    
    # Verificar e adicionar diretório de imagens se existir
    if 'imagens' not in include_dirs and os.path.exists(os.path.join(base_dir, 'imagens')):
        include_dirs.append('imagens')
        print("Diretório 'imagens' adicionado à lista de inclusão")
    
    files_list = collect_files(base_dir, include_dirs, include_env)
    
    first_file = True
    for root, file_path in files_list:
        add_file_to_doc(doc, base_dir, file_path, add_page_break=not first_file)
        first_file = False
    
    doc_format.add_empty_paragraph(doc)
    date_str = datetime.datetime.now().strftime("%d/%m/%Y")
    doc_format.add_paragraph_text(doc, f"Dourados, {date_str} -- (Assinatura)")
    
    output_dir = "arquivos-entrega"
    os.makedirs(output_dir, exist_ok=True)
    
    docx_path = os.path.join(output_dir, f"{output_filename}.docx")
    pdf_path = os.path.join(output_dir, f"{output_filename}.pdf")
    
    doc_format.save_document(doc, docx_path)
    print(f"Documento DOCX salvo em: {docx_path}")
    
    try:
        convert(docx_path, pdf_path)
        print(f"Documento PDF salvo em: {pdf_path}")
    except Exception as e:
        print(f"Erro ao converter para PDF: {str(e)}")