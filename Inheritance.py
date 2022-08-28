# Classes can inherit methods and definitions from a parent class

# Parent class
class Mammal:
  def walk(self):
    print("walk")
 

# instead of self, we pass the parent class as an argument
class Dog(Mammal):
  def bark(self):
    print("bark")
  pass #means nothing, but allows the class to have something to not throw an error
          #only needed if empty class


class Cat(Mammal):
  def meow(self):
    print("Meow")


