#! /usr/bin/python3

import json
import requests
from pprint import pprint

headers = {
    'cache-control': "no-cache",
    'postman-token': "77047c8b-caed-2b2c-ab33-dbddf52a7a9f"
    }


def main():
    url = "https://www.anapioficeandfire.com/api" 
    r = requests.get(url)
    #r = requests.request("GET", url, headers=headers)
    print("type(r):", type(r))
    pprint(r.json())

    rdict = r.json()
    for key in rdict.keys():
        newr = requests.get(rdict[key])
        pprint(newr.json())


main()
