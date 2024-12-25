import requests
class CountryStat:
	def getCountryStat(self):
		url = "https://covid-193.p.rapidapi.com/statistics"

		headers = {
			"X-RapidAPI-Key": "7e179f9702msh48dcaddec60d37cp1d6907jsn3e590cbd86b4",
			"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers)
		return response.json()

print(CountryStat().getCountryStat())