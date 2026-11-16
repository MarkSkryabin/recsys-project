# HW1: популярность и персонализация

Главный файл — `HW1_Скрябин_Марк.ipynb`. В нём находятся весь код,
пояснения, таблицы, графики и выводы.

Запускайте ноутбук из папки `lab_1`. Исходные данные читаются напрямую:
`data/ratings.dat` и `data/movies.dat`.

В `data` сохраняются только два файла, требуемые заданием:

- `split_seed2026.npz` — разбиение исходных оценок;
- `negative_examples_seed2026.npz` — искусственные нулевые примеры BP-N с повторами.

Все остальные результаты остаются в ячейках. Папка `artifacts` для работы ноутбука не нужна.

Для ручного запуска выберите Python с библиотеками из `requirements.txt` и выполните Run All.
Служебный `run_notebook.py` позволяет автоматически выполнить и сохранить ноутбук:

```powershell
python lab_1/run_notebook.py
```

В текущей конфигурации с локальными библиотеками Python 3.12:

```powershell
& 'C:\Users\skrya\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -X utf8 lab_1/run_notebook.py
```

`build_notebook.py` и `notebook_template.json` — вспомогательный шаблон;
для обычной работы с ноутбуком они не нужны. Генератор очищает outputs,
поэтому для повторного запуска используйте сам ноутбук или `run_notebook.py`.
