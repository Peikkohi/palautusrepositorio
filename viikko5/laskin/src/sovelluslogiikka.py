
class Sovelluslogiikka:
    "Komennot palauttavat voiko kumota"
    def __init__(self, arvo=0):
        self._historia = [arvo]

    def miinus(self, operandi):
        self.aseta_arvo(self.arvo() - operandi)
        return True

    def plus(self, operandi):
        self.aseta_arvo(self.arvo() + operandi)
        return True

    def nollaa(self):
        self.aseta_arvo(0)
        return True

    def kumoa(self):
        self._historia.pop()
        return len(self._historia) > 1

    def aseta_arvo(self, arvo):
        self._historia.append(arvo)

    def arvo(self):
        return self._historia[-1]
