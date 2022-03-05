#data creation in OOPS:
class Person:
    def __init__(self,name):
       self.name = name      #self = current object #name = object variable
    def greet(self):
        print("Hello " + self.name)

p1 = Person("AADITYA")
print(p1.name)
p1.greet()
