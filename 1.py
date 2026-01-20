import requests

url = "https://cricket-live-line1.p.rapidapi.com/liveMatches"

headers = {
	"x-rapidapi-key": "ea87c71a19msh44c066a91844f3ap1b6287jsnfd3a8b5a54f6",
	"x-rapidapi-host": "cricket-live-line1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())


import requests

url = "https://cricket-live-line1.p.rapidapi.com/recentMatches"

headers = {
	"x-rapidapi-key": "ea87c71a19msh44c066a91844f3ap1b6287jsnfd3a8b5a54f6",
	"x-rapidapi-host": "cricket-live-line1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
