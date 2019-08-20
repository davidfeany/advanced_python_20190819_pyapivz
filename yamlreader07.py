#! /usr/bin/python3

import yaml

def main():
    with open("myyaml.yml") as myyammy:
            yamldata = yaml.load(myyammy)
    print(type(yamldata))
    print(yamldata)

main()
