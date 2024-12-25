import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881"

headers = {
	"x-rapidapi-key": "7e179f9702msh48dcaddec60d37cp1d6907jsn3e590cbd86b4",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())