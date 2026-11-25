# Алгоритмическая обработка числовых рядов (`num_series_app`)

Модульное консольное приложение на Python для генерации числовых рядов, расчёта базовых статистических показателей, сглаживания (SMA, CMA, EMA — на списках и `collections.deque`), ввода-вывода (JSON, TXT, CSV) и бенчмаркинга.

## Структура проекта

```text
num_series_app/
├── num_series/
│   ├── __init__.py          # экспорт публичного API пакета
│   ├── generator.py         # генерация числовых рядов (random, sine, trend)
│   ├── stats.py             # базовые статистики (mean, median, spread, summarize)
│   ├── moving_average.py    # SMA (list и deque), CMA, EMA и benchmark
│   ├── deque_average.py     # потоковые реализации SMA, CMA, EMA на collections.deque
│   ├── io_json.py           # сохранение и чтение JSON с метаданными
│   └── io_file.py           # чтение TXT, CSV и автовыбор парсера
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   ├── test_stats.py
│   ├── test_moving_average.py
│   ├── test_deque_average.py
│   ├── test_io_json.py
│   ├── test_io_file.py
│   └── test_cli.py
├── conftest.py              # настройка путей pytest
├── pytest.ini               # конфигурация pytest
├── run_self_tests.py        # автономные тесты без внешних зависимостей
├── main.py                  # CLI-точка входа
└── README.md
```

## Примеры запуска

Базовая генерация и анализ:
```bash
python main.py --kind sine --n 20 --window 3 --alpha 0.3 --seed 7
```

Сохранение в JSON и загрузка из файла:
```bash
python main.py --kind random --n 50 --save data/random.json
python main.py --load data/random.json --window 5
```

Экспорт в CSV или вывод в JSON:
```bash
python main.py --kind trend --n 30 --export out.csv
python main.py --kind sine --n 10 --json
```

### Замер производительности скользящей средней

Для сравнения реализаций SMA через список и через `deque` используйте флаг `--benchmark`:
```bash
python main.py --kind random --n 5000 --window 20 --benchmark
```

## Запуск тестов

С помощью `pytest`:
```bash
pytest
```

Без установки сторонних библиотек:
```bash
python run_self_tests.py
```
