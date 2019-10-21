çap = input("Dairenin çapı: ")

#Kullanıcının verdiği çap bilgisini kullanarak
#yarıçapı hesaplayalım
yarıçap = int(çap) / 2

#sabit pi sayısı değerimiz
pi = 3.14159


#Yukarıdaki bilgileri kullanarak artık
#dairenin alanını hesaplayabiliriz
alan = pi * (yarıçap * yarıçap)

#Hesaplanan alanın verilmesi
print("çapı", çap,"cm olan dairenin alanı: ", alan, "cm2 dir")
