import calculator
try:
    print(calculator.sum(1, 2))
    print(calculator.sub(2, 10))
    print(calculator.mul(3, 3))
    print(calculator.div(10, 0))
except ZeroDivisionError:
    print("Division by zero is not allowed")
except Exception as e:
    print("An error occurred:", e)
