# assognments

azeez = "technical"
tacha = "admin"
trust = "manager"

# '=' if for assignment, '==' is comparison

# if azeez == "technical":
#     print("Yes Oh!!")
# else:
#     print("Never!!")

timi = {
    "name": "Timilaye",
    "username": "timothy",
    "password": "2019"
}

user = input("Insert username:")

if timi["username"] == user:
    pword = input("Insert Password:")

    if timi["password"] == pword:
        print("Thank you, Access Granted")
    else:
        print("Wrong Password, Try again!!")

else:
    print("wrong username, try again")