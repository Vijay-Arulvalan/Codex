pizza = {
        'crust': 'thick',
        'toppings': ['cheese', 'onion', 'mushroom'],
        }

print("You ordered a " + pizza['crust'] +"-crust pizza with the following toppings,")

for topping in pizza['toppings']:
    print('\t' + topping)

print('\n ***')

favourite_languages =   {
        'jen': ['C', 'C++'],
        'david': ['Dart', 'kotlin'],
        'vijay': ['Python', 'C++'],
        'than': ['java', 'kotlin'],
                        }
for name, languages in favourite_languages.items():
    print(name.title() + "'s favourite languages are: ")
    for language in languages:
        print('\t' + language.title())
