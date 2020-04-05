from time import time as detak
from random import shuffle as kocok
import time
from latihanmodul6 import mergeSort
from latihanmodul6 import*

k = [i for i in range(1, 6000)]
kocok(k)

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

def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiterkecil(A, i, n)
        if indexkecil != i:
            swap(A, i, indexkecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]

aw = detak(); bubbleSort(u_bub); ak = detak(); print('bubble : %g detik' % (ak-aw))
aw = detak(); selectionSort(u_sel); ak = detak(); print('selection : %g detik' % (ak-aw))
aw = detak(); insertionSort(u_ins); ak = detak(); print('insertion : %g detik' % (ak-aw))
aw = detak(); mergeSort(u_mrg); ak = detak(); print('merge : %g detik' % (ak-aw))
aw = detak(); quickSort(u_qck); ak = detak(); print('quick : %g detik' % (ak-aw))
