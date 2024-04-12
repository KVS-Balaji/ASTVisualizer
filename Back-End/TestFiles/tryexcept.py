try:
    result = 10 / 0 
except ZeroDivisionError:
    print("Division by zero error")
else:
    print("Else block")
finally:
    print("This is the finally block")