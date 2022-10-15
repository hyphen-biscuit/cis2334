# Dashiell Wendt 2033998

services =	{
  "Oil change": 35,
  "Tire rotation": 19,
  "Car wash": 7,
  "Car wax": 12
}
print(f"Davy's auto shop services")

for x, y in services.items():
    print(f"{x} -- ${y}")
    
print()
service = []
service.append(input("Select first service:\n"))
service.append(input("Select second service:\n"))

print()
print(f"Davy's auto shop invoice\n")
total = 0;

for x in range(len(service)):
    if(service[x] in services.keys()):
        print(f"Service {x+1}: {service[x]}, ${services[service[x]]}")
        total += services[service[x]]
    else:
        print(f"Service {x+1}: No service")
 
print()
print(f"Total: ${total}")