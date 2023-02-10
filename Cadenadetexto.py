
Palabra = str(input("Introduzca el texto para continuar: ").split())
while (len(Palabra) > 40) or (Palabra.isalpha()):
        Palabra = (input("Elija nuevamente: "))
else:
        print (Palabra)

## ENTRADA= "ejemplo de texto"
## SALIDA = ['ejemplo', 'de', 'texto']
