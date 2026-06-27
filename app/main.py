from operator import truediv
import sys
import os

def main():
    while 1:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_input = sys.stdin.readline().rstrip()
        if user_input == "exit":
            break

        handle_command(user_input)


def handle_command(cmd):
    match cmd.split()[0]:
        case "echo":
            print(cmd[5:])
        case "type":
            arg = cmd[5:]
            match arg:
                case "echo" | "exit" | "type":
                    print(f"{arg} is a shell builtin")
                case _:
                    check_if_in_path(arg)
        case _:
            sys.stdout.write(f"{cmd}: command not found\n")


def check_if_in_path(arg):
    PATH = os.getenv('PATH')
    found = False

    for dir in PATH.split(':'):
        # Check if file with command name exists within this dir
        # Check if it has execute permissions
        fp = f"{dir}/{arg}"
        if os.path.exists(fp) and os.access(fp, os.X_OK):
            print(f"{arg} is {fp}")
            found = True
            break
    
    if not found:
        print(f"{arg}: not found")


if __name__ == "__main__":
    main()
