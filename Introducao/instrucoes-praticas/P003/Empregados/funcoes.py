

def reajusta_dez_porcento(empregados_list):
    for (index, item) in enumerate(empregados_list):
        empregados_list[index]['salario'] = round((item['salario'] * 1.1), 2)
    
def getFileContent(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def getAllEmpregados(content, empregados_list):
    for i in content.split('\n'):
        item = i.split(',')
        empregado = {'nome': item[0],
                'sobrenome': item[1],
                'ano_nascimento': int(item[2]),
                'RG': item[3],
                'ano_admissao': int(item[4]),
                'salario': float(item[5])}
        
        empregados_list.append(empregado)
        
def listEmpregados(empregados_list):
    for index, item in enumerate(empregados_list):
        nome, sobrenome, ano_nascimento, rg, ano_admissao, salario = item.values()

        print(f'{index + 1}. Nome: {nome} | Sobrenome: {sobrenome} | Ano nascimento: {ano_nascimento} | RG: {rg} | Ano admissão: {ano_admissao} | Salário: {salario}')