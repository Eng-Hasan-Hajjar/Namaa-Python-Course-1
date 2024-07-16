
def myfuncmodule():
    x15=300
    def myinnerfunc():
        nonlocal x15
        x15=250
    myinnerfunc()
    return x15
 
ccc="ccc"