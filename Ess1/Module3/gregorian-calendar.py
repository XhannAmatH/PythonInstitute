#   Author  :   XhannAmatH

year = int(input("Enter a year: "))

#
# Write your code here.
#	
leap=""
if(year%4 and year>1581):
    leap="Common Year"
    if(year%100):
        leap="Leap Year"
        if(year%400):
            leap="Common Year"
else:
    leap="No within the Gregorian calendar period"
            
print(leap)
