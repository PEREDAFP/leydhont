"""Punto de entrada de la calculadora electoral D'Hondt.

Captura los datos por consola y muestra el reparto de escaños.
"""

import os
import sys

from dhondt import calcular_umbral, filtrar_partidos, calcular_dhondt, validar_datos


def limpiar_pantalla() -> None:
    """Limpia la pantalla del terminal de forma multiplataforma (stdlib)."""
    os.system("cls" if os.name == "nt" else "clear")

# Verde brillante para las preguntas, solo si la salida es una terminal
# (evita códigos de escape basura cuando se redirige a archivo o pipe).
_COLOR_PROMPT = "\033[92m" if sys.stdout.isatty() else ""
_COLOR_RESET = "\033[0m" if sys.stdout.isatty() else ""


def leer_entero(mensaje: str, permitir_cero: bool = True) -> int:
    """Lee un entero no negativo por consola, volviendo a pedirlo si es inválido."""
    while True:
        try:
            valor = int(input(f"{_COLOR_PROMPT}{mensaje}{_COLOR_RESET}"))
        except ValueError:
            print("Ingrese un número entero válido.")
            continue
        if valor < 0 or (not permitir_cero and valor == 0):
            print("No se admiten valores negativos ni cero.")
            continue
        return valor


def main() -> None:
    limpiar_pantalla()
    while True:
        try:
            print("--- Datos de la Circunscripción ---")
            escaños = leer_entero("Número de escaños a repartir: ", permitir_cero=False)
            votos_totales = leer_entero("Total de votos emitidos: ")
            votos_blanco = leer_entero("Votos en blanco: ")
            num_partidos = leer_entero("Número de partidos: ", permitir_cero=True)

            partidos = []
            for i in range(1, num_partidos + 1):
                nombre = (
                    input(f"{_COLOR_PROMPT}Nombre del partido {i}: {_COLOR_RESET}")
                    .strip()
                    or f"Partido {i}"
                )
                votos = leer_entero(f"Votos de {nombre}: ")
                partidos.append((nombre, votos))

            validar_datos(escaños, votos_totales, votos_blanco, partidos)
            break
        except ValueError as error:
            print(f"\nAdvertencia: {error}. Intente de nuevo.\n")

    umbral = calcular_umbral(votos_totales)
    partidos_filtrados = filtrar_partidos(partidos, umbral)
    excluidos = [(nombre, votos) for nombre, votos in partidos if votos < umbral]

    print("\n--- Resultados ---")
    print(f"Umbral mínimo (3%): {umbral:.0f} votos")
    if excluidos:
        detalle = ", ".join(f"{nombre} ({votos} votos)" for nombre, votos in excluidos)
        print(f"Partidos excluidos (< 3%): {detalle}")
    else:
        print("Partidos excluidos (< 3%): ninguno")

    print("\nReparto de escaños:")
    resultado = calcular_dhondt(escaños, partidos_filtrados)
    for nombre, _ in partidos_filtrados:
        escaños_partido = resultado[nombre]
        print(f"- {nombre}: {escaños_partido} escaño{'s' if escaños_partido != 1 else ''}")


if __name__ == "__main__":
    main()
