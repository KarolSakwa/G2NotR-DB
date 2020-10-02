from helpers import get_all_items

class MeleeWeapon:
    def __init__(self, instance):
        self.instance = instance
        self.file_content = self.get_file_content()
        self.dmg = self.get_dmg()
        self.range = self.get_range()

    def __str__(self):
        return '{}'.format(self.instance)

    def get_file_content(self):
        if self.instance in open('.\\game_content\\Items\\IT_Melee_weapons.d', 'r').read().lower():
            return open('.\\game_content\\Items\\IT_Melee_weapons.d', 'r').read().lower()
        elif self.instance in open('.\\game_content\\Items\\IT_Addon_Weapons.d', 'r').read().lower():
            return open('.\\game_content\\Items\IT_Addon_Weapons.d', 'r').read().lower()
        elif self.instance in open('.\\game_content\\Items\MissionItems_1.d', 'r').read().lower():
            return open('.\\game_content\\Items\MissionItems_1.d', 'r').read().lower()
        elif self.instance in open('.\\game_content\\Items\MissionItems_2.d', 'r').read().lower():
            return open('.\\game_content\\Items\MissionItems_2.d', 'r').read().lower()
        elif self.instance in open('.\\game_content\\Items\MissionItems_3.d', 'r').read().lower():
            return open('.\\game_content\\Items\MissionItems_3.d', 'r').read().lower()
        elif self.instance in open('.\\game_content\\Items\MissionItems_4.d', 'r').read().lower():
            return open('.\\game_content\\Items\MissionItems_4.d', 'r').read().lower()
        elif self.instance in open('.\\game_content\\Items\MissionItems_5.d', 'r').read().lower():
            return open('.\\game_content\\Items\MissionItems_5.d', 'r').read().lower()
        else:
            return open('.\\game_content\\Items\MissionItems_6.d', 'r').read().lower()
    
    def get_damage_const(self):
        return self.get_file_content().split(self.instance, 1)[1].split("};", 1)[0].split("damagetotal = ", 1)[1].split(";", 1)[0]

    def get_const_file_content(self):
        return open('.\\game_content\\Items\\Tuning_Melee_Weapons.d', 'r').read().lower()

    def get_dmg(self):
        return int(self.get_const_file_content().split(self.get_damage_const() + " = ", 1)[1].split(";", 1)[0])
        
    def get_ranage_const(self):
        return self.get_file_content().split(self.instance, 1)[1].split("};", 1)[0].split("range = ", 1)[1].split(";", 1)[0]
        
    def get_range(self):
        return int(self.get_const_file_content().split(self.get_ranage_const() + " = ", 1)[1].split(";", 1)[0])

weapon_file = open('.\\game_content\\Items\\IT_Melee_weapons.d', 'r').read().lower()
addon_weapon_file = open('.\\game_content\\Items\IT_Addon_Weapons.d', 'r').read().lower()
mission_items_1_file = open('.\\game_content\\Items\MissionItems_1.d', 'r').read().lower()
mission_items_2_file = open('.\\game_content\\Items\MissionItems_2.d', 'r').read().lower()
mission_items_3_file = open('.\\game_content\\Items\MissionItems_3.d', 'r').read().lower()
mission_items_4_file = open('.\\game_content\\Items\MissionItems_4.d', 'r').read().lower()
mission_items_5_file = open('.\\game_content\\Items\MissionItems_5.d', 'r').read().lower()
mission_items_6_file = open('.\\game_content\\Items\MissionItems_6.d', 'r').read().lower()
all_mission_items = get_all_items(mission_items_1_file) + get_all_items(mission_items_2_file) + get_all_items(mission_items_3_file) + get_all_items(mission_items_4_file) + get_all_items(mission_items_5_file) + get_all_items(mission_items_6_file)
all_mission_weapons = []
for item in all_mission_items:
    if item.startswith("itmw"):
        all_mission_weapons.append(item)
all_weapon_instances = get_all_items(weapon_file) + get_all_items(addon_weapon_file) 
unnecessary = all_weapon_instances[-6:]
for x in unnecessary:
    all_weapon_instances.remove(x)
for mission_weapon in all_mission_weapons:
    all_weapon_instances.append(mission_weapon)
all_melee_weapons = []
for instance in all_weapon_instances:
    all_melee_weapons.append(MeleeWeapon(instance))