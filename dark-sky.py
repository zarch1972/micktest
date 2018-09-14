import requests

response = requests.get("https://api.darksky.net/forecast/8a7143ee45a0238dcafe4b50fa5d9a6f/53.402540,-1.521180")
json_res = response.json()
print (json_res['currently']['temperature'])

