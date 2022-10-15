# Dashiell Wendt 2033998

f = open(input(), "r")

line = f.readline()

wordArray = line[:-1].split(",")

uniqueList = []
for x in wordArray:
    if x not in uniqueList:
        uniqueList.append(x)

for y in uniqueList:
    print(y, wordArray.count(y))