Игра Google динозаврик (fan edition :D)
-------------------------------------------------------------------
**Цель игры: Вы управляете динозавриком и ваша цель бежать вперед и
не допустить столкновения с различными обьектами.**
-------------------------------------------------------------------
###Обьекты:

Имеющиеся:
-Камень

В разработке:
-кактус
-птеродактель(летающий тип обьекта)
-------------------------------------------------------------------
* Если происходит столкновение с обьектом игра ничинаеться заново.
* В игре будет предусмотрена таблица рекордов в которой игрок сможет
видеть свои результаты.
-------------------------------------------------------------------
###Управление:
SPACE, arrow_up - Прыжок
R_SHIFT, arrow_down - Пригнуться

-------------------------------------------------------------------

Описание классов:

1. Class Stone
2. Class Cactus
3. Class Dino

* Class Dino - Основной класс проекта, отвечающий за управление динозаврика.
Методы:
__init__ - инициализация
cut_sheet - обрезка каритнки для ее анимации
update - Обновление класса
jump - Прыжок динозаврика


* Class Cactus - класс обьекта отвечающий за появление припятстви в виде камня 
Методы:
__init__ - инициализация
draw - рисование спрайта
update - обновление класса


* Class Stone - класс обьекта отвечающий за появление припятстви в виде кактуса 
Методы:
__init__ - инициализация
draw - рисование спрайта
update - обновление класса

-------------------------------------------------------------------

Файловая структура проекта

Файл main.py - содержит в себе основной игровой цикл который запускает
все остальные классы проекта 
Классов в себе не содержит.

Файл dinozavr.py - содердит в себе все что касаеться класса Dino
Имеет класс Dino

Файл objects.py - содержит в себе классы припятствий.
Имеет классы Cactus и Stone

Файл game_parts.py - содрежит в себе все необходимые глабальные переменные
и вызываеться во всех py файлах проекта.

Папка data - папка для хранения всех текстур проекта.

records.txt - файл для записи рекордов поставленных игроком во время игры.