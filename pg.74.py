done = False
while not done:
    number = int(input("Enter the numeric grade: "))
    if number >= and number <= 100:
        done = True
    else:
        print("Error: grade must be between 100 and 0")
        print(number) # Just echo the valid input
