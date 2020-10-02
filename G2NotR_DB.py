from tkinter import *
from tkinter import ttk
import random
from tkinter.ttk import Treeview
from PIL import ImageTk, ImageTk
from helpers import *
from npc import NPC
import re
import tkinter as tk
import sys



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('G2 NotR database')
        self.createWidgets()
        self.geometry("1280x720")
        self.iconbitmap('icon.ico')

    def createWidgets(self):
        my_notebook = ttk.Notebook()
        my_notebook.grid(pady=40, sticky="ns")
        global edit_db_tab
        edit_db_tab = Frame(my_notebook, width=1280, height=720)
        edit_db_tab.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        my_notebook.add(edit_db_tab, text="Edit database")
        global browse_db_tab
        browse_db_tab = Frame(my_notebook, width=1280, height=720)
        browse_db_tab.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        my_notebook.add(browse_db_tab, text="Browse database")
        global all_npc_tab
        all_npc_tab = Frame(my_notebook, width=1280, height=720)
        my_notebook.add(all_npc_tab, text="Show all NPCs")
        global create_db_btn
        create_db_btn = Button(edit_db_tab, text="Create database", command=create_db)
        create_db_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        global update_db_btn
        update_db_btn = Button(edit_db_tab, text="Update database", command=update_db)
        update_db_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        show_db_btn = Button(edit_db_tab, text="Show database", command=self.show_db)
        show_db_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        columns = ("Name", "Strength", "Weapon damage", "HP max", "Melee power", "Fight skills", "Protection - edge", "Total power")
        global npc_tree
        npc_tree=ttk.Treeview(all_npc_tab, columns=columns)
        npc_tree.place(x= 20, y= 0, width=1200, height=320)
        npc_tree.column("Name", width=100, minwidth=100)
        npc_tree.column("Strength", width=60, minwidth=60)
        npc_tree.column("Weapon damage", width=60, minwidth=60)
        npc_tree.column("HP max", width=60, minwidth=60)
        npc_tree.column("Melee power", width=60, minwidth=60)
        npc_tree.column("Fight skills", width=60, minwidth=60)
        npc_tree.column("Protection - edge", width=60, minwidth=60)
        npc_tree.column("Total power", width=100, minwidth=100)
        npc_scroll = Scrollbar(all_npc_tab, orient=VERTICAL, command=npc_tree.yview)
        npc_scroll.place(x= 1220, y= 0, width=20, height=320)
        npc_tree.configure(yscrollcommand=npc_scroll.set)
        for col in columns:
            npc_tree.heading(col, text=col, command=lambda _col=col: \
                     self.treeview_sort_column(npc_tree, _col, False))
        global selected
        selected = ""
        global selection_idx
        selection_idx = 0
        npc_tree.bind('<<TreeviewSelect>>', self.on_select)
        global select_npc_btn
        select_npc_btn = Button(all_npc_tab, text="Select fighter", command=self.print_selected)
        select_npc_btn.place(x= 20, rely= 0.55, width=200, height=30)
        fight_btn = Button(all_npc_tab, text="FIGHT!", command=self.start_fight)
        fight_btn.place(x= 230, rely= 0.55, width=200, height=30)


        con = sqlite3.connect('G2.db')
        c = con.cursor()
        c.execute("SELECT instance, name, strength, weapon_damage, hp_max, total_melee_power, fight_skills, protection_edge, total_power, is_main oid FROM npcs")
        npc_results = c.fetchall() 
        for result in npc_results:
            if result[9] == 1:
                npc_result=npc_tree.insert("", "end", text=result[0].upper(), values=(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]))


    def show_db(self):
        con = sqlite3.connect('G2.db')
        c = con.cursor() 
        c.execute("SELECT *, oid FROM npcs")
        records = c.fetchall()
        print(records)
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        query_label = Label(edit_db_tab, text=print_records)
        query_label.grid(row=4, column=0, columnspan=2)
        con.commit()
        con.close()

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            l.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))     


    def on_select(self, event):
        global selected
        selected = npc_tree.item(event.widget.selection())['text'].lower()
        
    def print_selected(self):
        global selection_idx
        if selection_idx == 0:
            global selected_npc_1
            global info_1
            selected_npc_1 = NPC(selected)
            selected_npc_1_melee_power = selected_npc_1.melee_weapon.dmg if selected_npc_1.melee_weapon != None else 0
            info_1 = Label(all_npc_tab, text=selected_npc_1.name + " - Strength: " + str(selected_npc_1.strength) + ", Weapon damage: " + str(selected_npc_1_melee_power)  + ", HP max: " + str(selected_npc_1.hp_max) + ", Melee power: " + str(selected_npc_1.total_melee_power) + ", Fight skills: " + str(selected_npc_1.fight_skills) + ", Protection - edge: " + str(selected_npc_1.armor.prot_edge) + ", Total power: " + str(selected_npc_1.total_power) + "\nvs.\n")
            info_1.place(x=0, y=330, width=800, height=50)
        elif selection_idx == 1:
            global selected_npc_2
            global info_2
            selected_npc_2 = NPC(selected)
            selected_npc_2_melee_power = selected_npc_2.melee_weapon.dmg if selected_npc_2.melee_weapon != None else 0
            info_2 = Label(all_npc_tab, text=selected_npc_2.name + " - Strength: " + str(selected_npc_2.strength) + ", Weapon damage: " + str(selected_npc_2_melee_power)  + ", HP max: " + str(selected_npc_2.hp_max) + ", Melee power: " + str(selected_npc_2.total_melee_power) + ", Fight skills: " + str(selected_npc_2.fight_skills) + ", Protection - edge: " + str(selected_npc_2.armor.prot_edge) + ", Total power: " + str(selected_npc_2.total_power))
            info_2.place(x=0, y=360, width=800, height=25)
        else: 
            info_3 = Label(all_npc_tab, text="You need to select two NPCs!")
            info_3.place(x=0, y=380, width=250, height=25)
            all_npc_tab.after(5000, info_3.destroy)
        selection_idx += 1

    def clear_selection(self):
        global selection_idx
        selected_npc_1 = ""
        selected_npc_2 = ""
        selection_idx = 0
        info_1.destroy()
        info_2.destroy()
        fight_result.destroy()
        select_npc_btn = Button(all_npc_tab, text="Select fighter", command=self.print_selected)
        select_npc_btn.place(x= 20, rely= 0.55, width=200, height=30)    

    def start_fight(self):
        global fight_result
        fight_result = Label(all_npc_tab, text=selected_npc_1.fight(selected_npc_2))
        selected_npc_1.hp = selected_npc_1.hp_max
        selected_npc_2.hp = selected_npc_2.hp_max
        fight_result.place(relx=0.05, rely=0.65, width=1250, height=150)
        select_npc_btn.destroy()
        new_fight_btn = Button(all_npc_tab, text="Select new fighters", command=self.clear_selection)
        new_fight_btn.place(x=20, rely=0.55, width=200, height=30)





Application().mainloop()


