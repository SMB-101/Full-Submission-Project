

import math

def main():
    print("Sphere Properties Calculator")
   
    
   
    try:
        radius = float(input("Enter the radius of the sphere (as a floating-point number): "))
        if radius <= 0:
            print("The radius must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid floating-point number.")
        return

    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    surface_area = 4 * math.pi * (radius ** 2)
    volume = (4 / 3) * math.pi * (radius ** 3)

    print("\nSphere Properties:")
    print(f"Diameter: {diameter:.2f} units")
    print(f"Circumference: {circumference:.2f} units")
    print(f"Surface Area: {surface_area:.2f} square units")
    print(f"Volume: {volume:.2f} cubic units")

if __name__ == "__main__":
    main()
