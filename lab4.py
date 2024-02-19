class Cat:
    # class attribute
    name = ""
    age = 0
# create cat1 object
cat1 = Cat()
cat1.name = "Catvy"
cat1.age = 10
# create another object cat2
cat2 = Cat()
cat2.name = "Catsy"
cat2.age = 15

# access attributes
print(f"{cat1.name} is {cat1.age} years old")
print(f"{cat2.name} is {cat2.age} years old")
print("\n")


#2. Init Function
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Student("John", 36)
print(p1.name)
print(p1.age)
print("\n")

#3. Str Function
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Student("John", 20)
print(p1)
print("\n")


#4. Inheritance
class Animal:
    def eat(self):
        print( "I can eat!")
    def sleep(self):
        print("I can sleep!")
# derived class
class Bird(Animal):
    def sing(self):
        print("I can sing! Chip chip!!")
# Create the object of the Bird class
bird1 = Bird()
# Calling members of the base class
bird1.eat()
bird1.sleep()
print("\n")


#5. Encapsulation
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price:{}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
# change the price
c.__maxprice = 1000
c.sell()
# using setter function
c.setMaxPrice(1000)
c.sell()
print("\n")

#6. render() method
class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")
class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")
class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
# create an object of Square
s1 = Square()
s1.render()
# create an object of Circle
c1 = Circle()
c1.render()
print("\n")

#7. Overriding
class Animal:
    # attributes and method of the parent class
    name = ""
    def eat(self):
        print("I can eat")
# inherit from Animal
class Cat(Animal):
    # override eat() method
    def eat(self):
        print("I like to eat fish")
# create an object of the subclass
persian = Cat()
# call the eat() method on the labrador
object
persian.eat()
print("\n")

#8. Super() method
class Animal:
    name = ""
    def eat(self):
        print("I can eat")
# inherit from Animal
class Cat(Animal):
    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()
        print("I like to eat fish")
# create an object of the subclass
persian = Cat()
persian.eat()
print("\n")


#9. Multiple Inheritance
class Mammal:
    def mammal_info(self):
        print("Mammals can give birth to their offspring.")
class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")
class Bat(Mammal, WingedAnimal):
    pass
# create an object of Bat class
b1 = Bat()
b1.mammal_info()
b1.winged_animal_info()
print("\n")

#TryThis1
class Vehicle:
   def __init__(self, seating_capacity):
       self.seating_capacity = seating_capacity
   def fare(self):
       return self.seating_capacity * 100

class Taxi(Vehicle):
   def fare(self):
       total_fare = super().fare()
       return total_fare + (total_fare * 0.10)

taxi = Taxi(4)
print(f"The total fare for the taxi instance is RM {taxi.fare():.2f}")
print("\n")

#TryThis2
class Employee:
    def __init__(self, salary, hours_worked):
       self.salary = salary
       self.hours_worked = hours_worked
    def getInfo(self):
        return f"Salary: RM{self.salary}, Hours Worked: {self.hours_worked} hours"
    def addSalary(self):
        if self.salary < 500:
            self.salary += 10
    def addWork(self):
        if self.hours_worked > 6:
            self.salary += 50
employee = Employee(100, 7)
print(employee.getInfo()) 
employee.addSalary()
employee.addWork()
print(employee.getInfo()) 
print("\n")

#TryThis3
class MyMath:
   def add(self, num1, num2, num3=None, num4=None):
       if num3 is None and num4 is None:
           return num1 + num2
       elif num4 is None:
           return num1 + num2 + num3
       else:
           return num1 + num2 + num3 + num4
my_math = MyMath()
print(my_math.add(1, 2)) 
print(my_math.add(1, 2, 3)) 
print(my_math.add(1, 2, 3, 4))
print("\n")

