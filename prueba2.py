numeros = []

# pedimos 5 números
for i in range(5):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

# el numero menor va ha ser el primero por el momento del array
menor = numeros[0]
# Recorremos y los comparamos
for numero in numeros:
    if numero < menor:
        menor = numero
# Imprimir el resultado
print("Menor:", menor)


#**Jose Julian Ramirez**#
