"""
maan 60
Abd fattah  58
ismail 40
manaf 44
gith 36
sedra 39
jaber 21
obia 16
Bhaa 9
lama 3
hussam 2
ahmad  1

"""

## for 
##ex1
players=[10,20,30]
for x in players:
    print("ex1",x)

##ex2
game="pubg"
for x in game:
    print("ex2",x,20)


##ex3
game="pubg"
for x in game:
    print("ex3",x,20)


##ex4
#sedra
game = "pubge"
index = 0
for x in game:
    print(f"{x}: {index}")
    index += 1

##ex5
# manaf
game = "pubg"

##for index, letter in (game):
##   print(f"Character '{letter}' is at index {index}")    
##ex6
##giath
game = "pubg"

##for index, char in enumerate(game):
##   print("ex2", char, index)

##ex7
## for 

players=[10,20,30]
for x in players:
    if (x!=20):
      print("ex7",x)


##ex8
## for 

players=[10,20,30]
for x in players:
    if (x==20):
        continue
    print("ex8",x)

##ex9
## for 

players=[10,20,30]
for x in players:
    if (x==30):
        break
    print("ex9",x)

## range()
for x in range(10):
    print(x)

## 
for x in range(2,8):
    print(x)

    ## 
v=range(2,8)  
print("v",v,type(v))

for x in range(2,30,5):
    print(x)

## 
playername=["Hasan" , "Ismail" , "gith"]
score=[8,10,9]

for x in playername:
    for y in score:
        print(x,y)
## pass with for
# 
for x in [0,1,5]:
    pass        


