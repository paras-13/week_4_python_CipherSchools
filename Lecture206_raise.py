def add(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    raise TypeError("You are entering wrong data type")
print(add(2,2))