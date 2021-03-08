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

def create_tab(notebook, my_text):
    tab = Frame(notebook, width=1280, height=720)
    tab.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
    notebook.add(tab, text=my_text)
    return tab

def create_button(tab, my_text, command, row):
    button = Button(tab, text=my_text, command=command)
    button.grid(row=row, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
    return button

def display_data_from_db(tree):
    con = sqlite3.connect('G2.db')
    c = con.cursor()
    c.execute("SELECT instance, name, strength, weapon_damage, hp_max, total_melee_power, fight_skills, protection_edge, total_power, is_main oid FROM npcs")
    npc_results = c.fetchall() 
    for result in npc_results:
        if result[9] == 1:
            npc_result=tree.insert("", "end", text=result[0].upper(), values=(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))

def show_db_func(tab):
    con = sqlite3.connect('G2.db')
    c = con.cursor() 
    c.execute("SELECT *, oid FROM npcs")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(tab, text=print_records)
    query_label.grid(row=4, column=0, columnspan=2)
    con.commit()
    con.close()

def get_selected_npc_label_txt(npc):
    selected_npc_melee_power = npc.melee_weapon.dmg if npc.melee_weapon != None else 0
    return npc.name + " - Strength: " + str(npc.strength) + ", Weapon damage: " + str(selected_npc_melee_power)  + ", HP max: " + str(npc.hp_max) + ", Melee power: " + str(npc.total_melee_power) + ", Fight skills: " + str(npc.fight_skills) + ", Protection - edge: " + str(npc.armor.prot_edge) + ", Total power: " + str(npc.total_power)