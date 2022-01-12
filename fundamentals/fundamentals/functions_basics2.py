# ========================================================================= #
# Answers for Functions Basics II Assignment
# *note: all functions have been commented out to prevent errors while 
# individual function; if you want to run an individual function, highlight
# the whole text block you want to run, and press CTRL + / to uncomment it
# all at once
# ========================================================================= #

# # 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from that number (as the 0th element) down to 0 (as the last element)
# def countdown(start_val):
#     new_list = []
#     # negatively iterating for loop; end value passed to range is -1 to be inclusive of 0
#     for i in range(start_val, -1, -1):
#         new_list.append(i)
    
#     return new_list

# print(countdown(5))

# # 2. Print and Return - Create a function that will receive a list with two number. Print the first value and return the second
# def print_and_return(num_list):
#     print(num_list[0])
#     return num_list[1]

# print(f"returned value: {print_and_return([5,8])}")

# # 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length
# def first_plus_length(num_list):
#     return num_list[0] + len(num_list)

# print(first_plus_length([1,2,3,4,5]))

# # 4. Values Greater Than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than it's 2nd value. Print how many values this is and then return the new list. If the list has less that 2 elements, have the function return False
# def gt_second(num_list):
#     # ...if list has less than 2 elements, return False
#     if len(num_list) < 2:
#         return False

#     new_list = []
    
#     # ...creates a new list containing only the values from the original list that are greater than the 2nd value
#     for i in range(len(num_list)):
#         if num_list[i] > num_list[1]:
#             new_list.append(num_list[i])

#     # ...print how many values this is
#     print(f"There are {len(new_list)} greater than {num_list[1]}")

#     # ...return the new list
#     return new_list

# print(gt_second([5,2,3,2,1,4]))
# print(gt_second([3]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value
def this_len_that_val(size, val):
    val_list = []
    for i in range(size):
        val_list.append(val)

    return val_list

print(this_len_that_val(4,7))
print(this_len_that_val(6,2))