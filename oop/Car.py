# My first OOP code

class Car:
    cars_to_sell  = 0
    
    def __init__(self, name, model, fuel, year):
        """Init class & count cars"""

        self.version = "v1.2-beta"
        self.author = "Raibisu Yuu Kuramu"
        self.website = "https://yuukuramu.xyz"

        self.name = name
        self.model = model
        self.fuel = fuel 
        self.year = year 

        print(f"Car {self.name} added!")
        
        Car.cars_to_sell += 1

    def show_info(self):
        """Method who show's car information"""

        return f"""
Car: {self.name}
Model: {self.model}
Fuel: {self.fuel}
Year: {self.year}

"""


bmw     = Car("BMW", "x5", "TDI 4l", "2015")
audi    = Car("Audi", "Q7", "95 2.5l", "2016")

print(audi.show_info())
print(bmw.show_info())

if Car.cars_to_sell > 0:
    print("Cars to sell", Car.cars_to_sell)
else:
    print("No more cars to sell!")