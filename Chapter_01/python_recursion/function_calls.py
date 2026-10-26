def a():
    print("a() was called")
    b()
    print("a() is returning")

def b():
    print("b() was called")
    c()
    print("b() is returning")

def c():
    print("b() was called")
    print("b() is returning")

a()