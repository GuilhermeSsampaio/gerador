import os
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

PAGE_WIDTH, PAGE_HEIGHT = A4
FONT_NAME = "Times-Roman"  # Times New Roman no ReportLab
FONT_SIZE = 12

def add_text(c, text, x, y, bold=False, font_size=FONT_SIZE, center=False):
    """Adiciona texto ao PDF, formatando conforme necessário"""
    font = "Times-Bold" if bold else FONT_NAME
    c.setFont(font, font_size)
    
    if center:
        text_width = c.stringWidth(text, font, font_size)
        x = (PAGE_WIDTH - text_width) / 2  # Centraliza horizontalmente

    text_lines = simpleSplit(text, font, font_size, PAGE_WIDTH - 100)  # Divide em múltiplas linhas se necessário
    for line in text_lines:
        c.drawString(x, y, line)
        y -= font_size + 2  # Ajusta a altura para a próxima linha
    return y

def format_file_title(base_dir, file_path):
    """Formata o título do arquivo no estilo: diretório.arquivo : src.entidades.maestro"""
    relative_path = os.path.relpath(file_path, base_dir)
    formatted_path = os.path.splitext(relative_path)[0].replace(os.sep, ".")
    return f"diretório.arquivo : {formatted_path}"

def add_file_to_pdf(c, base_dir, file_path, y_position, is_first_file):
    """Adiciona o conteúdo de um arquivo ao PDF"""
    
    # Se não for o primeiro arquivo, começa em uma nova página
    if not is_first_file:
        c.showPage()
        y_position = PAGE_HEIGHT - 50  # Reinicia no topo da nova página
    
    # Adiciona título do arquivo
    title_text = format_file_title(base_dir, file_path)
    y_position = add_text(c, title_text, 50, y_position, bold=True, font_size=14)
    y_position -= 10

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                if y_position < 50:  # Se estiver perto do final da página, adiciona uma nova
                    c.showPage()
                    y_position = PAGE_HEIGHT - 50
                y_position = add_text(c, line.strip(), 50, y_position, font_size=FONT_SIZE)
            y_position -= 20
    except Exception as e:
        y_position = add_text(c, f"Erro ao ler o arquivo: {file_path}\n{str(e)}", 50, y_position, font_size=FONT_SIZE)

    return y_position

def generate_pdf(base_dir, output_filename, include_dirs, include_env=True):
    """Gera um PDF com os arquivos do projeto"""
    output_dir = "arquivos-entrega"
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_path = os.path.join(output_dir, output_filename + ".pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    
    # Adiciona o título centralizado na primeira página
    title = "Linguagem de Programação III - Entrega 1 - Guilherme Silva Sampaio"
    y_position = add_text(c, title, 50, PAGE_HEIGHT - 50, bold=True, font_size=14, center=True)
    y_position -= 40

    files_list = []
    for root, dirs, files in os.walk(base_dir):
        if "node_modules" in root:
            continue
        relative_path = os.path.relpath(root, base_dir)
        if any(relative_path.startswith(d) for d in include_dirs):
            for file in files:
                if file.endswith(".env") and not include_env:
                    continue
                files_list.append(os.path.join(root, file))
    
    files_list.sort()

    is_first_file = True
    for file_path in files_list:
        y_position = add_file_to_pdf(c, base_dir, file_path, y_position, is_first_file)
        is_first_file = False  # Depois do primeiro arquivo, os outros vão para páginas separadas
    
    # Última página com assinatura
    c.showPage()
    date_str = datetime.datetime.now().strftime("%d/%m/%Y")
    add_text(c, f"Dourados, {date_str} -- (Assinatura)", 50, PAGE_HEIGHT - 50)

    c.save()
    print(f"PDF gerado: {pdf_path}")

# Gerar os PDFs
base_dir_front = "../front-end"
base_dir_back = "../back-end"

generate_pdf(base_dir_front, "front-end", ["public", "src"], include_env=False)
generate_pdf(base_dir_back, "back-end", ["src"], include_env=True)
