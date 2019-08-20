#! /usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "betelgeusian"},
                   {"name": "Arthur Dent",       "species": "human"},
                   {"name": "Ford Prefect",      "species": None}]

    # Here's how you dump yaml to string:
    # Dump to file in yaml format
    mystr = yaml.dump(hitchhikers)
    print(mystr)
    

    
if __name__ == "__main__":
    main()

