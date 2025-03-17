def newton(number, tolerance=1e-10):
   
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    estimate = number
    while True:
        better_estimate = (estimate + number / estimate) / 2
        if abs(better_estimate - estimate) < tolerance:
            return better_estimate
        estimate = better_estimate

def main():
    
    while True:
        user_input = input("Enter a number to compute its square root (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            result = newton(number)
            print(f"The estimated square root of {number} is {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
