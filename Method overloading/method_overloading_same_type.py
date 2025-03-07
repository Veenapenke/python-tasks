class Example:
    def show(self, a, b=None):  
        if b is None:
            print(f"Method with 1 parameter: a = {a}")
        else:
            print(f"Method with 2 parameters: a = {a}, b = {b}")

obj = Example()
obj.show(10)       
obj.show(10, 20)  
