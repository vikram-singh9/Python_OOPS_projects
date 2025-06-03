class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_rented = False

    def show_info(self):
        status = 'Rented' if self.is_rented else 'Available'
        print(f'{self.brand} {self.model} ({self.year}) - {status}')


class CarRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f'{car.brand} {car.model} added successfully!')

    def view_available_cars(self):
        print('\n🚗 Available Cars:')
        available = False
        for car in self.cars:
            if not car.is_rented:
                car.show_info()
                available = True
        if not available:n
            print('No cars available!')

    def rent_car(self, model):
        for car in self.cars:
            if car.model.lower() == model.lower() and not car.is_rented:
                car.is_rented = True
                print(f'\n✅ You rented: {car.brand} {car.model}')
                return
        print('❌ Car not available or already rented!')

    def return_car(self, model):
        for car in self.cars:
            if car.model.lower() == model.lower() and car.is_rented:
                car.is_rented = False
                print(f'\n🔁 You returned: {car.brand} {car.model}')
                return
        print('⚠️ Car not found or not rented.')


# ==== Testing ====

car_rental_system = CarRentalSystem()

# Add cars
car_rental_system.add_car(Car('Tesla', 'TSX', 2025))
car_rental_system.add_car(Car('Mercedes', 'Benz', 2023))

# View available cars
car_rental_system.view_available_cars()

# Rent a car
car_rental_system.rent_car('TSX')

# View again
car_rental_system.view_available_cars()

# Return car
car_rental_system.return_car('TSX')

# Final chec
car_rental_system.view_available_cars()
