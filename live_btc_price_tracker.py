# live Bitcoin and Ethereum price tracker using API
import requests
import time
while True:
    url = 'https://api.coincap.io/v2/assets'

    data = requests.get(url)
    info = data.json()

    # print(info['data'])

    # for i in range(len(info['data'])):
    print(f"1 Bit-coin is {info['data'][0]['priceUsd']} USD  \t|   1 Ethereum is {info['data'][1]['priceUsd']} USD")
    time.sleep(4)