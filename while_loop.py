# WHILE LOOP IS LIKE THE COMBINATION OF IF STATEMENT AND FOR LOOP

# msg = input("what is the secret password?:")
#
# while msg != "bananas":
#     print("wrong password!!")
#     msg = input("Try again:")
# print("Correct")


# for num in range(1, 11):
#     print(num)


# must declare a variable for while loop
# num = 1
# while num < 11:
#     print(num)
#     num += 1


# for num in range(1, 11):
#     print("\U0001f600" * num)
#
#
# times = 1
# while times < 11:
#     print("\U0001f600" * times)
#     times += 1


# without string multiplication
# for num in range(1, 11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "\U0001f600"
#         count += 1
#     print(smileys)


employee = {
    "username": "username",
    "password": "password"
}

username = input("Insert Username: ")
password = input("Insert password: ")

while employee["username"] != username or employee["password"] != password:
    print("username or password is incorrect")
    username = input("Insert Username: ")
    password = input("Insert password: ")
else:
    print("Access granted")