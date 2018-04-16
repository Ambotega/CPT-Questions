#!usr/bin/python
'''
prints all the divisors of a number
'''

while True:
    number = input("Enter number: ")
    try:
        number = int(number)
        break
    except:
        print("The entry is invalid")
        continue
 
for i in range(1, number + 1):
    if number % i == 0:
        print i

 
