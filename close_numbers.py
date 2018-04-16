#!usr/bin/python
'''
Checks if the difference between 2 numbers are within 0.001
'''


numbers = [0, 0]
words = ["first", "second"]
for i in range(len(numbers)):
    while True:
        number_entered = input("Enter the %s number: " %words[i])
        try:
            numbers[i] = float(number_entered)
            break
        except:
            print("The entry is invalid")
            continue

 

if abs(numbers[0] - numbers[1]) <= 0.001:
   print("Numbers are close")

else: 
    print("Numbers are not close")


