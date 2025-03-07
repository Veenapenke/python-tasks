try:
    print("Inside try block")
    1 / 0  
except ZeroDivisionError:
    print("Exception caught!")
finally:
    print("This will always execute.")
