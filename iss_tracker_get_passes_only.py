#!/usr/bin/python3

###########################################################################
# Given coordinates and altitude, return list of passes in future
# that ISS flybys will be visible from that location (assume good weather).
###########################################################################

import requests
from pprint import pprint

default_coordinates= {
        'latitude':   "45.1",
        'longitude':  "-122.35",
        'altitude':   "9999",
        'passes':     "10"
        }
    
# http://open-notify.org/Open-Notify-API/ISS-Pass-Times/
# Inptut    Description                                  Query string	Valid Range    Units	Required?
# Latitude  The latitude of the place to predict passes  lat            -80..80        degrees  YES
# Longitude The longitude of the place to predict passes lon            -180..180      degrees  YES
# Altitude  The altitude of the place to predict passes  alt            0..10,000      meters   No
# Number    The number of passes to return               n              1..100         –        No
def get_iss_passes(coordinates):
    mylookup = "http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}&alt={}".format(
            coordinates['latitude'],
            coordinates['longitude'],
            coordinates['passes'],
            coordinates['altitude']
            )
    print("Request message: ", mylookup)
    data = requests.get(mylookup)

    #pprint(data.json())    # Prints all data dump

    #################
    #    {
    #      "message": "failure",
    #      "reason": "Latitude must be number between -90.0 and 90.0"
    #    }
    #################
    #    {
    #      "message":   "success"
    #      "request":   {'altitude': 100, 'datetime': 1566361647, 'latitude': 45.1, 'longitude': -122.3, 'passes': 5}
    #      "response":  [
    #               {'duration': 413, 'risetime': 1566395142}, 
    #               {'duration': 640, 'risetime': 1566400786}, 
    #               {'duration': 645, 'risetime': 1566406589}, 
    #               {'duration': 626, 'risetime': 1566412436}, 
    #               {'duration': 650, 'risetime': 1566418259}
    #           ]
    #    }

    return data


def main():
    passes_data = get_iss_passes(default_coordinates)
    if passes_data.json()['message'] == 'failure':
        print("Failed: ", passes_data.json()['reason'])
        exit()
    else:
        if passes_data.json()['message'] == 'success':
            print("Successfully retrieved data.")
        else:
            print("Unexpected return state: ")
            pprint(passes_data.json())
            exit()
        
    if 'response' in passes_data.json():
        datalist = passes_data.json()['response']
    else:
            print("Unexpectedly found no response data in returned data structure: ")
            pprint(passes_data.json())
            exit()

    for iss_pass in datalist:
        pprint(iss_pass)
    

if __name__ == "__main__":
    main()

