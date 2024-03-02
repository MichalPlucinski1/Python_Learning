class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}: {self.age}'
    
    def print_name(self):
        print(self.name)


p1 = Person('Suzan', 22)
print(p1)


class Student(Person):
    def __init__(self, name, age, code):
        Person.__init__(self, name, age)
        self.code = code
    def __str__(self):
        return Person.__str__(self) + ' code: ' + self.code # also Super()




s1 = Student('Piotrek', 28, 'C3')

print(s1)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)