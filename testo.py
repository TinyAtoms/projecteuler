




squares = [i*i for i in range(1,5)]
for d in range(1,2):
    dsquares = (i * d for i in squares)
    for x in squares:
        # dsquares = (i * d for i in squares)
        for y in dsquares:
            print(x,y)