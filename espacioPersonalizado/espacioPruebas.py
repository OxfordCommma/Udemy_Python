"""lista = [(0, 'id', 'INTEGER', 0, None, 1), (1, 'album_name', 'TEXT', 0, None, 0), 
         (2, 'artist', 'TEXT', 0, None, 0), (3, 'genre', 'TEXT',"NTEGER", 0, None, 0), 
         (5, 'score', 'NTEGER', 0, None, 0), (5, 'score', 'INTEGER', 0, None, 0)]

fields = {}
index = 1
for field in lista:
    if field[1] not in fields.values():
        #fields.append(field[1])
        fields[index] = field[1]
        index = index + 1

for field in fields[::]:
    fields.append(f"{index} - {field}")
    del fields[0]
    index = index + 1

print(fields)
"""

from datetime import datetime
a = timestamp = datetime.now()
print(a)