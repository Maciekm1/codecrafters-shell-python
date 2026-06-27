import sys

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
                case "echo" | "exit":
                    print(f"{arg} is a shell builtin")
                case _:
                    print(f"{arg}: not found")

        case _:
            sys.stdout.write(f"{cmd}: command not found\n")


if __name__ == "__main__":
    main()
