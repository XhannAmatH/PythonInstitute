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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
