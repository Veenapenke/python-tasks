from protected_fields import A

class C(A):
    def access_protected(self):
        print(self._protected_var)  
        self._protected_method()    
if __name__ == "__main__":
    objC = C()
    objC.access_protected()

    objA = A()
   
