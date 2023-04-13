class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width
    
    def perimetr(self):
        return 2*(self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        print(f'Width - {self.width}')
        print(f'Length - {self.length}')
        print(f'Perimetr - {self.perimetr()}')
        print(f'Area - {self.area()}')
        
class Parallelepipede(Rectangle):
    def __init__(self,length, width, height):
        super().__init__(length, width)
        self.height = height
        
    def volume(self):
        return self.length * self.width * self.height
            
myRectangle = Rectangle(10 , 5)
myRectangle.display()
print("----------------------------------")
myParallelepipede = Parallelepipede(10 , 4 , 2)
print("the volume of myParallelepipede is: " , myParallelepipede.volume())