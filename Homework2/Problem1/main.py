## Dashiell Wendt 2033998

print(f"Birthday Calculator")
print(f"Current day")
currmonth = int(input("Month: "))
currday = int(input("Day: "))
curryear = int(input("Year: "))
print(f"Birthday")
birtmonth = int(input("Month: "))
birtday = int(input("Day: "))
birtyear = int(input("Year: "))
yearsold = curryear - birtyear - 1
if(currmonth > birtmonth):
    yearsold += 1
elif(currmonth == birtmonth):
    if(currday >= birtday):
        yearsold += 1
        if(currday == birtday):
            print(f"Happy Birthday!")
print(f"You are {yearsold} years old.")