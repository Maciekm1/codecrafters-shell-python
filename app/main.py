import sys
import os
import subprocess

from app.extensions.navigation import handle_path

BUILT_INS = {"echo", "exit", "type", "pwd", "cd"}


def main():
    while 1:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_input = sys.stdin.readline().rstrip()
        handle_command(user_input)


def handle_command(cmd: str):
    match cmd.split()[0]:

        case "echo":
            print(cmd[5:]) # Print the command without the "echo " (5 chr)

        case "type":
            arg = cmd[len("type")+1:]

            if arg in BUILT_INS:
                print(f"{arg} is a shell builtin")
            else:
                arg_in_path(arg, True)

        case "pwd":
            print(os.getcwd())

        case "cd":
            arg = cmd[len("cd")+1:]
            handle_path(arg)

        case "exit":
            sys.exit(0)

        case _:
            args = cmd.split(" ")
            if arg_in_path(args[0], False):
                subprocess.run(args) # Execute in a subprocess with args
            else:
                sys.stdout.write(f"{cmd}: command not found\n")


# Returns True if '{pwd}/arg' exists within PATH and has execute permissions i.e. not a built-in shell function
def arg_in_path(arg: str, verbose: bool) -> bool:
    PATH = os.getenv('PATH')
    found = False

    for dir in PATH.split(':'):
        fp = os.path.join(dir, arg)
        if os.path.exists(fp) and os.access(fp, os.X_OK):
            if verbose:
                print(f"{arg} is {fp}")
            found = True
            return True
    
    if not found:
        if verbose:
            print(f"{arg}: not found")
        return False


if __name__ == "__main__":
    main()
