def im_funkcia(n):
    zuyger = []
    kenter = []
    for i in n:
        if i%2==0:
            zuyger.append(i)
        else:
            kenter.append(i)
    return print(zuyger,kenter)
l=range(5,51)
im_funkcia(l)