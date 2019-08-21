#!/usr/bin/python3

import requests

def main():
    mylookup = "http://api.open-notify.org/iss-pass.json?lat=45.1&lon=-122.3"
    data = requests.get(mylookup)
    #print(data.json())    # Prints all data dump
    #    {
    #      "message": "failure",
    #      "reason": "Latitude must be number between -90.0 and 90.0"
    #    }

    datastruct = data.json()
    for key in datastruct.keys():
        print(f"KEY: {key}")
        data = datastruct[key]
        print(f"DATA: {data}")
    
    #for key in datastruct["Time Series (5min)"].keys():
    #    value = datastruct["Time Series (5min)"][key][item]
    #    print(f"{key}:  {item} --> {value}")

    

if __name__ == "__main__":
    main()

