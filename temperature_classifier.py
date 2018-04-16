#!usr/bin/python
'''
A temparature classifier program
'''

while True:
    temperature = input("Enter temperature to convert: ")
    try:
        temp = float(temperature)
        break
    except:
        print("The entry is invalid")
        continue
 
   
if temp < -273.15:
    print("Invalid, Temperature below absolute zero")
elif temp == -273.15:
    print ("Temperature is absolute zero")
elif temp > -273.15 and temp<0:
    print("Temperature is below freezing point")
elif temp == 0:
    print("Temperature is at freezing point")
elif temp > 0 and temp < 100:
    print("Temperature is at normal range")
elif temp == 100:
    print("Temperature is at boiling point")
else: 
    print("Temperature is above boiling point")

