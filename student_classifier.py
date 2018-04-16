#!usr/bin/python
'''
CLassifies students based on credits taken
'''


while True:
    credits = input("How many credits have you taken: ")
    try:
        credits = int(credits)
        break
    except:
        print("The entry is invalid")
        continue
 
   
if credits <= 23:
    print("You are still a freshman")
elif credits > 23 and credits <= 53:
    print("You are Sophomore")

elif credits >= 54 and credits <= 83:
    print("You are Junior")
else: 
    print("Wow, You are Senior")

