import numpy as np

a = [1,2,3,4]
b = [5,6,7,8]

ab = []

for i in range(9, len(a)):
    ab.append(a[i]*b[i])

# bunun yerine numpy kullanarak,

a = np.array[1,2,3,4]
b = np.array[5,6,7,8]
a*b

# numpy : listeye göre daha hızlıdır , tek tipte veri tutar. verimli işlem sağlar
# ayrıca yüksek seviyeden işlem yapmamızı sağlar. (çarpma gibi.)


# numpy arrayleri oluşturmak :

np.array([1,2,3,4]) # liste üzerinden numpy değeri oluşturduk.

# reshape : 

a = np.random.randint(1,10,size=9) 
a.reshape(3,3) 

# ( [3,9,6] , [7,4,2] , [ 7 , 4, 1] ) yapısına dönüşür fakat eleman sayısı 10 olsaydı hata alınırdı, üçe üçe çeviremez.

 
# arange : sıfırdan otuza kadar üçer üçer oluşturur 

v = np.arange(0,30,3) 

# fancy index : 

# bir numpy arrayine liste girdiğimizde kolay bir şekilde seçim sağlar.

v = np.arange(0,30,3) 
catch = [ 1, 2, 3] 
v[catch] 

# array([3,6,9]) çıktısı oluşur. 


