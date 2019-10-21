#Her bir ayın kaç gün çektiği hesaplanır
ocak=mart=mayıs=temmuz=agustos=ekim=aralık=31
nisan=haziran=eylül=kasım=30
şubat=28
#Doğalgazın vergiler dahil metreküp fiyatı
birimFiyat=0.79
#Kullanıcı ayda ne kadar tüketmiş?
aylıkSarfıyat= input("Aylık Doğalgaz sarfiyatınızı m3 olarak yazınız: ")
#Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")
ay=eval(dönem)
#Kullanıcının günlük sarfiyatını yazınız
günlükSarfiyat= int(aylıkSarfıyat) / ay
#Fatura tutarı
fatura = birimFiyat * günlükSarfiyat * ay
print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
"tahmini fatura tutarı: \t", fatura, " TL", sep="")
