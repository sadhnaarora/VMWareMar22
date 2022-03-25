
def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(gname):
            import emojis
            emojized = emojis.encode(greet + " :"  + sep + ": " + gname)
            print(emojized)
        return innerMostFun
    return innerFun

engGreet = outerFun("Welcome")
tigerRef = engGreet("tiger")
tigerRef("Prabhakar")

print("-" * 40)

lionRef = engGreet("lion")
lionRef("Sachin")

"""
outerFun("Welcome")("---->")("Sachin")

print("-" * 40)
engGreet = outerFun("Welcome")
sngArw = engGreet("----->")
dblArw = engGreet("=====>>")

sngArw("Sehwag")
dblArw("Messi")

"""