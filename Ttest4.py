from scipy.stats import ttest_ind

lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud. Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud. Kooliõpetaja kutsus mõlemad oma tuppa, kõneles nendega  natuke aega, käskis Arnol hoolas ja korralik ja seadis ta siis pinki ühe pikkade juustega poisi kõrvale istuma."
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa. Ei leia mina iial teal see suure, laia ilma peal, mis mul nii armas oleks ka kui sa, mu isamaa!"

#sõnade arv

th="aeiouöäõü"
print(lause1.lower())
#prindib lause 1 ilma suurte tähtedeta, täielikult väikestes tähtedes
print ([t for t in "koolimajja" if t in th])
#leiab sõnad kus on sees need täishäälikud ja prindib need terminali
print (len([t for t in "koolimajja" if t in th]))

def t_arv(sona):
    return len([t for t in sona if t in th])

print (t_arv("kalamaja"))
arvud1=[t_arv(sona) for sona in lause1.lower().split()]
print(arvud1)

#teise teksti arvud:
print(lause2.lower())
def t_arv(sona):
    return len([t for t in sona if t in th])
arvud2=[t_arv(sona) for sona in lause2.lower().split()]
print(arvud2)

print(ttest_ind(arvud1, arvud2))
print (sum(arvud1)/len(arvud1))
print (sum(arvud2)/len(arvud2))
#Kevade kahes lauses on sõnades leidvate täishäälikute aritmeetline keskmine 2.65
#hümni kahes lauses on sõnades leiduvate täishäälikute aritmeetiline keskmine 2.0

def keskmine(m):
        return sum(m)/len(m)

print(keskmine(arvud1), keskmine(arvud2))

#arve vaadates tundub nagu võiks olla hümnis rohkem kaashäälikuid kui Kevades
#proovime saada käte täishäälikute osakaalu
def t_osa(sona):
    return len([t for t in sona if t in th])/len(sona)

osakaalud1=[t_osa(sona) for sona in lause1.lower(). split()]
print(osakaalud1)
print(keskmine(osakaalud1))
#0.48

osakaalud2=[t_osa(sona) for sona in lause2.lower().split()]
print(osakaalud2)
print(keskmine(osakaalud2))
#0.53

print(ttest_ind(osakaalud1, osakaalud2))

#statistic - standardhälve
#keskmine plus1 miinus1 standardhälve moodustab 2/3 andmetest
# antud kahe keskmise osakaalu erinevus on 1,7 standardhälvet, seega kattuvus andmetes on üsna väike
#usaldus/kõikumisvahemik?

import statsmodels.stats.api as sms
cm = sms.CompareMeans(sms.DescrStatsW(osakaalud1), sms.DescrStatsW(osakaalud2))
print(cm.tconfint_diff(usevar='unequal'))
