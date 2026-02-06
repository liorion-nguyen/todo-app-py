from common import clear_screen, print_header, print_success, print_error, pause
from datetime import datetime

users = []
def display_menu_auth(list_users):
    global users
    users = list_users
    clear_screen()
    print_header("TODO APP - AUTH")

    print("1️⃣  Login")
    print("2️⃣  Register")
    print("0️⃣  Exit")
    print("-" * 50)

    choice = input("👉 Chọn chức năng: ")

    if choice == "1":
        return login()
    elif choice == "2":
        return register()
    elif choice == "0":
        print("👋 Tạm biệt!")
        exit()
    else:
        print_error("Lựa chọn không hợp lệ")
        pause()
        return False

def login():
    clear_screen()
    print_header("LOGIN")

    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            global account
            account = user
            print_success("Đăng nhập thành công")
            pause()
            return True

    print_error("Sai username hoặc password")
    pause()
    return False

def register():
    clear_screen()
    print_header("REGISTER")

    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    full_name = input("Full name: ")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    users.append({
        "username": username,
        "password": password,
        "email": email,
        "full_name": full_name,
        "active": True,
        "created_at": now,
        "updated_at": now,
    })

    print_success("Đăng ký thành công")
    pause()
    return False