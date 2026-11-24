"""Lógica de cálculo del método D'Hondt (biblioteca estándar de Python)."""

from typing import List, Tuple, Dict

Partido = Tuple[str, int]


def validar_datos(
    escaños: int,
    votos_totales: int,
    votos_blanco: int,
    partidos: List[Partido],
) -> None:
    """Valida las entradas según las reglas del README.

    - No se admiten valores negativos ni escaños igual a cero.
    - La suma de votos de los partidos no debe superar el total de
      votos emitidos (los votos en blanco se tienen en cuenta para el
      cálculo del umbral del 3 %, pero no restan capacidad a los
      partidos en esta validación).
    """
    if escaños <= 0:
        raise ValueError("El número de escaños debe ser mayor que cero.")
    if votos_totales < 0:
        raise ValueError("Los votos totales no pueden ser negativos.")
    if votos_blanco < 0:
        raise ValueError("Los votos en blanco no pueden ser negativos.")
    for nombre, votos in partidos:
        if votos < 0:
            raise ValueError(f"Los votos del partido {nombre} no pueden ser negativos.")
    if sum(votos for _, votos in partidos) > votos_totales:
        raise ValueError(
            "La suma de votos de los partidos no debe superar el total de votos emitidos."
        )


def calcular_umbral(votos_totales: int) -> float:
    """Umbral mínimo del 3 % sobre los votos totales emitidos."""
    return votos_totales * 0.03


def filtrar_partidos(partidos: List[Partido], umbral: float) -> List[Partido]:
    """Descarta los partidos con votos estrictamente inferiores al umbral."""
    return [(nombre, votos) for nombre, votos in partidos if votos >= umbral]


def calcular_dhondt(escaños: int, partidos: List[Partido]) -> Dict[str, int]:
    """Reparte los escaños aplicando la Ley D'Hondt.

    1. Divide los votos de cada partido entre 1, 2, ..., N (N = escaños).
    2. Ordena todos los cocientes de mayor a menor.
    3. Asigna los N escaños a los N cocientes más altos.
    """
    cocientes = []
    for nombre, votos in partidos:
        for divisor in range(1, escaños + 1):
            cocientes.append((votos / divisor, nombre))

    # Orden estable por cociente descendente; los empates conservan
    # el orden de aparición (orden de lista de partidos).
    cocientes.sort(key=lambda c: -c[0])

    resultado = {nombre: 0 for nombre, _ in partidos}
    for _, nombre in cocientes[:escaños]:
        resultado[nombre] += 1
    return resultado


def calcular_tabla_divisiones(escaños: int, partidos: List[Partido]):
    """Calcula la tabla de divisiones D'Hondt para mostrar por pantalla.

    Devuelve una lista de filas. Cada fila es una tupla:
        (nombre, votos, celdas, escaños_asignados)
    donde ``celdas`` es una lista de tuplas (divisor, cociente, gano) para
    divisor de 1 a escaños. ``gano`` es True si ese cociente es uno de los
    N cocientes más altos que se reparten un escaño.
    """
    todos = []
    for nombre, votos in partidos:
        for divisor in range(1, escaños + 1):
            todos.append((votos / divisor, nombre, divisor))

    # Orden estable descendente por cociente (empates conservan orden de inserción)
    todos.sort(key=lambda c: -c[0])

    # Los N primeros cocientes ganan un escaño
    ganadores = {(nombre, divisor) for _, nombre, divisor in todos[:escaños]}

    escaños_por_partido = {nombre: 0 for nombre, _ in partidos}
    for _, nombre, _ in todos[:escaños]:
        escaños_por_partido[nombre] += 1

    filas = []
    for nombre, votos in partidos:
        celdas = []
        for divisor in range(1, escaños + 1):
            cociente = votos / divisor
            gano = (nombre, divisor) in ganadores
            celdas.append((divisor, cociente, gano))
        filas.append((nombre, votos, celdas, escaños_por_partido[nombre]))
    return filas
