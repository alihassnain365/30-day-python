
#Call your function factorial, it takes a whole number as a parameter

def factorial(number):
    fact = 1
    if number == 0 :
        return 1
    for i in range(1,number+1):
        fact = fact * i
    return fact

print(f"Factorial of 10 is : {factorial(10)}")

#and it return a factorial of the number
#Call your function is_empty, it takes a parameter and it 
#checks if it is empty or not
#Write different functions which take lists. They should 
#calculate_mean, calculate_median, calculate_mode, calculate_range, 
#calculate_variance, calculate_std (standard deviation).

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_varience(data):
    mean = sum(data) / len(data)
    total = 0
    for i in data:
        total += (i - mean) ** 2
    return total / len(data)

#Write a function called greet which takes a default argument, name.
#If no argument is supplied it should print "Hello, Guest!", otherwise it should 
#greet the person by name.