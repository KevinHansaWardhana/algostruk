def cariTerkecil(kumpulan):
    n=len(kumpulan)
    terkecil=kumpulan[0]
    for i in range(1,n):
        if kumpulan[i] < terkecil:
            terkecil=kumpulan[i]
    return terkecil
