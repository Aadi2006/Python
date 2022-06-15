from json import tool
from cv2 import COLORMAP_DEEPGREEN
import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')

#Assign values of LON(colunm) to a list
lat = list(data['LAT'])
lon = list(data['LON'])
elev=list(data["ELEV"])
names=list(data["NAME"])

def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My map")

for lt, ln, el, name in zip(lat,lon,elev,names):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+' m', fill_color=color_producer(el), color='gray', fill_opacity=0.7, tooltip=name))

fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read()))
map.add_child(fg)
map.save("Map1.html")
