def is_equilateral(a, b, c):
    
    return a == b == c

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))


if is_equilateral(side1, side2, side3):
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
