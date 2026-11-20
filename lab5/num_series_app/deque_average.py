"""Скользящие средние и медианное сглаживание на основе collections.deque."""
from __future__ import annotations

from collections import deque
from typing import Deque, List, Sequence

from .stats import median


def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")


def _check_window(window: int, n: int) -> None:
    if not isinstance(window, int) or isinstance(window, bool):
        raise ValueError(f"window должен быть целым, получено: {window!r}")
    if window < 1:
        raise ValueError(f"window должен быть >= 1, получено: {window}")
    if window > n:
        raise ValueError(
            f"window ({window}) больше длины ряда ({n}) — операция невозможна"
        )


def _check_alpha(alpha: float) -> None:
    if isinstance(alpha, bool) or not isinstance(alpha, (int, float)) or not (0 < alpha <= 1):
        raise ValueError(f"alpha должен быть в (0, 1], получено: {alpha}")


def simple_moving_average_deque(
    data: Sequence[float],
    window: int,
) -> List[float]:
    """SMA через deque(maxlen=window) за O(n) по времени и O(window) по памяти."""
    _ensure_not_empty(data)
    _check_window(window, len(data))

    buf: Deque[float] = deque(maxlen=window)
    running = 0.0
    result: List[float] = []

    for i, x in enumerate(data):
        if len(buf) == window:
            running -= buf[0]
        buf.append(x)
        running += x
        if i >= window - 1:
            result.append(running / window)

    return result


def centered_moving_average_deque(
    data: Sequence[float],
    window: int,
) -> List[float]:
    """Центрированное MA: окно нечётное, результат выровнен по центру."""
    _ensure_not_empty(data)
    _check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"Центрированное MA требует нечётного window, получено: {window}"
        )

    buf: Deque[float] = deque(maxlen=window)
    running = 0.0
    result: List[float] = []

    for x in data:
        if len(buf) == window:
            running -= buf[0]
        buf.append(x)
        running += x
        if len(buf) == window:
            result.append(running / window)

    return result


def exponential_moving_average_deque(
    data: Sequence[float],
    alpha: float,
) -> List[float]:
    """EMA через deque ring-buffer."""
    _ensure_not_empty(data)
    _check_alpha(alpha)

    buf: Deque[float] = deque(maxlen=1)
    prev: float = float(data[0])
    buf.append(prev)
    result: List[float] = [prev]

    for x in data[1:]:
        prev = alpha * x + (1.0 - alpha) * prev
        result.append(prev)
        buf.append(prev)

    return result


def moving_median_deque(
    data: Sequence[float],
    window: int,
) -> List[float]:
    """Скользящая медиана через deque(maxlen=window) для чётного и нечётного окна."""
    _ensure_not_empty(data)
    _check_window(window, len(data))

    buf: Deque[float] = deque(maxlen=window)
    result: List[float] = []
    for x in data:
        buf.append(x)
        if len(buf) == window:
            result.append(median(list(buf)))
    return result


__all__ = [
    "simple_moving_average_deque",
    "centered_moving_average_deque",
    "exponential_moving_average_deque",
    "moving_median_deque",
]
