"""Константы: диапазоны, коэффициенты и пороги для расчёта прочности балки."""

# Диапазоны входных значений
SECTION_DIM_MIN = 10.0      # мм
SECTION_DIM_MAX = 1000.0    # мм

MOMENT_MIN = 0.1            # кН·м
MOMENT_MAX = 500.0          # кН·м

ALLOWABLE_STRESS_MIN = 50.0   # МПа
ALLOWABLE_STRESS_MAX = 400.0  # МПа

# Пороги использования материала (sigma / [sigma])
UTIL_LOW_THRESHOLD = 0.5
UTIL_HIGH_THRESHOLD = 1.0

# Названия классов использования
CLASS_HIGH_MARGIN = "большой запас"
CLASS_ACCEPTABLE = "допустимо"
CLASS_OVERLOAD = "перегрузка"

# Имена типов сечений
SECTION_TYPES = {
    "1": "Прямоугольное",
    "2": "Круглое",
    "3": "Двутавр"
}
