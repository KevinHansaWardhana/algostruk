class Manusia(object):
      keadaan='Lapar'
      
      def __init__(self,nama):
            self.nama=nama
      def ucapkansalam(self):
            print("salam, namaku",self.nama)
      def makan(self,s):
            self.keadaan='kenyang'
      def olahraga(self, k):
            print("Saya baru saja latihan",k)
            self.keadaan='lapar'
      def mengalikandengandua(self,n):
            return n*2
        
class mahasiswa(Manusia):
      def __init__(self,nama,NIM,kota,us):
            self.nama=nama
            self.NIM=NIM
            self.kotatinggal=kota
            self.uangsaku=us
      def __str__(self):
            s=self.nama + ', NIM '+str(self.NIM)\
               + ',  Tinggal di  '+self.kotatinggal\
               + ', Uang saku Rp '+str(self.uangsaku)\
               + ', tiap bulannya '
            return s
      def ambilNama(self):
            return self.nama
      def ambilNIM(self):
            return self.NIM
      def ambilUangSaku(self):
            return self.uangsaku
      def makan(self,s):
            print("Saya nbaru saja makan",s,"sambil tidur.")
            self.keadaan='kenyang'

class MhsTIF(mahasiswa):
    def katakanPy(self):
        print('Python is cool')
       
c0= MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1= MhsTIF('Budi', 51, 'Sragen', 240000)
c2= MhsTIF('Ahmad', 2, 'Surakarta', 240000)
c3= MhsTIF('Chandra', 18, 'Surakarta', 240000)
c4= MhsTIF('Eka', 4, 'Boyolali', 240000)
c5= MhsTIF('Fandi', 31, 'Salatiga', 240000)
c6= MhsTIF('Deni', 13, 'Klaten', 240000)
c7= MhsTIF('Galuh', 5, 'Wonogiri', 240000)
c8= MhsTIF('Janto', 23, 'Klaten', 240000)
c9= MhsTIF('Hasan', 64, 'Karanganyar', 240000)
c10= MhsTIF('Khalid', 29, 'Purwodadi', 240000)
Daftar=[c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

target ='Klaten'
for i in Daftar:
    if i.kotatinggal==target:
        print(i.nama+' tinggal di '+target)
