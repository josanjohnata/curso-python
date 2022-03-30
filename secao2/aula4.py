"""
Tipos de dados:
str - string = texto "Assim" ou 'Assim'
int - inteiro = 123 0 -1
float - real/ponto flutuante = 1.23 3.14 -1.23
bool - booleano = True False

Python é uma linguagem de tipagem dinâmica, isso significa que o lê os dados e
indetifica o tipo de dado.
"""

print("Josan")  # O Python interpreta o texto como uma string.
print("Josan", type("Josan"))  # A função type() retorna o tipo de dado.
# Nesse caso 'str'.
print(123, type(123))  # O Python interpreta o número como um inteiro.
print(3.14, type(3.14))  # O Python interpreta o número como um float.
print(True, type(True))  # O Python interpreta o valor como um booleano.

# O typecast é o processo de converter um tipo de dado para outro.
print(int("123"))  # O Python converte o texto para um inteiro.
print(float("123.45"))  # O Python converte o texto para um float.
print(str(123))  # O Python converte o inteiro para um texto.
print(bool(123))  # O Python converte o inteiro para um booleano.

# OBS.: Não é possível converter um float para uma string ou booleano.
# Não é possível converter um inteiro para uma string ou booleano.
# Não é possível converter um booleano para um inteiro, float ou string.
# Não é possível converter um texto para um inteiro, float ou booleano.

##############################################################################

# Exercícios:
# Exiba na tela o tipo de dado de cada dado do cadastro abaixo.
# String: nome
print("Josan", type("Josan"))

# Inteiro: idade
print(30, type(30))

# Float: altura
print(1.76, type(1.76))

# Booleano: se é maior de idade
print(30 > 18, type(30 > 18))
