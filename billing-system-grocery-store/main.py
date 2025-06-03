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
            print(f"{item.name} - {item.quantity} × {item.price_per_unit} = ₹{item.get_total_price()}")
        print("--------------------------")
        print(f"Total Amount: ₹{self.get_total_amount()}")
        print("==========================")
