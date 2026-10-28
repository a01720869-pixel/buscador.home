
# Buscador de archivos

Este programa busca la palabra "home" dentro de los archivos de una carpeta y muestra las rutas donde aparece.

## Integrantes

- Integrante 1: Recorrido de carpetas y archivos.
- Integrante 2: Busqueda de la palabra "home".
- Integrante 3: Programa principal e integracion.

## Requisitos

Python 3.

## Instrucciones de ejecucion

1. Descargar el repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el comando:

python3 main.py

4. Escribir la ruta de la carpeta donde se desea buscar.
5. El programa mostrara las rutas de los archivos encontrados.

## Funcionamiento

Primero se utiliza listar_archivos(carpeta) para obtener los archivos.

Despues se utiliza buscar_palabra(archivos, "home") para encontrar coincidencias.

Finalmente se muestran las rutas encontradas o un mensaje si no hay coincidencias.
