import re
#no1
f = open('Indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
pola = r'\sme\w+'
hasil= re.findall(pola, teks)
for e in hasil:
    print(e)
#no2
f = open('Indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
pola = r'\sdi\w+'
hasil= re.findall(pola, teks)
for e in hasil:
    print(e)

#no3
f = open('Indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
pola = r'\sdi\s[\w-]+'
hasil= re.findall(pola, teks)
for e in hasil:
    print(e)
    
#no4
f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
string = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
list = []
for i in string:
    list.append((i[0], float(i[1])))
print(list)
