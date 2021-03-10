class Animal:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def speak(self):
      return f"My name is {self.name} I am {self.age} years old"


class Dog(Animal):
  def __init__(self, name, age):
      super().__init__(name, age)
      # self.name = name
      # self.age = age

  def speak(self):
      return "Whoof Whoof"

class Cat(Animal):
  def __init__(self, name, age):
      super().__init__(name, age)
      # self.name = name
      # self.age = age