#Exemplo de escopo local:

def minha_funcao():
    x = 10  # Variável local, só visível dentro da função
    print(x)

minha_funcao()  # Saída: 10
print(x)  # Erro: NameError: name 'x' is not defined

#Exemplo de escopo global:

x = 10  # Variável global

def minha_funcao():
    print(x)  # Variável global acessível dentro da função

minha_funcao()  # Saída: 10

def altera_variavel_global():
    global x
    x = 20  # Modificando a variável global
    print(x)

altera_variavel_global()  # Saída: 20
print(x)  # Saída: 20 (variável global foi modificada)

#Encadeamento de Escopos (Closure):
def funcao_pai():
    x = 10

    def funcao_filha():
        print(x)  # A função filha pode acessar a variável x da função pai

    funcao_filha()

funcao_pai()  # Saída: 10
