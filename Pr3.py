
# Variable 1: Instance Variable ---> instance space
#          2: Class(Static) Variable ---- class space

class Car:

    wheels = 4

    def __init__(self) -> None:
        self.mil = 10
        self.com = "BMW"

c1 = Car()

print(c1.wheels)