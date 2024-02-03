pizzas = ['paperoni', 'pastrami', 'PH']
# for pizza in pizzas:
#     print(f"I like {pizza} pizza")
# print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append('chicken')
friend_pizzas.append('pina')

print(f"My favorite pizza are:")
for pizza in pizzas:
    print(pizza)
print("\n")

print(f"My friends favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)
