people = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 25,
    },
    'user_2': {
        'first_name': 'Johnd',
        'last_name': 'Doeee',
        'age': 27,
    }
}
# print(people['user_1']['first_name'])

for key, value in people.items():
    print(key, value)

