def main():
    print("Momentum Calculator")
    
    
   
    try:
        mass = float(input("Enter the object's mass (in kilograms): "))
        if mass <= 0:
            print("The mass must be a positive number.")
            return

        velocity = float(input("Enter the object's velocity (in meters per second): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for mass and velocity.")
        return

    momentum = mass * velocity

 
    print(f"\nThe momentum of the object is {momentum:.2f} kg·m/s.")

if __name__ == "__main__":
    main()
