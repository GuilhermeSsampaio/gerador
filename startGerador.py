import os
import sys
import subprocess


def main():
    # Detecta o sistema operacional
    if sys.platform.startswith("win"):  # Windows
        venv_activate = "venv\\Scripts\\activate"
        command = f"{venv_activate} && python main.py"
        shell = True
    else:  # Linux/macOS
        venv_activate = "source venv/bin/activate"
        command = f"{venv_activate} && python main.py"
        shell = True
    
    try:
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
