import sys
import os

BUILT_INS = {"echo", "exit", "type"}


def main():
    while 1:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_input = sys.stdin.readline().rstrip()
        handle_command(user_input)


def handle_command(cmd):
    match cmd.split()[0]:
        case "echo":
            print(cmd[len("echo")+1:])
        case "type":
            arg = cmd[len("type")+1:]

            if arg in BUILT_INS:
                print(f"{arg} is a shell builtin")
            else:
                check_if_in_path(arg)
        case "exit":
            sys.exit(0)
        case _:
            sys.stdout.write(f"{cmd}: command not found\n")


def check_if_in_path(arg):
    PATH = os.getenv('PATH')
    found = False

    # Check if file with command name exists within PATH and has execute permissions
    for dir in PATH.split(':'):
        fp = os.path.join(dir, arg)
        if os.path.exists(fp) and os.access(fp, os.X_OK):
            print(f"{arg} is {fp}")
            found = True
            break
    
    if not found:
        print(f"{arg}: not found")


if __name__ == "__main__":
    main()
