# Conjunto de Ejercicios Python

Este conjunto de ejercicios Python abarca diversas tareas de cálculo y conversión, desde la transformación de monedas y unidades de peso hasta cálculos geométricos y matemáticos.

## Transformación de Monedas

### Dólares a Euros y Yenes

Este ejercicio permite ingresar un valor en dólares y calcular su equivalente en euros y yenes.

```python
print("Transformar de dólares a euros y yenes")
dolares = float(input("Ingrese un valor en dólares: "))
euro = 1.0419
yen = 107.31982
euros = dolares / euro
yenes = dolares * yen
print("En euros es: ", euros)
print("En yenes es: ", yenes)
```

## Transformación de Unidades de Peso
### Libras a Kilos y Gramos
Este ejercicio permite ingresar un valor en libras y calcular su equivalente en kilos y gramos.

```python
print("<<< Transformar libras a kilos y gramos >>>")
kilo = 2.2046
gramo = 0.0022046
libras = float(input("Ingresa un peso en libras: "))
L_kilos = libras / kilo
L_gramos = libras / gramo
print("En kilos es: ", L_kilos, "K")
print("En gramos es: ", L_gramos, "g")
```

## Cálculo Matemático
### Teorema de Pitágoras
Este ejercicio calcula la hipotenusa de un triángulo rectángulo utilizando el teorema de Pitágoras.

```python
print("<<< Calcula el teorema de Pitágoras >>>")
co = float(input("Ingrese el Cateto Opuesto: "))
ca = float(input("Ingrese el Cateto adyacente: "))
h = ((co * co) + (ca * ca)) ** (1/2)
print("El valor de la Hipotenusa es: ", h)
```

## Cálculos Geométricos
### Cálculo del Área, Diámetro y Circunferencia de un Círculo
Este ejercicio permite ingresar el radio de un círculo y calcular su área, diámetro y circunferencia.

```python
print("<<< Calcular el Área, Diámetro y Circunferencia de un círculo >>>")
pi = 3.1416
radio = float(input("Ingrese el radio: "))
area = pi * (radio * radio)
L_circunferencia = 2 * pi * radio
diametro = L_circunferencia / pi
print("El área de la circunferencia es: ", area)
print("La longitud de la circunferencia es: ", L_circunferencia)
print("El diámetro de la circunferencia es: ", diametro)
```

## Contribuciones
Si deseas contribuir con ejercicios adicionales o mejoras en los existentes, ¡no dudes en enviar pull requests! Estamos abiertos a nuevas propuestas y contribuciones.

## Licencia
Este conjunto de ejercicios se encuentra bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles sobre los términos de uso.
