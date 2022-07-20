import requests
import folium


res=requests.get('https://ipinfo.io/')
data=res.json()
print(data)
location=data['loc'].split(',')
lat=float(location[0])
log=float(location[1])
# creating a feature group
fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('kenyan-counties.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[lat,log],popup="my location"))
map=folium.Map(location=[lat,log],zoom_stsrt=7)
map.add_child(fg)
map.save("location.html")