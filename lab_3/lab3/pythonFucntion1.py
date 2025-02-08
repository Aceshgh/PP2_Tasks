import math 
import random
import itertools
#1
#grams = float(input("Enter grams = "))
#ounces = 28.3495231*grams
#print("In ounces=", ounces)

#2
#F = float(input("Enter in fahrenheit = "))
#C = (5/9)*(F-32)
#print("In Celsium = ", C)

#3
#heads = 35
#legs = 94
#for chicks in range(heads+ 1):
#    rabb= heads-chicks
#    if (chicks*2 + rabb*4) ==legs:
#        print(f"Chickens = {chicks}, Rabbits = {rabb}")

#4
#num =input("Enter numbers = ").split()
#num = [int(n) for n in num]
#prime =[]
#for n in num:
#    if n > 1:
#        prime=True
#        for i in range(2,n):
#            if n%i == 0:
#                prime=False
#                break
#        if prime:
#            prime.append(n)
#print("Prime numbers = ", prime)

#5
#from itertools import permutations
#a =input("Enter = ")
#perm = permutations(a)
#for p in perm:
#    print("".join(p))

#6
#sentence = input("Enter sentence = ")
#words =sentence.split()
#words.reverse()
#print(" ".join(words))

#7
#nums = input("Enter numbers = ").split()
#nums = [int(n) for n in nums]
#found=False
#for i in range(len(nums) -1):
#    if nums[i]==3 and nums[i+1] ==3:
#        found=True
#print(found)

#8
#nums = input("Enter numbers ").split()
#nums = [int(n) for n in nums]
#code = [0,0,7]
#for n in nums:
#    if n==code[0]:
#        code.pop(0)
#    if len(code)==0:
#        print(True)
#        break
#else:
#    print(False)

#9
#r = float(input("Enter radius = "))
#pi = 3.14
#volume =(4/3)*pi*(r**3)
#print("Volume = ",volume)

#10
#list = input("Enter numbers = ").split()
#list = [int(n) for n in list]
#unique =[]
#for n in list:
#    if n not in unique:
#        unique.append(n)
#print("Unique = ",unique)

#11
#word = input("Enter word ")
#word = word.replace(" ", "").lower()
#if word ==word[::-1]:
#    print("It is a palindrome")
#else:
#    print("It isnt a palindrome")

#12
#data = input("Enter numbers = ").split()
#data = [int(n) for n in data]
#for num in data:
#    print("*" *num)

#13
#name = input("Hello! What is your name? ")
#print("I am thinking of a number between 1 and 20.")
#number = random.randint(1, 20)
#attempts =0
#while True:
#    guess = int(input("Enter number = "))
#    attempts +=1
#    if guess <number:
#        print("Your guess is too low")
#    elif guess >number:
#        print("Your guess is too low")
#    else:
#        print("Good job,",name,"! You guessed my num in",attempts,"guesses")
#        break
