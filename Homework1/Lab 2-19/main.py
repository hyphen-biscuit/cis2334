# Dashiell Wendt 2033998
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()
print(f"Lemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon:.2f} cup(s) lemon juice")
print(f"{water:.2f} cup(s) water")
print(f"{agave:.2f} cup(s) agave nectar\n")

newServings = float(input("How many servings would you like to make?\n"))
print()
ratio = newServings / servings

print(f"Lemonade ingredients - yields {newServings:.2f} servings")
print(f"{lemon*ratio:.2f} cup(s) lemon juice")
print(f"{water*ratio:.2f} cup(s) water")
print(f"{agave*ratio:.2f} cup(s) agave nectar\n")

print(f"Lemonade ingredients - yields {newServings:.2f} servings")
print(f"{lemon*ratio/16:.2f} gallon(s) lemon juice")
print(f"{water*ratio/16:.2f} gallon(s) water")
print(f"{agave*ratio/16:.2f} gallon(s) agave nectar")