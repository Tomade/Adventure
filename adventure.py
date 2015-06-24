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
        if what in objects_here:
            return objects_here[what]
        else:
            return "No such thing here."

    def search(self, what = None):
        """Return the list of visible objects in the room if arg is empty"""
        """if there is a 'what', for now return just the object description"""
        if what == "":
            objects_here = self.room["objects"]
            object_names = [str(x) for x in objects_here.keys()]
            name_list = ""
            for name in object_names:
                name_list += " {}".format(name)

            s = "You search around and find: " + name_list
            return s