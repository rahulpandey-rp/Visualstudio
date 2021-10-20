import requests
url = "https://httpbin.org"


def http_get(url):
    reponse = requests.get(url)
    print(reponse.headers)


def http_post(url):
    reponse = requests.post(
                        url + "/put",
                        data={'key1': 'value1', 'key2': 'value2'}
                        )
    print(reponse.headers)


def http_put(url):
    reponse = requests.put(
                        url + "/post",
                        data={'key1': 'value1', 'key2': 'value2'}
                        )
    print(reponse.headers)


def http_delete(url):
    reponse = requests.delete(
                            url + "/delete",
                            data={'key1': 'value1', 'key2': 'value2'}
                            )
    print(reponse.headers)


http_get(url)
http_post(url)
http_put(url)
http_delete(url)
