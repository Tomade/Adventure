__author__ = 'shade'

import json
import sys

class Adventure:
    def __init__(self, jsonfile):
        try:
            with open(jsonfile) as fp:
                self.data = json.load(fp)
            self.rooms = self.data["rooms"]
            self.room = self.rooms["start"]
        except:
            sys.exit("Could not initialize adventure data")

    def describe_location(self):
        return self.room["description"]

    def go(self, where):
        exits = self.room["exits"]
        if where in exits:
            new_room_name = exits[where]
            self.room = self.rooms[new_room_name]
            return self.describe_location()
        else:
            return "You can't go that way."

    def look_at(self, what):
        objects_here = self.room["objects"]
        if what in objectsHere:
            return objectsHere[what]

# while True:
#     print(room["description"] + "\n")
#     exits = room["exits"]
#     objectsHere = room["objects"]
#
#     action = input("==> ").lower()
#     if action == "quit":
#         break
#     if action in exits:
#         newroom = exits[action]
#         room = rooms[newroom]
#         continue
#     if action.startswith("look at"):
#         lookingAt = action.split()[2]
#         print("You're looking at the %s" % lookingAt)
#         if lookingAt in objectsHere:
#             print(objectsHere[lookingAt])
