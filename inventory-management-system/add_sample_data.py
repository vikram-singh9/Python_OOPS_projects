from main import InventoryManager

# Initialize the inventory manager
manager = InventoryManager()

# Sample product data
sample_products = [
    {"name": "Laptop", "quantity": 15, "price": 999.99, "category": "Electronics"},
    {"name": "Smartphone", "quantity": 25, "price": 599.99, "category": "Electronics"},
    {"name": "Desk Chair", "quantity": 10, "price": 199.99, "category": "Furniture"},
    {"name": "Coffee Maker", "quantity": 8, "price": 79.99, "category": "Appliances"},
    {"name": "Wireless Mouse", "quantity": 30, "price": 29.99, "category": "Electronics"},
    {"name": "Backpack", "quantity": 20, "price": 49.99, "category": "Accessories"},
    {"name": "Monitor", "quantity": 12, "price": 299.99, "category": "Electronics"},
    {"name": "Desk Lamp", "quantity": 15, "price": 39.99, "category": "Lighting"},
    {"name": "Keyboard", "quantity": 18, "price": 89.99, "category": "Electronics"},
    {"name": "Headphones", "quantity": 22, "price": 149.99, "category": "Electronics"}
]

# Add sample products to the database
for product in sample_products:
    manager.add_product(
        name=product["name"],
        quantity=product["quantity"],
        price=product["price"],
        category=product["category"]
    )

print("Sample products have been added to the inventory.")