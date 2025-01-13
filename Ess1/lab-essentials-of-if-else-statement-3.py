#   Author  :   XhannAmatH

income = float(input("Enter the annual income: "))

#
# Write your code here.
#

if(income > 0):
    if(income < 85528):
        tax = (income*0.18)-556.2
    elif(income >85528):
        tax = 14839+((income-85528)*0.32)
else:
    tax = 0
if(tax<=0):
    tax=0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

