import os
import argparse
from generate import generate_document

def main():
    # Criar um parser de argumentos de linha de comando
    parser = argparse.ArgumentParser(description='Gerador de documentos para entrega LPIII')
    parser.add_argument('--front', action='store_true', help='Gerar documento do front-end')
    parser.add_argument('--back', action='store_true', help='Gerar documento do back-end')
    parser.add_argument('--all', action='store_true', help='Gerar documentos de front-end e back-end')
    parser.add_argument('--front-dir', default='../front-end', help='Diretório base do front-end')
    parser.add_argument('--back-dir', default='../back-end', help='Diretório base do back-end')
    
    args = parser.parse_args()
    
    # Se nenhuma opção for especificada, gerar ambos os documentos
    if not (args.front or args.back or args.all):
        args.all = True
    
    print("Bem vindo ao gerador de documentação das matérias do Prof Joinville")
    print("Por enquanto só funciona em LP3, mas vai funcionar em todas as matérias")
    print("Aguarde a geração dos arquivos, serão gerados na pasta arquivos-entrega")
    
    # Verificar se os diretórios existem
    if (args.front or args.all) and not os.path.exists(args.front_dir):
        print(f"ERRO: Diretório front-end não encontrado: {args.front_dir}")
        return
        
    if (args.back or args.all) and not os.path.exists(args.back_dir):
        print(f"ERRO: Diretório back-end não encontrado: {args.back_dir}")
        return
    
    # Gerar documentos conforme solicitado
    try:
        if args.front or args.all:
            print(f"Gerando documento para o front-end a partir de {args.front_dir}...")
            generate_document(args.front_dir, "front-end", ["public", "src"], include_env=False)
            print("Documento front-end gerado com sucesso!")
            
        if args.back or args.all:
            print(f"Gerando documento para o back-end a partir de {args.back_dir}...")
            generate_document(args.back_dir, "back-end", ["src"], include_env=True)
            print("Documento back-end gerado com sucesso!")
            
    except Exception as e:
        print(f"Erro ao gerar documentos: {e}")

# Para testar se o negrito funciona
import format_docx
format_docx.test_bold_functionality()

if __name__ == "__main__":
    main()
    