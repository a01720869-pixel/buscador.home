import os


def buscar_palabra(archivos, palabra):
    encontrados = []

    for ruta in archivos:
        ruta = os.path.abspath(ruta)      # ruta completa

        if ruta in encontrados:           # evitar repetidos
            continue

        try:
            archivo = open(ruta, "r")
            texto = archivo.read()
            archivo.close()
        except:                           # no se puede leer o es binario
            continue

        if palabra in texto:
            encontrados.append(ruta)

    return encontrados
