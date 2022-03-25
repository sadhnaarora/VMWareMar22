
# closures
def outerFun(gname):                # HOF - Higher order function
    info = "Mr." + gname

    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")
        print(f"Greetings {info}")

    return innerFun

outerFun("Rahul")()             # calls the inner function

print("-" * 40)
print(outerFun.__name__)
print(outerFun("Virat").__name__)

print("-" * 40)
innerRef = outerFun("Sachin")
innerRef()
