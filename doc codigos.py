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