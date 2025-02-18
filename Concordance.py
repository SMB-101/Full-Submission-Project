from collections import Counter
import re

def compute_concordance(filename, n=1):
    """
    Computes a concordance for a given file.

    Parameters:
    filename (str): The path to the file.
    n (int): The number of words in each sequence (default is 1).

    Returns:
    list: A list of (sequence, frequency) tuples sorted alphabetically.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return []

    words = re.findall(r'\b\w+\b', text)
    sequences = [" ".join(words[i:i + n]) for i in range(len(words) - n + 1)]
    frequency = Counter(sequences)
    return sorted(frequency.items())

def display_concordance(concordance):
    """
    Displays the concordance.

    Parameters:
    concordance (list): A list of (sequence, frequency) tuples.
    """
    for sequence, freq in concordance:
        print(f"{sequence}: {freq}")

def main():
    filename = input("Enter the filename: ")
    n = int(input("Enter the number of words per sequence (default is 1): ") or 1)
    concordance = compute_concordance(filename, n)
    if concordance:
        print("\nConcordance:")
        display_concordance(concordance)

if __name__ == "__main__":
    main()
