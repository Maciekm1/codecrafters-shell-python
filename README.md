# My own Shell program

[![Python](https://img.shields.io/badge/python-3.14-blue?logo=python)](https://www.python.org/downloads/release/python-3140/)
[![uv](https://img.shields.io/badge/package%20manager-uv-blueviolet?logo=python)](https://docs.astral.sh/uv/)

My own implementation of a lightweight POSIX-style shell in Python, written to better understand how a shell works under the hood.

This project is part of the [CodeCrafters "Build Your Own Shell" challenge](https://app.codecrafters.io/courses/shell/overview), where you incrementally build a shell capable of parsing commands, running external programs, and supporting builtin commands like `cd`, `pwd`, and `echo`.


## Features

- Interactive REPL (Read-Evaluate-Parse Loop) with a `$` prompt
- Builtin commands: `echo`, `exit`, `type`, `cd` and `pwd`
- External command execution via `PATH` lookup
- Command-not-found error handling
- Navigation; `cd` and `pwd` builtins


## Roadmap

This shell is being built stage-by-stage. Upcoming work includes:

- Quoting; preserve whitespace and special characters
- Redirection; Standard output and error redirection (`>`, `>>`, etc.)
- Command Completion; autocomplete commands and executable files
- Filename Completion
- Programmable Completion; `complete` builtin, custom tab-completion behaviour
- Background Jobs; multiple commands in the background at once
- Pipelines (`|`)
- History; `history` builtin
- History Persistence; save history to a file
- Parameter Expansion; shell variables


## Lessons Learned so far

- How a REPL reads input, parses commands, and dispatches to builtins vs external programs
- How shells resolve executables using the `PATH` environment variable
- The difference between shell builtins and programs found on disk


## Installation

This project uses [uv](https://docs.astral.sh/uv/) as its package manager. Install uv if you don't have it yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Clone the repository:

```bash
git clone https://github.com/Maciekm1/codecrafters-shell-python
cd codecrafters-shell-python
```

Install dependencies (uv reads `pyproject.toml` and manages the Python version via `.python-version`):

```bash
uv sync
```


## Run Locally

Start the shell:

```bash
./your_program.sh
```

You should see a `$` prompt. Try a few commands:

```text
$ echo hello world
hello world
$ type echo
echo is a shell builtin
$ ls -l
<file listing>
$ exit
```

The entry point for the shell implementation is `app/main.py`. Locally, `your_program.sh` runs it via `uv run`.


## Usage / Examples

```python
# app/main.py — simplified flow
while True:
    user_input = read_line("$ ")
    handle_command(user_input)  # dispatches to builtins or subprocess
```

Example shell session:

```bash
$ echo hello
hello
$ type ls
ls is /usr/bin/ls
$ unknown_command
unknown_command: command not found
$ exit
```


## Submit to CodeCrafters

[![progress-banner](https://backend.codecrafters.io/progress/shell/9dfcf5e0-00ab-4958-b292-7cc85a999694)](https://app.codecrafters.io/users/Maciekm1?r=2qF)

To run tests on CodeCrafters servers:

```bash
codecrafters submit
```


## Related

- [CodeCrafters](https://app.codecrafters.io/)
- [uv documentation](https://docs.astral.sh/uv/)
