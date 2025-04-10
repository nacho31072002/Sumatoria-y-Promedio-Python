lista_numeros_ingresados = []

while True:
  ingresar_numeros = float(input('Ingrese numeros para suma y promedio.(Cortar numeros con 0): '))
  if ingresar_numeros == 0:
    break
  lista_numeros_ingresados.append(ingresar_numeros)
  suma = sum(lista_numeros_ingresados)
  promedio = (sum(lista_numeros_ingresados)) / len(lista_numeros_ingresados)

print(f'La lista de numeros es de: {lista_numeros_ingresados}')
print(f'La suma de los elementos es de: {suma}')
print(f'El promedio de los elementos es de: {promedio}')
