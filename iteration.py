# Iteration (For Loop)

# employees = ['Toyeeb', 'Kate', 'Prevail', 'Tims']
#
# salaries = [300000, 500000, 100000, 50000, 200000]

# for x in "toyeeb":
#     print(x)

# for x in salaries:
#     if x > 100000 and x < 500000:
#         print (x)

employee_salary = {
    "Toyeeb": 400000,
    "Timi": 50000,
    "Azeez": 400000,
    "Kate": 1000000,
    "Prevail": 800000,
}

def pension(s):
   x = 15/100 * int(s)
   return x

for x, y in employee_salary.items():
        print(f"{x} earns ${y}, so their pension is {pension(y)}")