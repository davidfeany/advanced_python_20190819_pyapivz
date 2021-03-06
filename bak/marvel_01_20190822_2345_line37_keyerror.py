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
        #print(f"privatekey: ({privatekey})")
    with open("/home/student/.apikeys/marvelpublic.key") as apikey:
        publickey = apikey.read().strip()
        #print(f"publickey: ({publickey})")

    #marvhash = md5(b"ts+privatekey+publickey")
    ts = "1"     # Timestamp/counter/unique-sequence-num/etc.
    marvmd5 = md5(b"15cd4a5938b1eeccb7e743cd70f465a2dda90b290b5c5ffa919d6fd0ddc1b57cb737a3717")
    marvhash = marvmd5.hexdigest()
    #print(f"marvhash:  {marvhash}")
    
    # apikey=publickey
    weblink = f"http://gateway.marvel.com/v1/public/comics?ts={ts}&apikey={publickey}&hash={marvhash}"
    print("Request message: ", weblink)
    data = requests.get(weblink)
    #pprint(data.json())    # Prints all data dump

    if data.json()["hash"] == marvhash:
        return ({"data": data, "result": "success"})
    else:
        return ({"data": data, "result": "failure"})


def main():
    result = get_marvel()
    if result.json()['result'] == 'failure':
        print("Failed: ", result.json()['data']['message'])
        exit()
    else:
        pass

    data = result.json()['data']
    pprint(iss_pass)
    

if __name__ == "__main__":
    main()

