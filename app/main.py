import sys

def main():
    while 1:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_input = sys.stdin.readline().rstrip()
        if user_input == "exit":
            break
        sys.stdout.write(f"{user_input}: command not found\n")

if __name__ == "__main__":
    main()
