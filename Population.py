def predict_population(initial_population, growth_rate, growth_period, total_hours):
    
    periods = total_hours // growth_period
    population = initial_population * (growth_rate ** periods)
    return population


initial_population = int(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the rate of growth (greater than 0): "))
growth_period = int(input("Enter the number of hours to achieve this rate: "))
total_hours = int(input("Enter the total number of hours for growth: "))


predicted_population = predict_population(initial_population, growth_rate, growth_period, total_hours)


print(f"The predicted population after {total_hours} hours is {int(predicted_population)} organisms.")
