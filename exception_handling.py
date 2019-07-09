def add(n1,n2):
    print(n1 + n2)

number1 = 10
number2 = input("Enter number : ")
try:
    # Attempt to run code that may have an error
    #add(number1, number2)
    result = 10 + 10
except:
    print("You aren't adding correctly")
else:
    print("Something went wrong")
