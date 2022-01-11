#Prints the number of days of a given month in a given year
def leapchecker(year):
    '''Checks if the input(int) is a leap year'''
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return True
def days_in_month():
    '''Prints the number of days in a given month and given year'''
    monthdays={
        "January":31,
        "February":28,
        "March":31,
        "April":30,
        "May":31,
        "June":30,
        "July":31,
        "August":31,
        "September":30,
        "October":31,
        "November":30,
        "December":31
        }
    y=int(input("Enter year"))
    if leapchecker(y):
        monthdays["February"]=29
    mon=input("Enter the required month for which you wanna check number of days").title()
    print(monthdays[mon])
days_in_month()
        
        
