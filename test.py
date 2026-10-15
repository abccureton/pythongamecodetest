print("welcome to test1 press any key to continue")
(input())


print("You enter building 244.")
print("to your left you see a hallway labelled finance")
print("straight ahead is a monster vending machine")
print("to your right is a hallway labeled DEERs")
print(".....")

direction = input("Choose left, forward, or right: ").lower()

if direction == "left":
    print("You went left and were robbed.")
elif direction == "forward":
    print("You went forward and were refreshed.")
elif direction == "right":
    print("You went right and got a divorce.")
else:
    print("Invalid choice. you are dead.")
