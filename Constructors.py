# Constructors come from classes

class Point:
  # function that gets called when a new "Point" object is made
  # Constructor:
  def __init__(self, x, y):
    # self is a reference to the current object
    self.x = x
    self.y = y
  
  # Class functions
  def move(self):
    print("move")
  
  def draw(self):
    print("draw")
    
  def values(self):
    return (self.x, self.y)

  
point1 = Point(3,5)
print(point1.values())
print(point1.x)
print(point1.y)
