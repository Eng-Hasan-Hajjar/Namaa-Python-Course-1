class Vehicle:
    def __init__(self, type, max_speed, health=100):
        self.type = type
        self.max_speed = max_speed
        self.health = health
    
    def drive(self, destination):
        print(f"Driving {self.type} to {destination} at max speed of {self.max_speed} km/h")
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The {self.type} has been destroyed!")
        else:
            print(f"The {self.type} took {damage} damage, {self.health} health remaining")
"""
# مثال عن استخدام Vehicle
buggy = Vehicle("Buggy", 90)
buggy.drive("Pochinki")
buggy.take_damage(50)
"""