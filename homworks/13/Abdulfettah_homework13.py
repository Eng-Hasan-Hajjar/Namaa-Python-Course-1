#Ex1
x=5
y=2
k=7
l=9
p=3
total=(x+y*k-l/p)
print(total)

#Ex2
def sum(x, y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def div(x, y):
        return "Error" if y==0 else x/y

print(sum(16,2))
print(sub(16,2))
print(multi(16,2))
print(div(16,2))
print(div(16,0))
