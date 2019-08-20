#! /usr/bin/python3

import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "betelgeusian"},
                   {"name": "Arthur Dent",       "species": "human"},
                   {"name": "Ford Prefect",      "species": None}]

    # Note that "None" will be changed to "null" in the output file for json format
    # Dump to file in json format
    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

    # Dump to string
    myhitchhikers = json.dumps(hitchhikers)
    
    # This will not work because it is a string, not a datastructure:
    # print(myhitchhikers[0]["name"])

if __name__ == "__main__":
    main()

