"""
generar_enunciado.py — Evaluación, Programación Científica 2026-1 (UNAL)

Genera el ENUNCIADO personalizado de cada estudiante a partir de su ID.
Los parámetros numéricos son únicos por ID

    python generar_enunciado.py 4815      # <- últimos 4 dígitos de su ID

Produce enunciado_XXXX.md.  (Los datos se generan aparte con generar_datos.py.)
"""
import sys
import numpy as np


def parametros(seed):
    r = np.random.default_rng(seed + 10_000)
    return dict(
        n=int(r.choice([8, 10, 12, 15])),        # señales por régimen
        K=int(r.choice([15, 20, 25, 30])),       # nº de frecuencias de la capa Fourier
        n_iter=int(r.choice([2000, 3000, 4000])),# iteraciones de entrenamiento
        eta=float(r.choice([0.02, 0.05, 0.1])),  # learning rate sugerido
        foco=int(r.choice([0, 1, 2])),           # régimen a analizar en detalle
        energia=int(r.choice([85, 90, 95])),     # umbral de compresión (%)
    )


def enunciado_md(seed, p):
    return f"""# Evaluación 2

**Programación Científica 2026-1 · Universidad Nacional de Colombia** — mbastidaso@unal.edu.co

**Modalidad:** individual · **Entrega:** GitHub (rama + Pull Request)

> ⚙️ **Enunciado personalizado — ID {seed}.** Los parámetros son únicos. 

---

## Idea central

Este semestre aproximamos funciones como combinación de bases, $\\hat f(t)=\\sum_i c_i\\phi_i(t)$. 

Una **red neuronal** hace lo mismo, pero **aprende** sus propias bases en vez de fijarlas.

En esta evaluación construimos una red que **reconstruye** una señal, y estudiamos qué pasa cuando su **primera capa es la Transformada de Fourier**. 

La pregunta que guía todo: *¿ayuda empezar con la base "correcta" (Fourier) en lugar de una base aleatoria?*

---

# Parte I — El fenómeno

## 1. Ondas que se dispersan

En un medio **sin dispersión** todas las frecuencias viajan igual y una onda mantiene su forma. En un medio **dispersivo**, distintas frecuencias viajan a distinta velocidad: es lo que separa los colores en un prisma, deforma un pulso en una fibra óptica, y hace que las olas largas lleguen antes que las cortas. Los datos vienen de un medio dispersivo.

## 2. La regla del medio

Una onda se compone de **modos**, cada uno con un número entero $k$ (su número de onda). La regla asigna a cada modo una **frecuencia** $\\omega(k)$:

$$\\omega(k) = \\sqrt{{c^2 k^2 + \\mu^2}}.$$

Esta información es dada: Si $\\mu=0$ las frecuencias son bajas; si $\\mu>0$, el término $\\mu^2$ **empuja las frecuencias hacia arriba** (mayor $\\mu$, oscilaciones más rápidas). El parámetro $\\mu$ define **tres regímenes** (las etiquetas `y` de los datos): 0 = sin dispersión (frecuencias bajas), 1 = intermedia, 2 = fuerte (frecuencias altas).

## 3. Lo que medimos

Un sensor fijo registra la suma de los modos en el tiempo:

$$f(t) = \\sum_j a_j \\cos\\bigl(\\omega(k_j)\\,t + \\varphi_j\\bigr).$$

**Cada señal es una suma de cosenos a frecuencias bien definidas**, justo lo que una base de senos y cosenos representa con pocos coeficientes. 

---

# Parte II — Los datos

Generar los datos con los 4 últimos dígitos del ID (script aparte) y cargarlos. 

El conjunto tiene **{p['n']} señales por régimen** ({3*p['n']} en total).

---

# Parte III — La red

Construir, **en JAX**, una red que recibe una señal $x\\in\\mathbb{{R}}^{{256}}$ y la **reconstruye** (su salida $\\hat x$ debe parecerse a $x$). 

La red se entrena minimizando el error (media cuadrática) entre la señal original y la reconstruida:

$$\\mathcal{{L}} = \\tfrac1N\\|\\hat x - x\\|^2$$

## La arquitectura

La red tiene dos capas. La **primera** es una capa lineal de tamaño $256 \\to 2K$ (con **K = {p['K']}** frecuencias) seguida de una no linealidad $\\tanh$; la **siguiente** es una capa lineal $2K \\to 256$ que reconstruye la señal:

$$\\hat x = W_2\\,\\tanh(W_1 x).$$

La idea central está en $W_1$. Sus pesos pueden **inicializarse como la matriz de Fourier**: las filas son $\\sin(2\\pi k t)$ y $\\cos(2\\pi k t)$, $k=1,\\dots,{p['K']}$ o de forma **aleatoria**. En ambos casos $W_1$ se sigue entrenando: lo único que cambia es el punto de partida.

## Lo que se espera

Este trabajo debe permitir responder, con evidencia propia, si conviene arrancar la red en la base de Fourier en lugar de una base aleatoria. Para ello:

- Construir la capa Fourier y verificar que, en su punto de partida, calcula efectivamente una transformada de Fourier de la señal.
- Entrenar la red con las **dos inicializaciones** (Fourier y aleatoria) sobre señales de los tres regímenes, durante **{p['n_iter']} iteraciones** (learning rate sugerido $\\eta={p['eta']}$), y estudiar la evolución de la pérdida (error) en cada caso.
- Prestar especial atención al **régimen {p['foco']}** y a la **velocidad** con que cada inicialización mejora.
- Explorar cuánta información de la señal vive en pocos coeficientes de la capa Fourier (compresión, con referencia al **{p['energia']}%** de la energía).

Las gráficas y resultados concretos que se deben entregar están en la **rúbrica** (documento de instrucciones de la evaluación).


# Entrega por GitHub

1. Rama propia: `git checkout -b eval2-APELLIDOS`
2. Carpeta con los **apellidos** en la raíz del repositorio:
   ```
   PerezGomez/
   ├── solucion.ipynb        # el notebook resuelto
   ├── enunciado_{seed}.md   # el enunciado personalizado
   └── datos_{seed}.npz      # los datos
   ```
3. **Varios Commits semánticos** (`feat:`, `fix:`, `docs:`, `data:`) no un único commit final.
4. Abre un **Pull Request** con una descripicón corta del trabajo.

> 📊 ** Acumulativo.** Este curso se evalúa de forma acumulativa, siempre debemos dar especial énfasis en visualización científica: ejes con unidades, tipo de gráfico y mapa de color justificados, leyendas claras, figuras que comuniquen una idea. Una reconstrucción correcta en una figura pobre no recibe puntaje completo.
"""


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Uso: python generar_enunciado.py XXXX   (últimos 4 dígitos de su cédula)")
        sys.exit(1)
    seed = int(sys.argv[1])
    p = parametros(seed)
    with open(f"enunciado_{seed}.md", "w", encoding="utf-8") as f:
        f.write(enunciado_md(seed, p))
    print(f"Enunciado generado para cédula {seed}: enunciado_{seed}.md")
    print(f"Los parámetros: K={p['K']}, iteraciones={p['n_iter']}, η={p['eta']}, "
          f"n={p['n']}/régimen, régimen foco={p['foco']}, compresión {p['energia']}%")
