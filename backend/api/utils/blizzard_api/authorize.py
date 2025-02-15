import os
import requests

class AuthToBlizzard:
    def __init__(self):
        self.client_id = os.getenv("BLIZZARD_CLIENT_ID")
        self.client_secret = os.getenv("BLIZZARD_CLIENT_SECRET")
        self.grant_type = "client_credentials"
        self.current_token = os.getenv("BLIZZARD_TOKEN", None)

    def get_token(self):
        is_valid = self.validate_token()
        if self.current_token is None or is_valid is False:
            self.current_token = self._get_token()
        return self.current_token
    
    def validate_token(self):
        print("")
        print("Try to validate token")
        url = "https://oauth.battle.net/oauth/check_token"
        data = {
            "token": self.current_token,
            ":region": "eu",
        }
        response = requests.post(url, data=data)
        is_valid = response.status_code == 200
        print("Token is valid: ", is_valid)
        return response.status_code == 200        

    def _get_token(self):
        url = "https://oauth.battle.net/token"
        data = {
            "grant_type": self.grant_type,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            ":region": "eu",
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()["access_token"]