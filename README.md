electro_supply
==============================

A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


Создание 'программы/микросервиса' для прогнозирования электропотребления на основе исторических данных о потреблении.

На вход программе будет подаваться график электропотребления и желаемый горизонт прогнозирования, на выходе будет получаться предсказываемый график электропотребления.

Проект разделен на два основных этапа:

1. Data sience/analysis: 
  
  а) анализ графика потребления
  
  б) обработка входных файлов (почасовые данные о потреблении) - создание требования по входному файлу
  
  в) выбор фич для модели машинного обучения (+ на будущее создание новых)
  
  г) сравнение алгоритмов машинного обучения (на данный момент линейная регрессия, lgbm, catboost) 
  
2. Data engineering/mlops

(Данный этап предназначен для отработки навыков по построению пайплайнов и "вывода модели машинного обучения до потребителья"
  
  а) разбивка кода из блокнота по модулям .py:
      
      1) обработка загружаемого файла и приведение его в нужный формат
      
      2) алгоритм машинного обучения (для начала линейная регрессия)
      
      3) оценка метрик
      
      4) визуализация
  
  б) шаблонизация проекта (cookiecutter)
  
  в) настройка пайплайна для запуска модулей (здесь подразумевается локальный запуск, например из командной строки. инструмент - DVC)
  
  г) завернуть проект в программу, данная тематика находится в процессе изучения
  
  
  
  
  Ближайшие задачи: 
  
  1) пофиксить модуль с предсказанием и добавить модуль с визуализацией
  
  2) сделать шаблон cookiecutter
  
  3) запустить код через click (https://digitology.tech/posts/napisanie-python-utilit-komandnoj-stroki-s-click/), ошибка с путем файла, в процессе исправления 
  
  3) посмотреть видео и сделать пайплайн через dvc https://www.youtube.com/watch?v=71IGzyH95UY&t=3s
  
  4) https://yandex.ru/q/loves/machine-learning/
 

