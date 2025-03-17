#Shelby Bennett
#February 23rd, 2025
#Michael Schnell



def analyze_text(text):
    # Clean and split the text into words
    words = text.split()
    cleaned_words = [word.lower().strip(".,!?;:()[]{}\"'") for word in words]

    # Find the unique words
    unique_words = sorted(set(cleaned_words))

    # Count total words and total letters
    total_words = len(cleaned_words)
    total_letters = sum(len(word) for word in cleaned_words if word.isalpha())
    total_lines = len(lines)

    # Display the results
    print("\n--- Text Analysis Results ---")
    print(f"Total words: {total_words}")
    print(f"Unique words count: {len(unique_words)}")
    print("\nUnique words (sorted):")
    print(", ".join(unique_words))
    print(f"\nTotal letters: {total_letters}\n")

    # Return results as dictionary
    return {
        "total_words": total_words,
        "unique_words": len(unique_words),
        "total_letters": total_letters,
    }



# Open the file in read mode
fileName=input("What is the file name? ")
file = open(fileName, "r")
# Read each line one by one
for line in file:
    print(line.strip())  # .strip() to remove newline characters
    # Run the analysis
    result = analyze_text(line)
# Close the file
file.close()

# Print the entire result dictionary
print("--- Summary of Results ---")
for key, value in result.items():
    print(f"{key.replace('_', ' ').capitalize()}: {value}")

