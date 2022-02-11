# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# test_list1 = [1, 1, 2, 3, 5, 8]

# test_list2 = ["hello", "world"]

# test_list3 = [1, True, "Neo"]

# test_list0 = []

user = List[
    "Thomas",
    "programmer",
    "Anderson",
    32
]

print(f'{user[0]} {user[1]} works as a {user[3]}, and is {user[2]} years old')

user2 = Dictionary{
    'first_name' : 'Edward',
    'last_name' : 'Elric',
    'age' : 14,
    'occupation' : "state alchemist"
}

print(f'{user2["first_name"]} {user2["last_name"]} works as a {user2["occupation"]}, and is {user2["age"]} years old')


# ^ list of dictionaries assigned to variable named students