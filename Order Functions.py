# Uma "High Order Function" (HOF) é uma função que aceita outras funções como argumentos e/ou retorna funções. Em outras palavras, 
# as HOFs manipulam funções e as utilizam como parte de sua lógica. As HOFs são uma parte importante da programação funcional em Python.

#Um exemplo de HOF é a função map(), que recebe uma função e um iterável como argumentos e aplica essa função a cada elemento do iterável, 
#retornando um novo iterável com os resultados.
Exemplo de uso da função map():

def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
dobro = map(dobrar, numeros)
print(list(dobro))  # Saída: [2, 4, 6, 8, 10]
Outro exemplo é a função filter(), que filtra os elementos de um iterável com base em uma função de teste.

Exemplo de uso da função filter():

def e_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5]
pares = filter(e_par, numeros)
print(list(pares))  # Saída: [2, 4]

# As High Order Functions proporcionam maior flexibilidade e poder à programação em Python, permitindo que as funções sejam tratadas como dados 
# e aplicadas a diferentes cenários de maneira mais elegante e concisa. Elas são amplamente utilizadas em programação funcional, facilitando 
# a criação de código mais modular e de fácil manutenção.

# Funções Lambda em Python
# As funções lambda em Python são funções anônimas e pequenas que podem ser definidas em uma única linha. Elas são uma forma concisa e rápida de criar funções simples que são usadas apenas uma vez e não precisam de um nome explícito.

Sintaxe
A sintaxe para criar uma função lambda é a seguinte:

lambda argumentos: expressao
lambda: Palavra-chave que indica que estamos criando uma função lambda.
argumentos: Parâmetros da função, separados por vírgula.
expressao: Expressão que define o retorno da função.
Exemplos
Exemplo de uma função lambda que retorna o dobro de um número:

dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10
Exemplo de uma função lambda que retorna a soma de dois números:

soma = lambda a, b: a + b
print(soma(3, 7))  # Saída: 10
Utilização de Lambdas com Funções HOF
As funções lambda são frequentemente usadas com funções HOF (High Order Functions), como map(), filter() e sorted(), que aceitam funções como argumentos.

Exemplo usando map() com lambda:

numeros = [1, 2, 3, 4, 5]
dobro = map(lambda x: x * 2, numeros)
print(list(dobro))  # Saída: [2, 4, 6, 8, 10]
Exemplo usando filter() com lambda:

numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4]