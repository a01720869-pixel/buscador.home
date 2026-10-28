import os

def listar_archivos(carpeta):
    archivos = []

    for ubicacion, carpetas, nombres in os.walk(carpeta):
        for nombre in nombres:
            ruta = os.path.join(ubicacion, nombre)
            archivos.append(ruta)

    return archivos


if __name__ == "__main__":
    carpeta = input("¿Qué carpeta quieres revisar? ")
    archivos = listar_archivos(carpeta)

    for archivo in archivos:
        print(archivo)
