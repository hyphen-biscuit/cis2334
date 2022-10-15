#Dashiell Wendt 2033998
from math import ceil                     # needed in Step #3

length = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
wallarea =  length*width
paint = float(wallarea)/350
cans = ceil(paint)
colors = {
  "red": 35,
  "green": 23,
  "blue": 25,
}

print(f'Wall area: {wallarea} square feet')
print(f'Paint needed: {paint:.2f} gallons')
print(f'Cans needed: {cans} can(s)')


canColor = input("\nChoose a color to paint the wall:\n")
print(f'Cost of purchasing {canColor} paint: ${colors[canColor]*cans}')