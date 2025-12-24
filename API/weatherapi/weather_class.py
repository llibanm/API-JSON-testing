import os
from dotenv import load_dotenv
import requests
import sqlite3

class weather_report():

    def __init__(self) -> None:

        load_dotenv("/home/vazek/Bureau/API_Json_Testing/.env")
        
        base_url = os.getenv("base_url") # base url which we will build the complete url upon
        api_key =  os.getenv("API_KEY")

        if base_url is not None and api_key is not None:

            self.base_url = base_url
            self.api_key = api_key


        else :
            raise ValueError('Error : base url and api key not found')

        #API METHOD
        # we will use just 2 for now
        self.current_weather = "/current.json"
        self.forecast = "/forecast.json"


    def sauvegarder_mes_donnees(self):

        # 2. Connexion à la base (crée le fichier 'mes_donnees.db' sur Linux)
        conn = sqlite3.connect('mes_donnees.db')
        cursor = conn.cursor()

        # 3. Création de la table (si elle n'existe pas encore)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultats_api (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT,
            valeur TEXT
        )
    ''')

         

    def build_request(self,city:str,current_weather : bool = True,forecast : bool = False,aqi : bool = False):
        complete_url = ""

        if current_weather is True:

            if aqi is False:

                complete_url = self.base_url + self.current_weather+'?'+'key='+self.api_key+'&'+'q='+city+'&aqi=no'

            else :
                complete_url = self.base_url + self.current_weather+'?'+'key='+self.api_key+'&'+'q='+city+'&aqi=yes'    

        return complete_url


if __name__=='__main__':

    weather = weather_report()
    weather.sauvegarder_mes_donnees()

    pass       
