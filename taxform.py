

def main():
    try:
        
        income = float(input("Enter your income: "))
        tax_rate = float(input("Enter the tax rate (in %): "))

       
        tax = income * (tax_rate / 100)
        print(f"The calculated tax is: {round(tax, 2)}")
    except ValueError:
        print("Please enter valid numerical values for income and tax rate.")

if __name__ == "__main__":
    main()
