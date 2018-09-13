import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev= list(data["ELEV"])
def color_produces(elevation)
  if elevation < 1000:
    return 'green'
  elif 100 <= elevation < 3000:
    return 'orange'
  else:
    return 'red'
map = folium.Map(location= [38,58,-99,09],zoom_start=6,tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
for lt,ln,el in zip (lat,lon,elev):
  fg.add_child(folium.Marker(locations=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color='green')))
 map.add_child(fg)
 map.save("Map1.html")
