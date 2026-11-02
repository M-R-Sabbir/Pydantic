# we have to store some data of user into our database let's it is a list for now

users = []

def user_data_insertion(name:str,age:int):
    users.append((name,age))
    print(users)
    print("Insertated Successfully")

# user_data_insertion("Sabbir","24")

# so here we face an issue is programmer can't protect user from putting wrong type
# what can we do now? we can apply logic so that user must have to provide right type

def user_insertion(name:str,age:int):
    if type(name)==str and type(age)==int:
        users.append((name,age))
        print(users)
        print("Inserted Successfully")
    else:
        raise TypeError("Put data based on the recommendation")
user_insertion("Sabbir",24)

# ok now it is solved? what if we have 100 functions who use this data ,so each and everytime we check this and use?
# it is not feasible enough, we Need to solve it any other way which will work universally
