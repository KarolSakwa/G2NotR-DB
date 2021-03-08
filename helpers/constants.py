# txt
column_names = ("Name", "Strength", "Weapon damage", "HP max", "Melee power", "Fight skills", "Protection - edge", "Total power")
edit_db_text = "Edit database"
browse_db_text = "Browse database"
show_all_npcs_text = "Show all NPCs"
create_db_text = "Create database"
update_db_text = "Update database"
show_db_text = "Show database"
select_fighter_text = "Select fighter"
fight_text = "FIGHT!"
select_new_fighters_text = "Select new fighters"
two_selected_npc_error = "You need to select two NPCs!"
fight_winner_text = ' zwycięża! Pozostało życia: '
fight_process_text = '%. \n Przebieg walki: \n'
# paths
npc_filepath_glob = "./game_content/Story/NPC/*.d"
armor_filepath = ".\\game_content\\Items\\IT_Armor.d"
addon_armor_filepath = '.\\game_content\\Items\IT_Addon_Armor.d'
melee_weapons_filepath = '.\\game_content\\Items\\IT_Melee_weapons.d'
addon_melee_weapons_filepath = '.\\game_content\\Items\\IT_Addon_Weapons.d'
mission_items_1_filepath = '.\\game_content\\Items\MissionItems_1.d'
mission_items_2_filepath = '.\\game_content\\Items\MissionItems_2.d'
mission_items_3_filepath = '.\\game_content\\Items\MissionItems_3.d'
mission_items_4_filepath = '.\\game_content\\Items\MissionItems_4.d'
mission_items_5_filepath = '.\\game_content\\Items\MissionItems_5.d'
mission_items_6_filepath = '.\\game_content\\Items\MissionItems_6.d'
tuning_melee_weapons_filepath = '.\\game_content\\Items\\Tuning_Melee_Weapons.d'
npc_filepath = '.\\game_content\\Story\\NPC\\{}.d'
text_filepath = '.\\game_content\\Story\\Text.d'
instances_to_remove = ['_FH', 'pir_1390_addon_inextremo_drpymonte', 'pir_1391_addon_inextremo_theflail', 'pir_1392_addon_inextremo_thomastheforger', 'pir_1393_addon_inextremo_unicorn', 'pir_1394_addon_inextremo_yellowpfeiffer', 'pir_1395_addon_inextremo_lutter', 'pir_1396_addon_inextremo_flex', 'pc_hero', 'pc_magetest', 'pc_levelinspektor']
disallowed_names = ['name', 'robotnik', 'strażnik głównej bramy', 'właściciel gospody, ogrodnik', 'kucharz', 'strażnik domu sędziego', 'strażnik wrót', 'klucznik', 'strażnik', 'włóczęga', 'bandyta', 'herszt bandy', 'rozbójnik', 'rabuś', 'strażnik niewolników', 'farmer']
ranger_instances = ["bau_970_orlan", "bau_961_gaan", "mil_350_addon_martin", "vlk_410_baltram", "none_addon_114_lance_adw", "bau_4300_addon_cavalorn", "sld_805_cord"]
attrs_set = {
    0: {
                'level': 3,
                'strength': 10,
                'dexterity': 10,
                'mana_max': 1000,
                'mana': 1000,
                'hp_max': 40,
                'hp': 40,
    }, 1: {
                'level': 10,
                'strength': 50,
                'dexterity': 50,    
                'mana_max': 1000, 
                'mana': 1000,  
                'hp_max': 160,  
                'hp': 160,
    }, 2: {
                'level': 20,
                'strength': 100,
                'dexterity': 100,  
                'mana_max': 1000,  
                'mana': 1000,
                'hp_max': 280,    
                'hp': 280,
    }, 3: {
                'level': 30,
                'strength': 125,
                'dexterity': 125,  
                'mana_max': 1000,  
                'mana': 1000,
                'hp_max': 400,    
                'hp': 400,
    }, 4: {
                'level': 40,  
                'strength': 150,
                'dexterity': 150, 
                'mana_max': 1000, 
                'mana': 1000,
                'hp_max': 520,   
                'hp': 520,
    }, 5: {
                'level': 50,
                'strength': 175,
                'dexterity': 175, 
                'mana_max': 1000, 
                'mana': 1000,
                'hp_max': 640,   
                'hp': 640,
    }, 6: {
                'level': 60,
                'strength': 200,
                'dexterity': 200,  
                'mana_max': 1000,
                'mana': 1000,
                'hp_max': 760,
                'hp': 760,
    }, "Raven": {
                'level': 50,
                'strength': 50,
                'dexterity': 50,  
                'mana_max': 666666,
                'mana': 666666,
                'hp_max': 500,
                'hp': 500,
    }
}