# Collect a employees name
# Collect a employees hrs worked during the week
# Display the collected data in this format:
# john worked 50 hours this week


# declare variables
int_hrs_week = 0
str_employee_name = ""
int_regular_hours = 0
int_OT_hours = 0
INT_REGULAR_HOURS_LIMIT = 40

# Program
str_employee_name = input("Enter employee name: ")
int_hrs_week = int(input("Enter weekly hours: "))

# Determine the number of regular hours, overtime hours:

# case 1: 0 hours inputted by user
# if int_hrs_week == 0:
#  int_regular_hours = 0
#  int_OT_hours = 0

# All cases: if hours less than or equal to INT_REGULAR_HOURS_LIMIT ->
# ELSE -> False

if int_hrs_week <= INT_REGULAR_HOURS_LIMIT:
    int_regular_hours = int_hrs_week
    int_OT_hours = 0
else:
    int_regular_hours = INT_REGULAR_HOURS_LIMIT
    int_OT_hours = int_hrs_week - INT_REGULAR_HOURS_LIMIT

# Output
print(str_employee_name + " worked " + str(int_regular_hours) + " regular rate hours " + "and " + \
str(int_OT_hours) + " overtime hours for a total of " + str(int_hrs_week) + " hours.")