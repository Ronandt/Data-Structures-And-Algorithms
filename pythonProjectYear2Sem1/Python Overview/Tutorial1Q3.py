def sum_of_squares(n):
    if n < 0:
        return f"Not a positive integer"
    else:
        sum = 0
        count = 0
        for i in range(n+1):
            num = n-count
            if int(num/2)*2 != num:
                sum += (n-count)**2
            count+=1

        return sum

sum = sum_of_squares(3)
print(sum)

