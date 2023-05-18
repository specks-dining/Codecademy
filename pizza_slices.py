# Our pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Our prices per slice
prices = [2, 6, 1, 3, 2, 7, 2]

# Number of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Length of how many toppings we offer
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")

# Prices of our pizzas
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sort prices lowest to highest
pizza_and_prices_sorted = sorted(pizza_and_prices)
print(pizza_and_prices_sorted)

# Save cheapest pizza
cheapest_pizza = pizza_and_prices_sorted[0]

# Save most expensive pizza
priciest_pizza = pizza_and_prices_sorted[-1]

# Anchovies sold out, need to remove
pizza_and_prices_sorted.pop()

# Add new pizza topping
pizza_and_prices_sorted.insert(4, [2.5, "peppers"])

# Three lowest cost slices ordered
three_cheapest = pizza_and_prices_sorted[:3]
print(three_cheapest)
