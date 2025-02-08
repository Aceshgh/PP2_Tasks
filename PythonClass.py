import math


#1
class CoolStringer:
    def self(self):
        self.txt = ""
    def getString(self):
        self.txt = input("Enter words = ")
    def printString(self):
        print(self.txt.upper())
#a =CoolStringer()
#a.getString()
#a.printString()

#2
class shape:
    def area(self):
        return 0
class square(shape):
    def self(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
#a= int(input("Side of a square = "))
#result = square(a) 
#print(result.area()) 

#3
class Rectangle(shape):
    def shape(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
#a = int(input("length = "))
#b = int(input("width = "))
#rect = Rectangle(a, b)
#print(rect.area())

#4
class pointclass:
    def self(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x},{self.y})")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#5
class BankAccountKaspi:
    def self(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"deposit {amount}. new balance {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print(f"withdraw = {amount}. new balance = {self.balance}")
#acc = BankAccountKaspi("name", 1000)
#acc.deposit(500)
#acc.withdraw(200)
#acc.withdraw(2000)

#6
def optimusprimer(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+ 1):
        if n%i ==0:
            return False
    return True

