import os
import hashlib
import subprocess

# Subprograma que busca el hash MD5 entre las imágenes de la carpeta
def buscar(carpeta, miHash):
    if not os.path.isdir(carpeta):
        print(f"La carpeta {carpeta} no existe.")
        return

    for archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, archivo)

        # Verificar si la ruta es un archivo antes de intentar abrirlo
        if not os.path.isfile(ruta_completa):
            continue
        
        print(f"Procesando archivo!: {archivo}")  # Para saber por qué imagen va
        
        hash_md5_imagen=calcularMD5(ruta_completa)
        
        if hash_md5_imagen == miHash:
            print(f"¡Coincidencia encontrada en la imagen: {archivo}!")
            print("SE ABRIRÁ STEGOSUITE, PARA EXTRAER LA FRASE HAZ LO SIGUIENTE EN LA PANTALLA QUE TE APARECERÁ: File->Open(selecciona el archivo que tiene el MD5 introducido)->Extract")
            extraer_mensaje_oculto(ruta_completa)
            return
    
    print("No se encontraron coincidencias de hash MD5.")
    
def calcularMD5(ruta_imagen):
    # Crear un objeto hash MD5
    hash_md5 = hashlib.md5()
    
    # Abrir la imagen en modo binario
    with open(ruta_imagen, "rb") as archivo:
        # Leer el archivo en bloques para no sobrecargar la memoria
        for bloque in iter(lambda: archivo.read(4096), b""):
            hash_md5.update(bloque)
    
    # Retornar el hash MD5 en formato hexadecimal
    return hash_md5.hexdigest()
    
def extraer_mensaje_oculto(ruta_imagen):
    try:
        # Abrir Stegosuite desde Python para que puedas interactuar con su GUI
        subprocess.run(["stegosuite", ruta_imagen])
        print("FIN, has debido de ver la frase en la pantalla que ha salido")
    except FileNotFoundError:
        print("No se encontró Stegosuite. Asegúrate de que está instalado y en tu PATH. (sudo apt install stegosuite)")

carpeta = input("Introduce la ruta de la carpeta: ")
miHash = input("Introduce el hash MD5 a buscar: ")

buscar(carpeta, miHash)
