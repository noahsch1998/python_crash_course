# import car and give it the alias 'c'
# the alias is not required
import car as c

my_mustang = c.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_tesla = c.ElectricCar('tesla', 'cybertruck', 2024)
print(my_tesla.get_descriptive_name())