class Car():
    def __init__(self,color,millage):
        self.color = color
        self.millage = millage

class Description(Car):
    def description(self):
        print("this car color are ",self.color)

d = Description('red',20)
print("hello")
print("hello")

print(d.millage)