from kivi_sakset_paperi import KiviSaksetPaperi
from tekoaly import Tekoaly


class KPSTekoaly(KiviSaksetPaperi):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _lopetus_siirto(self, aloitus_siirto):
        siirto =  self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
