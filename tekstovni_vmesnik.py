
import model
from model import Igra

def izpis_igre(igra:Igra):
    niz =  f"""{igra.pravilni_del_gesla()}
Nepravilni ugibi: {igra.nepravilni_del_gesla()}
Napačno lahko ugibaš še: {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}"""
    return niz
def izpis_zmage(igra:Igra):
    niz = f"Bravo, geslo je {igra.geslo}"
    return niz
def izpis_poraza(igra:Igra):
    niz =  f"Bravo retard, razočaral si svoje starše. Odgovor je bil {igra.geslo}. Debil."
    return niz

def zahtevaj_vnos():
    return input(">Ugibaj črko: ")

def run_tekstovni_vmesnik():
    igra = model.nova_igra()
    while not igra.zmaga() and not igra.poraz():
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        state = igra.ugibaj(crka)
    if igra.zmaga():
        print(izpis_zmage(igra))
    else:
        print(izpis_poraza(igra))

run_tekstovni_vmesnik()