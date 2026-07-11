import random
import sys
import string
print(sys.version)
# generating a six digit random
def user_id():
    id = ''
    for i in range(0,6):
        id = id + str(random.randint(0,9))
    return id

print(f"User id is {user_id()}")


def user_id_gen(no_char : int, no_ids:int):
    id = list()    
    for i in range(0,no_ids):
        id.append(''.join(random.choices(string.ascii_letters + string.digits, k = no_char)))

    return id

id = user_id_gen(int(input("Enter number of digits :")), int(input("Enter number of ids")))
print(f"Here are the ids : ")
for i in id:
    print(f"#{i}")


def rgb_gen():
    rgb = list()
    for i in range(0,3):
        rgb.append(random.randint(0,255))
    return rgb
print(f"Here is the rgb color schem : {rgb_gen()}")