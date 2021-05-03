import requests
import json
import os

class WotFact:
    def __init__(self, username):
        """
        Initializes Wot
        args: none
        returns: none
        """  
        self.api_url = "https://api.worldoftanks.com/wot/account/list/?application_id=51f802fc0bedd0f40e870f80387ba919&search="
        self.user = username
        self.api_url_end = self.api_url + self.user
        #self.api_url_end = os.environ["FACT_TOKEN"]
        self.request = ""
        self.id_json = ""
        
    def get(self):
        """
        Gets data from wot api
        args: none
        returns: none
        """
        ID = 0
        
        self.request = requests.get(self.api_url_end)
        self.id_json = self.request.json()
        ID = self.id_json["data"][0]["account_id"] 
        #print("USER ID: " + ID)

        return ID
            
    
