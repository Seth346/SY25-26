def print_menu():
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    return int(input("Enter your choice: "))
def add_item():
    item = input("Enter item to add: ")
    my_list.append(item)
    print(item + " added to your list")
print("Welcome to your shopping list manager!")
def view_list():
    if not my_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list:")
        for item in my_list:
            print(f"-{item}")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in my_list:
        my_list.remove(item)
        print(f"{item} has been removed from your shopping list")
    else:
        print(f"{item} is not in your shopping list")


choice = 0
my_list = []
while choice != 4:
    choice = print_menu()
    if choice == 1:
        add_item()
    if choice == 3:
        view_list()
    if choice == 2:
        remove_item()


print_menu()