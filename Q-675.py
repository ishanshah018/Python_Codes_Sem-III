class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Location:
    def __init__(self, location, destination):
        self.location = location
        self.destination = destination

    def reflection_x(self):
        print(f"Reflection of Destination: ({self.destination.x}, {-self.destination.y})")

location = Point(2, 3)
destination = Point(4, 5)
loc = Location(location, destination)
loc.reflection_x()
