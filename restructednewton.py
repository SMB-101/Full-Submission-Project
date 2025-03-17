def limitReached(estimate, prev_estimate, tolerance):
  
    return abs(estimate - prev_estimate) < tolerance

def improveEstimate(estimate, number):
   
 
    return (estimate + number / estimate) / 2

def newton(number, tolerance=1e-10):
   
    estimate = number / 2  
    prev_estimate = 0
    
    while not limitReached(estimate, prev_estimate, tolerance):
        prev_estimate = estimate
        estimate = improveEstimate(estimate, number)
    
    return estimate

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    result = newton(num)
    print(f"The square root approximation of {num} is {result}")
