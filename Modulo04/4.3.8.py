def liters_100km_to_miles_gallon(liters):
    return 100 * 1000 / 1609.344 * 3.785411784 / liters

def miles_gallon_to_liters_100km(mpg):
    return 100 * 3.785411784 / (mpg * 1.609344)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))