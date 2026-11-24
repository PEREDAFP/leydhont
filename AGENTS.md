# AGENTS.md

Calculadora Electoral — Método D'Hondt. CLI en Python puro, sin dependencias externas.

## Estructura del proyecto (esta carpeta)
- `main.py` — punto de entrada y captura de datos por consola.
- `dhondt.py` — lógica de filtrado (umbral 3 %) y cálculo D'Hondt (stdlib puro).
- `tests/test_dhondt.py` — pruebas unitarias con `unittest` (stdlib).
- `.gitignore` y `README.md` son los únicos archivos de configuración/docs.
- No hay CI, GitHub Actions, pre-commit, `opencode.json`, `requirements.txt`, lockfiles, linter ni typechecker configurados.

## Stack y requisitos
- Python 3.8+.
- Solo biblioteca estándar de Python. No ejecutar `pip install`; no existe `requirements.txt`.

## Comandos exactos
- Ejecutar la aplicación: `python3 main.py`
- Ejecutar pruebas (`unittest`, stdlib): `python3 -m unittest discover -s tests`

## Reglas de trabajo
- Escribir en español (README, código, commits).
- No añadir dependencias ni herramientas de terceros: el proyecto es stdlib puro y no está configurado para nada más.
- Utiilización de comprenshive list siempre que sea posible.
