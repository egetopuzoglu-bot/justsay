import sys

VALID_COMMANDS = ["write", "count", "newline", "repeat"]

def error(message):
    print(f'Error: {message}')
    sys.exit(1)

def process_line(line):
    line = line.strip()

    if line == "":
        error("Empty line")

    words = line.split()
    command = words[0]
    args = words[1:]

    # write
    if command == "write":
        if not args:
            error("Nothing to write")
        print(" ".join(args))
        return

    # count
    if command == "count":
        if not args:
            error("Nothing to count")
        print(len(args))
        return

    # newline
    if command == "newline":
        if args:
            error("newline takes no arguments")
        print()
        return

    # repeat
    if command == "repeat":
        if len(args) < 2:
            error("repeat requires a number and a command")

        count_str = args[0]

        if not count_str.isdigit():
            error("repeat count must be a positive integer")

        count = int(count_str)

        if count <= 0:
            error("repeat count must be positive")

        inner_command = args[1]
        inner_args = args[2:]

        if inner_command == "repeat":
            error("nested repeat is not allowed")

        if inner_command not in ["write", "newline"]:
            error("repeat supports only write or newline")

        for _ in range(count):
            if inner_command == "write":
                if not inner_args:
                    error("Nothing to write")
                print(" ".join(inner_args))
            elif inner_command == "newline":
                print()
        return

    # bilinmeyen komut
    error(f'Unknown command "{command}"')

def run_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        error("File not found")

    for line in lines:
        process_line(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        error("No file provided")

    run_file(sys.argv[1])
