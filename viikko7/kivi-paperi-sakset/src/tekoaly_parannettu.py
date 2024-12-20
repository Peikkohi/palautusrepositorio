# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaamuistinraja = 0

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan vanhin alkio
        if self._vapaamuistinraja == len(self._muisti):
            self._muisti[:-1] = self._muisti[1:]
            self._vapaamuistinraja -= 1

        self._muisti[self._vapaamuistinraja] = siirto
        self._vapaamuistinraja += 1

    def anna_siirto(self):
        if self._vapaamuistinraja in {0, 1}:
            return "k"

        viimeisin_siirto = self._muisti[self._vapaamuistinraja - 1]

        k = 0
        p = 0
        s = 0

        for tämä, seuraava in zip(
            self._muisti[:self._vapaamuistinraja],
            self._muisti[1:self._vapaamuistinraja]
        ):
            if viimeisin_siirto == tämä:
                if seuraava == "k":
                    k += 1
                elif seuraava == "p":
                    p += 1
                else:
                    s += 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            return "p"
        elif p > k or p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
