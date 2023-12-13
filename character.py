class Character:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def set_name(self, name):
        self.name = name

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

class Hero(Character):
    def __init__(self, name, id_number, level, loot):
        super().__init__(name, id_number)
        self.level = level
        self.loot = loot

    def set_level(self, level):
        self.level = level

    def set_loot(self, loot):
        self.loot = loot

    def get_level(self):
        return self.level

    def get_loot(self):
        return self.loot

class Boss(Character):
    def __init__(self, name, id_number, level, hp, attack_damage):
        super().__init__(name, id_number)
        self.level = level
        self.hp = hp
        self.attack_damage = attack_damage
        self.lifespan = 0

    def set_level(self, level):
        self.level = level

    def set_hp(self, hp):
        self.hp = hp

    def set_attack_damage(self, attack_damage):
        self.attack_damage = attack_damage

    def set_lifespan(self, lifespan):
        self.lifespan = lifespan

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def get_attack_damage(self):
        return self.attack_damage

    def get_lifespan(self):
        return self.hp / 300

