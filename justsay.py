import sys
import os
import random

MAX_WORDS = 10
COMMANDS = [
    "write",
    "say",
    "upper",
    "lower",
    "repeat",
    "count",
    "random"
]


def error(message):
    print(f"Error: {message}.")
    sys.exit(1)


def read_file(path):
    if not os.path.exists(path):
        error("file not found")

    with open(path, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        error("empty command")

    return content


def parse(content):
    lines = content.splitlines()

    if len(lines) > 1:
        first_line = lines[0].strip().lower()
        if not first_line.startswith("repeat"):
            error("unexpected line break")

    words = content.lower().split()

    if len(words) > MAX_WORDS:
        error("command must be 10 words or less")

    return words, lines


def run_command(words, lines):
    command = words[0]

    if command not in COMMANDS:
        error(f'unknown command "{command}"')

    if command in ["write", "say"]:
        if len(words) < 2:
            error("nothing to write")
        print(" ".join(words[1:]))

    elif command == "upper":
        print(" ".join(words[1:]).upper())

    elif command == "lower":
        print(" ".join(words[1:]).lower())

    elif command == "repeat":
        if len(words) < 2 or not words[1].isdigit():
            error("repeat requires a number")

        times = int(words[1])

        if len(lines) == 1:
            text = " ".join(words[2:])
        else:
            text = lines[1].strip()

        for _ in range(times):
            print(text)

    elif command == "count":
        if len(words) < 2:
            error("nothing to count")
        text = " ".join(words[1:])
        print(len(text.split()))

    elif command == "random":
        if len(words) != 3:
            error("missing range")

        try:
            min_val = int(words[1])
            max_val = int(words[2])
        except ValueError:
            error("numbers required")

        if min_val >= max_val:
            error("invalid range")

        if max_val - min_val > 100:
            error("range too large")

        print(random.randint(min_val, max_val))


def main():
    if len(sys.argv) != 2:
        print("Usage: justsay <file.Jsay>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = read_file(file_path)
    words, lines = parse(content)
    run_command(words, lines)


if __name__ == "__main__":
    main()
