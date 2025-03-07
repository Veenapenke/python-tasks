try:
    x = int("abc")  
    y = 10 / 0      
except ValueError:
    print("ValueError occurred!")
except ZeroDivisionError:
    print("ZeroDivisionError occurred!")
