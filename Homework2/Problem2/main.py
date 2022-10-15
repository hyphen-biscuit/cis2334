# Dashiell Wendt 2033998
import datetime

infile = open("inputDates.txt", "r")
outfile = open("parsedDates.txt", "w")

currday = datetime.datetime.now()

for x in infile:
    try:
        xDay = datetime.datetime.strptime(x, '%B %d, %Y\n')
    except:
        continue
    else:
        if(xDay < currday):
            stringFinal = xDay.strftime('%-d/%-m/%Y\n')
            outfile.write(stringFinal)