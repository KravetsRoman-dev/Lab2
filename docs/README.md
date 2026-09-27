# Lab2

Репозиторий содержит реализацию вычисления площади и периметра геометрических фигур: круга, прямоугольника и квадрата.

## Структура проекта

Проект состоит из трёх Python-модулей:

* `circle.py` — функции для работы с кругом;
* `rectangle.py` — функции для работы с прямоугольником;
* `square.py` — функции для работы с квадратом.

Каждый модуль содержит две функции:

* `area` — вычисляет площадь фигуры;
* `perimeter` — вычисляет периметр фигуры.

Все функции принимают параметры типа `float` и возвращают результат типа `float`.

### Используемые формулы

**Круг:**

* Площадь: `S = πr²`
* Периметр: `P = 2πr`

**Прямоугольник:**

* Площадь: `S = ab`
* Периметр: `P = 2(a + b)`

**Квадрат:**

* Площадь: `S = a²`
* Периметр: `P = 4a`

## Описание функций


### `circle.py`

#### `area(r: float) -> float`

Вычисляет площадь круга по заданному радиусу `r`.

**Пример вызова:**

```python
from circle import area

result = area(5.0)
print(result)
```

#### `perimeter(r: float) -> float`

Вычисляет длину окружности по заданному радиусу `r`.

**Пример вызова:**

```python
from circle import perimeter

result = perimeter(5.0)
print(result)
```

---


### `rectangle.py`

#### `area(a: float, b: float) -> float`

Вычисляет площадь прямоугольника по длинам его сторон `a` и `b`.

**Пример вызова:**

```python
from rectangle import area

result = area(5.0, 3.0)
print(result)
```

#### `perimeter(a: float, b: float) -> float`

Вычисляет периметр прямоугольника по длинам его сторон `a` и `b`.

**Пример вызова:**

```python
from rectangle import perimeter

result = perimeter(5.0, 3.0)
print(result)
```

---


### `square.py`

#### `area(a: float) -> float`

Вычисляет площадь квадрата по длине его стороны `a`.

**Пример вызова:**

```python
from square import area

result = area(5.0)
print(result)
```

#### `perimeter(a: float) -> float`

Вычисляет периметр квадрата по длине его стороны `a`.

**Пример вызова:**

```python
from square import perimeter

result = perimeter(5.0)
print(result)
```


## История изменений проекта

В таблице указаны основные изменения проекта. В последнюю строку необходимо добавить информацию о последнем коммите самостоятельно.

| Хеш коммита   | Название коммита     | Описание изменений             |
| ------------- | -------------------- | ------------------------------ |
| `a91ebd8`    | `Add docs directory`    | `Добавление директории для документации` |
| `2d305fd`    | `Create circle.py`    | `Создание файла circle.py с функционалом для круга` |
| `01fd5f4`    | `Add description for circle.py`    | `Добавление описания функций для circle.py` |
| `adaa4a3`    | `Create square.py`    | `Создание файла square.py с функционалом для квадрата` |
| `c3db1eb`    | `Add description for square.py`    | `Добавление описания функций для square.py` |
| `8cdbb33`    | `Create rectangle.py` | `Создание файла rectangle.py с функционалом для прямоугольника` |
| `3cc1484`    | `Add description for rectangle.py` | `Добавление описания функций для rectangle.py` |