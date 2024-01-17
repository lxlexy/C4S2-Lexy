#题目一
def case_counter(text1):
    countup = 0
    countlow = 0
    for letters in text1:
        if letters.isupper():
            countup += 1
        if letters.islower():
            countlow += 1
    print(f"Uppercase letters: {countup}, Lowercase letters:{countlow})

#题目1
# Inventory Management System
inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

#题目2
# Function to view all items in the inventory
def view_inventory():
    for x in inventory:
        print("%s: %s"%(x,inventory[x]))
###print(f"{item}:{quantity}") 这个格式很重要啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊

#题目3
def update_item(item, quantity):
     if item in inventory:
        inventory[item] = quantity
     else:
         print("The inventory name is not fount.")

#题目4
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            item = input("Please enter the item name:")
            quantity = int(input("please enter the item quantity"))
            add_item(item, quantity)
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == "4":
            break
        else:
            print("The choice is invalid.")
            
if __name__ == "__main__":
    manage_inventory()

##if choice == "1":
##
##try:
#quantity
##except:看笔记图片