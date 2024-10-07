def principal(frase): 
    # Crear un diccionario para contar las letras
    contador = {}

    # Contar las apariciones de cada letra
    for letra in frase:
        if letra.isalpha():  # Verificar si es una letra
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

    # Ordenar las letras según el número de apariciones (de mayor a menor)
    letras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    # Imprimir el resultado
    print("Estas son las letras que aparecen en el texto y su cantidad")
    for letra, cantidad in letras_ordenadas:
        print(f"{letra}: {cantidad}")
    print("------------------------------------------------------------------------------------------")

    # Convertimos el diccionario en un array
    letrasTexto = [letra for letra, _ in letras_ordenadas]

    # Creamos el diccionario con las frecuencias de las letras en castellano ordenadas
    frecuenciaEsp = ['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 't', 'c', 'p', 'm', 'y', 'q', 'b', 'h', 'g', 'f', 'v', 'j', 'ñ', 'z', 'x', 'k', 'w']

    definitiva = frase
    opcion = -1  # Inicializar opcion para el bucle while

    while opcion != 0:
        print("Estas letras quedan por ser sustituidas (por orden de aparición)")
        print('|'.join(letrasTexto))

        print("Estas letras quedan por añadirse a la frase (por orden de aparición)")
        print('|'.join(frecuenciaEsp))

        opcion = int(input("ELIGE: 0=salir, 1=sustituir palabras, 2=buscar palabras 2, 3=buscar palabras 3 letras:, 4= buscar palabras 1 letra    "))
        
        if opcion == 1:
            nuevafrase = ""  # Reiniciar nuevafrase	
            sustituida=input("Que letra quieres sustituir (MAYUSCULA):   ")
            sustitucion=input("Que letra quieres añadir:   ")
            # Sustituciones en la frase
            for letra in frase:
                if letra == sustituida:  
                    nuevafrase += sustitucion 
                else:
                    nuevafrase += letra  # Dejar otras letras sin cambios

            print("--------------------------------------------------------------------------------------------------------------------")
            print("")
            print(nuevafrase)
            print("--------------------------------------------------------------------------------------------------------------------")
            print("")
            fin = input("Así ha quedado la frase tras sustituir por frecuencia, ¿te gusta? (s/n): ")
            print("--------------------------------------------------------------------------------------------------------------------")
            print("")

            if fin == 'n':  # Si no le gusta, restaurar la frase original
                nuevafrase = ""
                frase = frase_original
            elif fin == 's':  # Si le gusta, continuar con los cambios
                letrasTexto.remove(sustituida)
                frecuenciaEsp.remove(sustitucion)
                
                frase = nuevafrase
                frase_original = nuevafrase  # Actualizar frase_original con la nueva frase
                nuevafrase = ""
        elif opcion == 2:
        	palabras2=buscar2l(frase)
        	print('|'.join(palabras2))
        elif opcion == 3:
        	palabras3=buscar3l(frase)
        	print('|'.join(palabras3))
        elif opcion == 4:
        	palabras1=buscar1l(frase)
        	print('|'.join(palabras1))

           

    print("ASÍ HA QUEDADO LA FRASE")
    print(frase_original)

def buscar1l(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Filtrar palabras de 2 letras o menos
    palabras_cortas = [palabra for palabra in palabras if len(palabra) == 1]
    
    return palabras_cortas


def buscar2l(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Filtrar palabras de 2 letras o menos
    palabras_cortas = [palabra for palabra in palabras if len(palabra) == 2]
    
    return palabras_cortas
    
def buscar3l(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Filtrar palabras de 3 letras
    palabras_cortas = [palabra for palabra in palabras if len(palabra) == 3]
    
    return palabras_cortas

# Solicitar entrada al usuario
frase_usuario = input("Introduce una frase (todo en una misma línea, sin párrafos): ")
principal(frase_usuario)
