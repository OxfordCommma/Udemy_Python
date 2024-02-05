import sqlite3 as sql
from datetime import date
import os

def createDB():
    conn = sql.connect("albums.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE albums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        album_name text,
        artist text,
        genre text,
        release_year integer,
        score integer,
        timestamp date
        )
        """
    )
    conn.commit()
    conn.close()

def getFields():
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = "PRAGMA table_info(albums)"
    #instruccion = f"UPDATE albums SET {column}={newValue} WHERE id={albumId}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()

    fields = {}
    index = 1
    for field in datos:
        if field[1] not in fields.values():
            #fields.append(field[1])
            fields[index] = field[1]
            index = index + 1

    conn.commit()
    conn.close()

    return fields

def insertRow(album_name, artist, genre, release_year, score, timestamp):
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = "INSERT INTO albums (album_name, artist, genre, release_year, score, timestamp) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(instruccion, (album_name, artist, genre, release_year, score, timestamp))
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM albums"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    for album in datos:
        print(album)

def insertRows(albumsList):
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO albums VALUES (?, ?, ?, ?, ?)"
    cursor.executemany(instruccion, albumsList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM albums ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def searchByName(artist_name):
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM albums WHERE artist LIKE '{artist_name}%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def modifyAlbum(column, newValue, albumId):
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE albums SET {getFields()[column]}=? WHERE id=?"
    cursor.execute(instruccion, (newValue, albumId))
    conn.commit()
    conn.close()

def deleteRows(artist_id):
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM albums WHERE id = {artist_id}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteAllRows():
    conn = sql.connect("albums.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM albums"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    
    if os.path.exists("albums.db"):
        pass
    else:
        createDB()
        createTable()

    print("Bienvenido a Listify")
    while True:
        
        print("\n1- Agregar álbum\n2- Ver Biblioteca\n3- Borrar álbum \n4- Borrar toda la biblioteca (test) \n5- Modificar album \n0- Salir\n")

        election = int(input("Ingresa la opcion: "))

        if election == 0:
            break

        elif election == 1:

            album_name = input("Ingresa el nombre del álbum: ")
            artist = input("Ingresa el nombre del artista: ")
            genre = input("Ingresa el género: ")
            year = int(input("Ingresa el año de lanzamiento: "))
            score = int(input("Ingresa tu valoración: "))
            timestamp = date.today()

            insertRow(album_name, artist, genre, year, score, timestamp)

        elif election == 2:
            readRows()

        elif election == 3:
            readRows()
            album_to_delete = int(input("Ingrese el ID: "))
            deleteRows(album_to_delete)
        
        elif election == 4:
            deleteAllRows()

        elif election == 5:

            for i, j in getFields().items():
                print(f"{i} - {j}")
            select_field = int(input("Ingrese la columna a modificar: "))

            readRows()
            select_id = int(input("Ingrese el id del album a modificar: "))

            if select_field in [1, 5, 6]:
                new_value = int(input("Ingrese el nuevo valor: "))
            
            else:
                new_value = input("Ingrese el nuevo valor: ")

            modifyAlbum(select_field, new_value, select_id)
