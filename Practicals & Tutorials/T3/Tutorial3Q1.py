numlist = [ 12, 19, 3, 13, 20, 5, 8, 16, 6, 15 ]

count = 0
for i in numlist:
    count+=1
    if i == 8:
        break

print(f"It takes {count} comparisons to find 8")