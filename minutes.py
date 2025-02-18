

def main():
    
    years = int(input("Enter the number of years: "))

  
    minutes_per_year = 365 * 24 * 60  
    total_minutes = years * minutes_per_year


    print(f"There are {total_minutes} minutes in {years} year(s).")

if __name__ == "__main__":
    main()
