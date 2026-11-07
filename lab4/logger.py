import sys
from __future__ import annotations
import datetime
from constants import LOG_FILE

_entries: list[str] = []

def log_error(message: str) -> None:
    """Выводит ошибку в стандартный поток ошибок или файл журнала."""
    print(f"[ЖУРНАЛ ОШИБОК] {message}", file=sys.stderr)







def clear() -> None:
    "Очистить журнал (используется в тестах)."
    _entries.clear()