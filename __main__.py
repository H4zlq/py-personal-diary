from __util__ import diary_menu, entry_diary, entry_username
from modules.date_module import get_datetime
from modules.file_module import read_file, append_file


def main():
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


if __name__ in "__main__":
    main()
