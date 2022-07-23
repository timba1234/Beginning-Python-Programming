# Learning point: Declare global and local variables
# Explore the scope of the variables
# Explore UPDATING a global variable within a function
# Using the "global" keyword

globalvar = 10

def local_function():
    global globalvar
    print(globalvar)
    globalvar = globalvar + 100
    print(globalvar)


print(globalvar)
                              
local_function()
print(globalvar)