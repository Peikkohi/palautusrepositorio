class HelppoTekoaly:
    def __init__(self):
        self._mones_siirto = 0

    def anna_siirto(self):
        self._mones_siirto = (self._mones_siirto + 1) % 3

        return "kps"[self._mones_siirto]

    def aseta_siirto(self, siirto):
        pass
