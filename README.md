# Uso
Recomiendo utilizar el programa desde la terminal, importando sus funciones directamente.
Para ello, primero debemos movernos al directorio donde tenemos nuestro archivo y entonces ejecutar el siguiente comando:
```bash
python or python3
```
y luego:
```python
from ejercicios import *
```
Ahora ya tenemos todas las funciones importadas, sientase libre de explorar las mismas.
## Funcionamiento
Cada función debe ser invocada como se indica en el titulo respectivo, con los paremetros que solicita.
### 1 - operaciones(a,b)
Se usa invocandola y pasandole 2 paremetros de tipo entero, la misma devuelve la suma, resta, el producto y el cociente entre ambos numeros.
```python
>>> print(operaciones(5,5))

        suma = 10
        resta = 0
        producto = 25
        cociente = 1.0   
```
### 2 - lista_ordenada()
Pide 3 números enteros por teclado, comprueba que sean distintos y devuelve una lista con los numeros ordenados.
```python
>>> lista_ordenada()
Ingrese el primer numero: 15
Ingrese el segundo numero: 45
Ingrese el tercer numero: 30
Numeros ingresados: 15, 45, 30.
'Lista ordenada: 15, 30, 45.'
```
### 3 - simula_descuento()
Una tienda ofrece un descuento del 15% sobre el total de la compra basado en el mes en transcurso. Dado un mes y un importe, calcula si corresponde aplicar un descuento y devuelve un ticket con toda la información solicitada.
```python
>>> print(simula_descuento())
Bienvenido, por favor, indique el mes actual en formato numerico: 10
Ingrese el importe a pagar: $100

                    ******************************************
                    Felicidades! Tiene un descuento disponible
                    Importe bruto: $100
                    Descuento aplicado: $15.0
                    ******************************************
                    Total: $85.0
```
### 4 - califica_alumnos()
Recibe una calificación y devuelve una cadena con información.
```python
>>> califica_alumnos()
Ingrese la calificacion: 10
'La calificación es 10 Ha obtenido una calificacion sobresaliente.'
```
### 5 - hola_5()
Imprime hola 5 veces.
```python
>>> hola_5()
hola
hola
hola
hola
hola

```
### 6 - suma_pares(numero)
Se debe invocar la funcion y pasarle un numero por parametro, se generará una lista con todos los números pares menores al número enviado, y se devuelve la suma de los mismos.
```python
>>> print(suma_pares(10))
30
```
### 7 - imprime_mes()
Recibe un mes en formato numerico y devuelve el nombre del mismo.
```python
>>> print(imprime_mes())
Ingrese un mes en formato numerico: 12
Diciembre
```
### 8 - valores()
Recibe 10 valores ingresados por teclado y devuelve la suma y el promedio de los mismos.
```python
>>> print(valores())
Ingrese un numero: 1
Ingrese un numero: 2
Ingrese un numero: 3
Ingrese un numero: 4
Ingrese un numero: 5
Ingrese un numero: 6
Ingrese un numero: 7
Ingrese un numero: 8
Ingrese un numero: 9
Ingrese un numero: 10

    suma: 55
    promedio: 5.5
```
### 9 - impares()
Devuelve la suma de todos los numeros impares debajo del 25.
```python
>>> print(impares())
169
```
