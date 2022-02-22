from random import randint


class Hero:
    # Шаблон персонажа(лвл ни на что не влияет)
    def __init__(self, name, lvl, health, armor, power, weapon):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.armor = armor
        self.power = power
        self.weight = 50
        # Общая сила учитывая силу оружия
        self.apower = self.power + weapon.atk
        # Подсчет ловкости засчепт параметров веса и скорости атаки оружия
        self.speed = (1 - ((self.armor / 10 + weapon.w_weight) / 100)) * weapon.atk_speed
        # Присвоил персонажу криты, чтобы не переписывать 2 раза функцию атаки для 2 персов
        self.crit_rate = weapon.crit_rate
        self.crit = weapon.crit

    def print_info(self, weap):
        # Инфа о созданном герое
        print('Овации для сегодняшнего героя', self.name, self.lvl + '-го уровня')
        print('Оружие:', weap.w_name)
        print('Уровень здоровья:', self.health)
        print('Сила героя:', self.apower)
        print('С уровнем защищенности', self.armor, )
        print('Коэффицент ловкости:', self.speed, '\n')
        print('Характеристики оружия', weap.w_name, '\nБазовый урон', weap.atk, '\nСкорость атаки', weap.atk_speed,
              '\nКритической урон', weap.crit, '%', '\nШанс критического удара', weap.crit_rate, '%\n\n')

    # Функция атаки
    def attack(self, knight):
        print('Нанесен удар! Герой', self.name, 'атаковал', knight.name, 'с силой удара', self.apower, '\n')
        # Подсчет вероятности крит удара
        ch = randint(1, 100)
        if ch >= self.crit_rate:
            # Крит не прошел
            knight.health -= self.apower - knight.armor
            print('Герой', knight.name, 'принял удар!\nУдар оставил рыцарю', knight.health, 'здоровья!\n')
        else:
            # Крит прошел, подсчет крита
            damage = (self.apower - knight.armor) * 1.5 * self.crit / 100
            knight.health -= damage
            print(self.name, 'Наносит критический урон и нанес рыцарю', damage, 'урона!\nУдар оставил рыцарю',
                  knight.health, 'здоровья!\n')
        # Просто чтобы оно не ушло сразу в конец кода
        input('Напишите что-нибудь, чтобы продолжить.')

    def parry(self, knight):
        # В случае непопадания в шанс удара
        print('Рыцарь', knight.name, 'парировал атаку ' + self.name + '!')
        input('Напишите что-нибудь, чтобы продолжить.')
    # Фаза каста атака и применения. И завершение если хп кого-то < 0

    def fight(self, knight):
        # Условие с количеством хп
        while self.health > 0 and knight.health > 0:
            # Переменная, чтобы не менять основную переменную
            punch_chance = self.speed
            # Если ловкость упадет до 0, то ход переходит к другому
            # хотел здесь сделать систему с увелечением шанса удара при каждом промахе, но связи с побочной переменной
            # и удобством в ее использовании я отказался от этой идеи

            while punch_chance > 0:
                # Если ловкость >1 идет 1 удар 100%
                if punch_chance > 1:
                    self.attack(knight)
                    punch_chance -= 1
                else:
                    # Иначе будет рулетка. Если, к примеру, в ловкости 0,8 выпадет рандомное число 0,77,
                    # то пройдет еще один удар. Иначе парирование удара(ничего не произойдет)
                    chance = randint(1, 100)
                    if chance < punch_chance * 100:
                        self.attack(knight)
                    else:
                        self.parry(knight)
                    # Обнуление, чтобы закончился цикл
                    punch_chance = 0
                # Если избил насмерть, то досрочно закончится цикл. Да, если пройдет вторая атака, то ты ударишь труп
                # и что?
                if knight.health <= 0:
                    print(knight.name, 'повержен! Овации рыцарю', self.name)
                    break
            # Я не уверен нужен ли этот break. Просто после него вроде как все заработало. Но если он не влияет ни на
            # что, то можешь убрать. Ниже такой же
            if knight.health <= 0:
                break

            # То же самое, но для второго героя. Т.е. self поменялся с knight, теперь второй бьет первого

            punch_chance = knight.speed
            while punch_chance > 0:
                if punch_chance > 1:
                    knight.attack(self)
                    punch_chance -= 1
                else:
                    chance = randint(1, 100)
                    if chance < punch_chance * 100:
                        knight.attack(self)
                    else:
                        knight.parry(self)
                    punch_chance = 0
                if self.health <= 0:
                    print(self.name, 'повержен! Овации рыцарю', knight.name)
                    break
            if self.health <= 0:
                break