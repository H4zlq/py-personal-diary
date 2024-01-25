from modules.date_module import get_datetime
from modules.file_module import read_file, append_file


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


def diary():
    username = entry_username()

    while True:
        choice = diary_menu()
        datetime = get_datetime()

        if choice == 1:
            entry = entry_diary()
            content = f"{datetime}: {entry}\n"

            if append_file(f"{username}-diary.txt", content):
                print("Successfully added diary.")
        elif choice == 2:
            entry = read_file(f"{username}-diary.txt")

            if entry:
                print(entry)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using our personal diary.")


def main():
    diary()


if __name__ in "__main__":
    main()
