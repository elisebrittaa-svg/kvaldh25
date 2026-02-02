from scipy.stats import ttest_ind
#print(ttest_ind([3, 5, 4], [12, 16, 14]))
print(ttest_ind([3, 5, 4, 6, 5, 4], [12, 16, 14, 16, 15, 14]))
print(ttest_ind([3, 5, 4, 6, 5, 4, 5, 5, 6, 3, 5, 6, 6, 7, 3, 4, 5, 8, 8, 5, 4], [12, 16, 14, 16, 15, 14, 16, 16, 13, 13, 11, 14, 11, 10, 11, 14, 15, 16, 13]))



# pip install scipy
# python Ttest.py

#pvalue näitab sarnasusteguri protsenti
