
class Engine:
    def __init__(self, item, rooms):
        #load and serialize data to create state
        #put into lists of room and item objects
        self.items = None
        self.rooms = None
        pass

    def deserialize(self):
        pass

    def player_command(self, player, command):
        #parse command
        #update game state
        #get return text
        pass
    
    def parse_command(self, player, command):
        pass

    #update time-based events for server
    def update(self):
        pass


class Player:
    def __init__(self, username):
        self.username = username
        self.properties = {}
        self.inventory = []
        #login player

class Room:
    def __init__(self, data):
        self.name = data["name"] #name is immutable by design
        self.descriptions = data["description"]
        self.edges = data["edges"]
        self.inventory = data["inventory"]
        self.params = data["params"]

        self.on_event = lambda type, room, default: default

    @property
    def description(self):
        return self.on_event("get description", self, self.descriptions["default"])

    @property
    def inventory(self):
        return self.on_event("get inventory", self, self.descriptions["default"])

    @property
    def edges(self):
        return self.on_event("get inventory", self, self.edges["default"])

    def render(self):
        default = "{}\n{}".format(
            self.description,
            "\n".join([item.render() for item in self.inventory])
        )
        return "{}\n{}".format(
            self.name,
            self.on_event("render", self, default)
        )

class Item:
    def __init__(self, data):
        self.name = data["name"]
        self.params = data["params"]

        self.on_event = lambda type, item, default: default

    def render(self):
        return self.on_event("render", self, self.name)
