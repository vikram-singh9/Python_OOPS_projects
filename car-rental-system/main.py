class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_rented = False

    def show_info(self):
        status = 'rented' if self.is_rented else 'available'
        print(f'{self.brand} {self.model} {self.year} - {status}')


class carRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f'{self.car} added successfuly!')

    def view_available_cars(self):
        print('\n🚗 Available Cars')
        available = False
        for car in self.cars:
            if not car.is_rented:
                car.show_info()
                available = True
        if not available:
            print('cars are not available!!')





