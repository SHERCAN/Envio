palabra = input('Escribe tu palabra: ')
oportunidades = 3
letras = 0
while True:
    longitud = len(palabra)
    print('La palabra tiene {} letras'.format(longitud))
    print('Te quedan {} intentos'.format(oportunidades))
    print('Has encontrado {}'.format(letras))
    letra = input('Escribe una letra: ')
    if palabra.count(letra) > 0:
        print('Has encontrado una letra: ')
        letras += palabra.count(letra)
    else:
        print('No acertaste')
        oportunidades -= 1
    if oportunidades == 0:
        print('No pudiste baboso')
        break
    if letras == longitud:
        print('Has ganado tio')
        break
