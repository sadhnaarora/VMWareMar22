
def outerFun():
    gname = "Sachin"

    def innerFun():
        nonlocal gname
        gname = "Rahul"
        print(f'Hello {gname}')

    innerFun()
    print(f"After :{gname}")

outerFun()