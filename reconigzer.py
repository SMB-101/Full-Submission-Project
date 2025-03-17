def read_numbers(filename):
    """Reads numbers from a file and returns them as a list of floats."""
    try:
        with open(filename, 'r') as file:
            return list(map(float, file.readlines()))
    except Exception as e:
        print(f"Error: {e}")
        return []

def compute_average(numbers):
    """Computes the average of a list of numbers."""
    return (sum(numbers) / len(numbers)) if numbers else 0

def main():
    filename = input("Enter the file name: ")
    numbers = read_numbers(filename)
    average = compute_average(numbers)
    print(f"Average: {average}")

if __name__ == "__main__":
    main()
