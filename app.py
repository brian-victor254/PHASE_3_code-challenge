#no one
def add_numbers(num1, num2):
    return num1 + num2

#no two
def is_even(number):
    return number % 2 == 0
#no three

def reverse_string(text):
    return text[::-1]
# no four
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)
#no five 
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#no six
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)



#no seven
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

#no eight
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

#no nine
# Existing Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

# ElectricCar class inheriting from Car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Sample usage of the ElectricCar class
if __name__ == "__main__":
    my_electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
    my_electric_car.display_info()
    
