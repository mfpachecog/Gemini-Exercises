# write a program that converts a given number of miutes into hours
# minutes. 

total_minutes = int(input("Enter the total number of minutes: "))

hours = total_minutes // 60

remaining_minutes = total_minutes % 60

print(f"{total_minutes} is equal to {hours} hours and {remaining_minutes} minutes. ")





