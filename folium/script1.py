import folium
import pandas

#deprecated
#map.simple_marker(location=[45.372, -121.697], popup='Mt. Hood Meadows', marker_color='red')
#map.simple_marker(location=[45.3311, -121.7311], popup='Timberlake Lodge', marker_color='green')

df = pandas.read_csv('Volcanoes-USA.txt')

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=4, tiles='Mapbox Bright')


def color(elev):
  minimum = int(min(df['ELEV']))
  step = int((max(df['ELEV'])-min(df['ELEV']))/3)

  if elev in range(minimum, minimum+step):
    col = 'green'
  elif elev in range(minimum+step, minimum+step*2):
    col = 'orange'
  else:
    col = 'red'

  return col


fg = folium.FeatureGroup(name="Volcano Locations")
map.add_child(fg)

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
   folium.Marker([lat, lon], popup=name, icon=folium.Icon(color=color(elev))).add_to(fg)

   #or alternatively we can use
   #map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev))))

#folium.Marker([45.3311, -121.7311], popup='Timberlake Lodge', icon=folium.Icon(color='red', icon='cloud')).add_to(map)


map.add_child(folium.GeoJson(data=open('world-geojson.json', encoding='utf-8-sig'),
  name='World Population',
  style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=1000000 else 'orange' if 1000000<x['properties']['POP2005']<2000000 else 'red'}))

#folium.GeoJson(open('world-geojson.geojson'), name='World Population').add_to(map)


map.add_child(folium.LayerControl())


map.save('test_map4.html')