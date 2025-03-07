class Example:
    static_var = 25
obj1 = Example()
obj1.static_var = 55
print(Example.static_var)
print(obj1.static_var)