users = {
        'aienstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'USA',
                    },
        'steobs': {
            'first': 'steve',
            'last': 'jobs',
            'location': 'san-jose',
                },
        }
for username, user_info in users.items():
    print("Username: " + username)
    full_name = user_info['first'] +' ' + user_info['last']
    location = user_info['location']

    print('\t Full name: ' + full_name.title())
    print('\t Location: ' + location.title() )
