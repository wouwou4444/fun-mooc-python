def div (a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Warning division by 0")
    except TypeError:
        print("only numbers")
    print("let's keep running")

def f(x):
    div(1,x)
