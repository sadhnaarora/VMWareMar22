
"""
functions
---------
"""

def greet():
    print("Welcome to python programming.....")

def greet_guest(fname,lname):
    print(f"Welcome {fname} {lname}")
    print("Pleasure to dine with you....")

# name is a non default argument, city is a default argument
def greet_city(name, city="Mumbai"):
    print(f"Welcome {name} from {city} to the event")


greet()

print("-" * 40)
greet_guest('Rahul', 'Dravid')

print("-" * 40)
greet_city("Sachin")
greet_city("Ajit")
greet_city("Sehwag", "Delhi")

print("-" * 40)
# functions can return values
def myProduct(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, myProduct(10, 20)))

# recursive calls -> python recursive calls
def fact(x):
    if x==1:
        return x
    else:
       return x * fact(x-1)

print(f"The fatorial of 5 is :{fact(5)}")

print("-" * 40)

def fib_series(n):
    if n <= 1:
        return n
    else:
        return(fib_series(n-1) + fib_series(n-2))

num = 8
if num <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci series...: ")
    for i in range(num):
        print(fib_series(i), end=" ")
print()

print("-" * 40)
# variable length arguments     -> * - tuple,  ** - dicitionary
def prodAll(*numbers):
    print(f"numbers :{numbers}")
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print("Multiply All =", prodAll(1, 2, 3, 4, 5, 6))

print("-" * 40)
# dictionary
def extract_detail(**detail):
    print(detail)
    print(f"Name  :{detail['name']}")
    print(f"Score :{detail['score']}")

extract_detail(name="Sachin", score=189, oppo="SA")

def admission(name, age=35, *tech, **marks):
    print(f"name :{name}")
    print (f"Age :{age}")
    print("technology ;", tech)
    print(f"Marks :{marks}")

admission("Micheal", 45,'java', 'j2ee', 'spring', 'hibernate', 'python', Xth='87%', XIIth='78%',
          degree='89%', pg='92%')

print(f"admission")

print("-" * 40)
def mul_me(x):
    y = x * x
    return y

print(mul_me(10))
a = mul_me(2)
b = mul_me(3)
print(a + b)

print("-" * 40)

def basicArithematic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = basicArithematic(10, 5)
print(f"res :{res}")


print("-" * 40)
# document string
def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 40)

def fun1(x, y):
    """
    fun1 is a function which takes two numbers and returns the largest of it

    largest_num = fun1(arg1, agr2)

    arg1 and arg2 is  integer values, we have used ternary operator to find the
    largest number.
    """
    return x if x > y else y

print(fun1(35, 55))
print(fun1(85, 55))

print("-" * 40)

help(fun1)
