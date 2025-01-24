#Escopo Local e Escopo Global em Python#
1. Escopo Local:
- O escopo local refere-se às variáveis que são definidas dentro de uma função.
- Essas variáveis só são acessíveis dentro da função em que foram criadas.
- Quando a função termina de ser executada, as variáveis locais deixam de existir.
- Se tentarmos acessar uma variável local fora da função, ocorrerá um erro de "NameError".
Exemplo de escopo local:

def minha_funcao():
    x = 10  # Variável local, só visível dentro da função
    print(x)

minha_funcao()  # Saída: 10
print(x)  # Erro: NameError: name 'x' is not defined

2. Escopo Global:
- O escopo global refere-se às variáveis que são definidas fora de qualquer função ou bloco de código.
- Essas variáveis são acessíveis em todo o programa, em qualquer função.
- Variáveis globais podem ser lidas (usadas) em uma função sem a necessidade de declará-las novamente, mas para modificá-las, 
é preciso usar a palavra-chave "global" para informar ao Python que queremos modificar a variável global e 
não criar uma variável local com o mesmo nome.
Exemplo de escopo global:

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
