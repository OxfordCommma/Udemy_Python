from datetime import datetime

def leer_lista_list():
    with open("favorite_albums_list.txt", "r") as my_file:
        lineas = my_file.readlines()
        return lineas

print("Bienvenido a Favolist, biblioteca de tus álbumes preferidos")

while True:

    print("\n1- Agregar álbum\n2- Ver Biblioteca\n3- Borrar álbum \n0- Salir\n")
    
    election = int(input("Ingresa la opcion: "))

    if election == 0:
        break

    elif election == 1:

        album_name = input("Ingresa el nombre del álbum: ")
        artist = input("Ingresa el nombre del artista: ")
        year = input("Ingresa el año de lanzamiento: ")

        genres = []
        while True:
            genre = input("Ingresa el género: ")
            genres.append(genre.title())

            new_genre = input("¿El álbum se considera de otro género más? S/N: ")
            new_genre = new_genre.upper()
            if new_genre == "N":
                break
            else:
                pass
        
        genres_str = ", ".join(genres)

        valoracion = input("Ingresa tu valoración: ")

        if isinstance(int(leer_lista_list()[-2]), int): # no funciono
            id = int(leer_lista_list()[-2]) + 1
        else:
            id = 0
            

        with open("favorite_albums_list.txt", "a+") as my_file:
            my_file.write(f"\nÁlbum: {album_name}\n")
            my_file.write(f"Artista: {artist}\n")
            my_file.write(f"Año: {year}\n")
            my_file.write(f"Genero/s: {genres_str}\n")
            my_file.write(f"Valoración: {valoracion}\n")
            my_file.write(f"Registrado en: {str(datetime.now())}\n")
            my_file.write(f"{str(id)}")
            my_file.write("----------------------------------")
            
            
            my_file.seek(0)
            content = my_file.read()

        if f"Artist: {artist}" not in content:
            with open("artists_dicc.txt", "a+") as artist_file:
                artist_file.write(f"\nArtist: {artist}\n")
        else:
            pass

    elif election == 2:
        with open("favorite_albums_list.txt", "r") as my_file:
            content = my_file.read()

        print(content)

    elif election == 3:

        album_a_borrar = input("Elija el álbum a borrar: ")

        contador = 0
        new_file = []

        for linea in leer_lista_list():

            if contador > 0:
                contador -= 1
                continue

            if album_a_borrar in linea:
                contador = 6

            else:
                new_file.append(linea)
                       
        with open("favorite_albums_list.txt", "w") as my_file:
            for linea in new_file:
                my_file.write(linea)

# Añadir índices a cada entrada