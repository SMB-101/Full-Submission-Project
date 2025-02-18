

def main():
    print("Cube Surface Area Calculator")
    
    
    
    try:
        edge_length = int(input("Enter the length of an edge of the cube (as an integer): "))
        if edge_length <= 0:
            print("The edge length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return


    surface_area = 6 * (edge_length ** 2)

    
    print(f"The surface area of a cube with edge length {edge_length} is {surface_area} square units.")

if __name__ == "__main__":
    main()
