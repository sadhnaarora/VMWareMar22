
# closures
def outerFun(gname):                # gname - local variable
    info = "Mr." + gname            # info  - local variable

    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")
        print(f"Greetings {info}")

    innerFun()

outerFun("Rahul")
