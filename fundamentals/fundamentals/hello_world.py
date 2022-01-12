# Answers for Hello World Practice Assignment
# note: "!" was added to the end of the print strings in 2. and 3., though I do not think it was entirely necessary to do so. Intention was consistency with specified instructions

# 1. print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Lucky"
print("Hello", name + "!")	# with a comma
print("Hello " + name + "!")	# with a +

# 3. print "Hello 42!" with the number in a variable
fav_num = 1.618
print("Hello", str(fav_num) + "!")	# with a comma
print("Hello " + str(fav_num) + "!")	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string
