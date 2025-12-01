def myevald(f, d):
    if isinstance(f, int) or isinstance(f, float):
        return f
    if isinstance(f, str):
        return d[f]
    op = f[0]
    a = myevald(f[1], d)
    b = myevald(f[2], d)
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    raise ValueError("Neznámy operator: " + op)
