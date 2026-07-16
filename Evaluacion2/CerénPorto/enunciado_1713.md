# Evaluación 2

**Programación Científica 2026-1 · Universidad Nacional de Colombia** — mbastidaso@unal.edu.co

**Modalidad:** individual · **Entrega:** GitHub (rama + Pull Request)

> ⚙️ **Enunciado personalizado — ID 1713.** Los parámetros son únicos. 

---

## Idea central

Este semestre aproximamos funciones como combinación de bases, $\hat f(t)=\sum_i c_i\phi_i(t)$. 

Una **red neuronal** hace lo mismo, pero **aprende** sus propias bases en vez de fijarlas.

En esta evaluación construimos una red que **reconstruye** una señal, y estudiamos qué pasa cuando su **primera capa es la Transformada de Fourier**. 

La pregunta que guía todo: *¿ayuda empezar con la base "correcta" (Fourier) en lugar de una base aleatoria?*

---

# Parte I — El fenómeno

## 1. Ondas que se dispersan

En un medio **sin dispersión** todas las frecuencias viajan igual y una onda mantiene su forma. En un medio **dispersivo**, distintas frecuencias viajan a distinta velocidad: es lo que separa los colores en un prisma, deforma un pulso en una fibra óptica, y hace que las olas largas lleguen antes que las cortas. Los datos vienen de un medio dispersivo.

## 2. La regla del medio

Una onda se compone de **modos**, cada uno con un número entero $k$ (su número de onda). La regla asigna a cada modo una **frecuencia** $\omega(k)$:

$$\omega(k) = \sqrt{c^2 k^2 + \mu^2}.$$

Esta información es dada: Si $\mu=0$ las frecuencias son bajas; si $\mu>0$, el término $\mu^2$ **empuja las frecuencias hacia arriba** (mayor $\mu$, oscilaciones más rápidas). El parámetro $\mu$ define **tres regímenes** (las etiquetas `y` de los datos): 0 = sin dispersión (frecuencias bajas), 1 = intermedia, 2 = fuerte (frecuencias altas).

## 3. Lo que medimos

Un sensor fijo registra la suma de los modos en el tiempo:

$$f(t) = \sum_j a_j \cos\bigl(\omega(k_j)\,t + \varphi_j\bigr).$$

**Cada señal es una suma de cosenos a frecuencias bien definidas**, justo lo que una base de senos y cosenos representa con pocos coeficientes. 

---

# Parte II — Los datos

Generar los datos con los 4 últimos dígitos del ID (script aparte) y cargarlos. 

El conjunto tiene **15 señales por régimen** (45 en total).

---

# Parte III — La red

Construir, **en JAX**, una red que recibe una señal $x\in\mathbb{R}^{256}$ y la **reconstruye** (su salida $\hat x$ debe parecerse a $x$). 

La red se entrena minimizando el error (media cuadrática) entre la señal original y la reconstruida:

$$\mathcal{L} = \tfrac1N\|\hat x - x\|^2$$

## La arquitectura

La red tiene dos capas. La **primera** es una capa lineal de tamaño $256 \to 2K$ (con **K = 20** frecuencias) seguida de una no linealidad $\tanh$; la **siguiente** es una capa lineal $2K \to 256$ que reconstruye la señal:

$$\hat x = W_2\,\tanh(W_1 x).$$

La idea central está en $W_1$. Sus pesos pueden **inicializarse como la matriz de Fourier**: las filas son $\sin(2\pi k t)$ y $\cos(2\pi k t)$, $k=1,\dots,20$ o de forma **aleatoria**. En ambos casos $W_1$ se sigue entrenando: lo único que cambia es el punto de partida.

## Lo que se espera

Este trabajo debe permitir responder, con evidencia propia, si conviene arrancar la red en la base de Fourier en lugar de una base aleatoria. Para ello:

- Construir la capa Fourier y verificar que, en su punto de partida, calcula efectivamente una transformada de Fourier de la señal.
- Entrenar la red con las **dos inicializaciones** (Fourier y aleatoria) sobre señales de los tres regímenes, durante **4000 iteraciones** (learning rate sugerido $\eta=0.1$), y estudiar la evolución de la pérdida (error) en cada caso.
- Prestar especial atención al **régimen 0** y a la **velocidad** con que cada inicialización mejora.
- Explorar cuánta información de la señal vive en pocos coeficientes de la capa Fourier (compresión, con referencia al **95%** de la energía).

Las gráficas y resultados concretos que se deben entregar están en la **rúbrica** (documento de instrucciones de la evaluación).


# Entrega por GitHub

1. Rama propia: `git checkout -b eval2-APELLIDOS`
2. Carpeta con los **apellidos** en la raíz del repositorio:
   ```
   PerezGomez/
   ├── solucion.ipynb        # el notebook resuelto
   ├── enunciado_1713.md   # el enunciado personalizado
   └── datos_1713.npz      # los datos
   ```
3. **Varios Commits semánticos** (`feat:`, `fix:`, `docs:`, `data:`) no un único commit final.
4. Abre un **Pull Request** con una descripicón corta del trabajo.

> 📊 ** Acumulativo.** Este curso se evalúa de forma acumulativa, siempre debemos dar especial énfasis en visualización científica: ejes con unidades, tipo de gráfico y mapa de color justificados, leyendas claras, figuras que comuniquen una idea. Una reconstrucción correcta en una figura pobre no recibe puntaje completo.

# Comentarios sobre la entrega:

### Capa Fourier (15 pts) - 10/15
- [5] La función que construye la capa Fourier (`matrixFourier(k)`, W1 con filas de senos y cosenos). Forma correcta `(2k, 256)`, filas intercaladas seno/coseno para cada `k=1..K`.
- [0] Evidencia de que, en su inicialización, la capa reproduce la transformada de Fourier de la señal (comparación con `np.fft`). **No está.** Solo se inspecciona el rango de amplitud de una fila (`np.min/np.max`, celda 24) y se explica conceptualmente por qué la matriz de Fourier "tiene sentido", pero nunca se compara numéricamente `W1@x` contra `np.fft.fft(x)`. No hay error relativo ni cuantitativo reportado para esta verificación.
- [5] **Reporta la energía media del dataset**: `round((X**2).mean(), 3)` → con los datos y parámetros de referencia dio `0.678`.

(**Comentario**: la construcción de $W_1$ es correcta y el reporte de energía está bien hecho, pero falta el paso central de "verificar contra `np.fft`" que pide explícitamente el enunciado.)

### Entrenamiento y reconstrucción (25 pts) - 7/25
- [2] **Gráfica:** señal original junto a su reconstrucción final, para una señal de cada régimen.
- [0] Red entrenada con las dos inicializaciones (Fourier y aleatoria).
- [5] Error de reconstrucción relativo `||x̂-x||/||x||` reportado para cada caso (celda 53), por régimen y por base.

(**Comentario**: Entrena una red por cada regimen no una red completa.)

### Comparación de inicializaciones (25 pts) — 12/25
- [3] **Gráfica:** curvas de la pérdida vs iteraciones con las dos inicializaciones superpuestas.
- [8] Medición de cuántas iteraciones necesita cada inicialización para que el error relativo < 0.1.
- [1] Análisis específico del régimen foco del enunciado del estudiante (**régimen 0**): 

(**Comentario**: La escala de la gráfica de pérdida (`semilogy` en vez de `loglog`), que es un detalle de visualización pedido explícitamente por la rúbrica.

### Compresión (10 pts) — 1/10
- [0] **Gráfica:** error de reconstrucción vs número de coeficientes conservados. **No existe.** No se grafica ni se calcula ningún error de reconstrucción en función de `m`.
- [1] El resultado impreso, `(0, 25)` no refleja ningún cálculo real: al recalcular correctamente con los datos y umbral de referencia, el rango real de coeficientes necesarios es **mínimo 4, máximo 15** .

(**Comentario**: la idea metodológica (ordenar energía descendente, usar `np.searchsorted` sobre la energía acumulada) es correcta y es la forma recomendada, pero la sección está incompleta y el único resultado numérico que se reporta es inválido por el choque de nombres `K`/`k`. 

