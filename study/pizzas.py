# pizzas = ['paperoni', 'pastrami', 'PH']
# # for pizza in pizzas:
# #     print(f"I like {pizza} pizza")
# # print("I really love pizza!")
#
# friend_pizzas = pizzas[:]
#
# pizzas.append('chicken')
# friend_pizzas.append('pina')
#
# print(f"My favorite pizza are:")
# for pizza in pizzas:
#     print(pizza)
# print("\n")
#
# print(f"My friends favorite pizza are:")
# for pizza in friend_pizzas:
#     print(pizza)
# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")
available_toppings = ['mushrooms', 'olives', 'green pappers', 'pepperoni', 'pinapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making your piza!")
