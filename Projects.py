def replace_word():
    str = "Hii guys, i am tomi"
    word_to_replace = input("Enter the Word Replace : ")
    word_replacement = input("Enter the Word Replacement : ")

    print(str.replace(word_to_replace, word_replacement))


# replace_word()


class Calculator:
    def __init__(self, x=0, y=0):
        self.num1 = x
        self.num2 = y

    def add(self):
        return int(self.num1) + int(self.num2)

    def sub(self):
        return int(self.num1) - int(self.num2)

    def mul(self):
        return int(self.num1) * int(self.num2)

    def div(self):
        return int(self.num1) / int(self.num2)

    def inputData(self):
        self.num1 = input("enter num1 : ")
        self.num2 = input("enter num2 : ")
        self.options = input("Option : ")

        if self.options == "+":
            print("Answer = ", self.add())
        elif self.options == "-":
            print("Answer = ", self.sub())
        elif self.options == "*":
            print("Answer = ", self.mul())
        elif self.options == "/":
            print("Answer = ", self.div())


# calc = Calculator()

# calc.inputData()


def EmailSlicer(file):
    data = open(file, "r")

    fileLocation = "newUser.txt"

    dataWrite = open(fileLocation, "w")

    for x in data:
        line = x.strip().split("@")
        print(line[0])
        dataWrite.write(line[0] + "\n")

    data.close()


# EmailSlicer("EmailData.txt")


def BinarySearch(list, key):
    
    pass


dataList = [55, 11, 10, 44, 66, 77]
