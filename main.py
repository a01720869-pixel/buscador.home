
from recorrido import listar_archivos
from buscar_palabra import buscar_palabra

def main():
    carpeta = input("Escribe la carpeta donde quieres buscar: ").strip()

    if not carpeta:
        print("Error: debes ingresar una carpeta.")
        return

    archivos = listar_archivos(carpeta)
    encontrados = buscar_palabra(archivos, "home")

    if encontrados:
        print("Archivos donde se encontro 'home':")
        for archivo in encontrados:
            print(archivo)
    else:
        print("No se encontraron coincidencias.")

if __name__ == "__main__":
    main()
