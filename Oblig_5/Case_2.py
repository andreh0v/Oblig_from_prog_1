#Oppgace.1
from datetime import date


class car:
    def __init__(self, brand,model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km
    def print_car_info(self):pass
    def get_car_age(self):pass
    def rent_car_monthly_price(self):pass
    def next_eu_control(self):pass
    def calculate_total_price(self):pass

def print_car_info(car):
    print(f"Brand : {car['brand']}")
    print(f"Model : {car['model']}")
    print(f"Price : {car['price']},-")
    print(f"Manufactured : {car['year']} - {car['month']}")
    if car['new']:
        print("condition : New")
    else:
        print("condition : Used")
test_car = {
    "brand": "Toyota",
    "model": "Corolla",
    "price": 96000,
    "year": 2012,
    "month": 8,
    "new": False,
    "km": 163000
}
#Task 2
def create_car(brand, model, price, year, month, new, km):
    car = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km":km
    }
    return car

my_car = create_car("Toyota", "Corolla", 96000, 2012, 8, False, 163000)
print_car_info(my_car)

#Task 3
def get_car_age(car):
   return date.today().year - car['year']
print(f"The car is {get_car_age(test_car)} years old.")

#Task 4
def rent_car_monthly_price(car):
    monthly = (car['price'] *0.4) / 12
    if car['new']:
        monthly += 1000
    return round(monthly,2)

print(f"Monthly rent: {rent_car_monthly_price(test_car)} kr")

#Task 5
def next_eu_control(car):
   return date(car['year'] + 2, car['month'],1)
 
print(f"Next EU control: {next_eu_control(test_car)}")

#Task 6
def calculate_total_price(car):
    age = get_car_age(car)
    if car['new']:
        fee=10783
    elif 0 <= age <=3:
        fee = 6681
    elif 4<=age<=11:
        fee = 4034
    elif 12<=age<=29:
        fee = 1729
    else: fee = 0
    return car['price'] + fee

print(f"Total price: {calculate_total_price(test_car)} kr")