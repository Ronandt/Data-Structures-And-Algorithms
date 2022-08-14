try:
    lines = []
    while True:
        line = input("Enter a line (cltr-D to stop): ")
        lines.append(line)

except EOFError:
    for i in reversed(lines):
        print(i)


lines2 = []

