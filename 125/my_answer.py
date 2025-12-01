prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finsihed.) "

answer = True

while answer:
    city = input(prompt)
    if city != 'quit':
        print(f"I'd love to go to {city.title()}")
    else:
        break

