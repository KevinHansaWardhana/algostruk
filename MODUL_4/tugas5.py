class MhsTIF(object):
      def __init__(self,nama,NIM,kota,uangsaku):
            self.nama=nama
            self.NIM=NIM
            self.kotatinggal=kota
            self.uangsaku=uangsaku
   
c0= MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1= MhsTIF('Budi', 51, 'Sragen', 230000)
c2= MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3= MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4= MhsTIF('Eka', 4, 'Boyolali', 240000)
c5= MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6= MhsTIF('Deni', 13, 'Klaten', 245000)
c7= MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8= MhsTIF('Janto', 23, 'Klaten', 245000)
c9= MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10= MhsTIF('Khalid', 29, 'Purwodadi', 265000)
Daftar=[c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

class node (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    def cari (self, cari):
        curNode = self
        while curNode is not None :
            if curNode.next != None :
                if curNode.data != cari :
                    curNode = curNode.next
                else :
                    print ("Item", cari, "ada dalam Linked List")
                    break
            elif curNode.next == None :
                print ("Item", cari, "tidak ada linked list")
                break    

a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)
a.next=b
b.next=c
c.next=d
b.cari(1)
b.cari(2)
