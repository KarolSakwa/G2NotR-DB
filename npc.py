from melee_weapon import MeleeWeapon, all_weapon_instances
from armor import Armor, all_armor_instances
import glob
import re
import random

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
        return open('.\\game_content\\Story\\NPC\\{}.d'.format(self.instance), 'r').read().lower()

    def get_name(self):
        const_file = open('.\\game_content\\Story\\Text.d', 'r').read().lower()
        name_part = self.file_content.split("name[0] = ", 1)[1].split(";")[0].lower()
        return re.sub(r'[^a-zA-Z ]+', '', (self.file_content.split("name", 1)[1].split(";")[0])).title().replace("  ", "") if not "name" in re.sub(r'[^a-zA-Z ]+', '', (self.file_content.split("name", 1)[1].split(";")[0])) else re.findall(r'"([^"]*)"', const_file.split(name_part, 1)[1].split(";", 1)[0])[0].title()

    def get_guild(self):
        return re.sub(r'=', '', (self.file_content.split("guild", 1)[1].split(";", 1)[0]))

    def get_id(self):
        return int(self.file_content.split("id = ", 1)[1].split(";", 1)[0])

    def get_flags(self):
        return 0 if "npc_flag_immortal" not in self.file_content else 1

    def get_is_main(self):
        disallowed = ['name', 'robotnik', 'strażnik głównej bramy', 'właściciel gospody, ogrodnik', 'kucharz', 'strażnik domu sędziego', 'strażnik wrót', 'klucznik', 'strażnik', 'włóczęga', 'bandyta', 'herszt bandy', 'rozbójnik', 'rabuś', 'strażnik niewolników', 'farmer']
        return 0 if any(x in (re.sub(r'[^a-zA-Z ]+', '', (self.file_content.split("name", 1)[1].split(";")[0]))) for x in disallowed) else 1

    def get_attr_set(self):
        return int(re.findall(r'\d+', (self.file_content.split("b_setattributestochapter", 1)[1].split(";")[0]))[0]) if "b_setattributestochapter" in self.file_content else 0

    def get_attrs(self, attr_set, attr):
        if(attr_set == 0):
            attrs = {
                'level': 3,
                'strength': 10,
                'dexterity': 10,
                'mana_max': 1000,
                'mana': 1000,
                'hp_max': 40,
                'hp': 40,
            }
        elif(attr_set == 1):
            attrs = {
                'level': 10,
                'strength': 50,
                'dexterity': 50,    
                'mana_max': 1000, 
                'mana': 1000,  
                'hp_max': 160,  
                'hp': 160,
            }
        elif(attr_set == 2):
            attrs = {
                'level': 20,
                'strength': 100,
                'dexterity': 100,  
                'mana_max': 1000,  
                'mana': 1000,
                'hp_max': 280,    
                'hp': 280,
            }
        elif(attr_set == 3):
            attrs = {
                'level': 30,
                'strength': 125,
                'dexterity': 125,  
                'mana_max': 1000,  
                'mana': 1000,
                'hp_max': 400,    
                'hp': 400,
            }
        elif(attr_set == 4):    
            attrs = {
                'level': 40,  
                'strength': 150,
                'dexterity': 150, 
                'mana_max': 1000, 
                'mana': 1000,
                'hp_max': 520,   
                'hp': 520,
            }
        elif(attr_set == 5):    
            attrs = {
                'level': 50,
                'strength': 175,
                'dexterity': 175, 
                'mana_max': 1000, 
                'mana': 1000,
                'hp_max': 640,   
                'hp': 640,
            }
        elif(attr_set >= 6):        
            attrs = {
                'level': 60,
                'strength': 200,
                'dexterity': 200,  
                'mana_max': 1000,
                'mana': 1000,
                'hp_max': 760,
                'hp': 760,
            }
        if self.instance == "bdt_1090_addon_raven":
            attrs = {
                'level': 50,
                'strength': 50,
                'dexterity': 50,  
                'mana_max': 666666,
                'mana': 666666,
                'hp_max': 500,
                'hp': 500,
            }
        return attrs[attr]

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
        if self.instance == "bau_970_orlan" or self.instance == "bau_961_gaan" or self.instance == "mil_350_addon_martin" or self.instance == "vlk_410_baltram" or self.instance == "none_addon_114_lance_adw" or self.instance == "bau_4300_addon_cavalorn" or self.instance == "sld_805_cord": return MeleeWeapon("itmw_rangerstaff_addon")
        for instance in all_weapon_instances:
            if instance in self.file_content:
                return MeleeWeapon(instance)
        if 'itmw_1h_mace_l_01' not in self.file_content:
            return None
        return melee_weapon

        #return melee_weapon
                
    def get_armor(self):
        armor = Armor('itar_test')
        for instance in all_armor_instances:
            if instance in self.file_content:
                armor = Armor(instance)
        if self.instance == "vlk_449_lares" or self.instance == "bau_970_orlan" or self.instance == "bau_961_gaan" or self.instance == "mil_350_addon_martin" or self.instance == "vlk_410_baltram" or self.instance == "none_addon_114_lance_adw": armor = Armor("itar_ranger_addon")
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
            return winner.name + ' zwycięża! Pozostało życia: ' + str(winner_percent_left) + '%. \n Przebieg walki: \n' + self.name + ": " + fight_process_self + "\n" + other.name + ": " + fight_process_other
        else:
            if winner == self:
                return self.name + ' zwycięża! Pozostało życia: ' + str(round(float(self_hp_list[-2].replace("(crit)", "")) / (self.hp_max * 10) * 100)) + '%. \n Przebieg walki: \n' + self.name + ": " + fight_process_self[:-1] + "\n" + other.name + ": " + fight_process_other
            elif winner == other:
                return other.name + ' zwycięża! Pozostało życia: ' + str(round(float(other_hp_list[-2].replace("(crit)", "")) / (other.hp_max * 10) * 100)) + '%. \n Przebieg walki: \n' + self.name + ": " + fight_process_self + "\n" + other.name + ": " + fight_process_other[:-1]


all_npc_instances = glob.glob("E:/Gothic/G2 polskie skrypty/G2MDK-PolishScripts-master/game_content/Story/NPC/*.d")
all_npc_instances = [x.replace('.d', '').replace('E:/Gothic/G2 polskie skrypty/G2MDK-PolishScripts-master/game_content/Story/NPC\\', '') for x in all_npc_instances]
instances_to_remove = ['_FH', 'pir_1390_addon_inextremo_drpymonte', 'pir_1391_addon_inextremo_theflail', 'pir_1392_addon_inextremo_thomastheforger', 'pir_1393_addon_inextremo_unicorn', 'pir_1394_addon_inextremo_yellowpfeiffer', 'pir_1395_addon_inextremo_lutter', 'pir_1396_addon_inextremo_flex', 'pc_hero', 'pc_magetest', 'pc_levelinspektor', ]
for instance in instances_to_remove:
    if instance in all_npc_instances:
        all_npc_instances.remove(instance)
all_npcs = []
for npc_instance in all_npc_instances:
    npc = NPC(npc_instance)
    all_npcs.append(npc)