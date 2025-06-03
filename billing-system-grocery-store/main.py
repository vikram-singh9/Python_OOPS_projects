class Item:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def get_total_price(self):
        return self.quantity * self.price_per_unit
    

class Cart:
    def __init__(self):
        self.items = []  # Empty list to store added items

    def add_item(self, item):
        self.items.append(item)  # Add an item object to the list

    def get_total_amount(self):
        total = 0
        for item in self.items:
            total += item.get_total_price()
        return total

    def print_bill(self):
        print("====== GROCERY BILL ======")
        for item in self.items:
            print(f"{item.name} - {item.quantity} × {item.price_per_unit} = pkr {item.get_total_price()}")
        print("--------------------------")
        print(f"Total Amount: pkr {self.get_total_amount()}")
        print("==========================")

item1 = Item("Apple", 76, 30)
item2 = Item("Orange", 12, 10)
item3 = Item("Mango", 4, 40)
item4 = Item("Grapes", 23, 90)

cart = Cart()

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)
cart.add_item(item4)

cart.print_bill()  # Print the bill with all items and total amount
