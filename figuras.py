
class kubs:
    #metode, kas inicializē objektu
    def __init__(self, garums, krasa):
        if garums>=2 and garums<=10:
            self.garums = garums
        else:
            print("Malas garums neatbilst nosacījumiem")
            self.garums = 2
        self.krasa = krasa

    #metode, kas aprēķina kuba tilpumu
    def aprekinat_tilpumu(self):
        tilpums = self.garums**3
        return tilpums
    
    #metode, kas izdzēš objektu
    def __del__(self):
        print("Objekts ir likvidēts, tā krāsa bija ", self.krasa)

#objekti
kubg = kubs(10, "zaļa")
kubr = kubs(1, "sarkans")
print (kubg.krasa, kubg.aprekinat_tilpumu())
print (kubr.garums)
#dzēšs objektu 
del kubr 
#pārbauda vai...
try:
    print(kubr.garums)
except:
    print("Objekts neeksistē")
print(kubg.garums)

#klases boks, kas manto no klases kubs
class bloks(kubs):
    def __init__(self, garums, krasa, kubu_skaits, forma):
        super().__init__(garums, krasa)
        if kubu_skaits>=1 and kubu_skaits<=4:
            self.__kubu_skaits = kubu_skaits
        else:
            print("Nepareiza kubu skaita vērtība")
        self.nosaukums = str(self.krasa)+str(kubu_skaits)
        formas_vertibas = [11,12,13,14,22]
        if forma not in formas_vertibas:
            print("Forma neatbilsts nosacījumiem")
            self.derigums = 0
        else:
            self.derigums = 1
    def tilpums(self):
        kuba_tilpums = self.garums**3 #rēķina blokam tilpumu
        bloka_tilpums = kuba_tilpums*self.__kubu_skaits
        return bloka_tilpums
    def mainit_formu(self, jauna_forma):
        formas_vertibas = [11,12,13,14,22]
        if jauna_forma not in formas_vertibas:
            print("Forma neatbilsts nosacījumiem")
            self.derigums = 0
        else:
            self.derigums = 1

#objektu veidošana
orange3 = bloks(5, "oranža", 3, 13)
print(orange3.nosaukums, orange3.tilpums())
blue5 = bloks(7, "zila", 5, 23)
print(blue5.nosaukums, blue5.derigums)
blue5.mainit_formu(12)
print(blue5.nosaukums, blue5.derigums)

