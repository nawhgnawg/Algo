n = int(input())
commands = [list(input().split()) for _ in range(n)]

d = {}

for command in commands:
    if command[0] == "add":
        cmd, k, v = command
        d[k] = v
    else:
        cmd, k = command
        if cmd == "remove":
            d.pop(k)
        elif cmd == "find":
            if k in d:
                print(d[k])
            else:
                print("None")


