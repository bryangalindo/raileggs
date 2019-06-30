import base64

import requests

from constants import uprr_request_token_url


class UnionPacific:
    def __init__(self, username, password):
    self.username = username
    self.password = password
    
    def get_encoded_credentials(self):
        return base64('{}:{}'.format(self.username, self.password)
                      
    def get_request_token(self)
        encoded_credentials = self.get_encoded_credentials()
        data = {
            "header": {
                "Authorization": "Basic {}".format(encoded_credentials),
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
                },
            "body": {
                "grant_type": "client_credentials"
                }
            }
        response = requests.post(uprr_request_token_url, data=data)
        token_dict = response.json()
        return token_dict
                      
    def get_containers_list():
        pass
    
    def get_departure_date():
        pass
    
    def get_eta():
        pass
                      
    def get_last_free_date():
        pass           
