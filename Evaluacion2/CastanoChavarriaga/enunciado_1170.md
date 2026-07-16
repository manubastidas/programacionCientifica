# Evaluación 2

**Programación Científica 2026-1 · Universidad Nacional de Colombia** — mbastidaso@unal.edu.co

**Modalidad:** individual · **Entrega:** GitHub (rama + Pull Request)

> ⚙️ **Enunciado personalizado — ID 1170.** Los parámetros son únicos. 

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

El conjunto tiene **8 señales por régimen** (24 en total).

---

# Parte III — La red

Construir, **en JAX**, una red que recibe una señal $x\in\mathbb{R}^{256}$ y la **reconstruye** (su salida $\hat x$ debe parecerse a $x$). 

La red se entrena minimizando el error (media cuadrática) entre la señal original y la reconstruida:

$$\mathcal{L} = \tfrac1N\|\hat x - x\|^2$$

## La arquitectura

La red tiene dos capas. La **primera** es una capa lineal de tamaño $256 \to 2K$ (con **K = 15** frecuencias) seguida de una no linealidad $\tanh$; la **siguiente** es una capa lineal $2K \to 256$ que reconstruye la señal:

$$\hat x = W_2\,\tanh(W_1 x).$$

La idea central está en $W_1$. Sus pesos pueden **inicializarse como la matriz de Fourier**: las filas son $\sin(2\pi k t)$ y $\cos(2\pi k t)$, $k=1,\dots,15$ o de forma **aleatoria**. En ambos casos $W_1$ se sigue entrenando: lo único que cambia es el punto de partida.

## Lo que se espera

Este trabajo debe permitir responder, con evidencia propia, si conviene arrancar la red en la base de Fourier en lugar de una base aleatoria. Para ello:

- Construir la capa Fourier y verificar que, en su punto de partida, calcula efectivamente una transformada de Fourier de la señal.
- Entrenar la red con las **dos inicializaciones** (Fourier y aleatoria) sobre señales de los tres regímenes, durante **3000 iteraciones** (learning rate sugerido $\eta=0.05$), y estudiar la evolución de la pérdida (error) en cada caso.
- Prestar especial atención al **régimen 0** y a la **velocidad** con que cada inicialización mejora.
- Explorar cuánta información de la señal vive en pocos coeficientes de la capa Fourier (compresión, con referencia al **95%** de la energía).

Las gráficas y resultados concretos que se deben entregar están en la **rúbrica** (documento de instrucciones de la evaluación).


# Entrega por GitHub

1. Rama propia: `git checkout -b eval2-APELLIDOS`
2. Carpeta con los **apellidos** en la raíz del repositorio:
   ```
   PerezGomez/
   ├── solucion.ipynb        # el notebook resuelto, con las 3 respuestas
   ├── enunciado_1170.md   # el enunciado personalizado
   └── datos_1170.npz      # los datos
   ```
3. **Varios Commits semánticos** (`feat:`, `fix:`, `docs:`, `data:`) no un único commit final.
4. Abre un **Pull Request** con una descripicón corta del trabajo.

> 📊 ** Acumulativo.** Este curso se evalúa de forma acumulativa, siempre debemos dar especial énfasis en visualización científica: ejes con unidades, tipo de gráfico y mapa de color justificados, leyendas claras, figuras que comuniquen una idea. Una reconstrucción correcta en una figura pobre no recibe puntaje completo.


# Comentarios sobre la entrega: 

### Capa Fourier (15 pts)
- [5] La función que construye la capa Fourier ($W_1$ con filas de senos y cosenos).
- [5] Evidencia de que, en su inicialización, la capa reproduce la transformada de Fourier de la señal (comparación con `np.fft`).
- [5] **Reporta la energía media del dataset** (`(X**2).mean()`, con 3 decimales).

### Entrenamiento y reconstrucción (25 pts)
- [5] **Gráfica:** la señal original junto a su reconstrucción final, para una señal de cada régimen.
- [5] Red entrenada con las dos inicializaciones (Fourier y aleatoria), con los parámetros del enunciado.
- [5] Error de reconstrucción relativo $\|\hat x - x\|/\|x\|$ reportado para cada caso.

(**Comentario**: Las gráficas son mejores sobrepuestas. Se entrena una red por cáda régimen (esto no está en las instrucciones). Además, hay varias semillas todas diferentes y se esperaba una semilla siempre para todo el trabajo. 

### Comparación de inicializaciones (25 pts)
- [10] **Gráfica:** curvas de la pérdida $\mathcal{L}$ vs iteraciones, con las dos inicializaciones superpuestas en la misma figura.
- [0] Medición de **cuántas iteraciones** necesita cada inicialización para que el **error relativo** 0.1.
- [5] **Gráfica/análisis del régimen indicado:** contrastar velocidad de convergencia para el régimen que indica el enunciado.

(**Comentario**: Las graficas son mejores en loglog. Se usa un optimizador mejor que el esperado en las instrucciones. No hay medida de iteraciones para el error relativo <0.1)

### Compresión (10 pts)
- [5] **Gráfica:** error de reconstrucción vs número de coeficientes conservados.
- [5] Cuántos coeficientes bastan para lograr umbral de energía del enunciado.

(**Comentario**: Hay muchas más cosas de las que se pidieron en la práctica entonces es difícil poder analizar lo que realmente estabamos evaluando)