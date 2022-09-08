time_rightnow_string = input("what is the time right now (in hours)? ")
amountof_time_string = input("number of hours? ")

time_rightnow_int = int(time_rightnow_string)
amountof_time_int = int(amountof_time_string)

hours = time_rightnow_int + amountof_time_int

timeofday = hours % 24

print(timeofday)