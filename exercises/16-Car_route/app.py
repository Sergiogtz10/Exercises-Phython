#Complete the function to return the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.
import math
def car_route(kilometres,km_day):
  return math.ceil(km_day/kilometres)


#Invoke the function with two intergers.
print(car_route(700,750))