for i in range(10):
    skip = False
    for j in range(10):
        if not skip:
            if i == 1 and j == 2:
                skip = True
            print (i,j)