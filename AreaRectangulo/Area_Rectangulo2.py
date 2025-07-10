def Area_rectangulo(base, altura):#Definimos la funcion para calcular el area del rectangulo
  return base * altura #Retornamos el resultado de la operacion

while True:
  try:
    base = float(input("Ingresa la base del rectangulo: "))#Solicitamos los datos al usuario
    altura = float(input("Ingresa la altura del rectangulo: "))#Solicitamos los datos al usuario
    print(f"El area del rectangulo es: {Area_rectangulo(base, altura)}")#Llamamos a la funcion y le pasamos los parametros
  except  ValueError:
    print("Debes ingresar un numero valido")#Si el usuario ingresa un valor no valido, se le notifica
    continue
  continuar = input("¿Desea ingresar otros datos? (Y/N): "). strip().lower()#Preguntamos si desea continuar
  if continuar != 'y':
    break

print("--------___--------")
print("Fin del programa --- Los magios")
