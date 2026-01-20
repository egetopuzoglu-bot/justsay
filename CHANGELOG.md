Changelog

All notable changes to this project are documented in this file.

v0.2-Beta;

Added:
-newline command to explicitly create empty lines in output
-repeat command to repeat a single command multiple times
-Strict single-line command execution
-Unified error output format


Changed:
-Removed hint system completely
-Enforced “one command per line” rule
-Empty lines in .Jsay files now produce an error


Fixed:
-Inconsistent error handling
-Ambiguous output caused by editor line breaks