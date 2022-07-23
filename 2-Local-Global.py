# Learning point: Declare global and local variables
# Explore the scope of the variables
# Explore UPDATING a global variable within a function

globalvar = 10

def local_function():
    localvar = 20
    print(localvar)
    # globalvar = globalvar + 100
    print(globalvar)

print(globalvar)
# print(localvar)
                              
local_function()