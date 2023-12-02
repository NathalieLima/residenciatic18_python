from modulos import *

def main():
    products_list = []
    options = ['Inserir produto',
            'Excluir produto',
            'Listar produtos',
            'Consultar produto']
    options_size = len(options)

    while True:
        setupMenu(options)
        
        opcao_usuario = int(input('\nSua opção: '))
        
        if (not (opcao_usuario > options_size)):
            print('-' * 20)
        
        match opcao_usuario:
            case 0:
                print('Fim do programa!')
                break
                
            case 1:
                moduloInserirProduto(products_list)

            case 2:
                moduloExcluirProduto(products_list)

            case 3:
                moduloListarProdutos(products_list)

            case 4:
                moduloConsultarProduto(products_list)
                
            case _:
                print('Insira um número entre 0 e', options_size)
            
        print() # Simples quebra de linha após execução de módulo


if __name__ == "__main__":
    main()