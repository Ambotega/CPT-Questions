#!usr/bin/python
'''this program converts centimeters to inches'''

while True:
    centimeters = input("enter centimeters: ")
    try:
        centimeters = int(centimeters)
    except:
        continue
    
    if centimeters < 0:
        print("the entry is invalid")
        
    else:
        break
        
        
inches = 2.54 * centimeters
print (inches)
	

