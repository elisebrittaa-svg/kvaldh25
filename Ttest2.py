from scipy.stats import ttest_ind

lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa"

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

#pväärtus on kõige olulisem Ttesti näitaja, teisesõnaga sarnasusväärtus
#piirarvestus on üldistavalt kokkuleppeliselt 0,05