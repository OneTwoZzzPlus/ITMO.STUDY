### Графическое приложение и библиотека:
- `main.py` - графическое приложение
- `meas` - библиотека для работы с измерениями

### Состав приложения
- `AskNameDialog.py` - окно ввода  
- `EntryEX.py` - Entry с поддержкой cut/copy/paste
- `MeasForm.py` - форма работы с Measurement
- `ExpressionForm.py` - форма работы с expression
- `DMMForm.py` - форма работы с DirectMultipleMeasurement
- `LMMForm.py` - форма работы с LinearMultipleMeasurement
- `GraphicSettingsFrame.py` - настройка графика в LMM
- `SaveMeasFrame.py` - параметры сохранения измерения в LMM и DMM
- `ListNotebook.py` - форма выбора и отображения форм
- `Models.py` - peewee ORM модели Experiment и Meas (хранит Measurement) 

### Состав библиотеки
- `__init__.py` - настройки импорта
- `BaseMeasurement.py` - абстрактный класс измерения
- `MultipleMeasurement.py` - абстрактный класс множественного измерения
- `Measurement.py` - измерение
- `DirectMultipleMeasurement.py` - прямое многократное измерение
- `IndirectMultipleMeasurement.py` - [nogui] косвенное многократное измерение
- `LinearMultipleMeasurement.py` - измерения в линейной зависимости (МНК)
- `Drawer.py` - статичный класс рисования графиков
- `Expression.py` - подсчёт косвенного измерения по выражению через sympy
- `MeasException.py` - исключения
- `Tools.py` - [nogui] генератор латеха

### Примеры:
- `MKN.py` - GUI постройка МКН 
- `lab1.04.ipynb` и `latex4.xml` - Лаба 1.04 с использование библиотеки
- `lab1.05.ipynb` и `latex4.xml` - Лаба 1.05 с использование библиотеки

### Зависимости
- matplotlib
- sympy
- tkinter
- peewee
