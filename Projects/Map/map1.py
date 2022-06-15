import folium
#Make open/ Open at this location
map = folium.Map(location=[23.153596036147327, 79.8751783496987], zoom_start=5.5, tiles="Stamen terrain")

house = {
    'coord': [28.9810571, 77.6860140],
    'popup': 'Home',
    'color': 'blue',
    'tooltip': 'I live here',
}
school = {
    'coord': [30.33528725905316, 78.03199409753077],
    'popup': 'School',
    'color': 'red',
    'tooltip': 'I study here',
}

#Add marker at this location
for loc in [house,school]:
    fg = folium.FeatureGroup(name="My Map")
    fg = folium.Marker(location=loc['coord'], popup=loc['popup'], icon=folium.Icon(color=loc['color']), tooltip=loc['tooltip']) #Make marker
    map.add_child(fg)                      #Add marker





map.save("Map1.html")