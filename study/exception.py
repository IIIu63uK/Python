# try:
#     # Code that may raise an exception
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except Exception as e:
#     print("An error occurred:", str(e))

# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# try: 
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     num3 = int(input("Enter another number: "))
#     num4 = int(input("Enter another number: "))
#     num5 = int(input("Enter another number: "))
#     result = max(num1, num2, num3, num4, num5)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

# try:
#     string_1 = input("Enter a string: ")
#     num_1 = float(string_1)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

# try:
#     file_name_1 = input("Enter a file name: ")
#     file = open(file_name_1, "r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("File not found.")