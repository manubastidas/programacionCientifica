"""
Genera Ejercicios/actividad3/plots/collage.md con galería oscura estilo HTML embebido.
Corre automáticamente desde el GitHub Action al hacer merge a main.
"""

from pathlib import Path
from datetime import datetime

PLOTS = Path("Ejercicios/actividad3/plots")
OUT   = PLOTS / "collage.md"
COLS  = 4

PLOTS.mkdir(parents=True, exist_ok=True)

imagenes = sorted(
    p for p in PLOTS.glob("*.jpg")
    if p.name != "collage.jpg"
)

def nombre_display(stem: str) -> str:
    """nombre1_nombre2 → Nombre1 Nombre2"""
    return " · ".join(w.capitalize() for w in stem.split("_"))

# ── encabezado ────────────────────────────────────────────────────────────────
lineas = [
    '<div align="center">',
    "",
    "```",
    " L I S S A J O U S",
    "```",
    "",
    '<p style="color:#8b949e; font-size:13px; letter-spacing:0.15em;">',
    "PROGRAMACIÓN CIENTÍFICA 2026-1 &nbsp;·&nbsp; UNIVERSIDAD NACIONAL DE COLOMBIA",
    "</p>",
    "",
    f'<p style="color:#484f58; font-size:11px;">{len(imagenes)} curvas · generado el {datetime.utcnow().strftime("%Y-%m-%d %H:%M")} UTC</p>',
    "",
    "<br>",
    "",
]

# ── cuadrícula ────────────────────────────────────────────────────────────────
lineas += ["<table>"]

filas = [imagenes[i:i+COLS] for i in range(0, len(imagenes), COLS)]

for fila in filas:
    lineas.append("<tr>")
    for img in fila:
        url = f"https://raw.githubusercontent.com/mbastidaso/programacionCientifica/main/Ejercicios/actividad3/plots/{img.name}"
        lineas.append(
            f'  <td align="center" style="background:#0d1117; padding:8px; border:none;">'
            f'<img src="{url}" width="180"/></td>'
        )
    for _ in range(COLS - len(fila)):
        lineas.append('  <td style="background:#0d1117; border:none;"></td>')
    lineas.append("</tr>")

    lineas.append("<tr>")
    for img in fila:
        lineas.append(
            f'  <td align="center" style="background:#0d1117; padding:2px 8px 12px; border:none;">'
            f'<sub><i style="color:#8b949e;">{nombre_display(img.stem)}</i></sub></td>'
        )
    for _ in range(COLS - len(fila)):
        lineas.append('  <td style="background:#0d1117; border:none;"></td>')
    lineas.append("</tr>")

lineas += [
    "</table>",
    "",
    "<br>",
    "",
    '<p style="color:#484f58; font-size:11px;">',
    "mbastidaso@unal.edu.co",
    "</p>",
    "",
    "</div>",
]

OUT.write_text("\n".join(lineas), encoding="utf-8")
print(f"collage.md generado con {len(imagenes)} imágenes → {OUT}")
