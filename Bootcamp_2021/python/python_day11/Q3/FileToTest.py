import requests
import unittest
from unittest.mock import Mock
requests = Mock()
def get_json():
    url = "https://api.github.com/search/repositories"
    reponse = requests.get(
                        url, headers={"Accept": "application/json"},
                        params={"q": "requests"}
                        )
    return(reponse.json)


class testJson(unittest.TestCase):
    def test_get_json(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
                                        "total_count": 1,
                                        "items": [
                                        {
                                        "id": 63476337,
                                        "name": "Python",
                                        "full_name": "TheAlgorithms/Python",
                                        "private": False,
                                        "description": "All Algorithms implemented in Python",
                                        "forks": 31806,
                                        "open_issues": 49,
                                        "watchers": 118919,
                                        "default_branch": "master",
                                        "score": 1.0
                                        }
                                        ]
                                        }
        

print(get_json())
