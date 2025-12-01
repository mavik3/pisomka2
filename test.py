from riesenie import myevald   

print(myevald(1, {}))                                # → 1
print(myevald('x', {'x': 10}))                       # → 10
print(myevald(1, {'x':10}))                          # → 1
print(myevald(['+', 'x', 1], {'x': 10}))             # → 11
print(myevald(['+', ['*','x','y'], 'x'], {'x':10,'y':5}))  # → 60
print(myevald(['/', ['*','x',1.5], 'y'], {'x':3.14,'y':256})) # → 0.0183984375
