# A List in a Dictionary

# Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a dictionary.

# Store information about a pizza being ordered.

pizza = { #1
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:") #2

for topping in pizza['toppings']: #3
    print("\t" + topping)

#My Solution:

# for topping in pizza['toppings']:
#     print(f"\t{topping}")


#1 - we begin with a dictionary that holds information about a pizza that has been ordered. 

# One keyin the dictionary is 'crust', and the associated value is the string 'thick'. 

# The next key, 'toppings', has a list as its value that stores all requested toppings. 

#2 - we summarize the order before building the pizza. 

# When you need to break up a long line in a print() call, choose an appropriate point at which to break the line being printed, and end the line with a quotation mark, and continue the string. 

# Python will automatically combine all of the strings.

# it finds inside the parentheses. To print the toppings, we write a for loop at #3. 

# To access the list of toppings, we use the key 'toppings', and Python grabs the list of toppings from the dictionary.