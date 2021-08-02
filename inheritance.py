class Base():
    def display(self):
        print("its is home class")

class Drived(Base):
    def display(self):
        print("its drived class")

class Drived2(Drived):    
    def display(self):
        super().display()
        print("its drived 2 class")
        


d = Drived2()
d.display()

