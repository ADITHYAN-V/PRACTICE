##travel_log=[
##{
##    "Country":"France",
##    "Visits":12,
##    "Cities":["Paris","Lille","Dijon"]
##},
##{
##    "country":"Germany",
##    "Visits":5,
##    "cities":["Berlin","Lille","Dijon"]
##},
##]
travel_log=[]

def add_new():
    newcountry=input("Enter new country name: ")
    times=input("Enter the number of times visited: ")
    cities=[]
    c='y'
    while c=='y':
        newname=input("Enter the city name you have visited: ")
        cities.append(newname)
        c=input("Do you wanna continue (y/n): ").lower()
    new_log={}
    new_log["Country"]=newcountry
    new_log["Times"]=times
    new_log["Cities"]=cities
    travel_log.append(new_log)
    
##    travel_log.append({"country":newcountry,"visits":times,"cities":cities})
    print(travel_log)
ch='y'
while ch=='y':
    add_new()
    ch=input("Do you wanna continue adding to the log (y/n)").lower()
    
print("***THANKYOU***"*5)
