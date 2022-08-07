import requests
import random

url = "https://api.giphy.com/v1/gifs/search?"

params = {
    "api_key": "V8yvCBRe3Ba0QAK4BLrdsT2hzlmWBK0F",
    "q": "capybara",
    "limit": "75"
}

response = requests.get(url, params=params)

gif_index = random.randint(0, 50)

print(response.json()['data'][gif_index]['url'])

