# # - 1. - # 
# # Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ]

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# z = [ {'x': 10, 'y': 20} ]

# # 1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3],[15,8,9] ]
# x[1][0] = 15
# print(x)

# # 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name'] = "Bryant"
# print(students)

# # 1.3 In the sport_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][1] = 'Andres'
# print(sports_directory)

# # 1.4 Change the value 20 in z to 30
# z[0]['y'] = 30
# print(z)

# - 2. - #
# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value

# ***note: students list is used for questions 2 and 3. Be careful not to comment out this code when testing only question 3
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     for element in students:
#         output_str = ""
#         comma = True

#         for key,val in element.items():
#             output_str += key + " - " + val

#             if comma:
#                 output_str += ", "
#                 comma = False
#             else:
#                 comma = True

#         print(output_str)

# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# Example Output:
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# - 3. - #
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

# def iterateDictionary2(key_name, some_list):
#     for i in some_list:
#         print(i[key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# - 4 - #
# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that, given a dictionary whose values are lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# def printInfo(dojo):
#     for key in dojo.keys():
#         print(len(dojo[key]), key.capitalize())
#         for i in dojo[key]:
#             print(i)

#         print("")

# printInfo(dojo)

class Dojo:
    def __init__(self, location, instructors):
        self.location = location
        self.instructors = instructors

    def change_loc(self, new_loc):
        self.location = new_loc

test_dojo = Dojo("Seattle", ["Mike", "Nichole", "Ryan"])

print(test_dojo.location)
test_dojo.change_loc("San Diego")
print(test_dojo.location)

# Example Output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

