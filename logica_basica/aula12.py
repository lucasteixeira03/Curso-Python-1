def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

nome = "Lucas Teixeira"
altura = 1.75
peso = 76

imc = calcular_imc(peso, altura)
categoria = categoria_imc(imc)

print("1° FORMA UTILIZADA COM FUNÇÕES - CLEAN CODE")
print(f"IMC de {nome} é: {imc:.2f} e ele se enquadra na categoria '{categoria}'")
print(end='\n')

nome_teste = 'Gabriel Tanabe'
altura_teste = 1.70
peso_teste = 70
imc_teste = peso_teste / (altura_teste ** 2)

print("2° FORMA UTILIZADA PADRÃO - INICIANTE")
print(f"{nome_teste} tem {altura_teste:.2f} de altura")
print(f"Pesa {peso_teste} quilos e seu IMC é: {imc_teste:.2f}")