class Vehicle():
    def __init__(self, brand):
        self.brand = brand
    
    def start_engine(self):
        print(f"Wroom Wroom")
        
class Engine():
    def __init__(self, name):
        self.name = name
    
    def engine_down(self):
        print("It is sleep time")

class GPS():
    def __init__(self, long, latt):
        self.long = long
        self.lat = latt
    
    def location(self):
        print("Use map")

class Car(Vehicle):
    def __init__(self, brand, doors, model):
        super().__init__(brand)
        self.doors = doors
        self.model = model
    
    def __str__(self):
        return (f"Car is {self.brand}")
    
    def start_engine(self):
        super().start_engine()
        print("Car engine starting with roar!!!")
    
    def honk(self):
        print("Beep! Beep!")

class Moto(Vehicle):
    def start_engine(self):
        print("Motorcycle is ready for adventures")
        
class SportCar(Car):
    def turbi_boot(self):
        print("Started the Turbo Mode")

class Plane(Engine, GPS):
    def __init__(self, name, long, latt, brand):
        Engine.__init__(self, name)
        GPS.__init__(self, long, latt)
        
        self.brand = brand

"""c = Car("BMW")
m = Moto("CFMOTD")"""

"""print(c.brand)
print(c)
print(m)"""

c = Car("Toyota", 4, "Supra")
m = Moto("CFMOTD")
"""print(c.doors)

try:
    print(m.doors)
except:
    print("error for motors")"""
    
c.start_engine()
m.start_engine()

t = SportCar("Ferrari", 2, "S")
t.turbi_boot()

p = Plane("LAstocka", 54, 49, "Boying")
print(p.long, p.lat)