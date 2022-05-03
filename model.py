




STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, NAPACNA_CRKA, PONOVLJENA_CRKA = '+','-', 'o'
ZMAGA, PORAZ = 'WIN', 'DEFEAT'
STATE = True


class Igra:
    def __init__(self,geslo,crke='') -> None:
        self.geslo = geslo.upper()
        self.crke = crke.upper()

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]


    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())
        
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        # ugibane = ''
        # for crka in self.geslo:
        #     if crka in self.pravilne_crke():
        #         ugibane += crka
        #     else:
        #         ugibane += '_'
        # return ugibane
        """kako se to reš z izpeljanim seznamom:"""
        return ''.join([(crka if crka in self.pravilne_crke() else '_') for crka in self.geslo ])
    
    def nepravilni_del_gesla(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self,crka):
        if crka.upper() in self.pravilne_crke():
            print(PONOVLJENA_CRKA)
        else:
            self.crke += crka.upper()
            if self.zmaga():
                print (ZMAGA)
            elif self.poraz():
                print (PORAZ)
            elif crka.upper() in self.pravilne_crke():
                print (PRAVILNA_CRKA)
            else:
                print (NAPACNA_CRKA)

with open('besede.txt', encoding='utf8') as besede:
    bazen_besed = besede.read().split('\n')

import random as rd

def nova_igra():
    geslo = rd.choice(bazen_besed)
    return Igra(geslo) 

# igra1 = Igra('abc','')
# igra1.ugibaj('a')
# igra1.ugibaj('a')
# igra1.crke
# igra1.ugibaj('b')
# igra1.ugibaj('d')
# igra1.ugibaj('c')

