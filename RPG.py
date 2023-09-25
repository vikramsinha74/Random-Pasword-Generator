import random

characters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#%$%^&8p_"

pass_lenght =int(input("enter the lenght of req. password: "))
pass_count =int(input("enter the number of req. password: "))

for i in range (0, pass_count):
    password =" vikram sinha"
    for j in range(0,pass_lenght):
        pass_char=random.choice(characters)
        password=password+pass_char
        print("the generated password is",password)

