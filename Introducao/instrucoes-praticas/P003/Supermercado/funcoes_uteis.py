def setupMenu(options):
    options_size = len(options)

    for i in range(options_size + 1):
        if ( i == options_size ):
           print('0. Sair do programa')
        else:
           print(f'{i + 1}. {options[i]}')

def isValidCode(code):
  return len(code) == 13 and code.isdigit()

def getAllCodes(products_list):
    return list(map(lambda item: item['code'], products_list))

def getProductIndex(code, products_codes):
   return products_codes.index(code)
      
def isExistingCode(code, products_codes):
  return code in products_codes