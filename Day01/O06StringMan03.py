

# c style
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "Superb")       # tuple
print(values)
print(format % values)

print("-" * 40)

format = "Welcome %s, your rating of %.3f, what a player"
print(f"format :{format}")
print(format % ("Sachin", 9))
print(format % ("Sachin", 9.87))
print(format % ("Sachin", 9.89999))
print("Welcome %s, your rating of %.3f, what a player" %  ("Sachin", 9.523))

# unix style
print("-" * 40)
from string import Template
tmpl = Template("Welcome $name, what a $adjective player")
# print(f"tmpl :{tmpl}")
res = tmpl.substitute(name="Sachin", adjective='Super')
print(f"res :{res}")

# python string formatting
print("-" * 40)
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {2}, what a {1} player for {0}".format("India", "class", "Sachin"))
print("Welcome {name}, what a {adj} player for {ctry}".format(ctry = "India", adj = "class", name="Sachin"))

# interpolation
print("-" * 40)
from math import pi, e
print(f"PI={pi} and Eulers constant={e}")

print("PI={} and Eulers Constant={}".format(pi, e))
print("PI={} and Eulers Constant={} and magic number {}".format(pi, e, 40585))

print("-" * 40)
full_name = ["Sacin", "Tendulkar"]
print("Mr. {name}".format(name=full_name))
print("Mr. {name[0]}".format(name=full_name))
print("Mr. {name[1]}".format(name=full_name))

print("-" * 40)
import math
print(math.__name__)            # double underscore name =>  dunder-name
print(__name__)

print("-" * 40)
# conversions
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=369857012))

#strings
print("-" * 40)
print("{num:10}Tendulkar".format(num=3))
print("{num:10}Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

# alinment
print("-" * 40)
print("{fname:<15}Tendulkar".format(fname='Sachin'))         # left alignment
print("{fname:^15}Tendulkar".format(fname='Sachin'))         # center alignment
print("{fname:>15}Tendulkar".format(fname='Sachin'))         # right alignment

print("one googol is :{}".format(10 ** 100))
print("one googol is :{:,}".format(10 ** 100))             # thousand seperator

print("{:$^50}".format("Womens World Cup 2022"))
print("{:*^50}".format("Womens World Cup 2022"))
print("{:-^50}".format("Womens World Cup 2022"))
print("Womens World cup 2022".center(50, "-"))
