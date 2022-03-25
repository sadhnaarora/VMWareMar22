

def add(x, y):
    print("add fun called....")
    return x + y

def sub(x, y):
    print("sub fun called....")
    return x - y

def mul(x, y):
    return x * y

def outerFun(fnc):              # HOF

    def helperFun(*arg):
        print("logging into a service....")
        print(fnc(*arg))                # call back
        print("Logging out of the service....")

    return helperFun

addRef = outerFun(add)
addRef(267, 575)

print("-" * 40)

subRef = outerFun(sub)
subRef(365, 290)

