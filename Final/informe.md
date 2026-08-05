# Fiat-Shamir: de protocolo interactivo a firma no interactiva

**Trabajo Final — Programación Científica 2026-1**

Integrantes: Delgado Ortiz, David · Fonseca Aldana, Miguel Angel · Moreno Ceballos, Jose Daniel · Ospina Ocampo, Juan Diego · Urrutia Manyoma, Haison

---

## 1. ¿Por qué se eligió este tema?

Se seleccionó el esquema Fiat-Shamir por su conexión directa con la temática de protocolos de
seguridad, vista previamente en el curso de Criptografía y Seguridad (sección de firmas
digitales). Sin embargo, ese acercamiento fue puramente teórico: se estudió la construcción
matemática del protocolo, pero no se exploró su comportamiento práctico ni su costo real de
cómputo. Este trabajo busca precisamente cerrar esa brecha, abordando el esquema desde una
perspectiva experimental y cuantitativa — algo que encaja naturalmente con las herramientas de
Programación Científica, en particular con el método de Monte Carlo, que permite poner a prueba
de forma empírica una de las suposiciones teóricas centrales del protocolo: que la función hash
se comporta como un oráculo aleatorio.

## 2. ¿Por qué es interesante en la ciencia?

El protocolo de Fiat-Shamir permite a un **Prover** convencer a un **Verifier** de que conoce
un secreto $s$ sin revelarlo — la propiedad de **zero-knowledge**. Originalmente (protocolo de
Schnorr) es un proceso **interactivo** de tres pasos: compromiso $x = r^2 \bmod N$, reto
$e \in \{0,1\}$ elegido por el Verifier, y respuesta $y = r \cdot s^e \bmod N$.

En 1986, **Amos Fiat** y **Adi Shamir** propusieron reemplazar el reto aleatorio del Verifier
por $e = H(x)$, usando una función hash criptográfica. Esto elimina la necesidad de que ambas
partes estén conectadas al mismo tiempo: el Prover genera una prueba completa que puede
guardarse y ser verificada después por cualquiera, sin su participación — convirtiendo un
protocolo de identificación en un esquema de **firma digital**. La seguridad de esta
transformación depende de modelar el hash como un **oráculo aleatorio**: impredecible y no
manipulable por el Prover.

La seguridad del esquema descansa en dos garantías distintas: **zero-knowledge** (el Verifier
no aprende nada más que "el Prover conoce el secreto") y **soundness** (un Prover que no
conoce el secreto no puede hacer que el Verifier acepte la prueba, salvo con probabilidad
despreciable). Esta última se puede demostrar de forma concreta: si un impostor lograra
responder correctamente a ambos valores posibles de $e$ con el mismo compromiso, eso
equivaldría a poseer dos raíces cuadradas distintas de $v = s^2 \bmod N$, lo cual permite
factorizar $N = p \cdot q$ mediante $\gcd(s_1 - s_2, N)$ — un problema que se asume
computacionalmente inviable para $N$ grande. Como el impostor debe adivinar de antemano el
reto, su probabilidad de éxito en una ronda es $1/2$, y cae a $2^{-k}$ al repetir $k$ rondas
independientes.

_(agregar aquí: 2-3 líneas de contexto histórico adicional — de dónde surge el problema de
identificación segura, por qué era relevante en la época — smart cards, necesidad de
autenticación sin hardware especializado, etc.)_

## 3. Ejemplo aplicado

Implementamos el protocolo completo en Python (generación de parámetros, prover, reto vía
hash, verificación — ver notebook adjunto) y lo usamos para explorar dos preguntas cuantitativas:

**(A) Costo computacional.** Medimos cómo escala el tiempo de generación y verificación de una
prueba en función del tamaño de $N$ (256, 512, 1024, 2048 bits).

_(agregar: resultado + gráfica de tiempo vs. tamaño de N, 2-3 líneas de interpretación)_

**(B) Comportamiento estadístico del hash.** Mediante simulación Monte Carlo, generamos miles
de compromisos aleatorios y analizamos si los retos resultantes de $H(x)$ se distribuyen de
forma uniforme — condición necesaria para que el modelo de oráculo aleatorio sea válido y el
esquema sea seguro.

_(agregar: resultado + gráfica de distribución, 2-3 líneas de interpretación)_

## 4. Opinión del grupo

_(cada integrante: 2-3 líneas de opinión sobre el tema + autoevaluación del curso)_

- **David Delgado Ortiz:** _(pendiente)_
- **Miguel Angel Fonseca Aldana:** _(pendiente)_
- **Jose Daniel Moreno Ceballos:** _(pendiente)_
- **Juan Diego Ospina Ocampo:** _(pendiente)_
- **Haison Urrutia Manyoma:** _(pendiente)_
