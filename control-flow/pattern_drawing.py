pattern_size = int(input("Enter the size of the pattern: "))
row = 0

while pattern_size > row:
    for i in range(pattern_size):
        print("*", end="")
    print()
    row += 1