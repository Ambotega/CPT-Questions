#!usr/bin/python
'''
Leap year identifier
'''


while True:
    year = input("Enter year: ")
    try:
        year = int(year)
        break
    except:
        print("The entry is invalid")
        continue
 
   
if year % 4 == 0:
    print("Leap Year")
elif year % 100 == 0 and year % 400 == 0:
    print("Leap Year")
else: 
    print("Not a Leap Year")

