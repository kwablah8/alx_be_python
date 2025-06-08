pattern_size = int(input("Enter the size of the pattern: "))

while pattern_size > 0:
    for i in range(pattern_size):
        print("*", end="")
    print()