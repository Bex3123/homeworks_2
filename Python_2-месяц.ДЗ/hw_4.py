from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    BLOCK_DAMAGE_AND_REVERT = 3
    HEAL = 4
    REVIVE = 5
    HACK = 6
    INSTANT_KILL = 7
    REFLECT = 8


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return (f'{self.__name} health: {self.__health} '
                f'damage: {self.__damage}')


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes: list):
        random_hero = choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes: list):
        for hero in heroes:
            if hero.health > 0:
                if (hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT
                        and self.__defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT):
                    hero.blocked_damage = int(self.damage / 5)
                    hero.health -= self.damage - hero.blocked_damage
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if type(ability) == SuperAbility:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss: Boss):
        boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss: Boss, heroes: list):
        coeff = randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage, boost_amount):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.__boost_amount = boost_amount

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage += self.__boost_amount
            print(f"Magic {self.name} boosted {hero.name}'s damage by {self.__boost_amount}")


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.heal_points = heal_points

    def apply_super_power(self, boss: Boss, heroes: list):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss: Boss, heroes: list):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted '
              f'damage to {self.__blocked_damage}')


class Witcher(Hero):
    def __init__(self, name, health, revive_chance):
        super().__init__(name, health, 0, SuperAbility.REVIVE)  # No damage
        self.__revive_chance = revive_chance
        self.__has_revived = False

    def apply_super_power(self, boss, heroes):
        if not self.__has_revived and randint(1, 100) <= self.__revive_chance:
            for hero in heroes:
                if hero.health <= 0 and hero != self:
                    hero.health = self.health
                    self.health = 0
                    print(f"Witcher {self.name} revived {hero.name}!")
                    self.__has_revived = True
                    break


class Hacker(Hero):
    def __init__(self, name, health, hack_amount):
        super().__init__(name, health, 0, SuperAbility.HACK)
        self.__hack_amount = hack_amount

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0:  # Hack every other round
            hero_to_heal = choice(heroes)
            boss.health -= self.__hack_amount
            hero_to_heal.health += self.__hack_amount
            print(f"Hacker {self.name} hacked {self.__hack_amount} health from Boss and gave it to {hero_to_heal.name}")


class SpitFire(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)
        self.__aggression_amount = 80

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0:
                self.damage += self.__aggression_amount
                print(f"Spitfire {self.name} shows aggression on {self.__aggression_amount} damage")


class King(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, 0, SuperAbility.INSTANT_KILL)
        self.__saitama_chance = 10

    def apply_super_power(self, boss: Boss, heroes: list):
        if randint(1, 100) <= self.__saitama_chance:
            print(f"King {self.name} summoned Saitama!")
            boss.health = 0



class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.REFLECT)


    def apply_super_power(self, boss, heroes):
        total_damage = sum([hero.damage for hero in heroes if hero != self])
        self.health -= total_damage // 5
        print(f'{self.name} took {total_damage // 5} damage for the team.')

        for hero in heroes:
            if hero != self:
                hero.attack(boss)
                hero.apply_super_power(boss, heroes)






round_number = 0


def start_game():
    boss = Boss('Roshan', 1000, 150)
    warrior_1 = Warrior('Charly', 270, 10)
    warrior_2 = Warrior('Arthur', 280, 15)
    magic = Magic('Loki', 290, 20, 5)
    berserk = Berserk('Thor', 260, 10)
    witcher = Witcher('Rubick', 260, 50)
    hacker = Hacker('Mirat', 280, 30)
    spitfire = SpitFire('Elza', 265, 10)
    king = King('Skeleton', 300, )
    golem = Golem('Stone', 500, 5)
    doc = Medic('Doc', 250, 5, 15)
    assistant = Medic('Assistant', 300, 5, 5)

    heroes_list = [warrior_1, warrior_2, doc, magic, berserk, witcher, hacker, spitfire, king, golem, assistant]
    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def play_round(boss: Boss, heroes: list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if (hero.health > 0 and boss.health > 0
                and boss.defence != hero.ability):
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def is_game_over(boss: Boss, heroes: list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def show_statistics(boss: Boss, heroes: list):
    print(f'ROUND - {round_number} ------------')
    print(boss)
    for hero in heroes:
        if hero.health <= 0:
            print(f'DEAD {hero}')
        else:
            print(hero)


start_game()
