from listagem import *

def sub_listagem():
    
    print("Diretório atual:", getDirAtual())
    
    if VerifyCorrectLP3Dir():
        print("Estamos em um subdiretório de LPIII")
        
        print("\nSubdiretórios de LPIII:")
        lpiii_dirs = listSubdirsOfLPIII()
        print(lpiii_dirs)
        
        print("\nSubdiretórios de back-end:")
        backend_dirs = listSubdirsOfBackend()
        print(backend_dirs)
        
        print("\nSubdiretórios de front-end:")
        frontend_dirs = listSubdirsOfFrontend()
        print(frontend_dirs)
    else:
        print("Não estamos em um subdiretório de LPIII")
        
        
def getDirsToCopy():
    # Listas de diretórios que devem ser excluídos (não copiados)
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

    # Obtém todos os diretórios
    dirs_backend = listSubdirsOfBackend()
    dirs_frontend = listSubdirsOfFrontend()
    
    # Filtra os diretórios, removendo os que estão na lista de exclusão
    filtered_backend = [dir_name for dir_name in dirs_backend if dir_name not in exclude_dirs and not dir_name.startswith('.')]
    filtered_frontend = [dir_name for dir_name in dirs_frontend if dir_name not in exclude_dirs and not dir_name.startswith('.')]
    
    # Retorna um dicionário com os diretórios filtrados
    return {
        'backend': filtered_backend,
        'frontend': filtered_frontend
    }

def getFilesToCopy():
    # Lista de extensões ou arquivos específicos a serem excluídos
    exclude_extensions = ['.log', '.tmp', '.cache']
    exclude_files = [
        '.DS_Store',
        # '.env', aqui tem que ver pq no back precisa dele
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
    
    
    # Obtém todos os arquivos
    files_backend = listFilesOfBackend() if not isinstance(listFilesOfBackend(), list) or "Erro" not in listFilesOfBackend()[0] else []
    files_frontend = listFilesOfFrontend() if not isinstance(listFilesOfFrontend(), list) or "Erro" not in listFilesOfFrontend()[0] else []
    
    # Filtra os arquivos, removendo os que estão na lista de exclusão ou têm extensões excluídas
    filtered_backend = []
    for file in files_backend:
        # Verifica se o arquivo não está na lista de exclusão
        if file not in exclude_files:
            # Verifica se a extensão do arquivo não está na lista de extensões excluídas
            extension = os.path.splitext(file)[1].lower()
            if extension not in exclude_extensions:
                filtered_backend.append(file)
    
    filtered_frontend = []
    for file in files_frontend:
        # Verifica se o arquivo não está na lista de exclusão
        if file not in exclude_files:
            # Verifica se a extensão do arquivo não está na lista de extensões excluídas
            extension = os.path.splitext(file)[1].lower()
            if extension not in exclude_extensions:
                filtered_frontend.append(file)
    
    # Retorna um dicionário com os arquivos filtrados
    return {
        'backend': filtered_backend,
        'frontend': filtered_frontend
    }

def listSubdirsOfBackendSrc():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Verifica se existe um diretório backend
        caminho_backend = os.path.join(getDirAtual(), "back-end")
        if os.path.isdir(caminho_backend):
            # Verifica se existe a pasta src no backend
            caminho_src = os.path.join(caminho_backend, "src")
            if os.path.isdir(caminho_src):
                # Muda para o diretório src do backend
                os.chdir(caminho_src)
                
                # Lista os subdiretórios do src
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
                return ["Erro: Diretório src não encontrado em back-end"]
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório back-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

def listSubdirsOfFrontendSrc():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Verifica se existe um diretório frontend
        caminho_frontend = os.path.join(getDirAtual(), "front-end")
        if os.path.isdir(caminho_frontend):
            # Verifica se existe a pasta src no frontend
            caminho_src = os.path.join(caminho_frontend, "src")
            if os.path.isdir(caminho_src):
                # Muda para o diretório src do frontend
                os.chdir(caminho_src)
                
                # Lista os subdiretórios do src
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
                return ["Erro: Diretório src não encontrado em front-end"]
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório front-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

def listContentOfFrontendPublic():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Verifica se existe um diretório frontend
        caminho_frontend = os.path.join(getDirAtual(), "front-end")
        if os.path.isdir(caminho_frontend):
            # Verifica se existe a pasta public no frontend
            caminho_public = os.path.join(caminho_frontend, "public")
            if os.path.isdir(caminho_public):
                # Muda para o diretório public do frontend
                os.chdir(caminho_public)
                
                # Lista todo o conteúdo (arquivos e diretórios) do public
                diretorio = getDirAtual()
                content = os.listdir(diretorio)
                
                # Retorna ao diretório original
                os.chdir(dir_original)
                return content
            else:
                # Retorna ao diretório original
                os.chdir(dir_original)
                return ["Erro: Diretório public não encontrado em front-end"]
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório front-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

def listFilesOfBackendSrc():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Verifica se existe um diretório backend
        caminho_backend = os.path.join(getDirAtual(), "back-end")
        if os.path.isdir(caminho_backend):
            # Verifica se existe a pasta src no backend
            caminho_src = os.path.join(caminho_backend, "src")
            if os.path.isdir(caminho_src):
                # Muda para o diretório src do backend
                os.chdir(caminho_src)
                
                # Lista os arquivos (não diretórios) do src
                diretorio = getDirAtual()
                files = []
                
                for item in os.listdir(diretorio):
                    caminho_completo = os.path.join(diretorio, item)
                    if os.path.isfile(caminho_completo):  # Filtra apenas arquivos
                        files.append(item)
                
                # Retorna ao diretório original
                os.chdir(dir_original)
                return files
            else:
                # Retorna ao diretório original
                os.chdir(dir_original)
                return ["Erro: Diretório src não encontrado em back-end"]
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório back-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

def listFilesOfFrontendSrc():
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII
    if VerifyCorrectLP3Dir():
        # Verifica se existe um diretório frontend
        caminho_frontend = os.path.join(getDirAtual(), "front-end")
        if os.path.isdir(caminho_frontend):
            # Verifica se existe a pasta src no frontend
            caminho_src = os.path.join(caminho_frontend, "src")
            if os.path.isdir(caminho_src):
                # Muda para o diretório src do frontend
                os.chdir(caminho_src)
                
                # Lista os arquivos (não diretórios) do src
                diretorio = getDirAtual()
                files = []
                
                for item in os.listdir(diretorio):
                    caminho_completo = os.path.join(diretorio, item)
                    if os.path.isfile(caminho_completo):  # Filtra apenas arquivos
                        files.append(item)
                
                # Retorna ao diretório original
                os.chdir(dir_original)
                return files
            else:
                # Retorna ao diretório original
                os.chdir(dir_original)
                return ["Erro: Diretório src não encontrado em front-end"]
        else:
            # Retorna ao diretório original
            os.chdir(dir_original)
            return ["Erro: Diretório front-end não encontrado em LPIII"]
    else:
        return ["Erro: Não estamos em um subdiretório de LPIII"]

# Função para obter arquivos de src com filtragem de tipos excluídos
def getFilesToCopyFromSrc():
    # Lista de extensões ou arquivos específicos a serem excluídos
    exclude_extensions = ['.log', '.tmp', '.cache']
    exclude_files = [
        '.DS_Store',
        'tsconfig.json',
        '.env.local',
        '.env.example',
        '.gitignore',
    ]
    
    # Obtém todos os arquivos de src
    files_backend_src = listFilesOfBackendSrc() if not isinstance(listFilesOfBackendSrc(), list) or "Erro" not in listFilesOfBackendSrc()[0] else []
    files_frontend_src = listFilesOfFrontendSrc() if not isinstance(listFilesOfFrontendSrc(), list) or "Erro" not in listFilesOfFrontendSrc()[0] else []
    
    # Filtra os arquivos, removendo os que estão na lista de exclusão ou têm extensões excluídas
    filtered_backend_src = []
    for file in files_backend_src:
        if file not in exclude_files:
            extension = os.path.splitext(file)[1].lower()
            if extension not in exclude_extensions:
                filtered_backend_src.append(file)
    
    filtered_frontend_src = []
    for file in files_frontend_src:
        if file not in exclude_files:
            extension = os.path.splitext(file)[1].lower()
            if extension not in exclude_extensions:
                filtered_frontend_src.append(file)
    
    # Retorna um dicionário com os arquivos filtrados
    return {
        'backend_src': filtered_backend_src,
        'frontend_src': filtered_frontend_src
    }

# Atualização na função test_filtering para incluir as novas funções
def test_filtering():
    print("\nDiretórios filtrados para cópia:")
    dirs_to_copy = getDirsToCopy()
    print("Backend:", dirs_to_copy['backend'])
    print("Frontend:", dirs_to_copy['frontend'])
    
    print("\nArquivos filtrados para cópia:")
    files_to_copy = getFilesToCopy()
    print("Backend:", files_to_copy['backend'])
    print("Frontend:", files_to_copy['frontend'])
    
    print("\nSubdiretórios de src do back-end:")
    backend_src_dirs = listSubdirsOfBackendSrc()
    print(backend_src_dirs)
    
    print("\nArquivos da pasta src do back-end:")
    backend_src_files = listFilesOfBackendSrc()
    print(backend_src_files)
    
    print("\nSubdiretórios de src do front-end:")
    frontend_src_dirs = listSubdirsOfFrontendSrc()
    print(frontend_src_dirs)
    
    print("\nArquivos da pasta src do front-end:")
    frontend_src_files = listFilesOfFrontendSrc()
    print(frontend_src_files)
    
    print("\nConteúdo de public do front-end:")
    public_content = listContentOfFrontendPublic()
    print(public_content)
    
    print("\nArquivos filtrados de src para cópia:")
    src_files_to_copy = getFilesToCopyFromSrc()
    print("Back-end src:", src_files_to_copy['backend_src'])
    print("Front-end src:", src_files_to_copy['frontend_src'])


test_filtering()

def recursivelyListDirContent(directory_path, relative_path=""):
    """Lista recursivamente o conteúdo de um diretório, incluindo subdiretórios e arquivos.
    Retorna uma estrutura de dados com a hierarquia das pastas e arquivos.
    """
    # Salva o diretório atual para restaurar depois
    dir_original = getDirAtual()
    
    result = {
        'path': relative_path,
        'directories': [],
        'files': []
    }
    
    if os.path.isdir(directory_path):
        # Muda para o diretório especificado
        os.chdir(directory_path)
        
        # Lista todo o conteúdo
        for item in os.listdir():
            # Caminho completo do item atual
            item_path = os.path.join(directory_path, item)
            # Caminho relativo para uso na estrutura de dados
            item_relative_path = os.path.join(relative_path, item).replace('\\', '/')
            
            if os.path.isdir(item):
                # Se for um diretório, recursivamente lista seu conteúdo
                subdir_content = recursivelyListDirContent(
                    item_path, item_relative_path)
                result['directories'].append(subdir_content)
            elif os.path.isfile(item):
                # Se for um arquivo, adiciona à lista de arquivos
                result['files'].append({
                    'name': item,
                    'path': item_relative_path
                })
        
        # Retorna ao diretório original
        os.chdir(dir_original)
        return result
    else:
        # Se não for um diretório válido, retorna a estrutura vazia
        os.chdir(dir_original)
        return result

def recursivelyListBackendSrc():
    """Lista recursivamente o conteúdo da pasta src do back-end"""
    # Salva o diretório atual
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII (sem mover-se permanentemente)
    if VerifyCorrectLP3Dir():
        # Voltamos ao diretório original após a verificação
        os.chdir(dir_original)
        
        # Obtém o caminho do diretório LPIII
        lpiii_dir = os.path.join(getDirAtual(), "..")
        # Verifica se existe um diretório backend
        caminho_backend = os.path.join(lpiii_dir, "back-end")
        if os.path.isdir(caminho_backend):
            # Verifica se existe a pasta src no backend
            caminho_src = os.path.join(caminho_backend, "src")
            if os.path.isdir(caminho_src):
                # Chama a função recursiva, começando da pasta src
                return recursivelyListDirContent(caminho_src, "src")
            else:
                return {"error": "Diretório src não encontrado em back-end"}
        else:
            return {"error": "Diretório back-end não encontrado em LPIII"}
    else:
        # Restaura o diretório original mesmo em caso de erro
        os.chdir(dir_original)
        return {"error": "Não estamos em um subdiretório de LPIII"}

def recursivelyListFrontendSrc():
    """Lista recursivamente o conteúdo da pasta src do front-end"""
    # Salva o diretório atual
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII (sem mover-se permanentemente)
    if VerifyCorrectLP3Dir():
        # Voltamos ao diretório original após a verificação
        os.chdir(dir_original)
        
        # Obtém o caminho do diretório LPIII
        lpiii_dir = os.path.join(getDirAtual(), "..")
        # Verifica se existe um diretório frontend
        caminho_frontend = os.path.join(lpiii_dir, "front-end")
        if os.path.isdir(caminho_frontend):
            # Verifica se existe a pasta src no frontend
            caminho_src = os.path.join(caminho_frontend, "src")
            if os.path.isdir(caminho_src):
                # Chama a função recursiva, começando da pasta src
                return recursivelyListDirContent(caminho_src, "src")
            else:
                return {"error": "Diretório src não encontrado em front-end"}
        else:
            return {"error": "Diretório front-end não encontrado em LPIII"}
    else:
        # Restaura o diretório original mesmo em caso de erro
        os.chdir(dir_original)
        return {"error": "Não estamos em um subdiretório de LPIII"}

def recursivelyListFrontendPublic():
    """Lista recursivamente o conteúdo da pasta public do front-end"""
    # Salva o diretório atual
    dir_original = getDirAtual()
    
    # Verifica se estamos em um subdiretório de LPIII (sem mover-se permanentemente)
    if VerifyCorrectLP3Dir():
        # Voltamos ao diretório original após a verificação
        os.chdir(dir_original)
        
        # Obtém o caminho do diretório LPIII
        lpiii_dir = os.path.join(getDirAtual(), "..")
        # Verifica se existe um diretório frontend
        caminho_frontend = os.path.join(lpiii_dir, "front-end")
        if os.path.isdir(caminho_frontend):
            # Verifica se existe a pasta public no frontend
            caminho_public = os.path.join(caminho_frontend, "public")
            if os.path.isdir(caminho_public):
                # Chama a função recursiva, começando da pasta public
                return recursivelyListDirContent(caminho_public, "public")
            else:
                return {"error": "Diretório public não encontrado em front-end"}
        else:
            return {"error": "Diretório front-end não encontrado em LPIII"}
    else:
        # Restaura o diretório original mesmo em caso de erro
        os.chdir(dir_original)
        return {"error": "Não estamos em um subdiretório de LPIII"}

def printDirectoryStructure(structure, indent=0):
    """Função auxiliar para imprimir a estrutura hierárquica de forma legível"""
    if 'error' in structure:
        print(structure['error'])
        return
    
    # Imprime o caminho atual
    print(' ' * indent + f"📁 {structure['path'] or 'root'}")
    
    # Imprime as subpastas (recursivamente)
    for directory in structure['directories']:
        printDirectoryStructure(directory, indent + 4)
    
    # Imprime os arquivos
    for file in structure['files']:
        print(' ' * (indent + 4) + f"📄 {file['name']}")

# Função de teste atualizada para incluir a visualização recursiva
def test_recursive_structure():
    print("\n===== Estrutura recursiva da pasta src do back-end =====")
    backend_structure = recursivelyListBackendSrc()
    printDirectoryStructure(backend_structure)
    
    print("\n===== Estrutura recursiva da pasta src do front-end =====")
    frontend_structure = recursivelyListFrontendSrc()
    printDirectoryStructure(frontend_structure)
    
    print("\n===== Estrutura recursiva da pasta public do front-end =====")
    public_structure = recursivelyListFrontendPublic()
    printDirectoryStructure(public_structure)


test_recursive_structure()