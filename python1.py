#--------------------------
'''
A maradek nevű függvény,
két számot kap bemenetként és 
visszatér a két szám hányadosának maradékával.
'''
def maradek(szam1,szam2):
   return szam1 % szam2


#--------------------------
'''
A kor_terulete nevű függvény, 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör területével.
'''
import math
def kor_terulete(sugar):
    return sugar**2*math.pi
    


#--------------------------
'''
A paros nevű függvény,
egy számot kap bemenetként, 
majd True-val tér vissza, ha a szám páros és 
False-al ha a szám páratlan.
'''
def paros(szam):
    if szam % 2 == 0:
        return True
    else:
        return False


#--------------------------
'''
A teglalap_kerulet nevű függvény, 
egy téglalap oldalhosszait kapja bemenetként és 
visszatér a téglalap kerületével.
'''
def kor_kerulete(sugar):
    return sugar*2*math.pi


#--------------------------
'''
A kettovel_oszthato nevű függvény, 
egy számot kap bemenetként és 
visszatér True-val, ha a szám kettővel osztható és 
visszatér False-al ha a szám kettővel nem ossztható.
'''
def kettovel_oszthato(szam):
    if szam % 2 == 0:
        return True
    else:
        return False
    


#--------------------------
'''
A negyzet_kerulet nevű függvény, 
egy négyzet oldalhosszát kapja bemenetként és 
visszatér a négyzet kerületével.
'''
def negyzet_kerulet(oldal):
    return 4*oldal


#--------------------------
'''
A negyzet_terulet nevű függvény,
egy négyzet oldalhosszát kapja bemenetként és 
visszatér a négyzet területével.
'''
def negyzet_terulet(oldal):
    return oldal*oldal


#--------------------------
'''
A hettel_oszthato nevű függvény, 
egy számot kap bemenetként és 
True-val tér vissza, ha a szám héttel osztható és 
False-al ha nem.
'''
def hettel_oszthato(szam):
    if szam % 7 == 0:
        return True
    else:
        return False


#--------------------------
'''
A teglalap_terulet nevű függvény,
egy téglalap oldalhosszait kapja bemenetként és 
visszatér a téglalap területével.
'''
def teglalap_terulet(oldal1,oldal2):
    return oldal1*oldal2


#--------------------------
'''
A nagyobb nevű függvény,
két számot kap és 
visszatér a nagyobb számmal.

Nem használhatod a max nevű függvényt.
'''
def nagyobb(szam1,szam2):
    if szam1<szam2:
        return szam2
    else:
        return szam1


#--------------------------
'''
A kocka_terfogat nevű függvény,
bemenetként megkapja a kocka oldal hosszúságát és 
a kocka térfogatával tér vissza.
'''
def kocka_terfogat(oldal):
    return oldal*oldal*oldal


#--------------------------
'''
A teglalap_atloja nevű függvény, 
bemenetként megkapja az oldalak hosszát és 
az átló hosszával tér vissza.
'''
def teglalap_atloja(oldal1,oldal2):
    return (oldal1**2+oldal2**2)**0.5


#--------------------------
'''
A derekszogu_haromszog_atfogo nevű függvény, 
bemenetként megkapja a befogók hosszát és 
az átfogó hosszával tér vissza.
'''
def derekszogu_haromszog_atfogo(b1,b2):
    return (b1**2+b2**2)**0.5


#--------------------------
'''
A harommal_oszthato nevű függvény,
egy számot kap bemenetként és 
True-val tér vissza, ha a szám hárommal osztható és 
False-al ha nem.
'''
def harommal_oszthato(szam):
    if szam % 3 == 0:
        return True
    else:
        return False


#--------------------------
'''
A derekszogu_haromszog_terulet nevű függvény, 
bemenetként megkapja a befogók hosszát és 
a háromszög területével tér vissza.
'''
def derekszogu_haromszog_terulet(oldal1,oldal2):
    return oldal1*oldal2/2


#--------------------------
'''
A szamtani_kozep nevű függvény, 
két számot kap és 
visszatér a számtani középpel.
'''
def szamtani_kozep(szam1,szam2):
    return (szam1+szam2)/2
    


#--------------------------
'''
A kor_kerulete nevű függvény 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör kerületével.
'''

def teglalap_kerulet(o1,o2):
    return 2*(o1+o2)


#--------------------------
'''
A kisebb nevű függvény,
két számot kap és 
visszatér a kisebbik számmal.

Nem használhatod a min nevű függvényt

'''
def kisebb(szam1,szam2):
    if szam1>szam2:
        return szam2
    else:
        return szam1


#--------------------------
'''
A teglatest_terfogat nevű függvény, 
bemenetként megkapja a téglatest oldalainak hosszúságát és 
a téglatest térfogatával tér vissza.
'''
def teglatest_terfogat(o1,o2,o3):
    return o1*o2*o3


#--------------------------
'''
A kulonbseg nevű függvény,
két számot kap bemenetként és 
visszatér a két szám különbségével.
'''
def kulonbseg(szam1,szam2):
    return szam1-szam2


#--------------------------
'''
Az osszead nevű nevű függvény,
két számot kap és 
visszatér a két szám összegével.

Nem használhatod a sum nevű függvényt!
    
'''
def osszead(szam1,szam2):
    return szam1+szam2


#--------------------------
'''
Az abszolut nevű függvény, 
a bemenő paraméterként kapott szám 
abszolút értékével tér vissza.
'''
def abszolut(szam):
    if szam > 0:
        return szam
    else:
        return -szam
    
    


#--------------------------
'''
A negyzet_atloja nevű függvény, 
bemenetként megkapja a négyzet oldalának hosszát és 
az átló hosszával tér vissza.
'''
def negyzet_atloja(oldal1):
    return 2**0.5*oldal1


#=====================================