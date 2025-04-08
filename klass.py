class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width 
    def area(self): #площадь комнаты
        return self.length * self.width
    def heating_power(self): #тепловая мощность
        return self.area() * 100

class Apartment: #комнаты
    def __init__(self, rooms):
        self.rooms = rooms
    def total_area(self): #площадь квартиры
        return sum(room.area() for room in self.rooms)
    def heating_power(self): #обогрев
        return sum(room.heating_power() for room in self.rooms)

class Building:
    def __init__(self, apartments):
        self.apartments = apartments  #список квартир
    def total_area(self):#площадь дома
        return sum(apartment.total_area() for apartment in self.apartments)
    def heating_power(self):#обогрев дома
        return sum(apartment.heating_power() for apartment in self.apartments)

if __name__ == "__main__":
    room1 = Room(4, 5)
    room2 = Room(3, 4) 
    room3 = Room(5, 6)
    apartment1 = Apartment([room1, room2])
    apartment2 = Apartment([room3])
    building = Building([apartment1, apartment2])
    print(f"S кв1 {apartment1.total_area()} м²")
    print(f"Ватт кв1 {apartment1.heating_power()} Вт")
    print(f"S кв2 {apartment2.total_area()} м²")
    print(f"Ватт кв2 {apartment2.heating_power()} Вт")
    print(f"S дома {building.total_area()} м²")
    print(f"Ватт дома {building.heating_power()} Вт")
