from classes.Melee_weapon import MeleeWeapon, all_weapon_instances
from classes.Armor import Armor, all_armor_instances
import glob
import re
import random
from helpers.constants import *

class NPC:
    def __init__(self, instance):
        self.instance = instance
        self.file_content = self.get_file_content()
        self.name = self.get_name()
        self.guild = self.get_guild()
        self.id = self.get_id()
        self.flags = self.get_flags()
        self.is_main = self.get_is_main()
        self.attr_set = self.get_attr_set()
        self.strength = self.get_strength()
        self.hp_max = self.get_hp_max()
        self.hp = self.get_hp()
        self.fight_skills = self.get_fight_skills()
        self.melee_weapon = self.get_melee_weapon()
        self.armor = self.get_armor()
        self.total_melee_power = self.get_total_melee_power()
        self.total_power = self.get_total_power()
        self.camp = self.get_camp()
        self.all_wps = self.get_all_wps()
        self.main_wp = self.get_main_wp()


    def __str__(self):
        return '{}'.format(self.instance)

#
    def get_file_content(self):
        return open(npc_filepath.format(self.instance), 'r').read().lower()

    def get_name(self):
        const_file = open(text_filepath, 'r').read().lower()
        name_part = self.file_content.split("name[0] = ", 1)[1].split(";")[0].lower()
        return re.sub(r'[^a-zA-Z ]+', '', (self.file_content.split("name", 1)[1].split(";")[0])).title().replace("  ", "") if not "name" in re.sub(r'[^a-zA-Z ]+', '', (self.file_content.split("name", 1)[1].split(";")[0])) else re.findall(r'"([^"]*)"', const_file.split(name_part, 1)[1].split(";", 1)[0])[0].title()

    def get_guild(self):
        return re.sub(r'=', '', (self.file_content.split("guild", 1)[1].split(";", 1)[0]))

    def get_id(self):
        return int(self.file_content.split("id = ", 1)[1].split(";", 1)[0])

    def get_flags(self):
        return 0 if "npc_flag_immortal" not in self.file_content else 1

    def get_is_main(self):
        return 0 if any(x in (re.sub(r'[^a-zA-Z ]+', '', (self.file_content.split("name", 1)[1].split(";")[0]))) for x in disallowed_names) else 1

    def get_attr_set(self):
        return int(re.findall(r'\d+', (self.file_content.split("b_setattributestochapter", 1)[1].split(";")[0]))[0]) if "b_setattributestochapter" in self.file_content else 0

    def get_attrs(self, attr_set_file, attr):
        if self.instance == "bdt_1090_addon_raven": return attrs_set["Raven"][attr]
        return attrs_set[attr_set_file][attr]

    def get_strength(self):
        return self.get_attrs(self.get_attr_set(), 'strength')

    def get_hp_max(self):
        return self.get_attrs(self.get_attr_set(), 'hp_max')

    def get_hp(self):
        return self.get_attrs(self.get_attr_set(), 'hp')

    def get_fight_skills(self):
        return int(self.file_content.split("b_setfightskills(self,", 1)[1].split(");", 1)[0])
        
    def get_melee_weapon(self):
        melee_weapon = MeleeWeapon('itmw_1h_mace_l_01')
        if self.instance in ranger_instances: return MeleeWeapon("itmw_rangerstaff_addon")
        for instance in all_weapon_instances:
            if instance in self.file_content:
                return MeleeWeapon(instance)
        if 'itmw_1h_mace_l_01' not in self.file_content:
            return None
        return melee_weapon
                
    def get_armor(self):
        armor = Armor('itar_test')
        for instance in all_armor_instances:
            if instance in self.file_content:
                armor = Armor(instance)
        if self.instance in ranger_instances[:-1]: armor = Armor("itar_ranger_addon")
        return armor
    
    def get_total_melee_power(self):
        if self.melee_weapon != None:
            return round((self.strength*1)+((self.melee_weapon.dmg*1 + (self.fight_skills*2))), 2)
        else:
            return self.strength/2

    def get_total_power(self):
        if self.melee_weapon != None:
            return round(self.total_melee_power*1.5 + self.armor.prot_edge*2 + self.hp_max/2)
        else:
            return round((self.total_melee_power*1 + self.armor.prot_edge*1.5 + self.hp_max/2)/1.2)

    def get_camp(self):
        camp = ''
        if self.instance.startswith("bau") or self.instance.startswith("sld"):
            camp = "bau"
        elif self.instance.startswith("bdt") and "addon" in self.instance:
            camp = "bdt"
        elif self.instance.startswith("kdf") or self.instance.startswith("nov"):
            camp = "mon"
        elif self.instance.startswith("mil") or self.instance.startswith("pal") or self.instance.startswith("vlk"):
            camp = "kho"
        elif self.instance.startswith("pir"):
            camp = "pir"
        else:
            camp = "other"
        return camp

    def get_all_wps(self):
        return (re.findall(r'"(.*?)"', self.file_content.split("func void rtn_", 1)[1])) if "func void rtn_" in self.file_content else "No wp"

    def get_main_wp(self):
        main_wp = ""
        for wp in self.all_wps:
            if wp.startswith("oc_") or wp.startswith("ow_") or wp.startswith("start"):
                main_wp = "old world"
                break
            elif wp.startswith("nw_"):
                main_wp = "world"
                break
            elif wp.startswith("bl_") or wp.startswith("adw_"):
                main_wp = "jarkendar"
                break
            elif wp.startswith("di_"):
                main_wp = "irdorath"
                break
        return main_wp

    def fight(self, other):
        self.hp *= 10
        other.hp *= 10
        other_hp_list = []
        self_hp_list = []
        while self.hp > 0 and other.hp > 0:
            crit_chances_1 = random.randint(1, 100)
            if self.melee_weapon != None:
                if crit_chances_1 <= self.fight_skills:
                    other.hp -= ((self.strength + self.melee_weapon.dmg)*2 - other.armor.prot_edge)
                    other_hp_list.append(str(round(other.hp, 2)))# + "(crit)"
                else:
                    other.hp -= ((self.strength + self.melee_weapon.dmg) - other.armor.prot_edge)
                    other_hp_list.append(str(round(other.hp, 2)))
            else: 
                if other.armor.prot_edge < self.strength:
                    other.hp -= (self.strength/2 - other.armor.prot_edge)
                else:
                    other.hp -= 1
                other_hp_list.append(str(round(other.hp, 2)))
            crit_chances_2 = random.randint(1,100)
            if other.melee_weapon != None:
                if crit_chances_2 <= other.fight_skills:
                    self.hp -= ((other.strength + other.melee_weapon.dmg)*2 - self.armor.prot_edge)
                    self_hp_list.append(str(round(self.hp, 2))) # +"(crit)"
                else:
                    self.hp -= ((other.strength + other.melee_weapon.dmg) - self.armor.prot_edge)
                    self_hp_list.append(str(round(self.hp, 2)))
            else: 
                if self.armor.prot_edge < other.strength:
                    self.hp -= (other.strength/2 - self.armor.prot_edge)
                else:
                    self.hp -= 1
                self_hp_list.append(str(round(self.hp, 2)))
        if self.hp > 0: winner = self
        elif other.hp > 0: winner = other
        else: winner = self if self.hp > other.hp else other
        winner_percent_left = round((winner.hp / (winner.hp_max * 10)) * 100) #if winner.hp > 0 else 
        fight_process_self = ""
        for hp in self_hp_list:
            fight_process_self += str(round((float(hp) / (self.hp_max * 10)) * 100)) + "%, "
        fight_process_other = ""
        for hp in other_hp_list:
            fight_process_other += str(round((float(hp) / (other.hp_max * 10)) * 100)) + "%, "
        if winner.hp > 0:
            return winner.name + fight_winner_text + str(winner_percent_left) + fight_process_text + self.name + ": " + fight_process_self + "\n" + other.name + ": " + fight_process_other
        else:
            if winner == self:
                return self.name + fight_winner_text + str(round(float(self_hp_list[-2].replace("(crit)", "")) / (self.hp_max * 10) * 100)) + fight_process_text + self.name + ": " + fight_process_self[:-1] + "\n" + other.name + ": " + fight_process_other
            elif winner == other:
                return other.name + fight_winner_text + str(round(float(other_hp_list[-2].replace("(crit)", "")) / (other.hp_max * 10) * 100)) + fight_process_text + self.name + ": " + fight_process_self + "\n" + other.name + ": " + fight_process_other[:-1]


all_npc_instances = glob.glob(npc_filepath_glob)
all_npc_instances = [x.replace('.d', '').replace('./game_content/Story/NPC\\', '') for x in all_npc_instances]
for instance in instances_to_remove:
    if instance in all_npc_instances:
        all_npc_instances.remove(instance)
all_npcs = []
for npc_instance in all_npc_instances:
    npc = NPC(npc_instance)
    all_npcs.append(npc)