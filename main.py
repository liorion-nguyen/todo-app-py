from auth import display_menu_auth
from todo import display_menu_main

users = [
    {
        "username": "admin",
        "password": "123456",
        "email": "admin@example.com",
        "full_name": "Admin User",
        "active": True,
        "created_at": "2026-01-18 10:00:00",
        "updated_at": "2026-01-18 10:00:00",
    },
    {
        "username": "user",
        "password": "123456",
        "email": "user@example.com",
        "full_name": "User User",
        "active": True,
        "created_at": "2026-01-18 10:00:00",
        "updated_at": "2026-01-18 10:00:00",
    },
]

tasks = [
    {
        "id": 1, # len(tasks) + 1
        "title": "Todo 1", # String
        "description": "Description 1", # String
        "status": "todo", # default: todo, in progress, completed
        "priority": "low", # String
        "created_at": "2026-01-18 10:00:00",
        "updated_at": "2026-01-18 10:00:00",
    }
]

# Authenticated
checkMenu = display_menu_auth(users)
while checkMenu == False:
    checkMenu = display_menu_auth(users)

# Main functionality
while True:
    display_menu_main(tasks)