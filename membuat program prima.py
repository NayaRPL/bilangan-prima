print("memahami logika tentang bilangan prima")

def bil_prima(x):
    for i in range (2, x): 
       if x % i == 0:
            return False
    return True
print(bil_prima(5))

def cari_bi_prima(awal,akhir):
    list_bi_prima=[]

    for x in range (awal, akhir+1):
        if bil_prima(x):
            list_bi_prima.append(x)
    return list_bi_prima
print(cari_bi_prima(10,20))
    
