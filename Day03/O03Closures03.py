
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)
    return innerFun


engGreet = outerFun("Welcome")

# simple curry
engGreet('Sachin')
engGreet('Sourav')

print("-" * 40)
kanGreet = outerFun("Namaskara")
kanGreet("Anil")

print("-" * 40)
tamilGreet = outerFun("Vanakam")
tamilGreet("Dhoni")
