"""Пакет алгоритмической обработки числовых рядов. 5.1 расширение вариант 8"""
from .generator import random_series, sine_series, trend_series, outliers_series
from .stats import mean, median, spread, trimmed_mean, summarize
from .moving_average import (
    simple_moving_average,
    simple_moving_average_deque,
    moving_median,
    centered_moving_average,
    exponential_moving_average,
    benchmark_moving_average,
)
from .deque_average import (
    centered_moving_average_deque,
    exponential_moving_average_deque,
    moving_median_deque,
)
from .io_json import save_series_json, load_series_json
from .io_file import load_series_txt, load_series_csv, load_series_auto

__all__ = [
    # генерация
    "random_series",
    "sine_series",
    "trend_series",
    "outliers_series",
    # статистика
    "mean",
    "median",
    "spread",
    "trimmed_mean",
    "summarize",
    # скользящие средние, медиана и бенчмарк
    "simple_moving_average",
    "simple_moving_average_deque",
    "moving_median",
    "centered_moving_average",
    "exponential_moving_average",
    "benchmark_moving_average",
    "centered_moving_average_deque",
    "exponential_moving_average_deque",
    "moving_median_deque",
    # ввод-вывод
    "save_series_json",
    "load_series_json",
    "load_series_txt",
    "load_series_csv",
    "load_series_auto",
]

__version__ = "1.3.0-var8"
