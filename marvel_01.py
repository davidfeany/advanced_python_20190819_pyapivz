#!/usr/bin/python3

###########################################################################
# 
###########################################################################

import requests
from pprint import pprint
from hashlib import md5

# Example link with no params
# curl "http://gateway.marvel.com/v1/public/comics"
# {"code":"MissingParameter","message":"You must provide a user key."}
# 
# Hash and Authorization:
# https://developer.marvel.com/documentation/authorization
def get_marvel():
    with open("/home/student/.apikeys/marvelprivate.key") as apikey:
        privatekey = apikey.read().strip()
    with open("/home/student/.apikeys/marvelpublic.key") as apikey:
        publickey = apikey.read().strip()

    ts = "1"     # Timestamp/counter/unique-sequence-num/etc.

    marvhashstring = f"{ts}{privatekey}{publickey}"
    marvhashmd5 = md5(marvhashstring.encode())
    marvhash = marvhashmd5.hexdigest()
    
    # apikey=publickey
    weblink = f"http://gateway.marvel.com/v1/public/comics?ts={ts}&apikey={publickey}&hash={marvhash}"
    print("Request message: ", weblink)
    data = requests.get(weblink)
    #pprint(data.json())    # Prints all data dump
    return data


def main():
    data = get_marvel()
    if data.json()["status"].lower() != "ok":
        print("Failed: ", data.json()['message'])
        exit()
    else:
        print("Success! You have retrieved your data! ", data.json()['status'])

    # Print the series information for each comic found
    for i in range(data.json()['data']['count']):
        print(f"{i})  " + data.json()['data']['results'][i]['series']['name'])

if __name__ == "__main__":
    main()

