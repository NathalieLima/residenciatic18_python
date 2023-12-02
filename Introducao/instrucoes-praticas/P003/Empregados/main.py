from funcoes import *
import os

def main():
    empregados_list = []
    
    # Pegar arquivo e diretório atual para definir caminho do arquivo
    file_name = "email.txt"
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, file_name)

    # Ler e retornar conteúdo presente no arquivo
    content = getFileContent(file_path)

    # Pegar empregado
    getAllEmpregados(content, empregados_list)

    # Listar antes do reajuste
    print('-' * 15, 'ANTES', '-' * 15)
    listEmpregados(empregados_list)

    # Reajuste dos salários
    reajusta_dez_porcento(empregados_list)

    # Listar depois do reajuste
    print('-' * 15, 'DEPOIS', '-' * 15)
    listEmpregados(empregados_list)


if __name__ == "__main__":
    main()