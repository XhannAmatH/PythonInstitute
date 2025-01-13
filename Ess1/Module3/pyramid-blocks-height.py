#   Author  :   XhannAmatH

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height=0
while(True):
    blocks-=height
    if(blocks<=height):
        break
    else:
        height+=1

print("The height of the pyramid:", height)
