#Ingresar un valor en libras y transformarlo a kilos y gramos
print("<<< Transformar libras a kilos y gramos >>>")
kilo = 2.2046                                           #Definimos el valor de un kilo
gramo = 0.0022046                                       #Definimos el valor de gramo
libras = float(input("Ingresa un peso en libras: "))    #Mandamos a ingresar las libras que desea convertir
L_kilos = libras/kilo                                   #Hacemos la conversion de libras a kilos
L_gramos = libras/gramo                                 #Hacemos la conversion de libras a gramos
print("En kilos es: ", L_kilos, "K")                    #Entrega el resultado de la conversion en kilos
print("En gramos es: ", L_gramos, "g")                  #Entrega el resultado de la conversion en gramos