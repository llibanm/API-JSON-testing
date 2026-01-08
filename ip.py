import os
from dotenv import load_dotenv
import requests
import geocoder

if __name__=='__main__':

    # Récupère la localisation actuelle basée sur l'IP
    g = geocoder.ip('me')

    if g.latlng:
        lat, lon = g.latlng
        city = g.city
        print(f"📍 Localisé à : {city}")
        print(f"Coordonnées : {lat}, {lon}")
        
        # Ensuite tu appelles ton API météo avec ces variables...
    else:
        print("Impossible de te localiser.")
