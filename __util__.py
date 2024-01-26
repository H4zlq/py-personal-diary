def entry_username():
    print("-" * 30)
    print("Welcome to our personal diary.")
    username = input("Enter your username: ")
    return username


def entry_diary():
    entry = input("Enter your diary: ")
    return entry


def diary_menu():
    print("-" * 30)
    print("[1] Add diary")
    print("[2] View diary")
    print("[3] Exit")

    try:
        choice = input("Enter your choice: ")
        return int(choice)
    except ValueError:
        return 0
