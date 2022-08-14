def MyFn(s):
    return s[-1]

list = [ (1, 7), (1, 3), (3, 4, 5), (2, 2) ]
print(sorted(list,key=MyFn))
