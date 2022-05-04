# Variáveis
"""
Iniciar com letra, podem conter números, _, letras maiúsculas e minúsculas
"""
name = 'Josan Johnata'
age = 30
height = 1.76
weight = 98
is_driver = age > 18
imc = round(weight / (height ** 2), 2)

print(name, 'tem', age, 'anos de idade e seu IMC é', imc)
