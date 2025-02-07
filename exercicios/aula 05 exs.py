#funcao recursiva, parametro, retorno : builtins // tratamento de excecao

# try : quando esta tudo ok
# except : queremos achar as excecoes(lidar com erros)
# else: executa se nao tiver erro
# finally: sempre é executado
#
#

#3dir(_builtins_)
#help(len)


 #palavra reservada do sistema def

# def nomeDaFuncao():
#     print("funcao")
#
# nomeDaFuncao()

# def funcaoComRetorno(x=0, y=0):
#  return x + y
# print(funcaoComRetorno(10, 5))

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def calculadora(a, b, operacao):
    if operacao == '+':
        return somar(a, b)
    elif operacao == '-':
        return subtrair(a, b)
    else:
        return 'Operação inválida'

r = input('Digite a operação (+ ou -): ')
print(calculadora(10, 20, r))


