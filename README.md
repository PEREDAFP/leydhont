# Calculadora Electoral — Método D'Hondt

Aplicación de línea de comandos (CLI) escrita íntegramente en **Python puro**, sin dependencias externas, diseñada para calcular el reparto de escaños de una circunscripción electoral aplicando la **Ley D'Hondt** y una barrera electoral del **3%**.

## Referencia Teórica

El algoritmo de reparto sigue las especificaciones del sistema proporcional D'Hondt:
- Documentación de referencia: [D'Hondt method — Wikipedia](https://en.wikipedia.org/wiki/D%27Hondt_method)

## Requisitos

- **Python 3.8** o superior.
- **Sin dependencias externas**: el proyecto utiliza exclusivamente la biblioteca estándar de Python (no requiere `pip install` ni paquetes de terceros).

## Especificaciones Funcionales

### 1. Datos de entrada (por consola)
Al ejecutar el programa, se solicitarán al usuario los siguientes datos de la circunscripción electoral:

1. **Escaños**: número total de escaños a repartir en la circunscripción.
2. **Votos totales**: total de votos emitidos en la circunscripción.
3. **Votos en blanco**: número de votos en blanco registrados.
4. **Número de partidos**: cantidad de candidaturas que concurren a las elecciones.
5. **Partidos y sus votos**: para cada partido, se pedirá su **nombre** (o siglas) y el **número de votos** obtenidos.

### 2. Reglas de cálculo
- **Barrera electoral del 3%**: antes de iniciar el reparto, se descartarán automáticamente todos aquellos partidos cuyos votos sean estrictamente inferiores al **3% del total de votos emitidos**:
  $$\text{Umbral mínimo} = \text{Votos totales emitidos} \times 0.03$$
- **Reparto de escaños (Ley D'Hondt)**:
  1. Con las candidaturas que igualen o superen el 3%, se dividen los votos obtenidos por cada partido entre $1, 2, 3, \dots, N$ (siendo $N$ el número de escaños a repartir).
  2. Se ordenan todos los cocientes resultantes de mayor a menor.
  3. Se asignan los $N$ escaños a los partidos propietarios de los $N$ cocientes más altos.
  4. **Desempate**: si dos cocientes son iguales, el escaño se asigna al partido con **más votos**, independientemente del orden de introducción. Solo si también empatan los votos se respeta el orden en que se introdujeron los partidos.
- **Validaciones básicas**:
  - No se admiten valores negativos ni un número de escaños igual a cero.
  - La suma de los votos de los partidos más los votos en blanco no debe superar el total de votos emitidos.

## Estructura Inicial del Proyecto

```text
calculadora-dhondt/
├── main.py              # Punto de entrada y captura de datos por consola
├── dhondt.py            # Lógica de filtrado (umbral 3%) y cálculo D'Hondt
├── tests/
│   └── test_dhondt.py   # Pruebas unitarias usando unittest (biblioteca estándar)
└── README.md            # Documentación del proyecto
```

## Ejecución

Clona o descarga el repositorio y ejecuta el archivo principal desde la terminal:

```bash
python3 main.py
```

### Ejemplo de flujo en consola

```text
--- Datos de la Circunscripción ---
Número de escaños a repartir: 5
Total de votos emitidos: 100000
Votos en blanco: 2000
Número de partidos: 4

Nombre del partido 1: Partido A
Votos de Partido A: 42000
Nombre del partido 2: Partido B
Votos de Partido B: 31000
Nombre del partido 3: Partido C
Votos de Partido C: 22500
Nombre del partido 4: Partido D
Votos de Partido D: 2500

--- Resultados ---
Umbral mínimo (3%): 3000 votos
Partidos excluidos (< 3%): Partido D (2500 votos)

Reparto de escaños:
- Partido A: 2 escaños
- Partido B: 2 escaños
- Partido C: 1 escaño
```

## Pruebas

Para ejecutar la batería de pruebas utilizando el módulo estándar `unittest`:

```bash
python3 -m unittest discover -s tests
```

