numeros = []
numero = []
num_impar = []
num_par = []
num_pos = []
num_neg = []
zeros = []

for x in range(10):
    numero = float(input(f"Digite o {x + 1}º número: "))
    numeros.append(numero)

    if numero % 2 != 0:
        num_impar.append(numero)
    else:
        num_par.append(numero)

    if numero > 0:
        num_pos. append(numero)
    elif numero < 0:
        num_neg.append(numero)
    else:
        zeros.append(numero)

print("Essses são os números ímpares:", num_impar)
print("Essses são os números  pares:", num_par)
print("Essses são os números positivos:", num_pos)
print("Essses são os números negativos:", num_neg)
print("Todos os zeros:", zeros)
