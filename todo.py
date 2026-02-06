from common import clear_screen, print_header, print_success, print_error, pause
from datetime import datetime

tasks = []
def display_menu_main(list_tasks):
    global tasks
    tasks = list_tasks
    clear_screen()
    print_header(f"TODO APP - Welcome")

    print("1️⃣  Xem danh sách Todo")
    print("2️⃣  Thêm Todo mới")
    print("3️⃣  Cập nhật Todo")
    print("4️⃣  Xoá Todo")
    print("0️⃣  Thoát")
    print("-" * 50)

    choice = input("👉 Chọn chức năng: ")

    if choice == "1":
        return view_list_todos()
    elif choice == "2":
        return create_new_todo()
    elif choice == "3":
        return update_todo()
    elif choice == "4":
        return delete_todo()
    elif choice == "0":
        print("👋 Hẹn gặp lại!")
        exit()
    else:
        print_error("Lựa chọn không hợp lệ")
        pause()
        return False

def view_list_todos():
    clear_screen()
    print_header("DANH SÁCH TODO")

    if not tasks:
        print("📭 Không có todo nào")
        pause()
        return False

    print(f"{'ID':<4} {'TITLE':<15} {'STATUS':<12} {'PRIORITY':<10}")
    print("-" * 50)

    for t in tasks:
        print(f"{t['id']:<4} {t['title']:<15} {t['status']:<12} {t['priority']:<10}")

    pause()
    return False

def create_new_todo():
    clear_screen()
    print_header("TẠO TODO MỚI")

    title = input("Title: ")
    description = input("Description: ")
    priority = input("Priority (low/medium/high): ")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": "todo",
        "priority": priority,
        "created_at": now,
        "updated_at": now,
    })

    print_success("Tạo todo thành công")
    pause()
    return False

def delete_todo():
    global tasks
    clear_screen()
    print_header("DANH SÁCH TODO")

    if not tasks:
        print("📭 Không có todo nào")
        pause()
        return False

    print(f"{'ID':<4} {'TITLE':<15} {'STATUS':<12} {'PRIORITY':<10}")
    print("-" * 50)

    for t in tasks:
        print(f"{t['id']:<4} {t['title']:<15} {t['status']:<12} {t['priority']:<10}")
    print_header("XOÁ TODO")
    id = input("ID: ")
    for t in tasks:
        if t['id'] == int(id):
            tasks.remove(t)
            print_success("Xoá todo thành công")
            pause()
            return False
    print_error("Todo không tồn tại")
    pause()
    return False
    # delete todo
    # print success
    # pause
    # return False
