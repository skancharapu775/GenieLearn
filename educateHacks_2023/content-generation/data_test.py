import requests

url = "https://sameerbhatia-proprofs-flashcards-maker.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "6dbf679bb0msh9a5b24765635297p1f0e7fjsn9317aec4a187",
	"X-RapidAPI-Host": "sameerbhatia-proprofs-flashcards-maker.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)