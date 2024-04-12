def fibonacci(n):
    """Calculates the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        result = 0
        prev1 = 1
        prev2 = 0
        for i in range(2, n + 1):
            result = prev1 + prev2
            prev2 = prev1
            prev1 = result
        return result

try:
    num = int(input("Enter a non-negative number for Fibonacci: "))
    if num < 0:
        print("Fibonacci sequence is not defined for negative numbers.")
    else: 
        fib_value = fibonacci(num)
        print("The", num, "th Fibonacci number is:", fib_value)

except ValueError:
    print("Invalid input. Please enter an integer.")

finally:
    print("Fibonacci calculation complete.")

# More complex expressions and a nested loop
discount = 0.0 
total_price = 150
item_prices = [25, 32, 18.5, 40] 

for price in item_prices:
    if price > 30:
        discount += 0.15 * price  # 15% discount
    else:
        discount += 0.1 * price   # 10% discount

final_price = total_price - discount
print("Final price after discount:", final_price)
