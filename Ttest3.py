from scipy.stats import ttest_ind

lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud. Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud. Kooliõpetaja kutsus mõlemad oma tuppa, kõneles nendega  natuke aega, käskis Arnol hoolas ja korralik ja seadis ta siis pinki ühe pikkade juustega poisi kõrvale istuma."
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa. Ei leia mina iial teal see suure, laia ilma peal, mis mul nii armas oleks ka kui sa, mu isamaa!"

#leia T-testi abil, kas nende lausete sõnade keskmine pikkus erineb üldistatavalt

sonad1=lause1.split()
print(sonad1)
print(sonad1[3])
print (len(sonad1[3])) #
print (len(sonad1)) #sõnu lauses kokku

sonapikkused1=[len(sona) for sona in sonad1]
print(sonapikkused1) #annab loetelu sõnade pikkustest mis esimeses lauses on

sonad2=lause2.split()
print(sonad2)
print(len(sonad2))

sonapikkused2=[len(sona) for sona in sonad2]
print(sonapikkused2)

print(ttest_ind(sonapikkused1, sonapikkused2))
print (sum(sonapikkused1)/len(sonapikkused1))

#6.129279566910947e-05 = 0.00000612
#sarnasuse märk on kordades väiksem kui ühe lausega
#kodutöö sarnaselt
#võib arvutada näiteks sõnade, aja kaupa
#kui palju kokku on