unconfirmed = ['chris', 'bob', 'david', 'sam']
confirmed = []

while unconfirmed:
    current_user = unconfirmed.pop()
    print("Verifying users: " + current_user.title())
    confirmed.append(current_user)

print('The following users have been confirmed: ')
for confirm in confirmed:
    print(confirm.title())
