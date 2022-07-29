numlist = [ 3, 6, 8, 10, 11, 15, 17, 18, 19, 20 ]

count = 0
for i in numlist:
    count+=1
    if i == 12:
        print(f"It takes {count} comparisons to find 12")
        break
    elif i > 12:
        print(f"It takes {count} comparisons to find 12 is not in the list")
        break


# Using sequential search, 10 comparisions is needed to find that 12 is not in the list
