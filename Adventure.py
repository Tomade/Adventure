__author__ = 'shade'

import json

data = json.load(open("labyrinth.json"))

# print(data)
"""
Look around, describe <thing>,
"""


rooms = data["rooms"]
room = rooms["start"]
while True:
    print(room["description"] + "\n")
    exits = room["exits"]
    objectsHere = room["objects"]

    action = input("==> ").lower()
    if action == "quit":
        break
    if action in exits:
        newroom = exits[action]
        room = rooms[newroom]
        continue
    if action.startswith("look at"):
        lookingAt = action.split()[2]
        print("You're looking at the %s" % lookingAt)
        if lookingAt in objectsHere:
            print(objectsHere[lookingAt])
