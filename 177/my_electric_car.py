# Now we can make a new file called my_electric_car.py, import the ElectricCar class, and make an electric car:


from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# This has the same output we saw earlier, even though most of the logic is hidden away in a module:

# 2019 Tesla Model S
# This car has a 75-kWh battery.
# This car can go about 260 miles on a full charge.
