import requests

url = "https://linkedin-api8.p.rapidapi.com/get-profile-data-by-url"

querystring = {"url":"https://www.linkedin.com/in/atanusarkhel/"}

headers = {
	"x-rapidapi-key": "7e179f9702msh48dcaddec60d37cp1d6907jsn3e590cbd86b4",
	"x-rapidapi-host": "linkedin-api8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())