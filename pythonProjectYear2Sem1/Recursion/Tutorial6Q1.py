def main():
    # Compute and print the sum of (1 + 2 + ... + 10)
    print(sum(10))


def sum(x):
    if x == 1:
        return 1
    elif x>=1:
        return x + sum(x-1)


    # Assuming x >= 1
    # Complete this function recursively

main()
