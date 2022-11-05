#Dashiell Wendt 2033998

input = input()
my_list = sorted([int(i) for i in input.split() if int(i) >= 0])
for value in my_list:
  print(value, end = ' ')