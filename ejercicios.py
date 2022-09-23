from statistics import mean

# 1
def operaciones(a,b):
    suma = a+b
    resta = a-b
    producto = a*b
    try:
        cociente = a/b 
    except ZeroDivisionError:
        return 'No se puede dividir por 0.'
    else:
        respuesta = f'''
        suma = {suma}
        resta = {resta}
        producto = {producto}
        cociente = {cociente}
        '''
    return respuesta

# 2
def lista_ordenada(numeros=[]):
    _numeros = numeros
    _puestos={0:'primer',1:'segundo',2:'tercer'}

    while len(_numeros) < 3:
        numero = input(f'Ingrese el {_puestos[len(_numeros)]} numero: ')
        if numero in _numeros:
            print('Numero invalido.')
            continue
        _numeros.append(numero.lstrip("0"))
    print(f'Numeros ingresados: {_numeros[0]}, {_numeros[1]}, {_numeros[2]}.')

    for i in _numeros:
        for j in range(len(_numeros) - 1):
            if _numeros[j] > _numeros[j+1]:
                _numeros[j], _numeros[j+1] = _numeros[j+1], _numeros[j]
    resultado = f'Lista ordenada: {_numeros[0]}, {_numeros[1]}, {_numeros[2]}.'
    return resultado

# 3
def simula_descuento():
    _mes_con_descuento = [10]
    mes_actual = int(input('Bienvenido, por favor, indique el mes actual en formato numerico: '))
    if mes_actual not in [1,2,3,4,5,6,7,8,9,10,11,12]:
        return f'Mes invalido.'
    importe = int(input('Ingrese el importe a pagar: $'))
    
    if mes_actual in _mes_con_descuento:
        return f'''
                    ******************************************
                    Felicidades! Tiene un descuento disponible
                    Importe bruto: ${importe}
                    Descuento aplicado: ${importe*0.15}
                    ******************************************
                    Total: ${importe-importe*0.15}
                '''
    return f'''
                ******************************************
                Importe a pagar: ${importe}\n            
            '''

# 4
def califica_alumnos():
    tabla_calificaciones ={
                    1:'Ha desaprobado.',
                    2:'Ha desaprobado.',
                    3:'Ha desaprobado.',
                    4:'Ha obtenido un aprobado.',
                    5:'Ha obtenido un aprobado.',
                    6:'Ha obtenido un aprobado.',
                    7:'Ha obtenido una calificacion notable.',
                    8:'Ha obtenido una calificacion notable.',
                    9:'Ha obtenido una calificacion sobresaliente.',
                    10:'Ha obtenido una calificacion sobresaliente.',
                    }
    calificacion = int(input('Ingrese la calificacion: '))
    if calificacion in tabla_calificaciones.keys():
        return f'La calificación es {calificacion} {tabla_calificaciones[calificacion]}'
    else:
        return 'Calificacion invalida.'

# 5
def hola_5():
    print('hola\n' * 5)

# 6
def suma_pares(numero):
    numeros_pares = [x for x in range(0,numero+1) if x % 2 == 0]
    return sum(numeros_pares)

# 7
def imprime_mes():
    meses = {
        1:'Enero',
        2:'Febrero',
        3:'Marzo',
        4:'Abril',
        5:'Mayo',
        6:'Junio',
        7:'Julio',
        8:'Agosto',
        9:'Septiembre',
        10:'Octubre',
        11:'Noviembre',
        12:'Diciembre'
    }
    mes = int(input('Ingrese un mes en formato numerico: '))
    if mes in meses.keys():
        return meses[mes]
    else:
        return 'Mes incorrecto.'

# 8
def valores():
    numeros = []
    while len(numeros) < 10:
        numeros.append(int(input(f'Ingrese un numero: ')))
    return f'''
    suma: {sum(numeros)}
    promedio: {mean(numeros)}
    '''

# 9
def impares():
    numeros = [x for x in range(0,26) if x % 2 != 0]
    return sum(numeros)
print(simula_descuento())