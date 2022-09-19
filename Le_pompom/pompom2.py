import folium
from pathlib import Path

data = Path("Coordonnees.txt").read_text().splitlines()

##
points = []
for lig in data:
    if not lig: continue
    la, lo = lig.split(" ")
    points.append((float(la), float(lo)))

##
carte = folium.Map(location=[45,0], tiles='cartodbpositron', zoom_start=3)
for pos in points:
    folium.CircleMarker(location=pos, radius=5, fill_color="#f00").add_to(carte)

carte.save("tracker_carte.html")
