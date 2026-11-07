import math

# Ограничения на входные данные (мин, макс)
DIMENSION_MIN = 10.0
DIMENSION_MAX = 1000.0

MOMENT_MIN = 0.1
MOMENT_MAX = 500.0

SIGMA_ALLOW_MIN = 50.0
SIGMA_ALLOW_MAX = 400.0

# Константы для типов сечений
SECTION_RECTANGULAR = 1
SECTION_ROUND = 2
SECTION_I_BEAM = 3

SECTION_NAMES = {
    SECTION_RECTANGULAR: "Прямоугольное",
    SECTION_ROUND: "Круглое",
    SECTION_I_BEAM: "Двутавр"
}

# Пороги использования балки
USAGE_SAFE_LIMIT = 0.5
USAGE_ALLOWABLE_LIMIT = 1.0

CLASS_SAFE = "большой запас"
CLASS_ALLOWABLE = "допустимо"
CLASS_OVERLOAD = "перегрузка"
