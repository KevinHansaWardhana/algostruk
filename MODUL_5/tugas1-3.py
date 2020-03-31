class MhsTIF():
   def __init__(self, nama, nim, asal, us):
        self.nama = nama
        self.nim = nim
        self.asal = asal
        self.uangsaku = us
    
c0 = MhsTIF("kevin","l200180004","sukoharjo",50000)
c1 = MhsTIF("aji","l200180011","sukoharjo",25000)
c2 = MhsTIF("edi","l200180010","klaten",10000)
c3 = MhsTIF("rifqi","l200180008","karanganyar",30000)
c4 = MhsTIF("ismi","l200180006","sukoharjo",40000)
c5 = MhsTIF("galih","l200180005","surakarta",15000)
c6 = MhsTIF("dhiul","l200180003","sukoharjo",12000)
c7 = MhsTIF("auzan","l200180001","sragen",22000)
c8 = MhsTIF("satria","l200180002","sukoharjo",26000)
c9 = MhsTIF("tito","l200180009","boyolali",35000)
c10 = MhsTIF("dika","l200180007","wonogiri",45000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


#No.1
def urut():
    n = len(Daftar)
    for i in range (n-1):
        for j in range (n-i-1):
            if Daftar[j].nim > Daftar[j+1].nim:
                swap(Daftar,j,j+1)
    Daftar2 = [Daftar[0].nim, Daftar[1].nim, Daftar[2].nim, Daftar[3].nim, Daftar[4].nim, Daftar[5].nim, Daftar[6].nim, Daftar[7].nim, Daftar[8].nim, Daftar[9].nim, Daftar[10].nim]
    print (Daftar2)




#No.2
A = [1, 3, 5, 7, 9]
B = [2, 4, 6, 8, 10]
C = []

def gabung():
    C.extend(A)
    C.extend(B)
    n = len(C)
    for i in range (n-1):
        for j in range (n-i-1):
            if C[j] > C[j+1]:
                swap(C,j,j+1)
    print (C)


#No.3
def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp


def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini + 1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil


def bubblesort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)


def selectionsort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiterkecil(A, i, n)
        if indexkecil != i:
            swap(A, i, indexkecil)


def insertionsort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubblesort(u_bub);ak = detak();print('Buble      : %g detik' % (ak - aw));
aw = detak();selectionsort(u_sel);ak = detak();print('Selection  : %g detik' % (ak - aw));
aw = detak();insertionsort(u_ins);ak = detak();print('Insertion  : %g detik' % (ak - aw));
