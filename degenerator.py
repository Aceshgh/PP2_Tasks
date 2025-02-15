#1
#def square_generator(n):
#    for i in range(n + 1):
#        yield i ** 2

#a = input()
#for num in square_generator(a):
#    print(num, end=" ")




#2
#def even_generator(n):
#    for i in range(0, n + 1, 2):
#        yield i

#n = int(input("Enter a number: "))
#print(",".join(map(str, even_generator(n))))





#3
#def divider(n):
#    for i in range(n+1):
#       if i%3 ==0 and i%4 ==0:
#            yield i

#print(list(divider(50)))





#4
#def square(a, b):
#    for i in range(a, b+1):
#        yield i**2

#a = input()
#b = input
#for value in square(a, b):
#    print(value,end=" ")




#5
#def cuntdown(n):
#    while n>= 0:
#        yield n
#        n -=1

#a = input()
#for num in cuntdown(5):
#    print(num,end=" ")
