def total_distance(initial_height, bounciness_index, bounces):
   
    distance = initial_height
    height = initial_height * bounciness_index
    
    for _ in range(bounces):
        distance += 2 * height
        height *= bounciness_index
    
    return distance

initial_height = float(input("Enter the initial height of the ball (in feet): "))
bounciness_index = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the number of times the ball is allowed to bounce: "))


total = total_distance(initial_height, bounciness_index, bounces)


print(f"The total distance traveled by the ball is {total:.2f} feet.")
