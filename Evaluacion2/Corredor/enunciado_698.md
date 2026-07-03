# Evaluaci?n 2

**Programaci?n Cient?fica 2026-1 ? Universidad Nacional de Colombia** ? mbastidaso@unal.edu.co

**Modalidad:** individual ? **Entrega:** GitHub (rama + Pull Request)

> ?? **Enunciado personalizado ? ID 698.** Los par?metros son ?nicos. 

---

## Idea central

Este semestre aproximamos funciones como combinaci?n de bases, $\hat f(t)=\sum_i c_i\phi_i(t)$. 

Una **red neuronal** hace lo mismo, pero **aprende** sus propias bases en vez de fijarlas.

En esta evaluaci?n construimos una red que **reconstruye** una se?al, y estudiamos qu? pasa cuando su **primera capa es la Transformada de Fourier**. 

La pregunta que gu?a todo: *?ayuda empezar con la base "correcta" (Fourier) en lugar de una base aleatoria?*

---

# Parte I ? El fen?meno

## 1. Ondas que se dispersan

En un medio **sin dispersi?n** todas las frecuencias viajan igual y una onda mantiene su forma. En un medio **dispersivo**, distintas frecuencias viajan a distinta velocidad: es lo que separa los colores en un prisma, deforma un pulso en una fibra ?ptica, y hace que las olas largas lleguen antes que las cortas. Los datos vienen de un medio dispersivo.

## 2. La regla del medio

Una onda se compone de **modos**, cada uno con un n?mero entero $k$ (su n?mero de onda). La regla asigna a cada modo una **frecuencia** $\omega(k)$:

$$\omega(k) = \sqrt{c^2 k^2 + \mu^2}.$$

Esta informaci?n es dada: Si $\mu=0$ las frecuencias son bajas; si $\mu>0$, el t?rmino $\mu^2$ **empuja las frecuencias hacia arriba** (mayor $\mu$, oscilaciones m?s r?pidas). El par?metro $\mu$ define **tres reg?menes** (las etiquetas `y` de los datos): 0 = sin dispersi?n (frecuencias bajas), 1 = intermedia, 2 = fuerte (frecuencias altas).

## 3. Lo que medimos

Un sensor fijo registra la suma de los modos en el tiempo:

$$f(t) = \sum_j a_j \cos\bigl(\omega(k_j)\,t + \varphi_j\bigr).$$

**Cada se?al es una suma de cosenos a frecuencias bien definidas**, justo lo que una base de senos y cosenos representa con pocos coeficientes. 

---

# Parte II ? Los datos

Generar los datos con los 4 ?ltimos d?gitos del ID (script aparte) y cargarlos. 

El conjunto tiene **10 se?ales por r?gimen** (30 en total).

---

# Parte III ? La red

Construir, **en JAX**, una red que recibe una se?al $x\in\mathbb{R}^{256}$ y la **reconstruye** (su salida $\hat x$ debe parecerse a $x$). 

La red se entrena minimizando el error (media cuadr?tica) entre la se?al original y la reconstruida:

$$\mathcal{L} = \tfrac1N\|\hat x - x\|^2$$

## La arquitectura

La red tiene dos capas. La **primera** es una capa lineal de tama?o $256 \to 2K$ (con **K = 15** frecuencias) seguida de una no linealidad $\tanh$; la **siguiente** es una capa lineal $2K \to 256$ que reconstruye la se?al:

$$\hat x = W_2\,\tanh(W_1 x).$$

La idea central est? en $W_1$. Sus pesos pueden **inicializarse como la matriz de Fourier**: las filas son $\sin(2\pi k t)$ y $\cos(2\pi k t)$, $k=1,\dots,15$ o de forma **aleatoria**. En ambos casos $W_1$ se sigue entrenando: lo ?nico que cambia es el punto de partida.

## Lo que se espera

Este trabajo debe permitir responder, con evidencia propia, si conviene arrancar la red en la base de Fourier en lugar de una base aleatoria. Para ello:

- Construir la capa Fourier y verificar que, en su punto de partida, calcula efectivamente una transformada de Fourier de la se?al.
- Entrenar la red con las **dos inicializaciones** (Fourier y aleatoria) sobre se?ales de los tres reg?menes, durante **4000 iteraciones** (learning rate sugerido $\eta=0.05$), y estudiar la evoluci?n de la p?rdida (error) en cada caso.
- Prestar especial atenci?n al **r?gimen 2** y a la **velocidad** con que cada inicializaci?n mejora.
- Explorar cu?nta informaci?n de la se?al vive en pocos coeficientes de la capa Fourier (compresi?n, con referencia al **85%** de la energ?a).

Las gr?ficas y resultados concretos que se deben entregar est?n en la **r?brica** (documento de instrucciones de la evaluaci?n).


# Entrega por GitHub

1. Rama propia: `git checkout -b eval2-APELLIDOS`
2. Carpeta con los **apellidos** en la ra?z del repositorio:
   ```
   PerezGomez/
   ??? solucion.ipynb        # el notebook resuelto, con las 3 respuestas
   ??? enunciado_698.md   # el enunciado personalizado
   ??? datos_698.npz      # los datos
   ```
3. **Varios Commits sem?nticos** (`feat:`, `fix:`, `docs:`, `data:`) no un ?nico commit final.
4. Abre un **Pull Request** con una descripic?n corta del trabajo.

> ?? ** Acumulativo.** Este curso se eval?a de forma acumulativa, siempre debemos dar especial ?nfasis en visualizaci?n cient?fica: ejes con unidades, tipo de gr?fico y mapa de color justificados, leyendas claras, figuras que comuniquen una idea. Una reconstrucci?n correcta en una figura pobre no recibe puntaje completo.
