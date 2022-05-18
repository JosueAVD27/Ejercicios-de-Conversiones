#Ingresar un valor en dólares y transformar en Euros y Yen.
print("Transformar de dolares a euros y yenes")
dolares = float(input("Ingrese un valor el dolares: ")) #Ingresa el valor en dolares por teclado
euro = 1.0419                                           #Determina el valor del euro
yen = 107.31982                                         #Determina el valor del yen
euros = dolares/euro                                    #Convierte el valor del dolar a euro
yenes = dolares*yen                                     #Convierte el valor del dolar a yen
print("En euros es: ", euros)                           #Entrega el valor del euro
print("En yenes es: ", yenes)                           #Entrega el valor del yen


