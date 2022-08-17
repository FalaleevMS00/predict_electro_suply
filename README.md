Создание 'программы/микросервиса' для прогнозирования электропотребления на основе исторических данных о потреблении.

На вход программе будет подаваться график электропотребления и желаемый горизонт прогнозирования, на выходе будет получаться предсказываемый график электропотребления.

Проект разделен на два основных этапа:

1. Data sience/analysis: 
  
  а) анализ графика потребления
  
  б) обработка входных файлов (почасовые данные о потреблении) - создание требования по входному файлу
  
  в) выбор фич для модели машинного обучения (+ на будущее создание новых)
  
  г) сравнение алгоритмов машинного обучения (на данный момент линейная регрессия, lgbm, catboost) 
  
2. Data engineering/mlops
  
  а) разбивка кода из блокнотв по модулям .py
  
  б) шаблонизация проекта (cookiecutter)
  
  в) настройка пайплайна для запуска модулей (здесь подразумевается локальный запуск, например из командной строки. инструмент - DVC)
  
  г) завернуть проект в программу, данная тематика находится в процессе изучения
  

