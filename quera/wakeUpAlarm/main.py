current_time = input()
alarm_time = input()

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

current_seconds = time_to_seconds(current_time)
alarm_seconds = time_to_seconds(alarm_time)

# Calculate the time difference in seconds
time_difference = alarm_seconds - current_seconds

# If the difference is negative, add the number of seconds in a day
if time_difference <= 0:
    time_difference += 24 * 60 * 60

# Convert the time difference back to hours, minutes, and seconds
hours = time_difference // 3600
minutes = (time_difference % 3600) // 60
seconds = time_difference % 60

# Format and print the result
formatted_result = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
print(formatted_result)



