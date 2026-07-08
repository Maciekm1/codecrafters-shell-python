import sys
import os
import subprocess

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
            # Print the command without the "echo " (5 chr)
            print(cmd[5:])

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
                # Execute in a subprocess with args
                subprocess.run(args)
            else:
                sys.stdout.write(f"{cmd}: command not found\n")


def handle_path(path: str):
    match path[0]:
        case "/":
            # Absolute path
            if os.path.exists(path):
                os.chdir(path)
            else:
                print(f"cd: {path}: No such file or directory")
        case ".":
            # Relative path
            pass
        case "~":
            # Home directory
            pass
        case _:
            print("invalid")

def arg_in_path(arg: str, verbose: bool) -> bool:
    PATH = os.getenv('PATH')
    found = False

    # Check if file with command name exists within PATH and has execute permissions
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
