#hogan lee
# this program will calculate the total cost of the road trip

total_milage=float(input("Enter the total miles you will go for this trip :"))
mpg=float(input("Enter the total miles per gallon of your car :"))
day_mile=float(input("Enter the miles per day you can travel :"))
hotel_fare=75
gas_per_gallon=3

#to calculate hotel cost
day_for_trip = total_milage // day_mile
hotel_cost = day_for_trip * hotel_fare

#to calculate the gas
gallon_needed = total_milage / mpg
gas_cost = gallon_needed * gas_per_gallon
total = hotel_cost + gas_cost

print("total travel cost: ", '%s %.1f' % ('$', total))


