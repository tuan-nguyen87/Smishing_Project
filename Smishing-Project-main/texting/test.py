import requests
import config
amnt_of_texts = requests.get('https://textbelt.com/quota/' + config.api_key)
print(amnt_of_texts.json())