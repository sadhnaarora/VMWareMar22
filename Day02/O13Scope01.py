
# local scope

glbX = 100          # global

def fun(x):         # local variable
    global glbX
    y  = 10         # local variable
    print(x, y)
    glbX = 500      # local variable with the name of the global variable
    print(f"glbX inside fun :{glbX}")

def fun1():
    pass

print(f"before glbX :{glbX}")

fun1()      # 100
fun(20)
fun1()      # 500

print(f"after glbX :{glbX}")
