"""Pruebas unitarias de la lógica D'Hondt (stdlib unittest)."""

import unittest

from dhondt import calcular_umbral, filtrar_partidos, calcular_dhondt, validar_datos


class TestUmbral(unittest.TestCase):
    def test_umbral_tres_por_ciento(self):
        self.assertEqual(calcular_umbral(100000), 3000.0)
        self.assertEqual(calcular_umbral(100), 3.0)


class TestFiltrado(unittest.TestCase):
    def test_excluye_por_debajo_del_umbral(self):
        partidos = [("A", 42000), ("B", 31000), ("C", 22500), ("D", 2500)]
        self.assertEqual(
            filtrar_partidos(partidos, 3000),
            [("A", 42000), ("B", 31000), ("C", 22500)],
        )

    def test_incluye_igual_al_umbral(self):
        self.assertEqual(filtrar_partidos([("X", 3000)], 3000), [("X", 3000)])


class TestDhondt(unittest.TestCase):
    def test_ejemplo_readme(self):
        escaños = 5
        partidos = [("Partido A", 42000), ("Partido B", 31000), ("Partido C", 22500)]
        resultado = calcular_dhondt(escaños, partidos)
        self.assertEqual(
            resultado, {"Partido A": 2, "Partido B": 2, "Partido C": 1}
        )

    def test_empate_gana_partido_con_mas_votos(self):
        # Partido B (introducido segundo) tiene más votos y gana el desempate.
        # Cocientes: A/1=3000, B/1=6000, A/2=1500, B/2=3000.
        # Top 2: B/1=6000 y el empate a 3000 entre A/1 y B/2 -> gana B.
        escaños = 2
        partidos = [("A", 3000), ("B", 6000)]
        resultado = calcular_dhondt(escaños, partidos)
        self.assertEqual(resultado, {"A": 0, "B": 2})

    def test_empate_total_respeta_orden_introduccion(self):
        # Misma votación: ante empate total se respeta orden de introducción.
        # Cocientes: A/1=3000, A/2=1500, B/1=3000, B/2=1500.
        # Top 2: empate a 3000 entre A/1 y B/1 -> gana A (introducido primero).
        escaños = 2
        partidos = [("A", 3000), ("B", 3000)]
        resultado = calcular_dhondt(escaños, partidos)
        self.assertEqual(resultado, {"A": 1, "B": 1})

    def test_suma_escaños_igual_a_n(self):
        escaños = 7
        partidos = [("A", 10000), ("B", 8000), ("C", 5000)]
        resultado = calcular_dhondt(escaños, partidos)
        self.assertEqual(sum(resultado.values()), escaños)


class TestValidaciones(unittest.TestCase):
    def test_escaños_cero_invalido(self):
        with self.assertRaises(ValueError):
            validar_datos(0, 100000, 0, [("A", 50000)])

    def test_negativos_invalidos(self):
        with self.assertRaises(ValueError):
            validar_datos(5, 100000, 0, [("A", -100)])

    def test_suma_partidos_excede_total(self):
        with self.assertRaises(ValueError):
            validar_datos(5, 100000, 0, [("A", 60000), ("B", 50000)])

    def test_suma_partidos_igual_a_total_pasa_con_blanco(self):
        # Partidos suman exactamente el total; el blanco no resta capacidad.
        validar_datos(5, 1200, 50, [("Partido 1", 1200), ("Partido 2", 0)])

    def test_suma_partidos_menor_a_total_pasa(self):
        validar_datos(5, 100000, 2000, [("A", 42000), ("B", 31000), ("C", 22500)])


if __name__ == "__main__":
    unittest.main()
