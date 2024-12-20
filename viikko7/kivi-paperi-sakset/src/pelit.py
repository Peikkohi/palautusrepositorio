from kivi_sakset_paperi import KiviSaksetPaperi
from helppo_tekoaly import HelppoTekoaly
from vaikea_tekoaly import VaikeaTekoaly

class VastaanPelaajaa(KiviSaksetPaperi):
    def _toka_siirto(self, _):
        return input("Toisen pelaajan siirto: ")

class VastaanTekoalya(KiviSaksetPaperi):
    def __init__(self, tekoaly):
        self._tekoaly = tekoaly

    def _toka_siirto(self, eka_siirto):
        siirto =  self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self._tekoaly.aseta_siirto(eka_siirto)
        return siirto

def luo_peli(valittu):
    if valittu.endswith("a"):
        return VastaanPelaajaa()
    elif valittu.endswith("b"):
        return VastaanTekoalya(HelppoTekoaly())
    elif valittu.endswith("c"):
        return VastaanTekoalya(VaikeaTekoaly(muistin_koko=10))
    else:
        return None
