class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def __str__(self):
        return self.name
"""
# مثال عن استخدام Weapon
akm = Weapon("AKM", 49)
m416 = Weapon("M416", 43)
"""