pattern = int(input("Enter the size of the pattern: "))
i = 0
while i < pattern :
    for x in range(pattern):
        print("*", end="")
    print()
    i += 1