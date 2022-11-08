#Dash Wendt 2033998
sections = input().split()
firstName = sections[0]
while firstName != '-1':
    try:
        age = int(sections[1]) + 1
    except ValueError as excpt:
        age = 0
    print('{} {}'.format(firstName, age))
    sections = input().split()
    firstName = sections[0]
    