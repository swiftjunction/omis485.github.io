#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)

# calculate total gas cost
tgc = (gallons_used * cost_per_gallon)
tgc = round(tgc, 2)

# calculate cost per mile
cpm = (tgc / miles_driven)
cpm = round(cpm, 2)

            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Cost Of Gas:\t\t" + str(tgc))
print("Cost Per Mile:\t\t" + str(cpm))
print()
print("Bye")


