class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_rented = False

    def show_info(self):
        status = 'rented' if self.is_rented else 'available'
        print(f'{self.brand} {self.model} {self.year} - {status}')
