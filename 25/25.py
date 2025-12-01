# How might this pop() method be useful? Imagine that the motorcycles in the list are
# stored in chronological order according to when we owned them. If this is the case, we can use the
# pop() method to print a statement about the last motorcylce we bought:

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}')