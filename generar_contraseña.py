import random      

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D']        ##creo la base de caracteres que utilizaré
    minusculas =['e', 'f', 'g', 'h']
    simolos = ['!', '#', '$', '&']
    numeros = ['9', '1', '8', '2']

    caracteres = mayusculas + minusculas + simolos + numeros    ##determino como se creará los carateres

    contrasena = []      ##utilizo un variable vacía contraseña

    for i in range(8):        #utilizo un ciclo for con un rango de 8 caracteres para formar la contraseña
        caracter_random = random.choice(caracteres)  ##selecciona al azar dentro de caracteres que se encuentran en la base
        contrasena.append(caracter_random)     ##se agrea a la variable contraseña, el caracter ramdom creado    
    
    contrasena = ''.join(contrasena)   ## join convierte una lista en una cadena formada por los elementos de la lista
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()