#Grocery List App

import datetime

#Date Time Code Goes Here
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

# Initial Grocery List

grocery = ["Meat", "Cheese"]

print("Welcome to the Grocery List App.")
print("Current Date and Time: " + month + "/" + day + "  " + hour + ":" + minute)

print(f"\nYou currently have {grocery[0]} and {grocery[1]}")

for i in range(1,4):
  food_item = input("Type of food to add to the grocery list: ")
  grocery.append(food_item.title())

print("\nHere is your grocery list:")
print(grocery)

#Sorted grocery list

grocery.sort()
print("\nHere is your sorted grocery list:")
print(grocery)

print("\nSimulate grocery shopping.... ")

print("\nCurrent grocery list: " + str(len(grocery)) + " items")
print(grocery)

new_food = input("\nWhat food did you just buy: ").title()
print("Removing " + new_food + " from the list ....")
grocery.remove(new_food)
print("\nCurrent grocery list: " + str(len(grocery)) + " items")
print(grocery)

new_food = input("\nWhat food did you just buy: ").title()
print("Removing " + new_food + " from the list ....")
grocery.remove(new_food)
print("\nCurrent grocery list: " + str(len(grocery)) + " items")
print(grocery)

new_food = input("\nWhat food did you just buy: ").title()
print("Removing " + new_food + " from the list ....")
grocery.remove(new_food)
print("\nCurrent grocery list: " + str(len(grocery)) + " items")
print(grocery)

print(f"\nSorry, the store is out of {grocery[1]}")

new_food = input("What food would you like instead: ").title()
grocery.pop()
grocery.insert(0,new_food)

print("\nHere is what remains on your grocery list:")
print(grocery)