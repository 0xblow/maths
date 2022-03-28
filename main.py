# Defining a constant global variable for the value of pi.
PI = 3.14159


# Function to contain the menu.
def menu():
    # Print the menu.
    print("Calculations")
    print("1. Calculate area of a square")
    print("2. Calculate area of a circle")
    print("3. Display palindromes up to 1,000")
    print("4. Exit")

    # Ask user for input.
    option = int(input("Enter an option: "))
    if option == 1:
        print("\n**** Area of a square ****")
        # Ask user for the width in cm.
        width = int(input("Enter width of square (cm): "))
        print("The area of a square of " + str(width) + "cm = " + str(area_square(width)) + "cm squared\n")
        # Return user to main menu.
        menu()
    elif option == 2:
        print("\n**** Area of a circle ****")
        # Ask User for the radius in cm.
        radius = int(input("Enter radius of circle (cm): "))
        # Print the area of the circle.
        print("The area of a circle of " + (str(radius)) + "cm = " + str(area_circle(radius)) + "cm squared\n")
        # Return user to main menu.
        menu()
    elif option == 3:
        print("\n**** Palindromes ****")
        for i in range(1000):
            if is_palindrome(i):
                # Print all the palindromes between 0 and 1000.
                print(i)
        # Return user to main menu.
        menu()
    # Menu option to close the program.
    elif option == 4:
        quit()
    # Error checking.
    elif option < 1 or option > 4:
        print("Invalid option")
        menu()


# Function to calculate the area of a square.
def area_square(width):
    return width * width


# Function to calculate the area of a circle.
def area_circle(radius):
    return PI * (radius * radius)


# Function to identify a palindrome.
def is_palindrome(num):
    st = str(num)
    reverse = ""
    for i in range(len(st), 0, -1):
        reverse += st[i - 1]
    return st == reverse


# Start running the program.
menu()
