# Curso de Programación Científica

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-Optimized-F9AB00?logo=googlecolab&logoColor=white)
![Git](https://img.shields.io/badge/Git-Workflow-orange?logo=git&logoColor=white)

Bienvenido al monorepositorio del curso. Este espacio centraliza los proyectos colaborativos. Utilizamos un flujo de trabajo basado en GitHub y Google Colab para la ejecución de código.

---

## 🔐 Acceso al Repositorio

Trabajaremos directamente sobre este repositorio como un equipo. **Debes enviar a por el chat del curso tu nombre de usuario de GitHub para agregarte como colaborador oficial del curso.** 

---

## Estructura del Repositorio

El directorio está organizado para soportar el trabajo simultáneo de todos los estudiantes:

* `Ejercicios/`: Ejercicios de clase y actividades varias.
* `Entregas/`: Proyectos del curso (en equipos).

---

## Flujo de Trabajo Principal

Ejecutamos el código en Google Colab y almacenamos el progreso en GitHub. Aplica estos pasos para cada tarea:

1. **Crea tu espacio (Rama/Branch):** Nunca trabajes directamente en `main`. Antes de iniciar, ve a GitHub y crea una nueva rama con tu nombre o el de tu equipo si es el caso (ej. `rama-juan-perez`).
2. **Ejecuta en Colab:** Abre los notebooks del curso directamente en tu navegador usando el botón que encontrarás en la parte superior de los archivos:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/)
3. **Guarda tu progreso:** Google Colab NO guarda automáticamente en GitHub. Para registrar tu trabajo:
   * Ve al menú superior en Colab: `Archivo` > `Guardar una copia en GitHub`.
   * **Repositorio:** Selecciona este repositorio.
   * **Rama (Branch):** Selecciona **TU RAMA** (ej. `rama-juan-perez`), nunca la rama `main`.
   * Escribe un mensaje de commit descriptivo.
4. **Entrega (Pull Request):** Ve a GitHub. Verás un banner sugiriendo hacer un "Compare & pull request" de tu rama. Ábrelo hacia la rama `main` para iniciar el proceso de evaluación.

---

## 🚦 Protocolo de Revisión por Pares (Peer Review)

Todo código nuevo debe pasar por un proceso de auditoría. Tu Pull Request no podrá fusionarse automáticamente. 
**Para fusionar tu código y completar la entrega, necesitas la aprobación explícita de Tres (3) compañeros distintos y La Profe :).**

* **Si eres el Autor:** * En tu Pull Request, ve a **"Reviewers"** (barra lateral derecha).
  * Etiqueta a 3 o más compañeros solicitando su revisión.
* **Si eres el Revisor:**
  * Ve a la pestaña **"Pull requests"** y abre el de un compañero.
  * Revisa su código en **"Files changed"**.
  * Si el código cumple la tarea y es correcto, haz clic en **"Review changes"**, selecciona **"Approve"** (Aprobar) y deja un comentario. Si hay errores, solicita cambios (`Request changes`).

Una vez que el Pull Request acumule 3 aprobaciones (marcas verdes), pasará a la fila de revisión de la profesora. **Solo la profesora revisará el código final y hará clic en el botón de Merge para oficializar tu entrega.**

---

## Reglas del Repositorio

1.  **Aislamiento:** Edita únicamente los archivos explícitamente asignados a ti o a tu equipo.
2.  **Límite de Datos:** No subas archivos mayores a 50 MB. Monta Google Drive en Colab para procesar datasets grandes.
3.  **Seguridad:** Omite credenciales, tokens y API keys en el código fuente.
4.  **Nomenclatura:** Utiliza nombres de archivo en minúsculas, sin espacios ni caracteres especiales (ej. `juan_perez.py`).
5.  **Historial Limpio:** Escribe mensajes de commit descriptivos que expliquen el cambio realizado (ej. "Añade cálculo de trayectoria al sensor Y").
