from funcoes_uteis import *

def moduloInserirProduto(products_list):
    is_valid_code = False

    while ( not is_valid_code ):
        product_code = input("Insira o código do produto: ") 

        # Verificar se o código é válido e único
        if ( isValidCode(product_code) and not isExistingCode(product_code, getAllCodes(products_list)) ):
           is_valid_code = True
        else:
           print('Este código é inválido ou já foi cadastrado.')

    product_name = input("Insira o nome do produto: ").capitalize() # Garantir que sempre comece com maiúscula
    product_price = round(float(input("Insira o preço do produto: ")), 2) # Ter duas casas decimais

    # Definir dicionário do produto
    product = {'code': product_code,
                'name': product_name,
                'price': product_price}

    # Inserir produto
    products_list.append(product)

    print('\nProduto adicionado com sucesso!')

def moduloExcluirProduto(products_list):
    product_code = input("Insira o código do produto: ") 

    # Pegar o código de todos os produtos
    products_codes = getAllCodes(products_list)

    # Verificar se código existe para removê-lo
    if ( isExistingCode(product_code, products_codes) ):
       
       # Pegar índice do produto
       product_index = getProductIndex(product_code, products_codes)

        # Remover produto
       products_list.pop(product_index)

       print('\nProduto removido com sucesso!')
    else:
       print(f'\nEste produto, referente ao código {product_code}, não existe.')

def moduloListarProdutos(products_list):
    print('Produtos cadastrados até o momento:')

    if ( len(products_list) == 0 ):
        print('Não há.')
    else:
        j = 1
        sorted_products = products_list # Utilização de variável auxiliar para não alterar valores originais

        # Sortear elementos com base no preço
        sorted_products.sort(key=lambda item: item['price'])

        for (index, item) in enumerate(sorted_products):
            # Exibir de 10 em 10
            if ( index % 10 == 0 or index == 0):
               print(f'{"-" * 10} GRUPO {j} {"-" * 10}')

               j += 1
            
            # Impressão do produto
            print(f"{index + 1}. {item['code']} - {item['name']} - {item['price']} reais")

def moduloConsultarProduto(products_list):
    product_code = input("Insira o código do produto: ") 

    # Pegar o código de todos os produtos
    products_codes = getAllCodes(products_list)

    # Verificar se código existe para removê-lo
    if ( isExistingCode(product_code, products_codes) ):
       
       # Buscar pelo preço do produto
       product_price = list(filter(lambda item: item['code'] == product_code, products_list))[0]['price']
       
       print(f'\nO produto de código {product_code} custa {product_price} reais.')
    else:
       print(f'\nEste produto, referente ao código {product_code}, não existe.')



