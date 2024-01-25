def append_file(file_name, content):
    try:
        with open(file_name, "a") as f:
            f.write(content)
        return True
    except FileNotFoundError as e:
        print(f"No such file or directory: {e.filename}")
        return False


def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            return f.read().strip()
    except FileNotFoundError as e:
        print(f"No such file or directory: {e.filename}")
        return False
