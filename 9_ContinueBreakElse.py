
# ========================
# 9_ContinueBreakElse.py:
# ========================

# Using "continue" and "break" in for loop and if/else


# Continue: This is used to bypass the code block

shopping_list = ["milk", "pasta", "spam", "eggs", "bread", "rice"] # List containing shopping list
for item in shopping_list:
    print("Buy "+item) #Concatenating Buy with item in shopping list

# Now if we don't want to buy spam, we can use Continue to bypass it.
print()
print("Ignore spam")
shopping_list = ["milk", "pasta", "spam", "eggs", "bread", "rice"] # List containing shopping list
for item in shopping_list:
    if item == "spam": # test to see if item == spam
        continue  # continue breaks line and goes back to next item in list
    print("Buy "+item)

# In below code, line "I am ignoring spam is printed after the
# test shows item is spam, but next print line after the Continue
# is ignored

print()
shopping_list = ["milk", "pasta", "spam", "eggs", "bread", "rice"] # List containing shopping list
for item in shopping_list:
    if item == "spam": # test to see if item == spam
        print("I am ignoring spam")
        continue  # continue breaks line and goes back to next item in list
    print("Buy "+item)



# Break - This one is used to completely exit out of the for loop
# Hence we will not see any results for items after spam.
# Will not see eggs, bread and rice

print("=================================")
shopping_list = ["milk", "pasta", "spam", "eggs", "bread", "rice"] # List containing shopping list
for item in shopping_list:
    if item == "spam": # test to see if item == spam
        print("If I encounter spam, I break from for loop")
        break  # to completely exit out of the for loop
    print("Buy "+item)

# Another example of using break
# Note that if there is no spam in the list, then nasty_food_item
# will not be initialized and will cause error sauing its not defined

print("==================================")
meal = ["eggs", "bacon", "spam", "sausages"] # list with food items
for item in meal: # loops thru items in meal
    if item == 'spam': # it checks for spam
        nasty_food_item = item # if spam found, it is assigned to nasty_food_item
        print("we found spam and will break from for loop")
        break # Then we break from the for loop
    print(item) # This prints the first two items that are not spam

if nasty_food_item: # If nasty_food_item is found, we print this
    print("Can't we have something without spam?")

# One way to resolve above issue is to initialize nasty_food_items
# With a null
# Now even if there is no spam, there is no error
# And print on line 75 is not printed because there is nothing in
# nasty_food_item

print("==================================")
meal = ["eggs", "bacon", "meat", "sausages"] # list with food items
nasty_food_item = ''
for item in meal: # loops thru items in meal
    if item == 'spam': # it checks for spam
        nasty_food_item = item # if spam found, it is assigned to nasty_food_item
        print("we found spam and will break from for loop")
        break # Then we break from the for loop
    print(item) # This prints the first two items that are not spam

if nasty_food_item: # If nasty_food_item is found, we print this
    print("Can't we have something without spam?")

# Else - causes the block to be executed if the for loop is not broken
# In below code, if there is spam, else is not run
# if there is no spam in meal, the else print is printed

print("==================================")
meal = ["eggs", "bacon", "meat", "sausages"] # list with food items
nasty_food_item = ''
for item in meal: # loops thru items in meal
    if item == 'spam': # it checks for spam
        nasty_food_item = item # if spam found, it is assigned to nasty_food_item
        print("we found spam and will break from for loop")
        break # Then we break from the for loop
    print(item) # This prints the first two items that are not spam
else:
    print("I will have a plate of that")

if nasty_food_item: # If nasty_food_item is found, we print this
    print("Can't we have something without spam?")
