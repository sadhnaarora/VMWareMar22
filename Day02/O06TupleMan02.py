
from collections import namedtuple

plyObj = namedtuple("Player", "fname lname age runs matches")
plyr = plyObj(fname="Sachin", lname="Tendulkar", age=42, runs=35000, matches=650)
print(f"Name :{plyr.fname + ' ' + plyr.lname}")
print(f"age  :{plyr.age}")

# plyr.runs = 32000

print(plyr)
