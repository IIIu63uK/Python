numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number_total = ""

for number in numbers:
    if number == 1:
        number_total = number_total + str(number) + "st "
    elif number == 2:
        number_total = number_total + str(number) + "nd "
    elif number == 3:
        number_total = number_total + str(number) + "rd "
    else:
        number_total = number_total + str(number) + "th "

print(number_total)
