from tuomari import Tuomari

class KiviSaksetPaperi:
    def pelaa(self):
        print(
            "Peli loppuu kun pelaaja antaa virheellisen "
            "siirron eli jonkun muun kuin k, p tai s"
        )
        tuomari = Tuomari()

        while True:
            aloitus_siirto = self._aloitus_siirto()
            lopetus_siirto = self._lopetus_siirto(aloitus_siirto)

            if not (
                self._kelpaako_siirto(aloitus_siirto) and
                self._kelpaako_siirto(lopetus_siirto)
            ):
                break

            tuomari.kirjaa_siirto(aloitus_siirto, lopetus_siirto)
        
        print("Kiitos!")
        print(tuomari)

    def _aloitus_siirto(self):
        return input("Ensimmäinen pelaajan siirto: ")

    def _lopetus_siirto(self, aloitus_siirto):
        raise Exception("Tämä metodi korvataan aliluokassa")

    def _kelpaako_siirto(self, siirto):
        return siirto in "kps"
