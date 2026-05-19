# Exposiciones de Visualización Científica

**Programación Científica 2026-1**

Universidad Nacional de Colombia, Medellín 

Manuela Bastidas Olivares

mbastidaso@unal.edu.co  

---

## Formato de trabajo

El trabajo se realiza en **grupos de tres**. No se aceptan entregas individuales.

**Objetivo:** identificar, analizar y corregir una visualización de datos aplicando los principios de diseño y comunicación vistos en clase.

---

## El problema a resolver

Cada pareja elige un conjunto de datos o problema para construir una comparación **Antes → Después**. Las fuentes posibles son:

1. **Problemas físicos** — algunos ejemplos al final de este documento.
2. **Datasets locales** — archivos disponibles en `evaluacion/data` del repositorio.
3. **Ejemplos externos** — un caso real o técnico publicado.

---

## Entrega del informe (PDF)

Subir a la carpeta `Visualizacion/evaluacion/entregas` en la rama `entregaVisualizacion` del repositorio. El documento es de **una sola página** con el siguiente contenido:

| | Descripción |
|---|---|
| **Figura "Original"** | Gráfica con problemas de escala, color, saturación, etiquetas faltantes u otros errores de contexto vistos en el curso. |
| **Figura "Corregida"** | Versión mejorada con **al menos 4 correcciones visibles** (cambio de colormap, ajuste de fuentes, eliminación de redundancias, anotaciones semánticas, etc.). |

<br>

> 🗓️ **Fecha límite: viernes 15 de mayo, 10:00 AM**
>
> El nombre del archivo sigue el orden **alfabético de apellidos** de los integrantes.  
> Ejemplo: si los integrantes son Julián Bastidas y Sergio Arango → `ArangoBastidas.pdf`

---

## Sustentación en clase

El viernes, en el horario habitual, cada pareja presenta en **2–3 minutos**:

- Describir brevemente el problema físico o estadístico y el origen de los datos.
- Comentar las dos gráficas: resaltar las correcciones realizadas y su justificación técnica basada en la teoría del curso.

---

## Calificación

| Componente | Peso | Criterio |
|---|---|---|
| **Profesora** | 70 % | Rigor técnico, correcciones de estilo y calidad de la sustentación. |
| **Co-evaluación** | 30 % | Asignada por un panel de jurados aleatorios. |


<br>
---

---
## Algunos problemas interesantes: 

### 1. Ecuación de Laplace

$$\nabla^2 u = 0$$

Condiciones de frontera: $u=0$ en tres lados, $u=\sin(\pi x/L)$ en el techo.

Solución exacta:

$$u(x,y) = \frac{\sinh(\pi y/L)}{\sinh(\pi)}\sin\!\left(\frac{\pi x}{L}\right)$$

Modela temperatura estacionaria, potencial electrostático, flujo potencial.


### 2. Membrana vibrante: modos normales

$$u_{mn}(x,y,t) = \sin\!\left(\frac{m\pi x}{L}\right)\sin\!\left(\frac{n\pi y}{L}\right)\cos(\omega_{mn}t)$$

Los **nodos** (líneas donde $u=0$ para todo $t$) son las líneas donde $\sin(m\pi x/L)=0$ o $\sin(n\pi y/L)=0$.
Los **antinodos** oscilan entre $\pm 1$.

### 3. Flujo potencial alrededor de un cilindro

$$\psi(r,\theta) = U_\infty\!\left(r - \frac{R^2}{r}\right)\sin\theta$$

El coeficiente de presión por la ecuación de Bernoulli:
$$C_p = 1 - \frac{|\mathbf{u}|^2}{U_\infty^2}$$

### 4. Dipolo eléctrico

$$V(x,y) = \frac{kq}{r_+} - \frac{kq}{r_-}, \qquad \mathbf{E} = -\nabla V$$

Las equipotenciales ($V=\text{cte}$) son perpendiculares a las líneas de campo.

### 5. Onda estacionaria 2D

$$u(x,y,t) = \cos(k_x x)\cos(k_y y)\cos(\omega t)$$

Los nodos (donde $u=0$ para todo $t$) son las líneas donde $\cos(k_x x)=0$ o $\cos(k_y y)=0$: una reticulación fija.

### 6. Celda de convección (Rayleigh-Bénard)

Flujo de Stokes en una celda de convección:

$$\psi = \sin(\pi x/L)\sin(\pi y/L), \qquad T = \cos(\pi x/L)\sin(\pi y/L)$$

### 7. Potencial gravitacional de $N$ cuerpos

$$\Phi(x,y) = -G\sum_{i=1}^{N}\frac{m_i}{r_i}$$

Los pozos gravitacionales (mínimos de $\Phi$) son zonas de atracción. El campo $\mathbf{g} = -\nabla\Phi$ apunta hacia las masas.

### 8. Vórtice de Lamb-Oseen

Solución exacta de Navier-Stokes para un vórtice axisimétrico:

$$\omega(r) = \frac{\Gamma}{\pi r_c^2}e^{-r^2/r_c^2}, \qquad
u_\theta(r) = \frac{\Gamma}{2\pi r}\left(1 - e^{-r^2/r_c^2}\right)$$

### 9. Difusión 2D: impulso gaussiano

$$u(x,y,t) = \frac{1}{4\pi\alpha t}\exp\!\left(-\frac{x^2+y^2}{4\alpha t}\right)$$

El flujo difusivo $\mathbf{J} = -\alpha\nabla u$ se aleja del máximo y la anchura crece como $\sigma = \sqrt{2\alpha t}$.

### 10. Campo magnético: espira circular (Biot-Savart)

$$d\mathbf{B} = \frac{\mu_0 I}{4\pi}\frac{d\boldsymbol{\ell}\times\hat{r}}{r^2}$$

Integramos sobre $N$ segmentos de la espira en $z=h$ y observamos el campo en el plano $z=0$.

### 11. Considere el siguiente campo escalar generado con la función de Himmelblau, definida como:

$$g(x,y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2$$

### 12. Temperatura superficial del mar (SST)

Considere un campo de **temperatura superficial del mar (SST)** sintético que simula:
- una corriente cálida de oeste a este en el ecuador,
- enfriamiento hacia los polos,
- giros oceánicos de mesoescala,
- ruido de pequeña escala (turbulencia).

### 13. Conjuntos de datos locales (Carpeta `evaluacion/data`)
Si prefieren trabajar con datos tabulares del mundo real o estadísticos, pueden elegir uno de los siguientes archivos CSV disponibles en el repositorio del curso:

* **`benchmark_sorting.csv`**: Tiempos de ejecución y rendimiento de diferentes algoritmos de ordenamiento (Ciencias de la Computación).
* **`calificaciones_curso.csv`**: Distribución estadística de notas de estudiantes.
* **`dengue_colombia.csv`**: Series de tiempo espaciales sobre casos epidemiológicos (Salud Pública).
* **`espectro_clorofila.csv`**: Datos de absorción de luz en función de la longitud de onda (Física/Biología).
* **`pib_latam.csv`**: Indicadores económicos e históricos de Latinoamérica (Economía).
* **`sistema_solar.csv`**: Parámetros planetarios como masas, distancias y periodos orbitales (Astronomía).

<br>

<br>

> ⚠️ **Nota importante sobre el rigor en las gráficas:** > Para los casos estadísticos o económicos 
(como las calificaciones, los algoritmos o el PIB), **las gráficas deben mantener un estricto rigor científico**. 
Esto implica que no basta con hacer un simple "gráfico de barras decorativo". Deben aplicar la teoría del curso: usar escalas adecuadas,
etiquetar correctamente los ejes con unidades, utilizar mapas de color con función semántica, manejar correctamente los datos atípicos (outliers) 
y eliminar todo elemento visual redundante. La gráfica debe tener peso analítico.
