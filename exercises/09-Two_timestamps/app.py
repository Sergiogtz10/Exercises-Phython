#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    one_hour = 3600
    one_min = 60 
    one_sec = 1
    return (one_hour*hr2 + min2*one_min + sec2*one_sec) - (one_hour*hr1 + min1*one_min + sec1*one_sec)


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))