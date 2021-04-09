import urllib.request as request
import json

def bitcoin_api():
    with request.urlopen('https://api.coindesk.com/v1/bpi/currentprice.json') as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')

    return data['bpi']['USD']['rate_float']


