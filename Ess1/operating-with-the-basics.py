#   Author  :   XhannAmatH

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
var_list = [] 

for n in my_list:
        
    if(n in var_list):
        continue
    else:        
        var_list.append(n)

my_list = var_list
del var_list
print("The list with unique elements only:")
print(my_list)
