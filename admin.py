user_names = ['admin', 'dmitrii', 'daria', 'tolik', 'max']

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f"Hello {user_name}, would you like to see a status reposrt?")
        else:
            print(f"Hello {user_name.title()}, thank you for logging in again.")
else:
    print("We need to ind some users!")
