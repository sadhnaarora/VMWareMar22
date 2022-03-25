
squares = {x: x ** 2 for x in range(1, 11)}
print(f"squares :{squares}")
print("-" * 40)

players = {
    'sachin': (280, 345, 250, 410, 320),
    'sehwag': (310, 225, 180, 2650, 320),
    'sourav': (230, 260, 350, 410,198),
    'dravid': (175, 245, 340, 385, 285),
    'yuvraj': (120, 185, 250, 305, 290),
    'zaheer': (85, 130, 185, 110, 220)
}

print(f"players :{players}")
print("-" * 40)

print(f"sachin :{players['sachin']}")
print(f"sachin :{sum(players['sachin'])}")

print("-" * 40)
score = {score for score in players}
print(f"score :{score}")

print("-" * 40)
score = {score for score in players.keys()}
print(f"score :{score}")

print("-" * 40)
score = {score for score in players.values()}
print(f"score :{score}")

print("-" * 40)
score = {k: v for (k, v) in players.items()}
print(f'score :{score}')

print("-" * 40)
score = {k: sum(v) for (k, v) in players.items()}
print(f"score :{score}")

print("-" * 40)
score = {k: (lambda scores: sum(scores) / len(scores))(v)
         for k, v in players.items()}
print(f"score :{score}")

print("-" * 40)
res = [{x :(lambda par: "Mr." + par) ("sachin {}".format(x))}
       for x in range(1, 6)]
print(f"res :{res}")

print("-" * 40)
score = [score for score in players.values()]
print(f"score :{score}")

print("-" * 40)
score = [scr for scores in players.values() for scr in scores]
print(f"score :{score}")

print("-" * 40)
score = [scr for scores in players.values() for scr in scores if scr > 200]
print(f"score :{score}")

print("-" * 40)
score = {name :[scr for scr in scores if scr > 200]
         for name, scores in players.items()}
print(f"score :{score}")
