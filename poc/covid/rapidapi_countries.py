import requests

class Countries:

	def getCounttry(self):
		url = "https://covid-193.p.rapidapi.com/countries"

		headers = {
			"X-RapidAPI-Key": "7e179f9702msh48dcaddec60d37cp1d6907jsn3e590cbd86b4",
			"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers)
		return response.json()
		#print(response.json())

a=Countries().getCounttry()
print(a)
