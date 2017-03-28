cars = 100
spaceInACar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
avgPassengersPerCar = passengers / carsDriven

print "there are", cars, "cars available"
print "there are only", drivers, "drivers available"
print "there will be", carsNotDriven, "empty cars today"
print "we can transport", carpoolCapacity, "people today"
print "we have", passengers, "to carpool today"
print "we need to put about", avgPassengersPerCar, "in each car"
