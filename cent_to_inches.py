#!usr/bin/python
'''this program converts centimeters to inches'''

while True:
    centimeters = input("Enter centimeters: ")
    try:
        centimeters = float(centimeters)
    except:
        continue
    
    if centimeters < 0:
        print("The entry is invalid")
        
    else:
        break
        
        
inches = 2.54 * centimeters
print (inches, "inches")
	

