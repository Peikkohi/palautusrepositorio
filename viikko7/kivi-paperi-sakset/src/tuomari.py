
# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, eka, toka):
        # sama siirto on tasapelitilanne
        onko_tasapeli = eka == toka
        # kuuluuko siirrot ekan voittotilanteisiin
        voittaako_eka = (
            (eka, toka) in {
                ("k", "s"),
                ("s", "p"),
                ("p", "k"),
            }
        )
        if onko_tasapeli:
            self.tasapelit += 1
        elif voittaako_eka:
            self.ekan_pisteet += 1
        else:
            self.tokan_pisteet += 1

    def __str__(self):
        return (
            "Pelitilanne: "
            f"{self.ekan_pisteet} - {self.tokan_pisteet}\n"
            f"Tasapelit: {self.tasapelit}"
        )
