def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i 
        return result

try:
    num = int(input("Enter a non-negative number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else: 
        fact = factorial(num)
        print("Factorial of", num, "is", fact)

except ValueError:
    print("Invalid input. Please enter an integer.")

finally:
    print("Calculation complete.")

result = (5 * 3) // 2 + 8 
print("Result of expression:", result)
