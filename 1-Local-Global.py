# Learning point: Declare global and local variables
# Explore the scope of the variables

globalvar = 10

def local_function():
    localvar = 20
    print(localvar)
    print(globalvar)

print(globalvar)
# print(localvar)
                              
local_function()