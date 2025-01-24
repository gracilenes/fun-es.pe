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