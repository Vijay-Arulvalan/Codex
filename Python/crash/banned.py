banned_users = ['andrew', 'carolina', 'david']

user = 'andrew'
if user not in banned_users:
    print(user.title() + ", you are permitted to this event!")
else:
    print(user.title() + ", you are not permitted, your account is restricted")
