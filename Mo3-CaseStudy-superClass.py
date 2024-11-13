#A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
#A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
#year
#make
#model
#doors (2 or 4)
#roof (solid or sun roof).


#super()


class automobile:
    def __init__(self, year, make, model, doors, roof):
        self.year = year 
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


class truck(automobile):
    def __init__(self, year, make, model, doors, roof):
        super().__init__(year, make, model, doors, roof)
        

class boat(automobile):
    def __init__(self):
