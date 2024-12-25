import requests

class HistoryData:
	def getHistoryData(self):
		url = "https://covid-193.p.rapidapi.com/history"

		querystring = {"country":"usa","day":"2020-06-02"}

		headers = {
			"X-RapidAPI-Key": "7e179f9702msh48dcaddec60d37cp1d6907jsn3e590cbd86b4",
			"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers, params=querystring)
		return response.json()

		#print(response.json())