def flag():
    for i in range(3):
        print("*****===============")
    for i in range(3):
        print("====================")

print("Hello")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print( name + ", You can vote")
    flag()
else:
    print("You cannot vote")
