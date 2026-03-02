# Actividad Colaborativa: Capture the Flag (Bandit)

**Objetivo:** Practicar conexiones SSH y comandos de terminal resolviendo el wargame Bandit https://overthewire.org/wargames/bandit/. 
Documentar las soluciones en equipo utilizando un flujo estricto de GitHub.

**Método:**

1. **Crea una rama:** Crea una rama nueva para tu nivel. Usa `git checkout -b bandit-nivel-X` (reemplaza la X con tu nivel).
3. **Conéctate por SSH:** Accede al servidor de Bandit. El juego utiliza el puerto 2220. Ejemplo para el nivel 0: `ssh bandit0@bandit.labs.overthewire.org -p 2220`.
4. **Captura la bandera:** Encuentra la contraseña del siguiente nivel usando comandos de Linux en la terminal remota.
5. **Edita el archivo:** Abre `soluciones_bandit.md` en tu editor. Añade tu solución siguiendo la plantilla estructural. 
Designa explícitamente al compañero que debe resolver el siguiente nivel.
6. **Sube los cambios y abre un Pull Request (PR):** Ve al repositorio en GitHub y abre un PR desde tu rama hacia `main`.
8. **Asigna revisores:** Etiqueta y asigna a dos compañeros diferentes (y la profe) como revisores de tu PR. 
9. **Aprueba y fusiona:** Los dos revisores verifican la sintaxis del comando y el formato Markdown, y aprueban los cambios. 
---

### Plantilla para `soluciones_bandit.md`

Agrega tu bloque al final del documento usando este formato exacto:

```markdown
### Nivel X a Nivel X+1
* **Autor:** [Tu Nombre y Apellido]
* **Comandos utilizados:** ```bash
  [inserta tus comandos aquí]
