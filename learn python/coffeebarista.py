print("Welcome to Coffeeshop!\n")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia":
  evil = input("Are you  evil?\n")
  if evil == "yes":
    good_deeds_today = int(input("howmany good deeds you did today?\n"))
    if good_deeds_today < 4:
      print("Get out " + name)
      exit()

  else:
    print("\nHello " + name + ", thank you for coming in today!\n")
else:
  print("\nHello " + name + ", thank you for coming in today!\n")

menu = "Black Coffee, Espresso, Latte, Cuppucino"

print(name + ", what would you like to order?\n\n" + "We have " + menu + ".\n")

order = input()

if order == "Black Coffee":
  price = 1.50
elif order == "Espresso":
  price = 3
elif order == "Latte":
  price = 4.50
elif order == "Cuppucino":
  price = 3.50
else:
  print("Sorry, we don't have that item on the menu")

num_cups = input("How many " + order + " would you like?\n")

print("\nSounds good " + name + ", we'll have your " + num_cups + " " + order + " ready for you in a moment\n")

print("\nThat would be " + str(price*int(num_cups)) + "$")

