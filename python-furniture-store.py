# Lovely Loveseat info
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = float(254.00)

# Stylish Settee info
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = float(180.50)

#Luxurious Lamp info
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = float(52.15)

# Sales tax
sales_tax = float(1.088)

#Customer One
customer_one_subtotal = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = lovely_loveseat_description, luxurious_lamp_description
customer_one_total = customer_one_subtotal * sales_tax
print("Customer One Items:", customer_one_itemization)
print("Customer One Total:", customer_one_total)
