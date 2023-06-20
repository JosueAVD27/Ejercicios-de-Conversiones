#Calcular el teorema de Pitágoras. h = raiz(co^2 + ca^2)
print("<<< Calcula el teorema de Pitagoras >>>")
co = float(input("Ingrese el Cateto Opuesto: "))        #Ingresa el dato del primer cateto
ca = float(input("Ingrese el Cateto adyacente: "))      #Ingresa el dato del segundo Cateto
h = ((co*co)+(ca*ca))**(1/2)                            #Realiza la operacion para obtener la hipotenusa mediante la formula
print("El valor de la Hopotenusa es: ", h)              #Entrega el resultado del calculo de la hipotenusa.