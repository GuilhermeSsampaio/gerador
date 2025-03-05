import os
import datetime
import pypandoc
import shutil
import sys
import re

# Definir PDF_ENGINE como variável global
PDF_ENGINE = 'xelatex'  # valor padrão

def check_dependencies():
    global PDF_ENGINE
    try:
        # Tenta baixar o pandoc se não estiver instalado
        if not pypandoc.get_pandoc_version():
            print("Baixando Pandoc portable...")
            pypandoc.download_pandoc()
            print("Pandoc baixado com sucesso!")
    except OSError:
        print("Baixando Pandoc portable...")
        pypandoc.download_pandoc()
        print("Pandoc baixado com sucesso!")
    
    # Verifica se o LaTeX (xelatex) está instalado
    latex_path = shutil.which('xelatex')
    if not latex_path:
        print("Erro: XeLaTeX não encontrado!")
        print("Tentando usar wkhtmltopdf como alternativa...")
        PDF_ENGINE = 'wkhtmltopdf'
    
    print("✓ Dependências configuradas")

def clean_text(text):
    # Remove caracteres não-imprimíveis exceto quebras de linha
    text = ''.join(char for char in text if char.isprintable() or char in '\n\r')
    # Remove caracteres Unicode inválidos
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text

def add_file_to_md(md_content, dir_name, file_path):
    relative_path = os.path.splitext(os.path.relpath(file_path, dir_name))[0].replace(os.sep, '.')
    prefix_doc = "diretório.arquivo : "
    
    # Adiciona quebra de página e título em negrito
    md_content.append("\n\\pagebreak\n")
    md_content.append(f"**{prefix_doc}{relative_path}**\n\n")
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
            # Limpa o texto antes de adicionar
            content = clean_text(content)
            # Adiciona o conteúdo do arquivo como bloco de código
            md_content.append("```")
            md_content.append(content)
            md_content.append("```\n")
    except Exception as e:
        md_content.append(f"Erro ao ler o arquivo: {file_path}\n{str(e)}\n")

def generate_document(base_dir, output_filename, include_dirs, include_env=True):
    check_dependencies()
    md_content = []
    
    # Adiciona título centralizado usando HTML e CSS
    md_content.append("""<div style="text-align: center; font-family: 'Times New Roman'; font-size: 12pt;">

**Linguagem de Programação III - Entrega 1 - Guilherme Silva Sampaio**

</div>
""")
    
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
    
    for root, file_path in files_list:
        add_file_to_md(md_content, base_dir, file_path)
    
    # Adiciona assinatura
    md_content.append("\n\\pagebreak\n")
    date_str = datetime.datetime.now().strftime("%d/%m/%Y")
    md_content.append(f"\nDourados, {date_str} -- (Assinatura)\n")
    
    # Criar diretório de saída se não existir
    output_dir = "arquivos-entrega"
    os.makedirs(output_dir, exist_ok=True)
    
    # Salvar arquivo Markdown
    md_path = os.path.join(output_dir, output_filename + ".md")
    pdf_path = os.path.join(output_dir, output_filename + ".pdf")
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_content))
    
    # Atualiza os argumentos extra para garantir a fonte em todo o documento
    if PDF_ENGINE == 'xelatex':
        extra_args = [
            '--pdf-engine=xelatex',
            '-V', 'geometry:margin=1in',
            '-V', 'mainfont=Times New Roman',
            '-V', 'fontsize=12pt',
            '--variable', 'fontfamily=times',
            '--include-in-header=' + os.path.join(os.path.dirname(__file__), 'header.tex')
        ]
    else:
        extra_args = [
            '--pdf-engine=wkhtmltopdf',
            '--variable', 'margin-top=25mm',
            '--variable', 'margin-right=25mm',
            '--variable', 'margin-bottom=25mm',
            '--variable', 'margin-left=25mm',
            '--css=' + os.path.join(os.path.dirname(__file__), 'style.css')
        ]
    
    try:
        pypandoc.convert_file(
            md_path,
            'pdf',
            outputfile=pdf_path,
            extra_args=extra_args
        )
        print(f"✓ PDF gerado com sucesso: {pdf_path}")
    except Exception as e:
        print(f"Erro na conversão para PDF: {str(e)}")
        print("Tentando método alternativo...")
        try:
            # Tenta converter primeiro para HTML e depois para PDF
            html_path = os.path.join(output_dir, output_filename + ".html")
            pypandoc.convert_file(
                md_path,
                'html',
                outputfile=html_path,
                extra_args=['--standalone']
            )
            pypandoc.convert_file(
                html_path,
                'pdf',
                outputfile=pdf_path,
                extra_args=extra_args
            )
            os.remove(html_path)  # Remove o arquivo HTML temporário
            print(f"✓ PDF gerado com sucesso usando método alternativo: {pdf_path}")
        except Exception as e2:
            print(f"Erro no método alternativo: {str(e2)}")
            print("Salvando apenas o arquivo Markdown...")

# Gerar os documentos
base_dir_front = "../front-end"
base_dir_back = "../back-end"

generate_document(base_dir_front, "front-end", ["public", "src"], include_env=False)
generate_document(base_dir_back, "back-end", ["src"], include_env=True)


