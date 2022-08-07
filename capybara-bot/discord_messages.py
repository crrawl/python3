import requests

class Discord_messages:
    def __init__(self, channel_url, payload, headers):
        self.channel_url = channel_url
        self.payload = payload
        self.headers = headers

    def send_message(self):
        return requests.post(
            self.channel_url, 
            data = self.payload, 
            headers = self.headers
            )