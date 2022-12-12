# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(self.name,self.age)
# class Employee(Person):
#     pass
# a = Employee("Nityam",19)
# a.display()




# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
    
#     def display(self):
#         print(self.name,self.age)
# class Employee(Person):
#     def __init__(self, name,age,year):
#         super().__init__(name, age)
#         self.year = year

#     def welcome(self):
#         print("Welcome",self.name,"you are",self.age,"year old your year is",self.year)

# a = Employee("Nityam",19,2003)
# a.welcome()

# class Animal:
#     def speak(self):
#         print("Animal is speaking")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking")

# class Puppy(Dog):
#     def eat(self):
#         print("Pupy is eating bread")

# a = Puppy()
# a.speak()
# a.bark()
# a.eat()

class Calc1:
    def add(self,a,b):
        return a+b
class Cal2:
    def mult(self,a,b):
        return a*b
class Calc3(Calc1,Calc2):
    def div(self,a,b):
        return a//b

a = Calc3()
print(a.add(10,20))
print(a.mult(4,3))
print(a.div(10,5))