"""
generar_datos.py — Evaluación 2, Programación Científica 2026-1 (UNAL)

Genera el conjunto de señales ÚNICO de cada estudiante a partir de su cédula.

    python generar_datos.py 4815      # <- últimos 4 dígitos de su cédula

Produce datos_XXXX.npz con:
    X : (n, 256)  señales medidas
    y : (n,)      régimen de cada señal (0, 1, 2)
    t : (256,)    instantes de muestreo

El número de señales por régimen lo fija el enunciado personalizado
(generar_enunciado.py). Por defecto son 12 por régimen.
"""
import sys
import getpass
import socket
import hashlib
import datetime
import numpy as np


def n_por_regimen(seed):
    # mismo criterio que generar_enunciado.py: parámetro derivado de la cédula
    return int(np.random.default_rng(seed + 10_000).choice([8, 10, 12, 15]))


def _huella():
    try:
        crudo = f"{getpass.getuser()}@{socket.gethostname()}"
    except Exception:
        crudo = "desconocido"
    return hashlib.sha256(crudo.encode()).hexdigest()[:16]


def generar(seed, n=None):
    if n is None:
        n = n_por_regimen(seed)
    r = np.random.default_rng(seed)
    _n = 256
    _t = np.linspace(0, 1, _n, endpoint=False)
    _v = 1.0
    _s = r.uniform(0.2, 0.6)
    _w = lambda kk, mm: np.sqrt((_v * kk) ** 2 + mm ** 2)

    def _mk(mm):
        _k = r.choice(np.arange(1, 12), size=3, replace=False)
        _a = r.uniform(0.3, 1.0, 3)
        _p = r.uniform(0, 2 * np.pi, 3)
        _u = np.zeros_like(_t)
        for _ki, _ai, _pi in zip(_k, _a, _p):
            _u += _ai * np.cos(_w(_ki, mm) * 2 * np.pi * _t - _ki * _s + _pi)
        return _u

    _X, _y = [], []
    for _lab, _mm in {0: 0.0, 1: 5.0, 2: 15.0}.items():
        for _ in range(n):
            _X.append(_mk(_mm) + r.normal(0, 0.02, _n))
            _y.append(_lab)
    _X, _y = np.array(_X), np.array(_y)
    _perm = r.permutation(len(_y))
    return _X[_perm], _y[_perm], _t


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Uso: python generar_datos.py XXXX   (últimos 4 dígitos de su cédula)")
        sys.exit(1)
    seed = int(sys.argv[1])
    X, y, t = generar(seed)
    meta = np.array([str(seed), _huella(),
                     datetime.datetime.now().isoformat(timespec="seconds")])
    np.savez(f"datos_{seed}.npz", X=X, y=y, t=t, meta=meta)
    print(f"Datos generados para cédula {seed}: X={X.shape}, y={y.shape}, t={t.shape}")
    print(f"Guardado en datos_{seed}.npz")