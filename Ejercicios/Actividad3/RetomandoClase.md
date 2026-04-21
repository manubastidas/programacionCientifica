# Taller: SSH · Git · Colab · Python
### Programación Científica 2026-1 · Universidad Nacional de Colombia
**Trabajo en parejas · 1.5 horas**

---

## Antes de empezar

Formen las parejas. Decidan desde qué computador van a trabajar juntos. Todo el taller se hace desde **una sola máquina por pareja**.

A lo largo del taller usarán `nombre1_nombre2` como identificador — reemplácenlo siempre por sus nombres reales en minúsculas sin tildes, separados por guión bajo. 
Ejemplo: `ana_luis`.

---

## Bloque 1 — Conexión SSH al servidor `(10 min)`

Abran una terminal. En Windows usen PowerShell.

```bash
ssh estudiante@IP_SERVIDOR
```

Una vez conectados, corran estos comandos y **dejen la terminal visible** — van a necesitar la salida más adelante:

```bash
whoami
hostname
date
pwd
```

Noten que están en un servidor Linux remoto. Exploren brevemente:

```bash
ls 
cat compartido/taller.ipynb
```

El archivo `taller.ipynb` es de solo lectura. No pueden modificarlo ni ejecutarlo aquí.

---

## Bloque 2 — Trabajar en el servidor `(20 min)`

### 2.1 Crear su carpeta y copiar el archivo

```bash
mkdir ~/nombre1_nombre2
cp /compartido/taller.ipynb ~/nombre1_nombre2/nombre1_nombre2.ipynb
cd ~/nombre1_nombre2
ls -lh
```

### 2.2 Abrir el notebook con vi

```bash
vi nombre1_nombre2.ipynb
```

El archivo es JSON. Busquen las celdas de tipo `"source"` — ahí está el contenido.

Comandos básicos de vi:

| Acción | Comando |
|--------|---------|
| Entrar en modo edición | `i` |
| Salir del modo edición | `Esc` |
| Guardar y salir | `Esc` → `:wq` → `Enter` |
| Salir sin guardar | `Esc` → `:q!` → `Enter` |
| Buscar texto | `Esc` → `/texto` → `Enter` |
| Siguiente resultado | `n` |

Deben hacer **dos modificaciones**. Guarden con `Esc → :wq → Enter` al terminar.

---

### Modificación 1 — Celda de identidad

Agreguen una nueva celda de tipo `markdown` al inicio del notebook (después de la primera celda de título) con el siguiente contenido, llenando sus datos reales:

```
## Quiénes somos y desde dónde

- **Nombres:** nombre1 nombre 2
- **Fecha y hora:** (salida de date)
```

---

### Modificación 2 — Celda de descripción del código

Agreguen otra celda `markdown` justo después del código con una descripción breve del código.
Deben responder en sus propias palabras: ¿Qué hace este código?

---

## Bloque 3 — GitHub desde el servidor `(15 min)`

### 3.1 Clonar el repositorio del curso

Clonen el repositorio **dentro de su propia carpeta**:

```bash
cd ~/nombre1_nombre2
git clone https://github.com/manubastidas/programacionCientifica.git
cd programacionCientifica
```

### 3.2 Configurar su identidad git (local, solo para este repo)

Como todos comparten el mismo usuario del servidor, configuren su identidad **localmente** — aplica solo a su clon y no afecta a las demás parejas:

```bash
git config user.name "Nombre"
git config user.email "correo@unal.edu.co"
```

Verifiquen:

```bash
git config user.name
git config user.email
```

Cuando pida credenciales:
- **Username:** su usuario de GitHub
- **Password:** su token de GitHub (ver abajo cómo crearlo)

> **Crear token:** GitHub → foto de perfil → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)** → marcar `repo` → **Generate token**. Copien el token antes de cerrar la página, no se vuelve a mostrar.


### 3.3 Moverse a su rama

Cada pareja tiene una rama ya creada (y al orden del día) con su nombre (alguno de los dos):

```bash
git fetch origin
git checkout BRANCH
git status
```

### 3.4 Copiar el notebook y hacer push

```bash
cp ~/nombre1_nombre2/nombre1_nombre2.ipynb .
git add nombre1_nombre2.ipynb
git status
git commit -m " Escribir lo que hicimos "
git push origin BRANCH
```

---

## Bloque 4 — Google Colab `(15 min)`

### 4.1 Abrir su notebook desde GitHub

En el navegador:

```
https://colab.research.google.com/github/.../nombre1_nombre2/nombre1_nombre2.ipynb
```

### 4.2 Parámetros únicos

En la celda de parámetros cambien los valores para que su curva sea **distinta a la de todas las demás parejas**. Coordinen con los grupos cercanos si es necesario.

| Parámetro | Qué controla | Valores sugeridos |
|-----------|-------------|-------------------|
| `a` | frecuencia en x | 1 – 7 |
| `b` | frecuencia en y | 1 – 7 |
| `delta` | desfase | `np.pi/6`, `np.pi/4`, `np.pi/3`, `np.pi/2` |
| `COLOR` | color de la curva | cualquier hex, ej `"#06d6a0"` |
| `FONDO` | color de fondo | `"#0d1117"`, `"#ffffff"`, `"#1a1a2e"` |
| `GROSOR` | grosor de línea | 0.8 – 3.0 |
| `ALPHA` | transparencia | 0.4 – 1.0 |

> **Regla:** ninguna pareja puede tener la misma combinación de `a`, `b` y `delta`.

### 4.3 Ejecutar el notebook

Corran todas las celdas en orden: `Runtime → Run all`.

Verifiquen que:
- La celda de identidad muestra sus datos del servidor
- La celda de descripción está escrita por ustedes
- La curva tiene sus parámetros únicos

### 4.3 Cambiar el nombre del archivo de salida

En la última celda, cambien:

```python
NOMBRE_ARCHIVO = "nombre1_nombre2"   # ← su nombre real
```

Corran esa celda. Esto genera `nombre1_nombre2.jpg` y lo descarga automáticamente.

### 4.4 Subir la imagen directamente a main en GitHub

- Add file → Upload files
- Suben nombre1_nombre2.jpg
- Seleccionan Create a new branch y la nombran plot-nombre1_nombre2
- Clic en Propose changes → abre el PR automáticamente
- Crean el PR hacia main

---

## Criterios de verificación

Al finalizar, la pareja debe poder mostrar:

| # | Evidencia | Cómo verificar |
|---|-----------|----------------|
| 1 | Carpeta creada en el servidor | `ls ~/nombre1_nombre2/` |
| 2 | Celda de identidad con datos reales del servidor | visible en Colab |
| 3 | Descripción escrita por la pareja | visible en Colab |
| 4 | Parámetros modificados, curva única | visible en la figura |
| 5 | Commit en su rama con mensaje semántico | `git log` en el servidor |
| 6 | PR abierto con la imagen | visible en GitHub |

---

*Programación Científica 2026-1 · Universidad Nacional de Colombia · mbastidaso@unal.edu.co*
