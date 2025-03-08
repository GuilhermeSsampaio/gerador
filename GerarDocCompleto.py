import os
import sys
import subprocess


def main():
    # Cria o ambiente virtual
    # command = "python -m venv venv"
    
    # try:
    #     # print("Criando ambiente virtual...")
    #     subprocess.run(command, shell=True, check=True)
    # except subprocess.CalledProcessError as e:
    #     print(f"Erro ao criar o ambiente virtual: {e}")
    #     sys.exit(1)

    # Verifica se o ambiente virtual foi criado corretamente
    if not os.path.exists("venv"):
        print("Erro: O ambiente virtual não foi criado.")
        sys.exit(1)

    # Detecta o sistema operacional
    if sys.platform.startswith("win"):  # Windows
        venv_activate = "venv\\Scripts\\activate"
        pip_install = "venv\\Scripts\\pip install -r requirements.txt"
        command = f"{venv_activate} && {pip_install} && python main.py"
        shell = True
    else:  # Linux/macOS
        venv_activate = "source venv/bin/activate"
        pip_install = "pip install -r requirements.txt"
        command = f"{venv_activate} && {pip_install} && python main.py"
        shell = True

    try:
        print("Ativando ambiente virtual, instalando dependências e executando main.py...")
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")
        sys.exit(1)

    # Executa o script Node.js
    command = "node screenshot_form.js"
    try:
        print("Executando screenshot_form.js...")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script Node.js: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()