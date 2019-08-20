#! /usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "betelgeusian"},
                   {"name": "Arthur Dent",       "species": "human"},
                   {"name": "Ford Prefect",      "species": None}]

    # Dump to file in yaml format
    with open("zfile.yml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)

    
if __name__ == "__main__":
    main()

