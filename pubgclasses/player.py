class Player:
    def __init__(self,name,health=100 ):
        self.name=name
        self.health=health
        self.inventory=[]
        self.position=(0,0)
    def move(self,x,y):
        self.position=(x,y)    
        print(f"{self.name} moved to position {self.position}")
    def take_damage(self,damage) :
        self.health -=damage
        if self.health<=0:
            print(f"{self.name} has been eliminated")    
        else:
            print(f"{self.name} took {damage} damage {self.health} health remaining")
    def pick_up_weapon(self,weapon):
        self.inventory.append(weapon) 
        print(f"{self.name} picked up {weapon}")           