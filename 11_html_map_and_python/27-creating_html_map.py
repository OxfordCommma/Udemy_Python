###Folium para la creación de mapas usando Python

#Importamos Folium
import folium


#------------------------------------------------

#Indicamos una variable que guarda al objeto Map. Este objeto contiene una ubicación geográfica
#También tiene como parámetros el estilo del mapa (pueden ser o por defecto o por atribución de otro creador)
#y el zoom de inicio

map = folium.Map(location = [-34.6044, -58.4476], tiles = "cartodb positron", zoom_start = 6)
#map = folium.Map(location = [-34.6044, -58.4476], tiles ='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', attr = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')

#------------------------------------------------

#Podemos ingresar elementos al mapa, como un icono de ubicación. Antes que nada, es buena práctica
#almacenarlos en un FeatureGroup.
#Usamos un bucle para colocar múltiples marcadores de ubicación 

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[-34.6, -58.4], [-35.6, -59.4]]:
    fg.add_child(folium.Marker(location = coordinates, popup="Soy un Marcador", icon=folium.Icon("green")))

map.add_child(fg)

#------------------------------------------------

#Luego de todo se debe guardar en un archivo externo al mapa configurado.

map.save("map1.html")