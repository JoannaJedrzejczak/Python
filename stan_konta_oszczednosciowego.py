# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:59:41 2021

@author: Joanna
"""

"Obliczanie stanu konta oszczędnosciowego"

ILOSC_LAT = 5
ILOSC_MIESIECY_W_ROKU = 12
PROCENT = 0.10 #czyli10%

WPLATA_MIESIECZNA = 100 #zl
stan_konta = 0

for rok in range(1, ILOSC_LAT + 1):
    for miesiąc in range (1, ILOSC_MIESIECY_W_ROKU +1):
        stan_konta += WPLATA_MIESIECZNA
        print(stan_konta)
    stan_konta += stan_konta * PROCENT
    
print(stan_konta)
