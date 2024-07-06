
from classesPubg.player import Player
from classesPubg.weapon import Weapon
from classesPubg.vehicle import Vehicle
from classesPubg.map import Map

player1 = Player("Player1")
player1.move(10, 20)
player1.take_damage(30)
player1.pick_up_weapon("AKM")
# إنشاء لاعبين
player2 = Player("Player2")
player3 = Player("Player3")

# إنشاء أسلحة
akm = Weapon("AKM", 49)
m416 = Weapon("M416", 43)

# إنشاء مركبات
buggy = Vehicle("Buggy", 90)
jeep = Vehicle("Jeep", 70)

# إنشاء خريطة
erangel = Map("Erangel", "8x8 km")

# إضافة لاعبين إلى الخريطة
erangel.add_player(player1)
erangel.add_player(player2)
erangel.add_player(player3)

# إضافة مركبات إلى الخريطة
erangel.add_vehicle(buggy)
erangel.add_vehicle(jeep)

# تحريك اللاعبين وأخذ أسلحة
player1.move(10, 20)
player1.pick_up_weapon(akm)
player2.move(15, 30)
player2.pick_up_weapon(m416)

# قيادة المركبات
buggy.drive("School")
jeep.drive("Military Base")

# إلحاق الأضرار
player1.take_damage(40)
buggy.take_damage(70)
