def clear_screen():
    print("\n" * 50)

def pause():
    input("\n👉 Nhấn Enter để tiếp tục...")

def print_header(title):
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

def print_success(msg):
    print(f"[SUCCESS] {msg}")

def print_error(msg):
    print(f"[ERROR] {msg}")