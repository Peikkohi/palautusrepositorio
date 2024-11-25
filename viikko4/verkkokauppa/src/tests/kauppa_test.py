import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            katalogi = {1: 10, 2: 9, 3: 0}
            return katalogi[tuote_id]

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            katalogi = {
                    1: Tuote(1, "maito", 5),
                    2: Tuote(2, "peruna", 3),
                    3: Tuote(3, "leipä", 7),
            }
            return katalogi[tuote_id]

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(
                self.varasto_mock,
                self.pankki_mock, 
                self.viitegeneraattori_mock)


    def test_ostoksen_paatytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock \
                .tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kahden_eri_tuotteen_summa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("etta", "23456")

        self.pankki_mock \
                .tilisiirto.assert_called_with("etta", ANY, "23456", ANY, 8)

    def test_kahden_saman_tuotteen_summa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("nelli", "45678")

        self.pankki_mock \
                .tilisiirto.assert_called_with("nelli", ANY, "45678", ANY, 10)

    def test_lisaa_vain_olevia_tuotteita(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("kalevi", "98765")

        self.pankki_mock \
                .tilisiirto.assert_called_with("kalevi", ANY, "98765", ANY, 5)

    def test_asiointi_aloittaa_uuden_ostoksen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("reetta", "13579")

        self.pankki_mock \
                .tilisiirto.assert_called_with("reetta", ANY, "13579", ANY, 3)

    def test_uusi_viite_joka_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("veeti", "24682")

        self.pankki_mock \
                .tilisiirto.assert_called_with(ANY, 1, ANY, ANY, ANY)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("usva", "35793")

        self.pankki_mock \
                .tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)

    def test_poistettu_tuote_ei_ole_summassa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("kuutamo", "11111")

        self.pankki_mock \
                .tilisiirto.assert_called_with("kuutamo", ANY, "11111", ANY, 3)

