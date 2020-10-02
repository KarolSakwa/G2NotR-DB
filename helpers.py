from tkinter import *
from tkinter import ttk
import random
import sqlite3

def get_all_items(file_content):
    instances_raw = file_content.split("instance")
    instances_list = []
    for idx in range(len(instances_raw)):
        if idx != 0:
            instances_list.append(instances_raw[idx].split("(c_item)")[0].replace(" ", ""))
    return instances_list

def create_db():
    con = sqlite3.connect('G2.db')
    c = con.cursor() 
    c.execute("""
    CREATE TABLE npcs (
        instance text,
        file_content text,
        name text,
        guild text,
        id integer,
        flags text,
        is_main integer,
        attr_set text,
        strength integer,
        weapon_damage integer,
        hp_max integer,
        hp integer,
        melee_weapon text,
        armor text,
        total_melee_power real,
        protection_edge integer,
        total_power real,
        fight_skills integer,
        camp text,
        all_wps text,
        main_wp text
    )""")
    c.execute("""
    CREATE TABLE melee_weapons (
        instance text,
        dmg_const text,
        dmg integer,
        range integer
    )""")
    c.execute("""
    CREATE TABLE armors (
        instance text,
        prot_edge integer,
        prot_blunt integer,
        prot_point integer,
        prot_fire integer,
        prot_magic integer
    )""")
    con.commit()
    con.close()

def update_db():
    con = sqlite3.connect('G2.db')
    c = con.cursor() 
    for npc in all_npcs:
        c.execute("INSERT INTO npcs (instance, file_content, name, guild, id, flags, is_main, attr_set, strength, weapon_damage, hp_max, hp, fight_skills, melee_weapon, armor, total_melee_power, protection_edge, total_power, camp, main_wp) VALUES (:instance, :file_content, :name, :guild, :id, :flags, :is_main, :attr_set, :strength, :weapon_damage, :hp_max, :hp, :fight_skills, :melee_weapon, :armor, :total_melee_power, :protection_edge, :total_power, :camp, :main_wp)", 
            {
                'instance': npc.instance,
                'file_content': npc.file_content,
                'name': npc.name,
                'guild': npc.guild,
                'id': npc.id,
                'flags': npc.flags,
                'is_main': npc.is_main,
                'attr_set': npc.attr_set,
                'strength': npc.strength,
                'weapon_damage': npc.melee_weapon.dmg if npc.melee_weapon != None else 0,
                'hp_max': npc.hp_max,
                'hp': npc.hp,
                'fight_skills': npc.fight_skills,
                'melee_weapon': npc.melee_weapon.instance if npc.melee_weapon != None else None,
                'armor': npc.armor.instance,
                'total_melee_power': npc.total_melee_power,
                'protection_edge': npc.armor.prot_edge,
                'total_power': npc.total_power,
                'camp': npc.camp,
                'main_wp': npc.main_wp
            }
    )
    for m_weap in all_melee_weapons:
        c.execute("INSERT INTO melee_weapons (instance, dmg_const, dmg, range) VALUES (:instance, :dmg_const, :dmg, :range)",
            {
                'instance': m_weap.instance,
                'dmg_const': m_weap.get_damage_const(),
                'dmg': m_weap.dmg,
                'range': m_weap.range
            }
    )
    for armor in all_armors:
        c.execute("INSERT INTO armors (instance, prot_edge, prot_blunt, prot_point, prot_fire, prot_magic) VALUES (:instance, :prot_edge, :prot_blunt, :prot_point, :prot_fire, :prot_magic)",
            {
                'instance': armor.instance,
                'prot_edge': armor.prot_edge,
                'prot_blunt': armor.prot_blunt,
                'prot_point': armor.prot_point,
                'prot_fire': armor.prot_fire,
                'prot_magic': armor.prot_magic
            }
    )
    c.execute("SELECT instance, is_main, total_power FROM npcs ORDER BY total_power DESC")
    npc_results = c.fetchall()
    c.execute("SELECT *, oid FROM melee_weapons")
    mw_results = c.fetchall()
    c.execute("SELECT *, oid FROM armors")
    armor_results = c.fetchall()
    print_npc_res = ''
    print_mw_res = ''
    print_armor_res = ''
    idx = 1
    for result in npc_results:
        if result[1] == 1:
            print_npc_res += str(idx) + ". " + str(result[0]) + ": " + str(result[2]) + "\n"
            idx += 1

    for result in mw_results:
        print_mw_res += "\n" + str(result) + "\n"
    for result in armor_results:
        print_armor_res += "\n" + str(result) + "\n"
    with open('C:\\Users\\krolg\\Desktop\\hlp.txt', 'a') as f:
        f.write(print_npc_res)
        #f.write(print_mw_res)
        #f.write(print_armor_res)
    con.commit()
    con.close()    