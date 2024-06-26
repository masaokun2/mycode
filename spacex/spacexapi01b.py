#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the requests library.
"""

# python3 -m pip install requests
import requests

# GLOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create a requests response object by sending an HTTP GET to SPACEXURI
    coreData = requests.get(SPACEXURI)

    # Pull JSON off 200 and convert to lists and dictionaries
    listOfCores = coreData.json()

    for core in listOfCores:
        print(core, end="\n\n")
        print(f"The original launch and core serial of this launch is {core['original_launch']},  {core['core_serial']}")
        print("Details: ", core['details'])


if __name__ == "__main__":
    main()

