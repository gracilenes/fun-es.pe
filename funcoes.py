def nome_da_funcao(parametros):
    # Bloco de código da função
    # Pode conter várias instruções
    return valor_de_retorno

#Parâmetros, parâmetros nomeados, retornos
def saudacao(nome):
    print(f"Olá, {nome}!")

def saudacao(nome, sexo):
    if sexo == 'f':
        print(f"Olá, senhora {nome}!")
    elif sexo == 'm':
        print(f"Olá, senhor {nome}!")        
    else:
        print(f"Olá, {nome}!")

saudacao('José', 'm')

def saudacao(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}!")

saudacao(sobrenome="Silva", nome="João")

#Retornos em Funções
def soma(a, b):
    resultado = a + b
    return resultado

#Chamada da função com retorno:
resultado_soma = soma(3, 5)
print(resultado_soma)  # Saída: 8

def saudacao(nome):
    print(f"Olá, {nome}!")
    # Sem instrução return

resultado = saudacao("Maria")
print(resultado)  # Saída: None

#Tipagem Opcional
def soma(a, b):
    resultado = a + b
    return resultado

#Chamada da função com tipos diferentes:
resultado_soma1 = soma(3, 5)
resultado_soma2 = soma("Olá, ", "Mundo!")
print(resultado_soma1)  # Saída: 8
print(resultado_soma2)  # Saída: Olá, Mundo!

#Declaração de Tipos em Parâmetros
def soma(a: int, b: int) -> int:
    resultado = a + b
    return resultado

#Declaração de Tipo de Retorno
Para especificar o tipo de retorno da função, utiliza-se a seta -> seguida do tipo desejado após o :.
Exemplo:
def saudacao(nome: str) -> str:
    return "Olá, " + nome

#Declaração de Tipo Opcional
Exemplo sem declarações de tipo:

def multiplicacao(a, b):
    return a * b
Exemplo com declarações de tipo:

def multiplicacao(a: int, b: int) -> int:
    return a * b

#Tipos Compostos e Anotações Avançadas
from typing import List, Dict, Tuple

def processa_dados(dados: List[str]) -> Dict[str, int]:
    resultado: Dict[str, int] = {}
    for item in dados:
        resultado[item] = len(item)
    return resultado

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

#Argumentos *args e **kwargs
O *args é usado para passar um número arbitrário de argumentos posicionais para uma função. O * antes de args indica que os argumentos 
serão empacotados em uma tupla, que pode ser acessada dentro da função.

Exemplo:

def soma(*args):
    total = 0
    for num in args:
        total += num
    return total

resultado = soma(1, 2, 3, 4, 5)
print(resultado)  # Saída: 15

O **kwargs é usado para passar um número arbitrário de argumentos nomeados (keyword arguments) para uma função. O ** antes de kwargs indica que os argumentos 
nomeados serão empacotados em um dicionário, que pode ser acessado dentro da função.

Exemplo:

def saudacao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

saudacao(nome="Alice", idade=25, cidade="São Paulo")

#Utilizando ambos *args e **kwargs
Você pode utilizar *args e **kwargs juntos em uma mesma função, permitindo que ela aceite qualquer combinação de argumentos posicionais e nomeados.

Exemplo:

def exemplo(*args, **kwargs):
    print("Argumentos posicionais:")
    for arg in args:
        print(arg)

    print("\nArgumentos nomeados:")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exemplo(1, 2, 3, nome="Alice", idade=25)

#Documentação de Código e Documentação de Funções em Python
A documentação em Python é uma prática importante para tornar o código mais legível, facilitar a manutenção e colaboração entre desenvolvedores. 
A documentação pode ser feita de diferentes formas, incluindo comentários explicativos no código e docstrings (strings de documentação) 
para descrever funções, módulos e classes.

#Comentários:
Comentários são trechos de texto que explicam o funcionamento do código. Eles são precedidos pelo caractere # e são ignorados pelo interpretador Python, ou seja, não afetam a execução do programa. Comentários são úteis para adicionar notas explicativas, esclarecimentos e dicas para outras pessoas (incluindo você mesmo no futuro) que lerão o código.

Exemplo de comentário:

# Calcula a média de uma lista de números
def calcular_media(lista):
    total = sum(lista)
    media = total / len(lista)
    return media

#Docstrings (Strings de Documentação)
As docstrings são strings que descrevem o propósito e o comportamento de funções, módulos ou classes em Python. Elas são colocadas logo após 
a definição de uma função, módulo ou classe, entre três aspas (simples ou duplas) e permitem que você escreva uma descrição mais detalhada da funcionalidade.

Exemplo de docstring em uma função:

def calcular_media(lista):
    """
    Calcula a média de uma lista de números.

    Parâmetros:
    lista (list): Uma lista contendo números para calcular a média.

    Retorna:
    float: A média dos números na lista.
    """
    total = sum(lista)
    media = total / len(lista)
    return media