#List Exercise, Week 5 homework NMETH 528
#Step 1, create a list with at least 6 items:
sports = ['football', 'basketball', 'soccer', 'hockey', 'ultimate frisbee']
sports.append('gymnastics')
sports.append('swimming')
#Step 2, print list:
print(sports)

#Step 3, print the first 2 list items with a statement:
print(f"The first two items on the list are: {sports[0:2]}")
#Step 4, print the middle 2 list items with a statement:
print(f"The middle two items on the list are: {sports[-4:-2]}")
#Step 5, print the first and last item on the list using indexes:
print(f"The first and last item on the list are: {sports[0]}, {sports[1]}")

#Tuple exercise:
#Step 1, store the 5 basic foods at a restaurant and store in a tuple
food_items = ('chicken', 'steak', 'spaghetti', 'pizza', 'salad')
#Step 2, print each item on the menu using a for loop
print("The original menu at this boring restaurant includes:")
for food_item in food_items:
    print(food_item)

#Step 3, the restaurant has updated its menu. Copy the tuple replacing 2 items:
food_items = ('chicken', 'steak', 'eggs', 'waffles', 'salad')
#Step 4, reprint the new menu
print("The revised menu at this still-boring restaurant includes:")
for food_item in food_items:
    print(food_item)