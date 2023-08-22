class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __str__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return total_price


brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

brunch = Menu("brunch", brunch_items, "11am", "4pm")
early_bird = Menu("early-bird", early_bird_items, "3pm", "6pm")
dinner = Menu("dinner", dinner_items, "5pm", "11pm")
kids = Menu("kids", kids_items, "11am", "9pm")

print(brunch)
print(early_bird)
print(dinner)
print(kids)

brunch_order = ['pancakes', 'home fries', 'coffee']
print("Total price for brunch order:", brunch.calculate_bill(brunch_order))

early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
print("Total price for early-bird order:", early_bird.calculate_bill(early_bird_order))

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __str__(self):
        return self.address

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store)
print(new_installment)

print("Available menus at 12 noon:", [menu.name for menu in flagship_store.available_menus("12pm")])
print("Available menus at 5pm:", [menu.name for menu in flagship_store.available_menus("5pm")])

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

arepas_menu = Menu("Take a' Arepa", {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50,
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10am", "8pm")

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

take_a_arepa = Business("Take a' Arepa", [arepas_place])
