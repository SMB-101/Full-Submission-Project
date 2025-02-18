# Summation with a for loop
theSum = 0
for count in range(1, 1000001):
    theSum += count
    print(theSum)
# Summation with a while loop
theSum = 0
count = 1
while count <= 100000:
    theSum += count
    count += 1
print(theSum) 
