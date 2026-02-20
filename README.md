# Curso de Programación Científica

Bienvenido al monorepositorio del curso. Este espacio centraliza los proyectos colaborativos. Utilizamos un flujo de trabajo basado en GitHub y Google Colab para la ejecución de código.

## Estructura del Repositorio

El directorio está organizado para soportar el trabajo simultáneo de todos los estudiantes:

* `Ejercicios/`: Ejercicios de clase.
* `Entregas/`: Proyectos integradores en equipos.

## Flujo de Trabajo Principal

Ejecutamos el código en Google Colab y almacenamos el progreso en GitHub. Aplica estos pasos para cada tarea:

1.  **Fork:** Crea una copia personal de este repositorio en tu cuenta de GitHub. Sincroniza tu fork antes de cada clase.
2.  **Ejecución:** Abre los notebooks usando el botón "Open in Colab".
3.  **Guardado:** Colab no guarda automáticamente en GitHub. Ve a `Archivo` > `Guardar una copia en GitHub`. Selecciona tu fork, la rama correcta y escribe un mensaje de commit claro.
4.  **Entrega:** Abre un Pull Request (PR) desde tu fork hacia la rama `main` de este repositorio original.

## Ejercicios:

1. Red de Sensores Global (Individual)
* **Objetivo:** Sincronizar datos sin generar conflictos.
* **Acción:** Crea un archivo `nombre_apellido.txt` en ---. Haz commit y abre un PR. 

## Reglas del Repositorio

1.  **Aislamiento:** Edita únicamente los archivos explícitamente asignados a ti o a tu equipo.
2.  **Límite de Datos:** No subas archivos mayores a 50 MB. Monta Google Drive en Colab para procesar datasets grandes.
3.  **Seguridad:** Omite credenciales, tokens y API keys en el código fuente. Utiliza la librería `google.colab.userdata`.
4.  **Nomenclatura:** Utiliza nombres de archivo en minúsculas, sin espacios ni caracteres especiales (ej. `juan_perez.py`).
5.  **Historial Limpio:** Escribe mensajes de commit descriptivos que expliquen el cambio realizado (ej. "Añade cálculo de trayectoria al sensor Y").
