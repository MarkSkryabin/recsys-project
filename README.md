# RecSys project

Учебные работы по рекомендательным системам. Автор: Скрябин Марк.

## Работа 1: популярность и персонализация

Отчёт с выполненным кодом, таблицами, графиками и выводами:
[HW1_Скрябин_Марк.ipynb](lab_1/HW1_Скрябин_Марк.ipynb).

На MovieLens 1M сравниваются Random, MostPopular, жанровый профиль и четыре
варианта baseline predictor. Проверяется польза собственного профиля относительно
чужого, качество для трёх групп пользователей и влияние размера профиля.

Ноутбук выполнен в Python 3.12. Зависимости:

```powershell
python -m pip install -r lab_1/requirements.txt
```

Скачайте [MovieLens 1M](https://grouplens.org/datasets/movielens/1m/) и положите
`ratings.dat` и `movies.dat` в `lab_1/data/`. Исходные данные не включены в Git:
их лицензия требует отдельного разрешения на распространение.

Откройте ноутбук с рабочим каталогом `lab_1` и выполните Run All. Все основные
результаты остаются в его ячейках. Два обязательных промежуточных файла — разбиение
и искусственные нулевые примеры — сохраняются в локальную папку `data`.

Для автоматического выполнения из корня проекта:

```powershell
python lab_1/run_notebook.py
```

## Данные и статьи

Данные: F. Maxwell Harper and Joseph A. Konstan (2015).
*The MovieLens Datasets: History and Context*.
[DOI](https://doi.org/10.1145/2827872).

Статьи к первой работе:

- Abdollahpouri et al. (2019), *The Unfairness of Popularity Bias in Recommendation*.
  [arXiv](https://arxiv.org/abs/1907.13286).
- Kowald et al. (2020), *The Unfairness of Popularity Bias in Music Recommendation:
  A Reproducibility Study*. [arXiv](https://arxiv.org/abs/1912.04696).

Скачанные PDF, данные, виртуальное окружение и служебные файлы остаются локально.
