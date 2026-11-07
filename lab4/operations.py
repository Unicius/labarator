import math
from constants import (
    SECTION_RECTANGULAR, SECTION_ROUND, SECTION_I_BEAM,
    USAGE_SAFE_LIMIT, USAGE_ALLOWABLE_LIMIT,
    CLASS_SAFE, CLASS_ALLOWABLE, CLASS_OVERLOAD
)

def calculate_w(section_type: int, size: float) -> float:
    if section_type == SECTION_RECTANGULAR:
        return (size * (size ** 2)) / 6
    elif section_type == SECTION_ROUND:
        return (math.pi * (size ** 3)) / 32
    elif section_type == SECTION_I_BEAM:
        return (size ** 3) / 12
    else:
        raise ValueError("Неизвестный тип сечения")

def calculate_sigma(moment_khm: float, w_mm3: float) -> float:
    return (moment_khm * 1_000_000) / w_mm3

def classify_usage(sigma: float, sigma_allow: float) -> tuple[float, str]:
    k_usage = sigma / sigma_allow
    if k_usage < USAGE_SAFE_LIMIT:
        return k_usage, CLASS_SAFE
    elif k_usage <= USAGE_ALLOWABLE_LIMIT:
        return k_usage, CLASS_ALLOWABLE
    else:
        return k_usage, CLASS_OVERLOAD
