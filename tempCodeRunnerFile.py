class Computer:
    def config(self):
        print("comp 1 15gb 12gb 1tb")



com1 = Computer()

com1.config()

Computer.config(com1)

print(type(com1))