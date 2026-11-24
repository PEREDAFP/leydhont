# AGENTS.md

Calculadora Electoral — Método D'Hondt. CLI en Python puro, sin dependencias externas.

## Hechos verificables del repositorio
- Solo hay dos archivos versionados: `.gitignore` y `README.md`.
- `main.py`, `dhondt.py` y `tests/` (descritos en el README) **no existen** en el árbol de trabajo ni en la rama `main`. Si se pide implementar, créelos dentro de esta carpeta.
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
