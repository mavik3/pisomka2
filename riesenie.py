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
def myderive(f, var):
    # constant
    if isinstance(f, (int, float)): return 0
    # variable
    if isinstance(f, str): return 1 if f == var else 0

    op = f[0]
    a = f[1]
    b = f[2]

    da = myderive(a, var)
    db = myderive(b, var)

    if op == "+":
        return ["+", da, db]

    if op == "-":
        return ["-", da, db]

    if op == "*":
        return ["+", ["*", da, b], ["*", a, db]]

    if op == "/":
        return ["/", ["-", ["*", da, b], ["*", a, db]], ["*", b, b]]

    raise ValueError("Neznamy Operator: " + op)


if __name__ == "__main__":
    print(myderive(1, "x"))
    print(myderive(["*", ["-", "x", 1], "x"], "x"))
