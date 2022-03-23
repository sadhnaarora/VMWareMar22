

emp = "emp001, Micheal Jordan, HR, MGR, 125000"
print(f"emp :{emp}")

print("split".center(40, "-"))
print(f"emp :{emp}")
emplst = emp.split(", ")
print(f"emplst :{emplst}")
print(type(emplst))
print(f"Name :{emplst[1]}")

print("Join".center(40, "-"))
print(f"emplst :{emplst}")
emp = ", ".join(emplst)
print(f"emp :{emp}")
print(type(emp))

print("find".center(40, "-"))
st = "hello world"
res = st.find("l")
print(f"res :{res}")

res = st.find("l", 4)
print(f"res :{res}")

st1 = "the quick brown fox jumps over the lazy dog"
print(f"st1 :{st1}")
res = st1.find("the")
print(f"res :{res}")

res1 = st1.find("the", 5)
print(f"res1 :{res1}")

print("replace".center(40, "-"))
st1 = "the quick brown fox jumps over the lazy dog"
print(f"st1 :{st1}")

res = st1.replace("fox", "tiger")
print(f"res :{res}")

res1 = st1.replace("the", "The")
print(f"res1 :{res1}")

res2 = st1.replace("the", "The", 1)
print(f"res2 :{res2}")

# maketrans, translate
print("maketrans".center(40, "-"))
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
restbl = st.maketrans(a,b)
print(f"restbl :{restbl}")

print("translate".center(40, "-"))
res = st.translate(restbl)
print(f"res :{res}")
