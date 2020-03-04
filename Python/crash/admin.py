#Exercise

users = ['vijay', 'admin', 'jidhu', 'sam', 'vicky']

for user in users:
    if 'admin' in user:
        print("Hello, " + user.title() + " Would you like to see the status")
    else:
        print("hello " + user.title() + " Welcome, you logged in")


test_user = []

if test_user:
    for test in test_user:
        print("Hello, there" + test)
else:
    print("\n\nWe need to find more user")


current_users = ['vijay', 'jidhu', 'vignesh', 'ganesh', 'thanos']
new_users = ['aashi', 'anand', 'Vignesh', 'balaji', 'thouseef']


if new_users:
    for new in new_users:
        new = new.lower()
        if new in current_users:
            print(new.title() + ' You need to enter new username')
        else:
            print(new.title() + ' You are entered')
