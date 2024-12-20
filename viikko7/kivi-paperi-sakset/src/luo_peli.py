from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(valittu):
    if valittu == '':
        return None

    valikoima = {
            'a': KPSPelaajaVsPelaaja(),
            'b': KPSTekoaly(),
            'c': KPSParempiTekoaly(muistin_koko=10),
    }

    return valikoima.get(valittu[-1])
