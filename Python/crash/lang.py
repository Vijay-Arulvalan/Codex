#dict assigning methods

favourite_languages =   {
        'jen': 'C',
        'david': 'Dart',
        'vijay': 'Python',
        'than': 'java',
                        }
print("Vijay favourite language is " +
    favourite_languages['vijay'].title() +
    '.')
print("\n *********")
#looping with dictionary

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')

#for only keys we need to take out then use the keys()-->keys, value()--> values.
#and if condition
print('\n********')
friends = ['david', 'jen']
for name in favourite_languages.keys():
    if name in friends:
        print(name.title() + ", Nice to hear from you, and i know your favourite language is "
        +favourite_languages[name].title() + "!")
    else:
        print(name.title()+ ", please take our poll")
