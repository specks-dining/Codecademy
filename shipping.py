# Weight of package
weight = 41.5

# Ground Shipping
if weight <= 2:
  price_per_pound = 1.5
elif weight <= 6:
  price_per_pound = 3
elif weight <= 10:
  price_per_pound = 4
else:
  price_per_pound = 4.75

# Ground Shipping Flat Rate Cost
flat_rate = 20

# Ground Shipping Calculator
shipping_cost = (weight * price_per_pound) + flat_rate

# Premium Shipping
p_shipping_cost = 125

# Drone Shipping
if weight <= 2:
  d_price_per_pound = 4.5
elif weight <= 6:
  d_price_per_pound = 9
elif weight <= 10:
  d_price_per_pound = 12
else:
  d_price_per_pound = 14.25

# Drone Shipping Calculator
d_shipping_cost = (weight * d_price_per_pound)

# Show Calculations
print("Ground Shipping Cost: "), print(shipping_cost)
print("Premium Shipping Cost: "), print(p_shipping_cost)
print("Drone Shipping Cost: "), print(d_shipping_cost)
