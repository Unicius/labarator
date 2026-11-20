"""Модуль базовой и устойчивой статистики """
from __future__ import annotations
from typing import Dict, Sequence


def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт статистики невозможен")

def mean(data: Sequence[float]) -> float:
    """Среднее арифметическое."""
    _ensure_not_empty(data)
    return sum(data) / len(data)

def median(data: Sequence[float]) -> float:
    """Медиана (устойчива к выбросам)."""
    _ensure_not_empty(data)
    s = sorted(data)
    k = len(s) // 2
    if len(s) % 2:
        return float(s[k])
    return (s[k - 1] + s[k]) / 2.0

def spread(data: Sequence[float]) -> float:
    """Размах ряда: max - min."""
    _ensure_not_empty(data)
    return float(max(data) - min(data))

def trimmed_mean(data: Sequence[float], proportion: float = 0.1) -> float:
    """Устойчивая статистика (Вариант 8): усечённое среднее (по умолчанию 10% с каждого конца)."""
    _ensure_not_empty(data)
    if isinstance(proportion, bool) or not isinstance(proportion, (int, float)) or not (0.0 <= proportion < 0.5):
        raise ValueError(f"proportion должен быть в [0, 0.5), получено: {proportion!r}")

    s = sorted(data)
    cut = int(len(s) * proportion)
    trimmed = s[cut : len(s) - cut] if cut > 0 else s
    if not trimmed:
        trimmed = s
    return sum(trimmed) / len(trimmed)

def summarize(data: Sequence[float]) -> Dict[str, float]:
    """Сводный отчёт: count, mean, median, trimmed_mean, spread, min, max."""
    _ensure_not_empty(data)
    return {
        "count": len(data),
        "mean": mean(data),
        "median": median(data),
        "trimmed_mean": trimmed_mean(data, 0.1),
        "spread": spread(data),
        "min": float(min(data)),
        "max": float(max(data)),
    }
