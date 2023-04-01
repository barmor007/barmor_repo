import requests

def test_api_1():
    #valid website address
    url = 'https://fruityvice.com/api/fruit/banana'
    response = requests.get(url)
    assert 400 > response.status_code >= 200

def test_api_2():
    #non valid website address
    url = 'https://fruityvice.com/api/fruit/mazda'
    response = requests.get(url)
    expected = True
    actual = False
    if (response.status_code < 200):
        actual = True #get error
    if (response.status_code >= 400):
        actual = True #get error
    assert expected == actual