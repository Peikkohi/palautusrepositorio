KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    @staticmethod
    def _luo_lista(koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        def luonnollinen_lukuko(luku):
            return isinstance(luku, int) and luku >= 0
        assert luonnollinen_lukuko(kapasiteetti), "Väärä kapasiteetti"
        assert luonnollinen_lukuko(kasvatuskoko), "Virheellinen kasvatuskoko"

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.alkio_maara = 0

    def iterate(self):
        for alkio in self.alkiot[:self.alkio_maara]:
            yield alkio

    def kuuluu(self, luku):
        # return luku in self.alkiot
        for alkio in self.iterate():
            if alkio == luku:
                return True
        return False

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        self.alkiot[self.alkio_maara] = luku
        self.alkio_maara += 1

        self.varaa_tilaa()

        return True

    def varaa_tilaa(self):
        if self.alkio_maara == len(self.alkiot):
            vanhat_alkiot = self.alkiot
            self.alkiot = self._luo_lista(self.alkio_maara + self.kasvatuskoko)
            self.alkiot[:self.alkio_maara] = vanhat_alkiot

    def poista(self, luku):
        loytyiko = False
        for i, alkio in enumerate(self.iterate()):
            if alkio == luku:
                loytyiko = True
            if loytyiko:
                self.alkiot[i] = self.alkiot[i + 1]

        if loytyiko:
            self.alkio_maara -= 1
            return True

        return False

    def mahtavuus(self):
        return self.alkio_maara

    def to_int_list(self):
        taulu = self._luo_lista(self.alkio_maara)

        for i, _ in enumerate(taulu):
            taulu[i] = self.alkiot[i]

        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdistejoukko = IntJoukko()

        for luku in joukko_a.iterate():
            yhdistejoukko.lisaa(luku)

        for luku in joukko_b.iterate():
            yhdistejoukko.lisaa(luku)

        return yhdistejoukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkausjoukko = IntJoukko()

        for luku in joukko_a.iterate():
            if joukko_b.kuuluu(luku):
                leikkausjoukko.lisaa(luku)

        return leikkausjoukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotusjoukko = IntJoukko()

        for luku in joukko_a.iterate():
            erotusjoukko.lisaa(luku)

        for luku in joukko_b.iterate():
            erotusjoukko.poista(luku)

        return erotusjoukko

    def __str__(self):
        # alkioiden_alue = self.alkiot[:self.alkio_maara]
        # return f"{{{', '.join(alkioiden_alue)}}}"

        if self.alkio_maara == 0:
            return "{}"

        tuloste = str(self.alkiot[0])
        for luku in self.alkiot[1:self.alkio_maara]:
            tuloste = f"{tuloste}, {luku}"
        return f"{{{tuloste}}}"
