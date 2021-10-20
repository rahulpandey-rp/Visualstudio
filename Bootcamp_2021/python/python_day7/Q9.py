import requests
url = "https://api.github.com/search/repositories"
reponse = requests.get(
                        url, headers={"Accept": "application/json"},
                        params={"q": "requests"}
                        )
print(reponse.json()["total_count"])
