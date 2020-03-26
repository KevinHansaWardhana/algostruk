def swap(A,p,q):
    tmp=A[p]
    A[p]=A[q]
    A[q]=tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil=i
    return posisiTerkecil

#Latihan 5.1
def bubbleSort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swap(a,j,j+1)

#Latihan 5.2
def selectionSort(a):
    n=len(a)
    for i in range(n-1):
        indexKecil=cariPosisiYangTerkecil(a,i,n)
        if indexKecil != i:
            swap(a,i,indexKecil)

#Latihan 5.3
def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        nilai=a[i]
        pos=i
        while pos > 0 and nilai < a[pos-1]:
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos] = nilai
