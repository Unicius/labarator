"""Точка входа CLI (Вариант 8: шум + 2 выброса, trimmed mean, SMA list/deque, скользящая медиана). Сделал вариант 8"""

from __future__ import annotations
import argparse
import csv
import json
import sys
from typing import List, Optional, Tuple

from num_series_app import (
    random_series,
    sine_series,
    trend_series,
    outliers_series,
    summarize,
    simple_moving_average,
    simple_moving_average_deque,
    moving_median,
    benchmark_moving_average,
    save_series_json,
    load_series_auto,
)

def build_series(kind: str, n: int, seed: int) -> List[float]:
    """Генерирует ряд заданного типа."""
    if kind == "outliers":
        return outliers_series(n, low=0.0, high=10.0, outlier_factor=10.0, num_outliers=2, seed=seed)
    if kind == "random":
        return random_series(n, low=-50, high=50, seed=seed)
    if kind == "sine":
        return sine_series(n, amplitude=10, frequency=2, noise=1.5, seed=seed)
    if kind == "trend":
        return trend_series(n, start=0, step=1.0, noise=0.5, seed=seed)
    raise ValueError(f"Неизвестный тип ряда: {kind!r}")

def obtain_series(args: argparse.Namespace) -> Tuple[List[float], str]:
    """Возвращает (ряд, описание источника)."""
    if args.load:
        data = load_series_auto(args.load)
        return data, f"файл: {args.load}"
    data = build_series(args.kind, args.n, args.seed)
    return data, f"сгенерирован ({args.kind}, n={args.n}, seed={args.seed})"

def export_series_csv(path: str, data: List[float]) -> None:
    """Экспорт ряда в CSV: столбцы i, value."""
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["i", "value"])
            for i, v in enumerate(data):
                w.writerow([i, v])
    except OSError as err:
        raise ValueError(f"Не удалось записать CSV {path}: {err}") from err

def print_series_preview(title: str, values: List[float], fmt: str = "{:>8.3f}", limit: int = 12) -> None:
    """Печатает ряд целиком (если короткий) или первые/последние элементы."""
    print(f"\n{title} (n={len(values)}):")
    if len(values) <= limit:
        print(" " + " ".join(fmt.format(v) for v in values))
    else:
        head = " ".join(fmt.format(v) for v in values[:6])
        tail = " ".join(fmt.format(v) for v in values[-6:])
        print(f" {head}  ...  {tail}")

def print_header(source: str) -> None:
    print("=" * 64)
    print(f"Источник данных: {source}")
    print("-" * 64)

def print_stats(stats: dict) -> None:
    print(f"Количество точек        : {stats['count']}")
    print(f"Среднее арифметическое  : {stats['mean']:>10.4f}")
    print(f"Усечённое среднее (10%) : {stats['trimmed_mean']:>10.4f}")
    print(f"Медиана                 : {stats['median']:>10.4f}")
    print(f"Размах (max - min)      : {stats['spread']:>10.4f}")
    print(f"min / max               : {stats['min']:>10.4f} / {stats['max']:.4f}")

def print_footer() -> None:
    print("=" * 64)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Алгоритмическая обработка числовых рядов (Вариант 8)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Пример: python main.py --kind outliers --n 1500 --window 10 --benchmark",
    )
    parser.add_argument(
        "--kind",
        choices=["outliers", "random", "sine", "trend"],
        default="outliers",
        help="тип генерируемого ряда",
    )
    parser.add_argument("--n", type=int, default=1500, help="количество точек в ряде")
    parser.add_argument("--seed", type=int, default=42, help="зерно ГПСЧ для воспроизводимости")
    parser.add_argument(
        "--load",
        metavar="PATH",
        help="загрузить ряд из файла (.json/.txt/.csv); отменяет --kind/--n/--seed",
    )
    parser.add_argument("--save", metavar="PATH", help="сохранить ряд в JSON-файл")
    parser.add_argument("--export", metavar="FILE", help="экспортировать ряд в CSV (i, value)")
    parser.add_argument("--json", action="store_true", help="вывести результат анализа в формате JSON")
    parser.add_argument("--window", type=int, default=10, help="размер окна k (чётное или нечётное)")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="замерить время выполнения SMA для list и deque",
    )
    return parser

def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        data, source = obtain_series(args)
    except ValueError as err:
        print(f"Ошибка получения ряда: {err}", file=sys.stderr)
        return 1

    if args.save:
        meta = {"source": source}
        if not args.load:
            meta.update({"kind": args.kind, "seed": args.seed})
        try:
            save_series_json(data, args.save, meta=meta)
            print(f"[сохранено] {args.save} ({len(data)} точек)")
        except ValueError as err:
            print(f"Ошибка сохранения: {err}", file=sys.stderr)
            return 1

    if args.export:
        try:
            export_series_csv(args.export, data)
            print(f"[экспортировано] {args.export} ({len(data)} точек)")
        except ValueError as err:
            print(f"Ошибка экспорта: {err}", file=sys.stderr)
            return 1

    try:
        stats = summarize(data)
        sma_list = simple_moving_average(data, args.window)
        sma_deque = simple_moving_average_deque(data, args.window)
        mmed = moving_median(data, args.window)
    except ValueError as err:
        print(f"Ошибка анализа: {err}", file=sys.stderr)
        return 1

    if args.json:
        payload = {
            "source": source,
            "stats": stats,
            "sma_list": sma_list,
            "sma_deque": sma_deque,
            "moving_median": mmed,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print_header(source)
    print_stats(stats)

    parity = "чётное" if args.window % 2 == 0 else "нечётное"
    print_series_preview("Исходный ряд", data)
    print_series_preview(f"SMA list (window={args.window})", sma_list)
    print_series_preview(f"SMA deque (window={args.window})", sma_deque)
    print_series_preview(f"Медианное сглаживание (window={args.window}, {parity})", mmed)

    if args.benchmark:
        print("-" * 64)
        print("Замер времени выполнения SMA (среднее за 1000 повторов):")
        timings = benchmark_moving_average(data, args.window, repeats=1000)
        print(f"  list  : {timings['list']:.8f} с")
        print(f"  deque : {timings['deque']:.8f} с")
        if timings["deque"] > 0:
            print(f"отношение (list/deque): {timings['list'] / timings['deque']:.2f}")

    print_footer()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
