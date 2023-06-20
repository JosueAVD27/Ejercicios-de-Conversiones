#Encontrar el diámetro, la circunferencia y el área del círculo. 
# area = pi*radio^2, L_circunferencia = 2pi*radio, diametro = L_circunferencia/pi
print("<<< Calcular el Area, Diametro y Circunferencia de un circulo >>>")
pi = 3.1416                                                         #Define el valor de PI
radio = float(input("Ingrese el radio: "))                          #Pide por teclado el radio
area = pi * (radio*radio)                                           #Realiza los calculos en base a la formula del area
L_Circunferencia = 2*pi*radio                                       #Realiza los calcilos en base a la formula de la longitud de la circunferencia
diametro = L_Circunferencia/pi                                      #Realiza los calcilos en base a la formula del diametro
print("El area de la circunferencia es: ", area)                    #Muestra los resultados del area
print("La longitud de la circunferencia es: ", L_Circunferencia)    #Muestra los resultados de la longitud de la circunferencia
print("El diametro de la circunferencia es: ", diametro)            #Muestra los resultados del diametro