from npc import NPC
from melee_weapon import all_mission_weapons, all_weapon_instances

class TestMeleeWeapon:
    def test_melee_weapon_instance_is_none(self):
        hyglas = NPC("kdf_510_hyglas")
        desired = None
        actual = hyglas.get_melee_weapon()
        assert desired == actual

    def test_last_mission_weapon_is_itmw_1h_ferrossword_mis(self):
        desired = 'itmw_1h_ferrossword_mis'
        actual = all_mission_weapons[-1]
        assert desired == actual

    def test_last_weapon_is_itmw_1h_ferrossword_mis(self):
        desired = 'itmw_1h_ferrossword_mis'
        actual = all_weapon_instances[-1]
        assert desired == actual