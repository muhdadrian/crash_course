# Checking That a List Is Not Empty

requested_toppings = [] # 1

if requested_toppings: # 2
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else: # 3
    print("Are you sure you want a plain pizza?")

# 1 - we start with empty list
# 2 - Instead of jumping right into a for loop, we do a quick check at 2. Python returns True if the
# list contains at least one item; an empty list evaluates to False. If requested_toppings passes the
# conditional test, we run the same for loop we used in the previous example. If the conditional test
# fails, we print a message asking the customer of if they really want a plain pizza with no toppings
# at 3.
# @ The list is empty in this case, so the output asks if the user really wants a plain pizza:
# Are you sure you want a plain pizza?
# @ You can try to fill in the list.
