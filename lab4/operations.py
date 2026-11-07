"""Модуль геометрии и расчётов прочности балки."""

import math
from constants import (
    UTIL_LOW_THRESHOLD, UTIL_HIGH_THRESHOLD,
    CLASS_HIGH_MARGIN, CLASS_ACCEPTABLE, CLASS_OVERLOAD
)


def calculate_w_rectangle(b: float, h: float) -> float:
    """Момент сопротивления прямоугольного сечения W = (b * h^2) / 6 (см^3 при b, h в мм -> W в мм^3, вернем в см^3/м^3).
    В задаче формула W = b * h^2 / 6 (с учетом переводных коэффициентов далее).
    """
    return (b * (h ** 2)) / 6.0


def calculate_w_circle(d: float) -> float:
    """Момент сопротивления круглого сечения W = (pi * d^3) / 32."""
    return (math.pi * (d ** 3)) / 32.0


def calculate_w_i_beam(h: float) -> float:
    """Упрощённый момент сопротивления двутавра W = h^3 / 12."""
    return (h ** 3) / 12.0


def calculate_stress_and_status(w_mm3: float, moment_kNm: float, allowable_stress: float):
    """
    Расчёт напряжений sigma и коэффициента использования.
    Формула из задания: sigma = M * 1000 / W * 1000 (в МПа), 
    где M в кН·м, W в мм^3 (при умножении M на 10^6 N*mm получается sigma в МПа).
    """
    # M [кН*м] * 10^6 -> N*mm
    # W [мм^3]
    # sigma [МПа] = (M * 10^6) / W
    sigma = (moment_kNm * 1_000_000.0) / w_mm3
    utilization = sigma / allowable_stress

    if utilization < UTIL_LOW_THRESHOLD:
        status_class = CLASS_HIGH_MARGIN
    elif utilization <= UTIL_HIGH_THRESHOLD:
        status_class = CLASS_ACCEPTABLE
    else:
        status_class = CLASS_OVERLOAD

    return sigma, utilization, status_class