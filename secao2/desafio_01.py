"""
* Criar variáveis para armazenar nome(str) e idade(int),
* altura(float) e peso(float) de uma pessoa.
* Criar variável com o ano atual(int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
import datetime


name = "Johnata Pontes"
age = 30
height = 1.76
weight = 80.0
current_year = datetime.date.today().year
birth_year = current_year - age
imc = weight / (height ** 2)

print(f"{name} tem {age} anos, tem {height} de altura e pesa {weight}Kg.")
print(f"O IMC de {name} é {imc:.2f}.")
print(f"{name} nasceu em {birth_year}.")
