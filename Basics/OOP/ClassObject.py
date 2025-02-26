class Car:
  def __init__(self, b, m):
    self.model = m
    self.brand = b
    
my_car = Car('Toyota', "Corolla")
print(my_car.brand)
print(my_car.model)

new_my_car = Car("Tata", "Safari")
print(new_my_car.brand)
print(new_my_car.model)