#   Author  :   XhannAmatH

def is_year_leap(year):
    is_leap = False

    if(year%4==0):
        is_leap = True
        if(year%100==0):
            is_leap = False
            if(year%400==0):
                is_leap = True

    return is_leap

def days_in_month(year, month):
    months =[31,28,31,30,31,30,31,31,30,31,30,31]

    if(is_year_leap(year)):
        if(month==2):
            return months[month-1]+1

    return months[month-1]

def day_of_year(year, month, day):
    leap = is_year_leap(year)
    months =[31,28,31,30,31,30,31,31,30,31,30,31]

    if(leap):
        months[1]=29

    days = [d for d in months[:month-1]]
    days = sum(days)
    days += day
    
    return days

print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(2025, 1, 13))


