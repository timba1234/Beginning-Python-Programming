# Logical "or" Operator:

intA = 20
intB = 30
intC = 40

if intA < intB or intA < intC:
    print("intA is less than intB or intA is less than intC")

if intA > intB or intA < intC:
    print("intA is greater than intB or intA is less than intC")
else:
     print("intA is greater than intB or intA is less than intC: False")
