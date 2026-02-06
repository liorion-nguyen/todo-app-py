import json
def read_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)
    
def write_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

users = read_file('users.json')
users.append({
    "username": "user",
    "password": "123456",
    "email": "user@example.com",
    "full_name": "User User",
    "active": "true",
    "created_at": "2026-01-18 10:00:00",
    "updated_at": "2026-01-18 10:00:00"
})
write_file('users.json', users)
print(users)