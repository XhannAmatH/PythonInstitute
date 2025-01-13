#   Author  :   XhannAmatH
#   12:15 and 45 duration should print 13:00

def resultTime(hour, mins, dura):
    if(hour+(mins+dura)//60 >23):
        print(str((hour+(mins+dura)//60)-24)+':'+str((mins+dura)%60))
    else:
        print(str(hour+(mins+dura)//60)+":"+str((mins+dura)%60))


hour = int(input("Insert the hour : "))
mins = int(input("Insert the minutes : "))
dura = int(input("Insert the duration of an event : "))


resultTime(hour,mins,dura)
