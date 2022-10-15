#Dashiell Wendt 2033998
a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())
b3 = int(input())
for x in range(-10, 10):
    for y in range(-10, 10):
        if(a1 * x + a2 * y == a3 and b1 * x + b2 * y == b3):
            print(x, y)
            exit()
print('No solution')