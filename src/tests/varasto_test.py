import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_nolla(self):
        self.varasto.lisaa_varastoon(0)

    def test_ylitaytto(self):
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 1)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_ota_tyhjasta_varastosta(self):
        self.varasto.ota_varastosta(1000000)
        self.assertEqual(self.varasto.ota_varastosta(10), 0)

    def test_merkkijonotus(self):
        self.assertEqual(str(self.varasto), f"saldo = 0, vielä tilaa 10")

    def test_otto_nolla(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.ota_varastosta(0), 0)

    def test_negatiivinen_tilavuus(self):
        tmp = Varasto(-100)
        self.assertAlmostEqual(tmp.tilavuus, 0)

    def test_negatiivinen_saldo(self):
        tmp = Varasto(100, -100)
        self.assertAlmostEqual(tmp.saldo, 0)

    def test_saldo_enemman_kuin_tilavuus(self):
        tmp = Varasto(100, 200)
        self.assertAlmostEqual(tmp.saldo, tmp.tilavuus)

    def test_lisays_negatiivinen_maara(self):
        prev = self.varasto.saldo
        self.varasto.lisaa_varastoon(-100)
        self.assertAlmostEqual(prev, self.varasto.saldo)

    def test_lisays(self):
        prev = self.varasto.saldo
        self.varasto.lisaa_varastoon(2)
        self.assertAlmostEqual(prev + 2, self.varasto.saldo)

    def test_negatiivinen_otto(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)
