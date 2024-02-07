def insertRow(a, b, c):
    return f"{a}, {b}, {c}"

 
album_name = input("Ingresa el nombre del álbum: ")
while album_name == '':
    album_name = input("Ingresa el nombre del álbum: ")


artist = input("Ingresa el nombre del artista: ")
while artist == '':
    artist = input("Ingresa el nombre del artista: ")

genre = input("Ingresa el género: ")
while genre == '':
    genre = input("Ingresa el género: ")

print(insertRow(album_name, artist, genre))