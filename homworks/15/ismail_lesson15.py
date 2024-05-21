f = ["ford", "bmw", "dodge"]
s = ["ford", "bmw", "dodge"]
z = f

print(f is z)
#
print(f is s)
##############
f = ["ford", "bmw", "dodge"]
s = ["ford", "bmw", "dodge"]
z = f
print(f is not z)

print(f is not s)
#####################
f = ["ford", "bmw", "dodge"]
print("ford" in f)

print("bmw" not in f)