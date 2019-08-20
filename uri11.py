#!/usr/bin/python3

import requests

options = [
            "1. open",
            "2. high",
            "3. low",
            "4. close",
            "5. volume"
        ]

def main():
    with open("/home/student/.apikeys/uri11.key") as apikey:
        myapikey = apikey.read()

    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=" + myapikey
    data = requests.get(mylookup)
    #print(data.json())    # Prints all data dump

    print("\n".join(options))
    useritem = int( input("which do you want?  ") )
    if useritem in range(6):
        item = options[useritem - 1]
    else:
        print(f"Invalid option: {useritem}")
        exit()
    print(f"item: {item}")

    datastruct = data.json()
    for key in datastruct.keys():
        # Key Meta Data
        # Key Time Series (5min)
            #    "Time Series (5min)": {
            #        "2019-08-20 09:45:00": {
            #            "1. open": "137.7525",
            #            "2. high": "137.8100",
            #            "3. low": "138.4400",
            #            "4. close": "138.8100",
            #            "5. volume": "289471"
            #            },

        print(f"Key {key}")
    
    for key in datastruct["Time Series (5min)"].keys():
        value = datastruct["Time Series (5min)"][key][item]
        print(f"{key}:  {item} --> {value}")

    

if __name__ == "__main__":
    main()

