def mean(numbers):
    """
    Computes the mean (average) of a list of numbers.
    Returns 0 if the list is empty.
    """
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    """
    Computes the median of a list of numbers.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    numbers.sort()
    mid = len(numbers) // 2
    return (numbers[mid - 1] + numbers[mid]) / 2 if len(numbers) % 2 == 0 else numbers[mid]

def mode(numbers):
    """
    Computes the mode of a list of numbers.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    from collections import Counter
    return Counter(numbers).most_common(1)[0][0]

def main():
    """
    Tests the mean, median, and mode functions with a sample list.
    """
    numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]
    print(f"Numbers: {numbers}")
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")

if __name__ == "__main__":
    main()
