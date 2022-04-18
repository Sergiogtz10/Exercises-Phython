#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  one_hour = 3600
  one_min = 60
  return secs//one_hour, secs//one_min




#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))