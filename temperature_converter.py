#!usr/bin/python
'''This program is a temparature converter'''

while True:
    temperature = input("Enter temperature to convert: ")
    try:
        temperature = float(temperature)
    except:
        print("The entry is invalid")
        continue
    units_options = "cCfF"
    while True:
        units = input("Enter the units of the temperature you entered, enter C for Celcius or F for Fahrenheits: ")
        if units not in units_options:
        
            print("invalid units, Enter C or F: ")
            continue
        else:
             break
    break
    
if units in "cC":
    converted_units = "degree Fahrenheits"
    converted_temp = ((9*temperature)/5) +32
else:
    converted_units = "degree Celsius"
    converted_temp = (5/9)*(temperature - 32)
    
    
print(converted_temp, converted_units)
    

