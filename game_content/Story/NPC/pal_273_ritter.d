
instance PAL_273_RITTER(NPC_DEFAULT)
{
	name[0] = NAME_RITTER;
	guild = GIL_PAL;
	id = 273;
	voice = 4;
	flags = 0;
	npctype = NPCTYPE_OCAMBIENT;
	b_setattributestochapter(self,4);
	fight_tactic = FAI_HUMAN_STRONG;
	EquipItem(self,itmw_2h_pal_sword);
	b_createambientinv(self);
	b_setnpcvisual(self,MALE,"Hum_Head_Bald",FACE_N_MORDRAG,BODYTEX_P,itar_pal_m);
	Mdl_SetModelFatness(self,2);
	Mdl_ApplyOverlayMds(self,"Humans_Militia.mds");
	b_givenpctalents(self);
	b_setfightskills(self,75);
	daily_routine = rtn_start_273;
};


func void rtn_start_273()
{
	ta_smalltalk(8,0,23,0,"OC_TO_MAGE");
	ta_smalltalk(23,0,8,0,"OC_KNECHTCAMP_02");
};

