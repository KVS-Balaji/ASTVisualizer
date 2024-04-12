for x in range(5):
    if x % 2 == 0:
        for y in range(x):
            print(x * y)
    else:
        print("x is odd")
