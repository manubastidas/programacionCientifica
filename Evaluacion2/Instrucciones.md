# Evaluación #2 -- Instrucciones

**Programación Científica 2026-1**

**Universidad Nacional de Colombia, sede Medellín**

mbastidaso@unal.edu.co

**Modalidad:** individual · **Fecha límite:** Lunes 13 de julio, 23:59

---

## Cómo empezar

La evaluación es **personalizada**: los parámetros y las preguntas dependen de los números de documento de identidad (ID). 

### Paso 1 — Descargas los generadores

Descargas `generar_enunciado.py` y `generar_datos.py` del repositorio del curso.

### Paso 2 — Genera la tarea

Ejecuta **ambos** con los últimos 4 dígitos del ID:

```bash
python generar_enunciado.py 4815      # <- reemplaza 4815
python generar_datos.py 4815
```

Esto crea:

- **`enunciado_XXXX.md`** — un enunciado completo y personalizado. Contiene la física y los parámetros de las preguntas. **Leer: es la evaluación.**

- **`datos_XXXX.npz`** — las señales, únicas.

### Paso 3 — Resuelve

Sigue el `enunciado_XXXX.md` y desarrolla la solución en **un notebook** `.ipynb`. 

---

## Qué entregas

Un solo notebook `.ipynb` resuelto, más los dos archivos generados, en la carpeta de GitHub:

```
Apellidos/
├── solucion.ipynb        # el notebook resuelto, con las 3 respuestas
├── enunciado_XXXX.md     # el enunciado personalizado (generado)
└── datos_XXXX.npz        # los datos (generados)
```


### Pasos de entrega

1. Rama propia: `git checkout -b eval2-Apellidos`
2. Crear la carpeta "apellidos" en Evaluacion2 e incluir los tres archivos.
3. Usar **commits semánticos** (`feat:`, `fix:`, `docs:`, `data:`) a lo largo del trabajo.
4. Abre un **Pull Request** hacia la rama principal con un resumen del trabajo.

---

## Rúbrica de evaluación (100 pts)

El notebook debe contener, como mínimo, los siguientes entregables. Las gráficas deben cumplir los principios de visualización científica.

### Capa Fourier (15 pts)
- [ ] La función que construye la capa Fourier ($W_1$ con filas de senos y cosenos).
- [ ] Evidencia de que, en su inicialización, la capa reproduce la transformada de Fourier de la señal (comparación con `np.fft`).
- [ ] **Reporta la energía media del dataset** (`(X**2).mean()`, con 3 decimales).

### Entrenamiento y reconstrucción (25 pts)
- [ ] **Gráfica:** la señal original junto a su reconstrucción final, para una señal de cada régimen.
- [ ] Red entrenada con las dos inicializaciones (Fourier y aleatoria), con los parámetros del enunciado.
- [ ] Error de reconstrucción relativo $\|\hat x - x\|/\|x\|$ reportado para cada caso.

### Comparación de inicializaciones (25 pts)
- [ ] **Gráfica:** curvas de la pérdida $\mathcal{L}$ vs iteraciones, con las dos inicializaciones superpuestas en la misma figura.
- [ ] Medición de **cuántas iteraciones** necesita cada inicialización para bajar de error relativo 0.1.
- [ ] **Gráfica/análisis del régimen difícil:** el mismo contraste para el régimen que te indica el enunciado, con la diferencia de velocidad de convergencia.

### Compresión (10 pts)
- [ ] **Gráfica:** error de reconstrucción vs número de coeficientes conservados.
- [ ] Cuántos coeficientes bastan para el umbral de energía del enunciado.

### GitHub (10 pts)
- [ ] Rama, carpeta con apellidos (con `.ipynb`, `enunciado_XXXX.md`, `datos_XXXX.npz`), commits y PR.

### Sesión presencial de revisión (15 pts)
- [ ] El viernes 10 de Julio en horario de clase, la profesora hará aleatoriamente una revisión rápida de PRs.

> Como cada quien tiene parámetros y datos únicos, los resultados no son transferibles: una entrega que no corresponda al ID será evidente.

---

## Reglas

- **Es individual.** El enunciado y los datos son únicos.
- **Todos los números y figuras** deben salir de *los* datos particulares.
- **Visualización (acumulativo).** El curso se evalúa de forma acumulativa, con énfasis en visualización científica. Una reconstrucción correcta presentada en una figura pobre no recibe puntaje completo.

---

## Resumen del flujo

```
generar_enunciado.py + generar_datos.py  +  cédula
        │
        ├─►  enunciado_XXXX.md    (evaluación)
        └─►  datos_XXXX.npz       (señales)
                │
                ▼
        resolver en  solucion.ipynb
                │
                ▼
        entregar la carpeta Apellidos/ por Pull Request
```
