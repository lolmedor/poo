def uso_if():
    x = int(input("Ingresa un entero, por favor: "))
    if x < 0:
      x = 0
      print('Negativo cambiado a cero')
    elif x == 0:
      print('Cero')
    elif x == 1:
      print('Uno')
    else:
      print('Ninguna opcion')
    x='10'
    print("x es entero") if type(x)==int else print("x es tring")
#uso_if()

def vocales(frase):
     for car in frase:
         if car in('a','e','i','o','u','M'):
            print(car)

#vocales("Maria se fue")

