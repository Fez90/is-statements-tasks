car='subaru'
print("Is car =='subaru'? I predict True")
print(car=='subaru')

pizzas_top=['pepperoni','parmesan','sausage']
if pizzas_top !='tomato':
    print("\nDont serve pizza")

cities='Miami'
if cities.lower() == 'miami':
    print("\nTrue")
else:
    print("False")

age_1 = 24
age_2 = 26
age_3 = 26
if age_1>21 and age_2>21 and age_3>21:
    print("\nYou can buy drink")
else:
   print("\nYou not allowed to drink")

invited_friends=['jack','andrew','sara','taylor','emily']
guest = 'john'
if guest in invited_friends:
    print("\nWelcome to the party")
else:
    print("\nYou were not invited")  

guest_1 = 'hailey'
if guest_1 not in invited_friends: 
    print("\nPlease, join our party")
  
allien_color = 'green'
if allien_color == 'green':
    print("\nPlayer earned 5 points")

if allien_color == 'red':
    print("\nPlayer earned 5 points")
else:
    print("\nPlayer earned 10 points")

allien_color = 'red'
if allien_color == 'green':
    print("\nPlayer earned 5 points")
elif allien_color == 'yellow':
    print("\nPlayer earned 10 points")
elif allien_color == 'red':
    print("\nPlayer earned 15 points")
else:
    print("\nPlayer earned 0 points")

age = 76
if age<2:
    print("\nbaby")
elif age>2 and age<4:
    print("\ntoddler")
elif age>4 and age<13:
    print("\nkid")
elif age>13 and age<20:
    print("\nteenager")
elif age>20 and age<65:
    print("\nadult")
else:
    print("\nelder")

user_names = ['Sara','Jack','Tom','Jessica','Admin']
for user_name in user_names:
    if user_name == 'Admin':
        print("\nHello Admin, would you like to see status report?")
    else:
        print(f"Hello {user_name}, you logged in")

current_users = ['jane','james','celine','taylor','mary']
new_users = ['jane','smith','abigail','mary']
for new_user in new_users:
    if new_user in current_users:
        print("\nYou need to change your user name")
    elif new_user == 'smith':
        print("Username should not be accepted")
    else:
        print(f"{user_name.upper()} is available")

ordinal_numbers = [1,2,3,4,5,6,7,8,9]
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    else:
        print(f"{ordinal_number}th")