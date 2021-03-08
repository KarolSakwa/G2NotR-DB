from helpers.helpers import get_all_items
from helpers.constants import *

class Armor:
    def __init__(self, instance):
        self.instance = instance
        self.file_content = self.get_file_content()
        self.prot_edge = self.get_prot_edge()
        self.prot_blunt = self.get_prot_blunt()
        self.prot_point = self.get_prot_point()
        self.prot_fire = self.get_prot_fire()
        self.prot_magic = self.get_prot_magic()

    def __str__(self):
        return '{}'.format(self.instance)

    def get_file_content(self):
        return open(armor_filepath, 'r').read().lower() if self.instance in open(armor_filepath, 'r').read().lower() else open(addon_armor_filepath, 'r').read().lower()

    def get_file_content_part(self):
        return self.get_file_content().split("instance " + self.instance, 1)[1].split("};", 1)[0]

    def get_prot_edge(self):
        return int(self.get_file_content_part().split('protection[prot_edge] = ', 1)[1].split(';', 1)[0])
        
    def get_prot_blunt(self):
        return int(self.get_file_content_part().split('protection[prot_blunt] = ', 1)[1].split(';', 1)[0])
        
    def get_prot_point(self):
        return int(self.get_file_content_part().split('protection[prot_point] = ', 1)[1].split(';', 1)[0])
        
    def get_prot_fire(self):
        return int(self.get_file_content_part().split('protection[prot_fire] = ', 1)[1].split(';', 1)[0])
        
    def get_prot_magic(self):
        return int(self.get_file_content_part().split('protection[prot_magic] = ', 1)[1].split(';', 1)[0])

armor_file = open(armor_filepath, 'r').read().lower()
addon_armor_file = open(addon_armor_filepath, 'r').read().lower()
all_armor_instances = get_all_items(armor_file) + get_all_items(addon_armor_file)
all_armors = []
for instance in all_armor_instances:
    all_armors.append(Armor(instance))