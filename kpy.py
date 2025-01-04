# Escreva um programa em Python que solicita ao usuário para
# digitar seu nome, o valor do seu salário mensal e o valor
# do bônus que recebeu. O programa deve, então, imprimir uma
# mensagem saudando o usuário pelo nome e informando o valor
# do salário em comparação com o bônus recebido.
#
# Instruções:
# 1. O programa deve começar solicitando ao usuário que insira
# seu nome.
#
# 2. Em seguida, o programa deve pedir ao usuário para inserir
# o valor do seu salário. Considere que este valor pode ser
# um número decimal.
#
# 3. Depois, o programa deve solicitar a porcentagem do bônus
# recebido pelo usuário, que também pode ser um número decimal.
#
# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
#
# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte
# formato: "Olá [nome], o seu valor bônus foi de 5000".
#
# 6. Salve esse script python como kpi.py
#
# 7. Faça uma documentação simples de como executar esse programa,
# utilize o README.
#
# 8. Salve no Git e no Github.

# Coletando o nome do usuario
nome_do_usuario = input("Digite o nome do usuário: ")

# Coletando o valor do salário
valor_salario = float(input("Digite o valor do salário: "))

# Calculando o bônus do usuário
valor_bonus = 1000 + valor_salario * 1.5

# Retornando o resultado
print(f"Olá {nome_do_usuario}, o seu bônus foi de {valor_bonus}.")
