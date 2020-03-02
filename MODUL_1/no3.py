vokal = 'aiueo'
def jumlahHurufVokal(kata):
    jmlVkl = 0
    pjgKata = len(kata)
    for huruf in kata:
        if huruf in vokal:
            jmlVkl += 1
    print('(' + str(pjgKata) + ',' + str(jmlVkl) + ')')

def jumlahHurufKonsonan(kata):
    jmlKonso = 0
    pjgKata = len(kata)
    for huruf in kata:
        if huruf not in vokal:
            jmlKonso += 1
    print('(' + str(pjgKata) + ',' + str(jmlKonso) + ')')
