# mashiqlar3_0612
#1
sozlar = ["hello", "123", "world", "456"]
faqat_harflar = [s for s in sozlar if s.isalpha()]
print(faqat_harflar)


#2
tanlangan = [x for x in range(1, 21) if x % 3 == 1]
print(tanlangan)

#3
sonlar = [1, 2, 3, 4, 5]
natija = ["even" if x % 2 == 0 else "odd" for x in sonlar]
print(natija)
