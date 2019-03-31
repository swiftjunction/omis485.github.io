#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()


# While loop 
Loop_Again = "y"

while Loop_Again.lower() == 'y':
    print()
    # get input from the user
    miles_driven = float(input("Enter miles driven:\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t"))
    cost_per_gallon = float(input("Enter cost per gallon:\t\t"))


    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
        continue
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
        continue
    elif cost_per_gallon <= 0:
        print ("Cost of a gallon must be greater than zero. Please try again.")
        continue
    else:
        print()
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        mpg = round(mpg, 2)
        print("Miles Per Gallon:\t\t", mpg)

        #Total Cost of Gas
        Total_cost_of_gas = (cost_per_gallon * gallons_used)
        Total_cost_of_gas = round(Total_cost_of_gas, 2)
        print("Total Gas Cost:\t\t\t", Total_cost_of_gas)

        # calculate cost per mile
        cost_per_mile = (Total_cost_of_gas / miles_driven)
        cost_per_mile = round(cost_per_mile, 1)
        print("Cost Per Mile:\t\t\t", cost_per_mile)
        print()

        Loop_Again = input("Get entries for another trip (y/n): ")
                   


print("Bye")




