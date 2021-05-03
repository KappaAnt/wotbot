import requests
import json
import os

class WotFact2:
    def __init__(self, ID):
        """
        Initializes Wot
        args: none
        returns: none
        """
    
        self.api_url = "https://api.worldoftanks.com/wot/account/info/?application_id=51f802fc0bedd0f40e870f80387ba919&account_id="
        self.userID = str(ID)
        self.api_url_end = self.api_url + self.userID
        #self.api_url_end = os.environ["FACT_TOKEN"]
        self.request = ""
        self.id_json = ""
       
        
    def get(self):
        """
        Gets data from wot api
        args: none
        returns: none
        """
   
        ArtyHits = 0
        self.request = requests.get(self.api_url_end)
        self.id_json = self.request.json()
        ArtyHits = self.id_json["data"][self.userID]["statistics"]["all"]["explosion_hits_received"]
        print("Hit By Arty: " + str(ArtyHits) + " times!")

        return ArtyHits
            
    


            
    
