import json
from mudengine import Engine, Room, Player

with open("data/items.json") as f:
    ITEMS = json.load(f)

with open("data/rooms.json") as f:
    ROOMS = json.load(f)

class MUD:
    def __init__(self):
        self.e = Engine(ITEMS, ROOMS)

    def cold_room_desc(self):
        pass