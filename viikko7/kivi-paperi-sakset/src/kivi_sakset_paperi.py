from tuomari import Tuomari

class KiviSaksetPaperi:
    def pelaa(self):
        print(
            "Peli loppuu kun pelaaja antaa virheellisen "
            "siirron eli jonkun muun kuin k, p tai s"
        )
        tuomari = Tuomari()

        while True:
            eka_siirto = self._eka_siirto()
            toka_siirto = self._toka_siirto(eka_siirto)

            if not (
                self._kelpaako_siirto(eka_siirto) and
                self._kelpaako_siirto(toka_siirto)
            ):
                break

            tuomari.kirjaa_siirto(eka_siirto, toka_siirto)
        
        print("Kiitos!")
        print(tuomari)

    def _eka_siirto(self):
        return input("Ensimmäinen pelaajan siirto: ")

    def _toka_siirto(self, eka_siirto):
        raise Exception("Tämä metodi korvataan aliluokassa")

    def _kelpaako_siirto(self, siirto):
        return siirto in "kps"
