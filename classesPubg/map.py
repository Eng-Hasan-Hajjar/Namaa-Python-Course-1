class Map:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.players = []
        self.vehicles = []
    
    def add_player(self, player):
        self.players.append(player)
        print(f"{player.name} joined the map {self.name}")
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle.type} added to the map {self.name}")

# مثال عن استخدام Map
#erangel = Map("Erangel", "8x8 km")
#erangel.add_player(player1)
#erangel.add_vehicle(buggy)
