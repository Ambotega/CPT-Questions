#!usr/bin/python
'''
CLassifies student according to credits taken
'''


while True:
    credits = input("Enter credits taken: ")
    try:
        credits = int(credits)
        break
    except:
        print("The entry is invalid")
        continue
 
   
if credits <= 23:
    print("Freshman")
elif credits > 23 and credits <= 53:
    print("Sophomore")

elif credits >= 54 and credits <= 83:
    print("Junior")
else: 
    print("Senior")

