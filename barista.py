print("Hello, welcome to our coffee shop!")
name = input("What is your name?\n")

if name.lower() == "ben":
    print("You are not welcome here, Evil Ben!")
    exit()
else:
    print("Good to see you, " + name + "! Thank you for visiting us today.\n")


menu = "Black Coffee, Latte, Cappuccino, Espresso"
print("What would you like from our menu today? Here is what we are serving:\n" + menu)
order = input()
print("Great choice, " + name + "! Your " + order + " will be ready shortly.")

price = 8
cups = input("How many cups of coffee would you like?\n")
total = price * int(cups)
print("Not a problem, Your total is: $" + str(total) + ".\nWe'll have your " + cups + " " + order + " ready for you in a moment.")