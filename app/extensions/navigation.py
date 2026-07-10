import os


def handle_path(path: str):
    
    if not path:
        return

    # Split path elements into list and handle '..' via a stack pop
    stack = os.getcwd()[1:].split("/") if path[0] == '.' else [] # For relative path, start with cur dir on stack
    for l in path.split("/"):
        if l == "." or l =='':
            pass
        elif l == "..":
            if stack:
                stack.pop()
        elif l == "~":
            stack.append(os.getenv("HOME"))
        else:
            stack.append(l)

    new_dir = "/" + "/".join(stack)

    if os.path.exists(new_dir) or new_dir == "/":
        os.chdir(new_dir)
    else:
        print(f"cd: {path}: No such file or directory")