#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1 Kullanıcının girdiği sayının tek mi çift mi olduğunu bulma
sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print(f"{sayi} çifttir.")
else:
    print(f"{sayi} tektir.")

    
#2 Kullanıcının notunu alarak harf notunu hesaplama
notu = int(input("Notunuzu girin: "))

#not 100den büyük olmasın diye önlem aldım
if notu>100:
    print("Not 100'den büyük olamaz!")
    notu = int(input("Notunuzu girin: "))
    
if 90 <= notu <= 100:
    harf_notu = "A"
elif 80 <= notu <= 89:
    harf_notu = "B"
elif 70 <= notu <= 79:
    harf_notu = "C"
elif 60 <= notu <= 69:
    harf_notu = "D"  
else:
    harf_notu = "F"

print(f"Notunuz: {notu}, Harf Notunuz: {harf_notu}")


#3 Kullanıcının yaş grubunu belirleme
yas = int(input("Yaşınızı girin: "))

if 0 <= yas <= 12:
    yas_grubu = "Çocuk"
elif 13 <= yas <= 19:
    yas_grubu = "Genç"
elif 20 <= yas <= 59:
    yas_grubu = "Yetişkin"
else:
    yas_grubu = "Yaşlı"

print(f"{yas} yaşındasınız ve {yas_grubu} grubundasınız.")


# In[ ]:





# In[ ]:




