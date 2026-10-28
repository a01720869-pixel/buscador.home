from buscar import buscar_palabra

# crear archivos de prueba
with open("a.txt", "w") as f:
    f.write("mi home")

with open("b.txt", "w") as f:
    f.write("nada aqui")

with open("bin.dat", "wb") as f:
    f.write(b"\xff\xfe\x00home")

lista = ["a.txt", "b.txt", "a.txt", "no_existe.txt", "bin.dat"]
print(buscar_palabra(lista, "home"))
