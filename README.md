# JustSay v0.1-Beta

JustSay is a beginner-friendly programming language that allows users to write
simple English sentences and get direct results.

No syntax rules.
No symbols.
Just say it.

This project is currently in **beta**.

---

## What is JustSay?

JustSay is a general-purpose, English-based language designed for beginners.
Users do not write code logic — they write **sentences**, and the interpreter
handles the rest.

Example:

write hello world

Output:
hello world

---

## Key Features

- English-based commands
- No variables, functions, or complex syntax
- Beginner-friendly by design
- Clear and strict error messages
- Command-line interpreter
- Maximum 10 words per command

---

## File Extension

JustSay source files use the `.Jsay` extension.

Example:
example.Jsay

---

## Commands

### write / say
Prints text to the screen.

write hello world

---

### upper
Converts text to uppercase.

upper hello

Output:
HELLO

---

### lower
Converts text to lowercase.

lower HELLO

Output:
hello

---

### count
Counts the number of words.

count hello world

Output:
2

---

### random
Generates a random number between two values.

random 1 10

---

### repeat
Repeats the next line a given number of times.

repeat 3
hello

---

## Rules

- Maximum 10 words per command
- Commands must be written in English
- Unknown commands cause an error
- Meaningless line breaks cause an error
- Old output is cleared on each run
- Users cannot define new commands (v0.1)

---

## Usage

Run a `.Jsay` file using Python:

py justsay.py example.Jsay

---

## Version

v0.1-Beta

---

## License

MIT License

You are free to use, modify, and distribute this project.
