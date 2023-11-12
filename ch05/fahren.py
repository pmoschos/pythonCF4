fahrenheit_temps = [32, 67, 90, 102, 75, 68, 55]

# generate a list comprehension
celcius_temps = ["{:.2f}".format((temp -32) * 5 / 9) for temp in fahrenheit_temps]
print("celcius_temps:", celcius_temps)

# generate a generator
celcius_temps = ("{:.2f}".format((temp -32) * 5 / 9) for temp in fahrenheit_temps)
print("celcius_temps:", celcius_temps)

for celcius in celcius_temps:
    print(celcius)
