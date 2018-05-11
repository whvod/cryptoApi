import urllib.parse
import requests

def main(): 

    cryptoApi = 'https://api.coinmarketcap.com/v2/ticker/?'
    convert = 'USD'
    url = cryptoApi + urllib.parse.urlencode({'convert': convert})

    json_data = requests.get(url).json()
    for dataId in json_data["data"]: 
        rank = json_data["data"][str(dataId)]["rank"]
        name = json_data["data"][str(dataId)]["name"]
        price = json_data["data"][str(dataId)]["quotes"]["USD"]["price"]
        if rank <= 10:
            print(f"{name}: {price}")       

if __name__ == '__main__':
    main()
