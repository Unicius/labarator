from typing import List, Sequence

def check_window(window: int, n: int) -> None:
    """Валидация размера окна сглаживания."""
    if window < 1:
        raise ValueError(f"Размер окна должен быть целым числом >= 1 (получено: {window})")
    if window > n:
        raise ValueError(f"Размер окна ({window}) не должен превышать длину ряда ({n})")

def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Простая скользящая средняя (SMA), реализованная через бегущую сумму."""
    n = len(data)
    check_window(window, n)
    
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, n):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированная скользящая средняя для нечётного окна с сохранением исходной длины."""
    n = len(data)
    check_window(window, n)
    if window % 2 == 0:
        raise ValueError(f"Окно для центрированного MA должно быть нечётным (получено: {window})")
        
    half_w = window // 2
    result = []
    for i in range(n):
        start = max(0, i - half_w)
        end = min(n, i + half_w + 1)
        result.append(sum(data[start:end]) / (end - start))
    return result

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """Экспоненциальная скользящая средняя (EMA)."""
    if not data:
        raise ValueError("Ряд пуст: невозможно рассчитать EMA")
    if not (0 < alpha <= 1):
        raise ValueError(f"Коэффициент сглаживания alpha должен быть в диапазоне (0, 1] (получено: {alpha})")
        
    result = [float(data[0])]
    for i in range(1, len(data)):
        ema_val = alpha * data[i] + (1 - alpha) * result[-1]
        result.append(ema_val)
    return result
