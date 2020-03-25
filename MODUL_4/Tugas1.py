class MhsTIF(object):
      def __init__(self,nama,NIM,kota,uangsaku):
            self.nama=nama
            self.NIM=NIM
            self.kotatinggal=kota
            self.uangsaku=uangsaku
   
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

def carikotatinggal(n,target):
      x=[]
      y=0
      for i in Daftar:
            if i.kotatinggal==target:
                  x.append(y)
            y+=1
      print(x)
