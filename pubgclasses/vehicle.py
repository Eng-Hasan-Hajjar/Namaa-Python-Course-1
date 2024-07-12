class Vehicle:
    def __init__(self,typee,max_speed,health=100):
        self.type=typee
        self.max_speed=max_speed
        self.health=health

    def drive(self,destination):
        print(f"Driving {self.type} to {destination} at max speed of {self.max_speed} km/h ")    
    
    def take_damage(self,damage) :
        self.health -=damage
        if self.health<=0:
            print(f"{self.type} has been destroyed")    
        else:
            print(f"{self.type} took {damage} damage {self.health} health remaining")









