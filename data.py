import requests

parameters = {
    "amount": 18,
    "type": "boolean",
    "category":18,
}

response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data = response.json()
question_data = print(data["results"])
