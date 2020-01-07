cars = 100
space_in_cars = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = space_in_cars * cars_driven
average_person_per_car = passengers / cars_driven

print("There are", cars, "cars availabe")
print("There are only", drivers, "total drivers are available")
print("There will be", cars_not_driven, "empty care are there")
print("We can transport", car_pool_capacity, "people today")
print("We have", passengers, "passengers to transport")
print("We need to put about", average_person_per_car, "in each car")
