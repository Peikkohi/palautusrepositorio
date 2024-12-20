from kivi_sakset_paperi import KiviSaksetPaperi
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviSaksetPaperi):
    def __init__(self, muistin_koko):
        self.tekoaly = TekoalyParannettu(muistin_koko)

    def _lopetus_siirto(self, aloitus_siirto):
        siirto =  self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(aloitus_siirto)
        return siirto
