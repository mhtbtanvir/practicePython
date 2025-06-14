import os
import json
people_bids = {}


def clear():
    os.system('cls')

 # Call the function to clear the screen


def aution_dashboard():

    while True:
        name = input("whats yo name boy?:")

        if name == 'done13':
            result()
            False
            break

        bid = int(input("whats your bid?:"))
        people_bids[name] = bid

        clear()


def result():
    bids = people_bids.values()
    highest_bid = max(bids)

    for name in people_bids:
        if people_bids[name] == highest_bid:
            print(
                f"name of the winners are: {name} \nwith a bid of:{people_bids[name]}")
    print(" \nperticipents:")

    print(json.dumps(people_bids, indent=4))


aution_dashboard()
