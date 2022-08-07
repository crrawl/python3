import requests
import random

class Capybara_gif:
    def __init__(self, url, params):
        self.__author__ = "Raibisu Yuu Kuramu"
        self.__email__  = "yuukuramu@proton.me"
        self.__version__ = "v1.2-alpha"

        self.url = url
        self.params = params 

    def hello_author(self):
        print(f"hello {self.__author__}")

    def get_capybara_url(self):
        print("Sending capybara...")
        
        response = requests.get(self.url, params=self.params)
        gif_index = random.randint(0, 25)

        print("Capybara sended!")
        return response.json()['data'][gif_index]['url']
