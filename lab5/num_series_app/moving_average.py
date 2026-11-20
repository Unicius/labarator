"""Модуль скользящей средней (SMA на list и deque, скользящая медиана, CMA, EMA, бенчмарк)."""
from __future__ import annotations

import time
from collections import deque
from typing import Dict, List, Sequence

from .stats import median


def check_window(window: int, n: int) -> None:
    """Проверка корректности размера окна."""
    if n <= 0:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    if not isinstance(window, int) or isinstance(window, bool):
        raise ValueError(f"window должен быть целым, получено: {window!r}")
    if window < 1:
        raise ValueError(f"window должен быть >= 1, получено: {window}")
    if window > n:
        raise ValueError(
            f"window ({window}) больше длины ряда ({n}) — операция невозможна"
        )


def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Простая скользящая средняя (SMA) через бегущую сумму за O(n)."""
    check_window(window, len(data))
    running = float(sum(data[:window]))
    result: List[float] = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result


def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]:
    """SMA с использованием deque (двусторонней очереди)."""
    check_window(window, len(data))
    result: List[float] = []
    d: deque[float] = deque()
    running_sum = 0.0
    for x in data:
        d.append(x)
        running_sum += x
        if len(d) > window:
            running_sum -= d.popleft()
        if len(d) == window:
            result.append(running_sum / window)
    return result


def moving_median(data: Sequence[float], window: int) -> List[float]:
    """Медианное сглаживание (скользящая медиана окна window, чётного и нечётного)."""
    check_window(window, len(data))
    buf: deque[float] = deque(maxlen=window)
    result: List[float] = []
    for x in data:
        buf.append(x)
        if len(buf) == window:
            result.append(median(list(buf)))
    return result


def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное MA: окно нечётное, выход выровнен по центру."""
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"Центрированное MA требует нечётного window, получено: {window}"
        )
    return simple_moving_average(data, window)


def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """Экспоненциальная скользящая средняя (EMA), 0 < alpha <= 1."""
    if not data:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")
    if isinstance(alpha, bool) or not isinstance(alpha, (int, float)) or not (0 < alpha <= 1):
        raise ValueError(f"alpha должен быть в (0, 1], получено: {alpha}")

    prev = float(data[0])
    result: List[float] = [prev]
    for x in data[1:]:
        prev = alpha * x + (1.0 - alpha) * prev
        result.append(prev)
    return result


def benchmark_moving_average(
    data: Sequence[float],
    window: int,
    repeats: int = 1000,
) -> Dict[str, float]:
    """
    Замеряет среднее время выполнения SMA для реализаций на list и deque.
    Возвращает словарь с ключами 'list' и 'deque' (время в секундах).
    """
    check_window(window, len(data))
    if repeats < 1:
        raise ValueError(f"repeats должен быть >= 1, получено: {repeats}")

    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average(data, window)
    t_list = (time.perf_counter() - t0) / repeats

    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average_deque(data, window)
    t_deque = (time.perf_counter() - t0) / repeats

    return {"list": t_list, "deque": t_deque}
