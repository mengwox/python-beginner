# for Statements
print("for Statements==========================")
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Eleonore': 'inactive', '京太郎': 'active'}
# strategy1: iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

users = {'Hans': 'active', 'Eleonore': 'inactive', '京太郎': 'active'}
# strategy2: create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)
