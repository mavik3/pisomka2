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
    print(myderive(1,"x"))
    print(myderive("y","x"))
    print(myderive("x","x"))
    print(myderive("y","x"))
    print(myderive(["-",2,"x"],"x"))
    print(myderive(["*",2,"x"],"x"))
    print(myderive(["*","x","x"],"x"))
    print(myderive(["*","x","x"],"y"))
    print(myderive(["*",["-","x",1],"x"],"x"))
    print(myderive(["+","x","x"],"x"))
    print(myderive(["+","y","x"],"x"))
    print(myderive(["/","x","y"],"y"))
