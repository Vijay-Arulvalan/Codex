import json

def get_stored_info():
    """Get stored information if available"""
    filename = 'info.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_username():
    """prompt for a new username"""
    username = input ("What's your name: ")
    filename = 'user.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_info()
    if username:
        print('Welcome back ' + username + '.')
    else:
        username = get_username()
        print('We will remember you when you come back ' + username + '.')

greet_user()
