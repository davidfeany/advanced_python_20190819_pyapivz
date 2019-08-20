#! /usr/bin/python3

import json

def main():

    # This method will return a string, not a datastructure.
    with open("datacenter.json", "r") as datacenter:
        datacenterstr = datacenter.read()

    print(type(datacenterstr))
    datacenterdict = json.loads(datacenterstr)

    print(type(datacenterdict))
    print(datacenterdict["row1"])


    with open("datacenter.json", "r") as datacenter:
        datacentershort = json.load(datacenter)
    print(type(datacentershort))

    # This doesn't work
    #with open("datacenter.json", "r") as datacenter:
        #datacentershort2 = datacenter.load()
    #print(type(datacentershort2))



if __name__ == "__main__":
    main()
