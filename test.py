import requests

BASE = "http://127.0.0.1:9001/"

response = requests.get(BASE + "postreceive")
print(response.json())