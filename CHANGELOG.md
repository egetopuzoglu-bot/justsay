# Changelog

All notable changes to this project are documented in this file.

---

## v0.1-Beta

Initial beta release of **JustSay**.

### Added
- Core JustSay interpreter written in Python
- Support for `.Jsay` file extension
- English-based command parsing
- `write` and `say` commands for text output
- `upper` command for uppercase text
- `lower` command for lowercase text
- `count` command to count words
- `random` command to generate random numbers
- `repeat` command to repeat the next line
- Command-line execution support

### Rules
- Maximum 10 words per command
- Commands must be written in English
- Users cannot define new commands
- Meaningless line breaks produce errors
- Unknown commands produce clear error messages
- Output is cleared on each run

### Known Limitations
- No variables or data storage
- No user-defined commands
- No GUI or web interface
- Interpreter-only (CLI-based)

---

## Planned (v0.2)

- Improved error language system
- Hint system for beginners
- Better multiline handling
- Extended command set
- More example files
