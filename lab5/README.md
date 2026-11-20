# num_series_app

Модульное консольное приложение на Python для генерации, анализа, сглаживания и сохранения числовых рядов

## Структура проекта

```text
num_series_app/
├── num_series/
│   ├── __init__.py          # экспорт публичного API
│   ├── generator.py         # генерация рядов (random, sine, trend)
│   ├── stats.py             # базовая статистика (mean, median, spread, summarize)
│   ├── moving_average.py    # SMA, CMA, EMA, deque-SMA и benchmark_moving_average
│   ├── deque_average.py     # отдельный модуль скользящих средних на collections.deque
│   ├── io_json.py           # сохранение и чтение JSON
│   └── io_file.py           # чтение .txt / .csv и автовыбор парсера
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   ├── test_stats.py
│   ├── test_moving_average.py
│   ├── test_io.py
│   └── test_cli.py
├── conftest.py
├── pytest.ini
├── run_self_tests.py        # запуск тестов без pytest
├── main.py                  # CLI-точка входа
└── README.md
```

## Примеры запуска

Генерация и анализ ряда:
```bash
python main.py --kind sine --n 20 --window 3 --alpha 0.3 --seed 7
```

Сохранение в JSON и загрузка из файла:
```bash
python main.py --kind random --n 50 --save data/random.json
python main.py --load data/random.json --window 5
```

Экспорт в CSV:
```bash
python main.py --kind trend --n 30 --export out.csv
```

### Замер производительности скользящей средней

Для сравнения реализаций SMA через список (`list`) и через `deque` используйте флаг `--benchmark`:
```bash
python main.py --kind sine --n 1000 --window 10 --benchmark
```
Будут выведены средние времена выполнения (в секундах) для обеих реализаций и их отношение.

## Запуск тестов

Через `pytest`:
```bash
pytest
```

Без `pytest` (встроенный раннер):
```bash
python run_self_tests.py
```
