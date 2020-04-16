prompt = ("\n Tell me the city you visited")
prompt += ("\n Enter 'quit' after you complete: ")

while True:
    city = input(prompt)

    if city == 'quit':
        break

    else:
        print("\n I'd love to goto the " + city.title() + " one day!")
