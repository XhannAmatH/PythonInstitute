#   Author  :   XhannAmatH

p = 'spathiphyllum'
s = input()
if(s == p.title()):
    print("Yes - "+p.title()+" is the best plant ever")
elif(s == p):
    print("No, I want a big "+p.title())
else:
    print(p.title()+"! Not "+s+"!")
