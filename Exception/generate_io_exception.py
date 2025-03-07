try:
    f = open("/root/protected.txt", "w")  
except OSError as e:
    print(f"I/O Error: {e}")
