class Map:
    def __init__(self,name ,size):
        self.name=name
        self.size=size
        self.players=[]
        self.vehicles=[]
    def add_player(self,player):
        self.players.append(player)
        print(f"{player.name} joined the map {self.name}")
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle.type} added the map {self.name}")
            

