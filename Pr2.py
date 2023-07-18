class Computer:
    def __init__(self):
        self.name = "Smruti"
        self.age = 12

    def update(self):
        self.age += 30

    def compare(self,c2):
        if self.age == c2.age:
            return True
        else :
            return False

c1 = Computer()
c2 = Computer()

c1.name = "srn"
c1.age = 12

c1.update()
c2.update()

print(c1.age)
print(c2.age)

print(c1.compare(c2))


# in pythone every element is object 

# id : addredd of the object 