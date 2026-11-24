# test_reduction.py - lancer avec : python -m unittest test_reduction.py -v
import unittest
from reduction import calcul_reduction, prix_final


class TestReduction(unittest.TestCase):
    def test_aucune_reduction(self):
        self.assertAlmostEqual(prix_final(80, False, 0), 80.0)

    def test_etudiant_80(self):
        self.assertAlmostEqual(prix_final(80, True, 0), 72.0)

    def test_fidele_80(self):
        self.assertAlmostEqual(prix_final(80, False, 5), 68.0)

    def test_etudiant_et_fidele_80(self):
        self.assertAlmostEqual(prix_final(80, True, 5), 60.0)

    def test_fidelite_4_ans_pas_de_remise(self):
        self.assertAlmostEqual(prix_final(80, False, 4), 80.0)

    def test_150_sans_statut(self):
        self.assertAlmostEqual(prix_final(150, False, 0), 145.0)

    def test_150_etudiant_et_fidele(self):
        # 150 - 15 - 22.5 - 5 = 107.5
        self.assertAlmostEqual(prix_final(150, True, 5), 107.5)

    def test_seuil_100_exclu(self):
        self.assertAlmostEqual(calcul_reduction(100, False, 0), 0.0)

    def test_prix_jamais_negatif(self):
        self.assertEqual(prix_final(0, False, 0), 0.0)
        self.assertGreaterEqual(prix_final(1, True, 10), 0.0)


if __name__ == "__main__":
    unittest.main()
