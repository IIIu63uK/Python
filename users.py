current_users = ['Dmitrii', 'admin', 'daria', 'tolik', 'max']
current_users = ['dmitrii', 'admin', 'daria', 'tolik', 'max']

new_users = ['sergey', 'dmitrii', 'Max', 'vlad', 'daria']

for user in new_users:
    if user in current_users:
        print(f"{user} is not available, need choose other name.")
    else:
        print(f"Name {user} is available.")
