# Gerador de Documentação Automática

Este projeto gera documentos Word e PDF contendo códigos-fonte organizados a partir de diretórios específicos, formatando os arquivos corretamente e incluindo uma assinatura ao final.

## Funcionalidades

- Gera um documento `.docx` e um `.pdf` automaticamente.
- Ordena arquivos e pastas alfabeticamente.
- Formata corretamente os títulos e o conteúdo dos arquivos.
- Ignora diretórios `node_modules` e arquivos `.env` (exceto quando explicitamente solicitado).
- Inclui cabeçalho centralizado e um rodapé com local, data e assinatura.

## Tecnologias Utilizadas

- Python
- `python-docx` (para gerar documentos Word)
- `docx2pdf` (para converter Word para PDF)

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Como Usar

Execute o script principal para gerar os documentos:

```sh
python script.py
```

Os arquivos serão gerados na pasta raiz do projeto.

## Estrutura dos Arquivos Gerados

- O documento gerado contém um cabeçalho com o título do trabalho.
- Cada arquivo é listado em uma página separada com seu nome formatado como `diretório.arquivo : nome_do_arquivo`.
- No final, há uma seção com a data e um espaço para assinatura.

## Personalização

- Para incluir arquivos `.env`, altere o parâmetro `include_env` para `True` na função `generate_document`.
- Para adicionar novos diretórios, modifique a lista `include_dirs`.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
