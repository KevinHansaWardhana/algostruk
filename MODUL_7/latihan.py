import re

#latihan 7.1
s = 'sebuah contoh kata:teh!!'
s = 'sebuah contoh kata:batagor!!'
s = 'sebuah contoh kata:es teh!!'
cocok = re.findall(r'kata:\w\w\w', s)
if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')


#latihan7.2
cocok=re.findall(r'eee','teeeh')
if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')
cocok1=re.findall(r'ehs','teeeh')
if cocok:
    print('menemukan', cocok1)
else:
    print('tidak menemukan')
cocok2=re.findall(r'..h','teeeh')
if cocok:
    print('menemukan', cocok2)
else:
    print('tidak menemukan')
cocok3=re.findall(r'\d\d\d','t123h di 2019 bulan 02')
if cocok:
    print('menemukan', cocok3)
else:
    print('tidak menemukan')
cocok4=re.findall(r'\w\w\w', '@@a*bc#def*tghh!!')
if cocok:
    print('menemukan', cocok4)
else:
    print('tidak menemukan')


#latihan7.3
cocok=re.findall(r'te+','ghdteeeh')
if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')
cocok1=re.findall(r'e+','teeheeee')
if cocok1:
    print('menemukan', cocok1)
else:
    print('tidak menemukan')
polanya=r'\d\s*\d\s*\d'
cocok2=re.findall(polanya,'xx1 2 3xx')
if cocok2:
    print('menemukan', cocok2)
else:
    print('tidak menemukan')
cocok3=re.findall(polanya,'xx12 3xx')
if cocok3:
    print('menemukan', cocok3)
else:
    print('tidak menemukan')
cocok4=re.findall(polanya,'xx123xx')
if cocok4:
    print('menemukan', cocok4)
else:
    print('tidak menemukan')
cocok5=re.findall(r'^k\w+','mejakursi')
if cocok5:
    print('menemukan', cocok5)
else:
    print('tidak menemukan')
cocok6=re.findall(r'k[\w\s]+','mejakursi tamu saya')
if cocok6:
    print('menemukan', cocok6)
else:
    print('tidak menemukan')

#latihan7.4
s='Alamatku adalah dita-b@google.com mas'
pola=r'[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+'
cocok = re.findall(pola, s)
print(cocok)


#latihan7.5
s= 'Alamatku sr@google.com serta joko@abc.com ok bro. atau don@email.com'
pola= r'([\w\.-]+)@([\w\.-]+)'
e= re.findall(pola, s)
print(e)
for tup in e:
    print('user', tup[0], 'dengan host:',tup[1])
