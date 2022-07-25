


# declare variables
list_hrs_week = []
list_employee_name = []
list_regular_hours = []
list_OT_hours = []
INT_REGULAR_HOURS_LIMIT = 40
continue_looping = True # add a loop condition

# Declare a function to update the lists and perform calculations as requried
def calculate_hours(emp_name, numb_hours):
    list_employee_name.append(emp_name)
    list_hrs_week.append(numb_hours)
 
    if numb_hours <= INT_REGULAR_HOURS_LIMIT:
        list_regular_hours.append(numb_hours) 
        list_OT_hours.append(0)
    else:
        list_regular_hours.append(INT_REGULAR_HOURS_LIMIT)
        list_OT_hours.append(numb_hours - INT_REGULAR_HOURS_LIMIT)
   
# Program
# Main run loop:

while continue_looping == True:
    str_employee_name = input("Enter employee name: ")
    int_hrs_week = int(input("Enter weekly hours: "))

    # Call the function:
    calculate_hours(str_employee_name,int_hrs_week)

    loop_again = input("Enter another (y/n)? ")
    if loop_again == "n":
        continue_looping = False



# Output
print(list_employee_name)
print(list_hrs_week)
print(list_OT_hours)
print(list_regular_hours)

i = 0
while i < len(list_employee_name):
    print(list_employee_name[i] + " worked " + str(list_regular_hours[i]) + " regular rate hours " + "and " + \
        str(list_OT_hours[i]) + " overtime hours for a total of " + str(list_hrs_week[i]) + " hours.")
    i = i + 1

#print(str_employee_name + " worked " + str(int_regular_hours) + " regular rate hours " + "and " + \
#str(int_OT_hours) + " overtime hours for a total of " + str(int_hrs_week) + " hours.")