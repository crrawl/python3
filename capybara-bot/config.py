from capybara_bot import Capybara_gif

api_url = "https://api.giphy.com/v1/gifs/search?"

params = {
    "api_key": "", # Enter your giphy API key
    "q": "capybara",
    "limit": "50"
}

channel_url = "" # Enter your channel url

payload = {
    "content": Capybara_gif(api_url, params).get_capybara_url()
    # "content": "hello"
}
headers = {
    "Authorization":"" # Enter your discord auth key
}