print("Bienvenido a Favolist, biblioteca de tus álbumes preferidos")

while True:

    print("\n1- Agregar álbum\n2- Ver Biblioteca\n3- Borrar álbum \n0- Salir\n")
    
    election = int(input("Enter the option: "))

    if election == 0:
        break

    elif election == 1:

        album_name = input("Enter the name of the album: ")
        artist = input("Enter the name of the artist: ")
        year = input("Enter the release year: ")

        genres = []
        while True:
            genre = input("Enter the genre: ")
            genres.append(genre.title())

            new_genre = input("Has the album another genre? Y/N: ")
            new_genre = new_genre.upper()
            if new_genre == "N":
                break
            else:
                pass
        
        genres_str = ", ".join(genres)

        with open("favorite_albums_list.txt", "a+") as my_file:
            my_file.write(f"\nAlbum: {album_name}\n")
            my_file.write(f"Artist: {artist}\n")
            my_file.write(f"Year: {year}\n")
            my_file.write(f"Genre/s: {genres_str}\n")
            my_file.write("----------------------------------")
            
            my_file.seek(0)
            content = my_file.read()

        if f"Artist: {artist}" not in content:
            with open("artist_dicc.txt", "a+") as artist_file:
                artist_file.write(f"\nArtist: {artist}\n")
        else:
            pass

    elif election == 2:
        with open("favorite_albums_list.txt", "r") as my_file:
            #my_file.seek(0) no lo veo necesario, funciona sin él
            content = my_file.read()

        print(content)

# Me falta la funcion de borrar álbum, para ello debo aprender más
# También registrar el album escuchado, y la fecha en la que se escuchó
# Al registrar el album, también registrar 