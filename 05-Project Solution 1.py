
# Collect a employees name
# Collect a employees hrs worked during the week
# Display the collected data in this format:
# john worked 50 hours this week


# declare variables
int_hrs_week = 0
str_employee_name = ""

# Program
str_employee_name = input("Enter employee name: ")
int_hrs_week = int(input("Enter weekly hours: "))

# Output
print(str_employee_name + " worked " + str(int_hrs_week) + " hours this week")
