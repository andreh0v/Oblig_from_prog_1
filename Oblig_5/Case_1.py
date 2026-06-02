#Case 1 Oblig 5
all_wares = {
"amd_processor": {
"name": "AMD Ryzen 9 5900X Processor",
"price": 5590.0,
"number_in_stock": 50,
"ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
"description": "All the cores and threads you'll need!",
},
"playstation_5": {
"name": "PlayStation 5",
"price": 5999.0,
"number_in_stock": 0,
"ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
"description": "Next generation console, never in stock!",
},
"hdmi_cable": {
"name": "Belkin Ultra High Speed HDMI Cable - 2m",
"price": 349.0,
"number_in_stock": 3,
"ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
"description": "A high speed overprices HDMI cable!",
}
}
test_ware = {
    "name": "AMD Ryzen 9 5900X",
    "price": 5590.0,
    "number_in_stock": 50,
    "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
    "description": "All the cores and threads you'll need!"
}
def is_in_stock(ware):
   return ware['number_in_stock'] >= 1
#Oppgave 1
class product:
    def __init__(self, name, price, number_in_stock, description, score):
        self.name = name
        self.price = price
        self.number_in_stock = number_in_stock
        self.description = description
        self.score = score

def print_ware_information(ware):
    print(f" Name: {ware['name']}")
    print(f" Price: {ware['price']},-")
    print(f" Number in stock: {ware['number_in_stock']}")
    print(f" Description: {ware['description']}")



#Oppgave 2
def calculate_average_ware_rating(ware) :
    try:
        ratings=ware['ratings']
        return round(sum(ratings) / len(ratings), 1)
    except ZeroDivisionError:
        return 0
#Oppgave 3
def get_all_wares_in_stock(all_wares):
    in_stock = {}
    for ware_key, ware in all_wares.items(): #ware_key = "amd_processor", "ps5" etc.
        if is_in_stock(ware):
            in_stock[ware_key] = ware
    return in_stock
in_stock = get_all_wares_in_stock(all_wares)
for ware in in_stock.values():
    print_ware_information(ware)
    print()
#Oppgave 4
def is_number_of_ware_in_stock(all_wares):
    