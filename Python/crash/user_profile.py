def build_profile(first, last, **user_info): #python will create an empty dictionay called user_info
#user_info has two key and value called location and field ... this is looped in 7th line.
    """Build a dictionary containing everything we know about user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
