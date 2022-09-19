# Le Pompon

Nous sommes certains que le Dr Risk a utilisé un moyen de transport pour acheminer ses propagateurs.

Nous pensons qu'il a chargé du matériel durant son trajet lors de sa seconde étape après son départ.

Trouvez l'indicatif UNLOCODE de l'endroit pour confirmer nos doutes.

Le Flag est à fournir sous forme `INNN{UN/LOCODE}`

[Fichier fourni](tracker.txt)

## Résolution

Le fichier contient des trames NMEA1803 (GPS). On commence par récupérer les 
positions contenues dans le fichier (latitude et longitude).
Ces positions sont dans [Coordonnees.txt](Coordonnees.txt).

Le fichier [pompom2.py](pompom2.py) lit ces coordonnées et construit une carte avec `folium` :
[tracker_carte.html](tracker_carte.html).

Sur cette carte, on relève le nom de la seconde escale : *San Pedro* en *Côte d'Ivoire*.
<https://unece.org/trade/cefact/unlocode-code-list-country-and-territory>

On trouve `CI SPY`

Flag : `INNN{CI/SPY}`

