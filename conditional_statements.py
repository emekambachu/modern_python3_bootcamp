# conditional Statements

# name = "Chukwuma"
#
# if name == "Chukwuma":
#     print("my name is " + name)
# elif name == "emeka":
#     print("are you sure ?")
# else:
#     print("Nothing to do here")

# answer = input("what is your favorite color ?")
# if answer.lower() == "purple":
#     print('How adorable')
# elif answer == "red":
#     print('how scary!!')
# elif answer == "green":
#     print('ah, my man')
# else:
#     print('good one man')


# comparisons

# a = 40
# b = 12
# c = 3
#
# employee = {
#     'name':'Chukwuma',
#     'age': 30,
#     'occupation': 'Networking boy',
# }
#
# if employee['age'] == 30 and employee['occupation'] == 'Networking':
#     print('you don old oh')
# else:
#     print('Nothing for you!!')

age = input("How old are you?")

if age != "":
    if int(age) >= 18 and int(age) < 21:
        print("You are old enough to get drunk!!")
    elif int(age) < 18:
        print("Please go home")
else:
    print("Please insert something")