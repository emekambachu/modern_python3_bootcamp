# for x in range(1, 10):
#     print(x)
#     print(x*x)

# for x in "developer":
#     print(x)

# list = ['eraser', 'pen', 'notebook']
#
# for x in list:
#     if x == 'eraser':
#         print(x + " is inside this list")


dict = {
    'chukwuma': 400000,
    'pius': 700000,
    'cathrine': 1000000
}


def pension(x):
    p = (15/100) * x
    return p

for key, value in dict.items():
    print(f"{key}'s pension amount is {pension(value)}")

