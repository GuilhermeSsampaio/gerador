import os

def getDirAtual():
    return os.getcwd()

def ChangeToDirPai():
    os.chdir('..') #muda o diretório atual para o diretório pai
    return os.getcwd()

def VerifyCorrectLP3Dir():
    dirPai = ChangeToDirPai()
    nomeDir = os.path.basename(dirPai)
    if(nomeDir == 'LPIII'):
        return True
    return False

def listSubdirsOfLPIII():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Já mudou para o diretório pai (LPIII) dentro da função VerifyCorrectLP3Dir
        diretorio = getDirAtual()  # Este agora deve ser o diretório LPIII
        subDirs = []
        
        for item in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, item)
            if os.path.isdir(caminho_completo):
                subDirs.append(item)
                
        # Retorna ao diretório original
        os.chdir(dir_original)
        return subDirs
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

# Executa o código apenas se o diretório pai for LPIII
correctDir = VerifyCorrectLP3Dir()

# Como VerifyCorrectLP3Dir() já mudou para o diretório pai, voltamos para o diretório original
os.chdir('gerador')  # Assumindo que estamos no diretório 'gerador'


    
def listSubdirsOfFrontend():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Já estamos no diretório LPIII (pois VerifyCorrectLP3Dir muda para ele)
        
        # Verifica se existe um diretório frontend
        caminho_frontend = os.path.join(getDirAtual(), "front-end")
        if os.path.isdir(caminho_frontend):
            # Muda para o diretório frontend
            os.chdir(caminho_frontend)
            
            # Lista os subdiretórios do frontend
            diretorio = getDirAtual()
            subDirs = []
            
            for item in os.listdir(diretorio):
                caminho_completo = os.path.join(diretorio, item)
                if os.path.isdir(caminho_completo):
                    subDirs.append(item)
            
            # Retorna ao diretório original
            os.chdir(dir_original)
            return subDirs
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório frontend não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

def listSubdirsOfBackend():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Já estamos no diretório LPIII (pois VerifyCorrectLP3Dir muda para ele)
        
        # Verifica se existe um diretório backend
        caminho_backend = os.path.join(getDirAtual(), "back-end")
        if os.path.isdir(caminho_backend):
            # Muda para o diretório backend
            os.chdir(caminho_backend)
            
            # Lista os subdiretórios do backend
            diretorio = getDirAtual()
            subDirs = []
            
            for item in os.listdir(diretorio):
                caminho_completo = os.path.join(diretorio, item)
                if os.path.isdir(caminho_completo):
                    subDirs.append(item)
            
            # Retorna ao diretório original
            os.chdir(dir_original)
            return subDirs
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório back-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

def listFilesOfBackend():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Já estamos no diretório LPIII (pois VerifyCorrectLP3Dir muda para ele)
        
        # Verifica se existe um diretório backend
        caminho_backend = os.path.join(getDirAtual(), "back-end")
        if os.path.isdir(caminho_backend):
            # Muda para o diretório backend
            os.chdir(caminho_backend)
            
            # Lista os arquivos do backend (não diretórios)
            diretorio = getDirAtual()
            files = []
            
            for item in os.listdir(diretorio):
                caminho_completo = os.path.join(diretorio, item)
                if os.path.isfile(caminho_completo):  # Usa isfile em vez de isdir
                    files.append(item)
            
            # Retorna ao diretório original
            os.chdir(dir_original)
            return files
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório back-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

def listFilesOfFrontend():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Já estamos no diretório LPIII (pois VerifyCorrectLP3Dir muda para ele)
        
        # Verifica se existe um diretório frontend
        caminho_frontend = os.path.join(getDirAtual(), "front-end")
        if os.path.isdir(caminho_frontend):
            # Muda para o diretório frontend
            os.chdir(caminho_frontend)
            
            # Lista os arquivos do frontend (não diretórios)
            diretorio = getDirAtual()
            files = []
            
            for item in os.listdir(diretorio):
                caminho_completo = os.path.join(diretorio, item)
                if os.path.isfile(caminho_completo):  # Usa isfile em vez de isdir
                    files.append(item)
            
            # Retorna ao diretório original
            os.chdir(dir_original)
            return files
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório front-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

# Se quiser uma função mais genérica que liste arquivos de qualquer diretório:
def listFilesOfDirectory(directory_path):
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    if os.path.isdir(directory_path):
        # Muda para o diretório especificado
        os.chdir(directory_path)
        
        # Lista os arquivos (não diretórios)
        files = []
        
        for item in os.listdir():
            if os.path.isfile(item):
                files.append(item)
        
        # Retorna ao diretório original
        os.chdir(dir_original)
        return files
    else:
        return [f"Erro: Diretório {directory_path} não encontrado"]

    
# # Adicione esse código ao final do arquivo para testar a função
# if correctDir:
#     print("\nSubdiretórios de back-end:")
#     backend_dirs = listSubdirsOfBackend()
#     print(backend_dirs)
    
#     print("\nSubdiretórios de frontend:")
#     frontend_dirs = listSubdirsOfFrontend()
#     print(frontend_dirs)
    
#     print("\nArquivos do back-end:")
#     backend_files = listFilesOfBackend()
#     print(backend_files)
    
#     print("\nArquivos do front-end:")
#     frontend_files = listFilesOfFrontend() 
#     print(frontend_files)