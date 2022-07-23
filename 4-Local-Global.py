# Learning point: Declare global and local variables
# Explore the scope of the variables
# Explore UPDATING a global variable within a function
# Use a return value within a function

globalvar = 10

def local_function():
    localvar = globalvar
    print(localvar)
    localvar = localvar + 100
    print(localvar)
    return localvar


print(globalvar)
                              
globalvar =  local_function()
print(globalvar)