import os

def list_files():
    """Lists all files in the current directory."""
    files = [f for f in os.listdir() if os.path.isfile(f)]
    print("\n".join(files) if files else "No files available.")

def view_file():
    """Displays the contents of a selected file."""
    list_files()
    filename = input("Enter the file name: ")
    if os.path.isfile(filename):
        try:
            with open(filename, 'r') as file:
                print("\n" + file.read() + "\n")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("File not found.")

def main():
    while True:
        choice = input("\n1 - List files\n2 - View file\n3 - Exit\nChoose: ")
        if choice == '1':
            list_files()
        elif choice == '2':
            view_file()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
