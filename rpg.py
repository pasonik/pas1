from weapon import Weapon
from hero import Hero

# Задаю свойства оружию и героям
rapier = Weapon('Рапира "Ярость Бездны" ', 3, 450, 2.7, 70, 65)
claymore = Weapon('Меч безжалостной волны', 14, 1900, 0.8, 175, 50)
axe = Weapon('Топор раскола', 9, 2300, 0.9, 500, 10)
bow = Weapon('Лук растущей бури', 4, 600, 2.9, 0, 0)
sword = Weapon('Рубитель времени', 5, 1600, 1.1, 125, 50)

# Характеристики "скелета" персонажа
# 15000 (хп), 500 (броня), 1500 (сила атаки), 0 (доп. масса), 0 (доп. ловкость), 0 (доп крит. шанс)
knight = Hero('Иоанн Б.', 0, 0, 0, 0, 0, 0)
ninja = Hero('Си-Фу', -4000, -400, -250, -12,  1, 0)
archer = Hero('Усолант', -2000, -155, -300, -10, 0.7, 0)
heavy_knight = Hero('Безыменный страж', 3000, 200, 300, 15, -0.5, 0)
student = Hero('"Некто РРР"', -2500, 300, 150, -8, -0.2, 15)

# Коррекция статов героев
student.stats(rapier)
knight.stats(rapier)

# Вывожу инфу о героях и их оружиях на экран
student.print_info(rapier)
knight.print_info(rapier)

# Бой
student.fight(knight)
# Нужно сделать панель выбора классов и оружий с описанием классов и оружий, соответственно
