from latihanmodul6 import mergeSort
from latihanmodul6 import quickSort

class mahasiswa():
    keadaan = 'lapar'
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.nim) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' perharinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print('Saya baru saja makan', s, 'sambil belajar')
        self.keadaan = 'kenyang'
        
class mhsTIF(mahasiswa):
    def katakanPy(self):
        print('Python is cool')

c1=mhsTIF('ana',55,'Boyolali',250000)
c2=mhsTIF('Ahmad',22,'Salatiga',250000)
c3=mhsTIF('Budi',15,'Surakarta',235000)
c4=mhsTIF('Dika',4,'Sragen',240000)
c5=mhsTIF('aji',38,'Surakarta',230000)

A = [c1.nim, c2.nim, c3.nim, c4.nim, c5.nim]
mergeSort(A)
print(A)
