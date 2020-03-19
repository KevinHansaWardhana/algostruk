#if target in arrayTempatYangDicari:
#    print("targetnya terdapat di array itu.")
#else:
#    print("targetnya tidak terdapata di array itu.")

def cariLurus(wadah, target):
    n=len(wadah)
    for i in range(n):
        if wadah[i]== target:
            return True
    return False

