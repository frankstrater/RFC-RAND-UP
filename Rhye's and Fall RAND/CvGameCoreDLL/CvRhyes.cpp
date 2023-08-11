//Rhye

#include "CvGameCoreDLL.h"
#include "CvRhyes.h"

// rhyes.cpp


//Rhye - RFCRAND
//int EARTH_X = GC.getMapINLINE().getGridWidthINLINE();
//int EARTH_Y = GC.getMapINLINE().getGridHeightINLINE();
int assignedCiv[31] = {8, 16, 7, 3, 13, 26, 5, 28, 17, 10, 21, 32, 1, 18, 30, 11, 9, 12, 29, 24, 20, 27, 15, 22, 2, 25, 0, 34, 35, 36, 6};
int assignedEarlyLeader[31] = {38, 2, 37, 17, 35, 10, 19, 24, 47, 52, 34, 39, 41, 46, 22, 28, 13, 8, 36, 51, 29, 23, 21, 16, 32, 31, 50, 53, 53, 42, 6};

int startingTurn[27] = {0, 0, 0, 0, 50, 84, 86, 90, 97, 121, 145, 177, 183, 187, 193, 196, 203, 205, 207, 213, 220, 234, 236, 240, 241, 249, 346}; 
int startingRange[27][2] = {
	{0,140}, //egy
	{0,220}, //ind
	{0,220}, //chi
	{0,140}, //bab
	{0,140}, //gre
	{0,140}, //per
	{0,140}, //car
	{0,140}, //rom
	{100,220}, //jap
	{0,220}, //eth
	{0,140}, //may
	{140,220}, //vik
	{140,220}, //ara
	{140,220}, //khm
	{180,280}, //spa
	{180,280}, //fra
	{180,280}, //eng
	{180,360}, //ger
	{180,280}, //rus
	{180,280}, //net
	{0,220}, //mal
	{180,280}, //por
	{0,220}, //inc
	{100,220}, //mon
	{0,220}, //azt
	{180,280}, //tur
	{260,360}}; //ame

	//100-140 classical, 180-220 medieval, 260-280 renaissance

//Alphabetical order:		  	  AME		ARA		AZT		BAB		XXX		CAR		XXX		CHI		EGY		 ENG	 ETH	 FRA	  GER	  GRE	   XXX	    INC		IND		JAP		KHM	    XXX	    MAL		MAY	     MON	 XXX     HOL      TUR	  PER	  POR     ROM	 RUS	 SPA	 XXX    VIK		XXX
char loadingTime[34][4] =     {   "60",   "20",   "35",    "0",     "X",   "5",    "X",     "0",    "0",    "30",    "10",   "25",   "30",   "2",     "X",     "35",    "0",    "10",   "20",   "X",   "35",    "15",   "35",    "X",    "30",   "35",    "5",   "35",   "5",   "30",  "25",   "X",   "20",  "X"};
char loadingTime600AD[34][4] = {  "30",   "0",   "15",     "0",     "X",    "0",    "X",     "0",    "0",    "10",    "0",    "5",    "10",   "0",     "X",     "15",    "0",    "0",    "2",    "X",   "15",    "0",    "15",    "X",    "10",   "15",    "0",    "15",   "0",    "10",  "5",    "X",   "0",   "X"};
char startingYear[34][6] =      {"1775 ", "620 ", "1200 ", "3000 ", "XXX ", "820 ", "XXX ", "3000 ", "3000 ", "820 ", "295 ", "750 ", "840 ", "1600 ", "XXX ", "1150 ", "3000 ", "655 ", "660 ", "XXX ", "980 ", "65 ", "1190 ", "XXX ", "920 ", "1280 ", "850 ", "1130 ", "760 ", "860 ", "720 ", "XXX ", "545 ", "XXX "};
bool startingEra[34] =		    {true,   true,   true,   false,   false,   false,  false,   false,   false,   true,  false,   true,   true,   false,   false,   true,   false,  false,  true,  false,  true,   true,  true,   false,    true,   true,   false,   true,  false,  true,  true,  false,   true,  false};   //AD or BC
char startingYear600AD[34][6] = {"1775 ", "600 ", "1200 ", "3000 ", "XXX ", "820 ", "XXX ", "600 ", "3000 ", "820 ", "295 ", "750 ", "840 ", "1600 ", "XXX ", "1150 ", "3000 ", "600 ", "660 ", "XXX ", "980 ", "65 ", "1190 ", "XXX ", "920 ", "1280 ", "850 ", "1130 ", "760 ", "860 ", "720 ", "XXX ", "600 ", "XXX "};
bool startingEra600AD[34] =		{true,   true,   true,   false,   false,   false,  false,   true,   false,   true,  false,   true,   true,   false,   false,   true,   false,   true,  true,  false,  true,   false,  true,   false,    true,   true,   false,   true,  false,  true,  true,  false,     true,  false};   //AD or BC


char uniquePower[34][2][16]  = {
	{"TXT_KEY_UP_AME", "TXT_KEY_UP_AME2"},
	{"TXT_KEY_UP_ARA", "TXT_KEY_UP_ARA2"},
	{"TXT_KEY_UP_AZT", "TXT_KEY_UP_AZT2"},
	{"TXT_KEY_UP_BAB", "TXT_KEY_UP_BAB2"},
	{"XXX", "XXX"},
	{"TXT_KEY_UP_CAR", "TXT_KEY_UP_CAR2"},
	{"XXX", "XXX"},
	{"TXT_KEY_UP_CHI", "TXT_KEY_UP_CHI2"},
	{"TXT_KEY_UP_EGY", "TXT_KEY_UP_EGY2"},
	{"TXT_KEY_UP_ENG", "TXT_KEY_UP_ENG2"},
	{"TXT_KEY_UP_ETH", "TXT_KEY_UP_ETH2"},
	{"TXT_KEY_UP_FRA", "TXT_KEY_UP_FRA2"},
	{"TXT_KEY_UP_GER", "TXT_KEY_UP_GER2"},
	{"TXT_KEY_UP_GRE", "TXT_KEY_UP_GRE2"},
	{"XXX", "XXX"},
	{"TXT_KEY_UP_INC", "TXT_KEY_UP_INC2"},
	{"TXT_KEY_UP_IND", "TXT_KEY_UP_IND2"},
	{"TXT_KEY_UP_JAP", "TXT_KEY_UP_JAP2"},
	{"TXT_KEY_UP_KHM", "TXT_KEY_UP_KHM2"},
	{"XXX", "XXX"},
	{"TXT_KEY_UP_MAL", "TXT_KEY_UP_MAL2"},
	{"TXT_KEY_UP_MAY", "TXT_KEY_UP_MAY2"},
	{"TXT_KEY_UP_MON", "TXT_KEY_UP_MON2"},
	{"XXX", "XXX"},
	{"TXT_KEY_UP_HOL", "TXT_KEY_UP_HOL2"},
	{"TXT_KEY_UP_TUR", "TXT_KEY_UP_TUR2"},
	{"TXT_KEY_UP_PER", "TXT_KEY_UP_PER2"},
	{"TXT_KEY_UP_POR", "TXT_KEY_UP_POR2"},
	{"TXT_KEY_UP_ROM", "TXT_KEY_UP_ROM2"},
	{"TXT_KEY_UP_RUS", "TXT_KEY_UP_RUS2"},
	{"TXT_KEY_UP_SPA", "TXT_KEY_UP_SPA2"},
	{"XXX", "XXX"},	
	{"TXT_KEY_UP_VIK", "TXT_KEY_UP_VIK2"},
	{"XXX", "XXX"}};


char uniqueGoals[34][3][18]  = {
	{"TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3"},
	{"TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"},
	{"TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"},
	{"TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2", "TXT_KEY_UHV_BAB3"},
	{"XXX", "XXX", "XXX"},
	{"TXT_KEY_UHV_CAR1", "TXT_KEY_UHV_CAR2", "TXT_KEY_UHV_CAR3"},
	{"XXX", "XXX", "XXX"},
	{"TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"},
	{"TXT_KEY_UHV_EGY1", "TXT_KEY_UHV_EGY2", "TXT_KEY_UHV_EGY3"},
	{"TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"},
	{"TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"},
	{"TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"},
	{"TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"},
	{"TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2", "TXT_KEY_UHV_GRE3"},
	{"XXX", "XXX", "XXX"},
	{"TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2", "TXT_KEY_UHV_INC3"},
	{"TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"},
	{"TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"},
	{"TXT_KEY_UHV_KHM1", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"},
	{"XXX", "XXX", "XXX"},
	{"TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2", "TXT_KEY_UHV_MAL3"},
	{"TXT_KEY_UHV_MAY1", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"},
	{"TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"},
	{"XXX", "XXX", "XXX"},
	{"TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"},
	{"TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"},
	{"TXT_KEY_UHV_PER1", "TXT_KEY_UHV_PER2", "TXT_KEY_UHV_PER3"},
	{"TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"},
	{"TXT_KEY_UHV_ROM1", "TXT_KEY_UHV_ROM2", "TXT_KEY_UHV_ROM3"},
	{"TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"},
	{"TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"},
	{"XXX", "XXX", "XXX"},
	{"TXT_KEY_UHV_VIK1", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"},
	{"XXX", "XXX", "XXX"}};



char rating[34][6][15]  = {
//		    TRA				 PRO				CUL					GRO				S.S.
//America
	{"TXT_KEY_4STARS", "TXT_KEY_5STARS", "TXT_KEY_1STAR", "TXT_KEY_5STARS", "TXT_KEY_1STAR" },
//Arabia
	{"TXT_KEY_4STARS", "TXT_KEY_1STAR", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS" },
//Aztec
	{"TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_1STAR" },
//Babylonia
	{"TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS" },
//
	{"XXX", "XXX", "XXX", "XXX", "XXX"},
//Carthage
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS" },
//
	{"XXX", "XXX", "XXX", "XXX", "XXX"},
//China
	{"TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_3STARS" },
//Egypt
	{"TXT_KEY_3STARS", "TXT_KEY_1STAR", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS" },
//England
	{"TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS" },
//Ethiopia
	{"TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS"},
//France
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS", "TXT_KEY_2STARS" },
//Germany
	{"TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_3STARS" },
//Greece
	{"TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS" },
//
	{"XXX", "XXX", "XXX", "XXX", "XXX"},
//Inca
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_1STAR" },
//India
	{"TXT_KEY_4STARS", "TXT_KEY_1STAR", "TXT_KEY_5STARS", "TXT_KEY_1STAR", "TXT_KEY_4STARS" },
//Japan
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS" },
//Khmer
	{"TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS"},
//
	{"XXX", "XXX", "XXX", "XXX", "XXX"},
//Mali
	{"TXT_KEY_5STARS", "TXT_KEY_1STAR", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS" },
//Maya
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_1STAR"},
//Mongolia
	{"TXT_KEY_1STAR", "TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_4STARS" },
//
	{"XXX", "XXX", "XXX", "XXX", "XXX"},
//Netherlands
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_1STAR"},
//Turkey
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_5STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS" },
//Persia
	{"TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS" },
//Portugal
	{"TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_2STARS", "TXT_KEY_5STARS", "TXT_KEY_1STAR"},
//Rome
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS" },
//Russia
	{"TXT_KEY_1STAR", "TXT_KEY_4STARS", "TXT_KEY_2STARS", "TXT_KEY_4STARS", "TXT_KEY_5STARS" },
//Spain
	{"TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS", "TXT_KEY_3STARS" },
//
	{"XXX", "XXX", "XXX", "XXX", "XXX"},
//Vikings
	{"TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_2STARS", "TXT_KEY_3STARS", "TXT_KEY_4STARS" },
//
	{"XXX", "XXX", "XXX", "XXX", "XXX"}};


int turnPlayed[32] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};


int civSpreadFactor[32][7]  = {
//		JUD	 CHR  ISL  HIN  BUD  CON  TAO
//Egypt
	{	 70, 250, 350,  20,  20,  20,  20 },	//100, 200, 300,  20,  20,  20,  20  before removal of Aggressive trait
//India
	{	 20,  90, 180, 400, 180,  20,  60 },	// 20,  80, 150, 300, 100,  20,  40  before removal of Aggressive trait
//China
	{	 20,  80,  20,  20, 200, 300, 200 },
//Babylonia
	{	 50, 200, 350,  20,  20,  20,  20 },
//Greece
	{	 40, 300,  40,  70,  50,  20,  20 },
//Persia
	{	 70,  20, 300,  40,  40,  20,  20 },
//Carthage
	{	 80, 200, 400,  20,  20,  20,  20 },
//Rome
	{	 40, 300,  40,  20,  40,  20,  20 },
//Japan
	{	 20,  40,  20,  20, 300, 120, 100 },
//Ethiopia
	{	200, 400, 400,  80,  80,  80,  80 }, //was 80, 300, 300,  20,  20,  20,  20 before; increased to help with their UHV
//Maya
	{	 70, 300,  80,  80,  80,  80,  80 },
//Viking
	{	 40, 300,  80,  20,  40,  20,  20 },
//Arabia
	{	 40,  30, 400,  20,  20,  20,  20 },	
//Khmer
	{	 20,  40,  20,  80, 400,  80, 100 },
//Spain
	{	 80, 400, 100,  20,  40,  20,  20 },
//France
	{	 60, 300, 100,  20,  40,  20,  20 },
//England
	{	 70, 300,  80,  20,  40,  20,  20 },
//Germany
	{	 70, 300,  80,  20,  40,  20,  20 },
//Russia
	{	 70, 300,  40,  20,  40,  20,  20 },
//Holland
	{	120, 300,  40,  20,  20,  20,  20 },
//Mali
	{	 50,  90, 400,  20,  20,  20,  20 },
//Portugal
	{	 40, 400, 100,  20,  40,  20,  20 },
//Inca
	{	 70, 300,  80,  80,  80,  80,  80 },
//Mongolia
	{	 20, 120,  80,  20, 300, 100,  80 },
//Aztec
	{	 70, 400,  90,  90,  90,  90,  90 },
//Turkey
	{	 50,  80, 400,  20,  20,  20,  20 },
//America
	{	100, 300,  20,  20,  20,  20,  20 },
//Independent
	{	 80, 250, 250,  50, 100,  50,  40 },
//Independent2
	{	 80, 200, 200,  80, 150,  80,  80 },
//Native
	{	120, 200, 200,  80,  80,  80,  80 },
//Celtia
	{	 80, 300,  80,  20,  40,  20,  20 }, 
//Barbarian
	{	100, 100, 100, 100, 100, 100, 100 }};


int borders[27][27]  = { // 1 = share borders, 3 = close, 4 = quite close, 5 = distant
//		EGY	IND CHI BAB GRE PER CAR ROM JAP ETH MAY VIK ARA KHM SPA FRA ENG GER RUS HOL MAL POR INC MON AZT TUR AME
//Egypt
	{	 0,  5,  5,  4,  1,  4,  3,  4,  5,  1,  5,  5,  1,  5,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  4,  5 },
//India
	{	 5,  0,  4,  4,  5,  1,  5,  5,  5,  5,  5,  5,  4,  3,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5 },
//China
	{	 5,  4,  0,  5,  5,  5,  5,  5,  1,  5,  5,  5,  5,  3,  5,  5,  5,  5,  5,  5,  5,  5,  5,  1,  5,  5,  5 },
//Babylonia
	{	 4,  4,  5,  0,  4,  1,  5,  5,  5,  4,  5,  5,  1,  5,  5,  5,  5,  5,  1,  5,  4,  5,  5,  5,  5,  1,  5 },
//Greece
	{	 1,  5,  5,  4,  0,  4,  4,  1,  5,  4,  5,  5,  4,  5,  5,  5,  5,  4,  3,  5,  5,  5,  5,  5,  5,  1,  5 },
//Persia
	{	 4,  1,  5,  1,  4,  0,  5,  5,  5,  5,  5,  5,  1,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  5,  5,  4,  5 },
//Carthage
	{	 3,  5,  5,  5,  4,  5,  0,  3,  5,  4,  5,  5,  5,  5,  1,  5,  5,  5,  5,  5,  4,  3,  5,  5,  5,  5,  5 },
//Rome
	{	 4,  5,  5,  5,  1,  5,  3,  0,  5,  4,  5,  5,  5,  5,  4,  1,  5,  1,  5,  4,  5,  4,  5,  5,  5,  5,  5 },
//Japan
	{	 5,  5,  1,  5,  5,  5,  5,  5,  0,  5,  5,  5,  5,  4,  5,  5,  5,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5 },
//Ethiopia
	{	 1,  5,  5,  4,  4,  5,  4,  4,  5,  0,  5,  5,  1,  5,  5,  5,  5,  5,  5,  5,  3,  5,  5,  5,  5,  4,  5 },
//Maya
	{	 5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  0,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  1,  5,  5 },
//Viking
	{	 5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  0,  5,  5,  5,  5,  3,  1,  3,  1,  5,  5,  5,  5,  5,  5,  5 },
//Arabia
	{	 1,  4,  5,  1,  4,  1,  5,  5,  5,  1,  5,  5,  0,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  4,  5 },
//Khmer
	{	 5,  3,  3,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  0,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5 },
//Spain
	{	 5,  5,  5,  5,  5,  5,  1,  1,  5,  5,  5,  5,  5,  5,  0,  1,  5,  5,  5,  5,  5,  1,  5,  5,  5,  5,  5 },
//France
	{	 5,  5,  5,  5,  5,  5,  5,  1,  5,  5,  5,  5,  5,  5,  1,  0,  1,  1,  5,  1,  5,  4,  5,  5,  5,  5,  5 },
//England
	{	 5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  3,  5,  5,  5,  1,  0,  4,  5,  1,  5,  5,  5,  5,  5,  5,  5 },
//Germany
	{	 5,  5,  5,  5,  5,  5,  5,  1,  5,  5,  5,  1,  5,  5,  5,  1,  4,  0,  1,  1,  5,  5,  5,  5,  5,  4,  5 },
//Russia
	{	 5,  5,  5,  1,  3,  4,  5,  5,  5,  5,  5,  3,  5,  5,  5,  5,  5,  1,  0,  5,  5,  5,  5,  4,  5,  3,  5 },
//Holland
	{	 5,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5,  1,  5,  5,  5,  1,  1,  1,  5,  0,  5,  5,  5,  5,  5,  5,  5 },
//Mali
	{	 5,  5,  5,  5,  5,  5,  4,  5,  5,  3,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  0,  5,  5,  5,  5,  5,  5 },
//Portugal
	{	 5,  5,  5,  5,  5,  5,  3,  4,  5,  5,  5,  5,  5,  5,  1,  4,  5,  5,  5,  5,  5,  0,  5,  5,  5,  5,  5 },
//Inca
	{	 5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  0,  5,  5,  5,  5 },
//Mongolia
	{	 5,  4,  1,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  0,  5,  5,  5 },
//Aztec
	{	 5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  1,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  0,  5,  4 },
//Turkey
	{	 4,  5,  5,  1,  1,  4,  5,  5,  5,  4,  5,  5,  4,  5,  5,  5,  5,  4,  3,  5,  5,  5,  5,  5,  5,  0,  5 },
//America
	{	 5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  4,  5,  0 }};
//		EGY	IND CHI BAB GRE PER CAR ROM JAP ETH MAY VIK ARA KHM SPA FRA ENG GER RUS HOL MAL POR INC MON AZT TUR AME






// (dynamic civ names - not jdog's)
CvWString civDynamicNames[27][22]  = {
//				//people		monarchy		monarchy ext		monarchy mod		monarchy ext mod		republic			communism			fascism				islam monarchy		islam republic			vas. Persia			vas. Rome			vas. Arabia			vas. Spain				vas. France			vas. England		vas. Germany			vas. Russia			vas. Mongolia			vas. Turkey			vas. Chi/Jap/Khm	vassal generic					
//Egypt
	{	 "TXT_KEY_DN_EGY00", "TXT_KEY_DN_EGY01", "TXT_KEY_DN_EGY02", "TXT_KEY_DN_EGY03",  "TXT_KEY_DN_EGY04",  "TXT_KEY_DN_EGY05",  "TXT_KEY_DN_EGY06",  "TXT_KEY_DN_EGY07",  "TXT_KEY_DN_EGY08",  "TXT_KEY_DN_EGY09",  "TXT_KEY_DN_EGY10",  "TXT_KEY_DN_EGY11",  "TXT_KEY_DN_EGY12",  "TXT_KEY_DN_EGY13",  "TXT_KEY_DN_EGY14",  "TXT_KEY_DN_EGY15",  "TXT_KEY_DN_EGY16",  "TXT_KEY_DN_EGY17",  "TXT_KEY_DN_EGY18",  "TXT_KEY_DN_EGY19",  "TXT_KEY_DN_EGY20",  "TXT_KEY_DN_EGY21" },
//India
	{	 "TXT_KEY_DN_IND00", "TXT_KEY_DN_IND01", "TXT_KEY_DN_IND02", "TXT_KEY_DN_IND03",  "TXT_KEY_DN_IND04",  "TXT_KEY_DN_IND05",  "TXT_KEY_DN_IND06",  "TXT_KEY_DN_IND07",  "TXT_KEY_DN_IND08",  "TXT_KEY_DN_IND09",  "TXT_KEY_DN_IND10",  "TXT_KEY_DN_IND11",  "TXT_KEY_DN_IND12",  "TXT_KEY_DN_IND13",  "TXT_KEY_DN_IND14",  "TXT_KEY_DN_IND15",  "TXT_KEY_DN_IND16",  "TXT_KEY_DN_IND17",  "TXT_KEY_DN_IND18",  "TXT_KEY_DN_IND19",  "TXT_KEY_DN_IND20",  "TXT_KEY_DN_IND21" },
//China
	{	 "TXT_KEY_DN_CHI00", "TXT_KEY_DN_CHI01", "TXT_KEY_DN_CHI02", "TXT_KEY_DN_CHI03",  "TXT_KEY_DN_CHI04",  "TXT_KEY_DN_CHI05",  "TXT_KEY_DN_CHI06",  "TXT_KEY_DN_CHI07",  "TXT_KEY_DN_CHI08",  "TXT_KEY_DN_CHI09",  "TXT_KEY_DN_CHI10",  "TXT_KEY_DN_CHI11",  "TXT_KEY_DN_CHI12",  "TXT_KEY_DN_CHI13",  "TXT_KEY_DN_CHI14",  "TXT_KEY_DN_CHI15",  "TXT_KEY_DN_CHI16",  "TXT_KEY_DN_CHI17",  "TXT_KEY_DN_CHI18",  "TXT_KEY_DN_CHI19",  "TXT_KEY_DN_CHI20",  "TXT_KEY_DN_CHI21" },
//Babylonia
	{	 "TXT_KEY_DN_BAB00", "TXT_KEY_DN_BAB01", "TXT_KEY_DN_BAB02", "TXT_KEY_DN_BAB03",  "TXT_KEY_DN_BAB04",  "TXT_KEY_DN_BAB05",  "TXT_KEY_DN_BAB06",  "TXT_KEY_DN_BAB07",  "TXT_KEY_DN_BAB08",  "TXT_KEY_DN_BAB09",  "TXT_KEY_DN_BAB10",  "TXT_KEY_DN_BAB11",  "TXT_KEY_DN_BAB12",  "TXT_KEY_DN_BAB13",  "TXT_KEY_DN_BAB14",  "TXT_KEY_DN_BAB15",  "TXT_KEY_DN_BAB16",  "TXT_KEY_DN_BAB17",  "TXT_KEY_DN_BAB18",  "TXT_KEY_DN_BAB19",  "TXT_KEY_DN_BAB20",  "TXT_KEY_DN_BAB21" },
//Greece
	{	 "TXT_KEY_DN_GRE00", "TXT_KEY_DN_GRE01", "TXT_KEY_DN_GRE02", "TXT_KEY_DN_GRE03",  "TXT_KEY_DN_GRE04",  "TXT_KEY_DN_GRE05",  "TXT_KEY_DN_GRE06",  "TXT_KEY_DN_GRE07",  "TXT_KEY_DN_GRE08",  "TXT_KEY_DN_GRE09",  "TXT_KEY_DN_GRE10",  "TXT_KEY_DN_GRE11",  "TXT_KEY_DN_GRE12",  "TXT_KEY_DN_GRE13",  "TXT_KEY_DN_GRE14",  "TXT_KEY_DN_GRE15",  "TXT_KEY_DN_GRE16",  "TXT_KEY_DN_GRE17",  "TXT_KEY_DN_GRE18",  "TXT_KEY_DN_GRE19",  "TXT_KEY_DN_GRE20",  "TXT_KEY_DN_GRE21" },
//Persia
	{	 "TXT_KEY_DN_PER00", "TXT_KEY_DN_PER01", "TXT_KEY_DN_PER02", "TXT_KEY_DN_PER03",  "TXT_KEY_DN_PER04",  "TXT_KEY_DN_PER05",  "TXT_KEY_DN_PER06",  "TXT_KEY_DN_PER07",  "TXT_KEY_DN_PER08",  "TXT_KEY_DN_PER09",  "TXT_KEY_DN_PER10",  "TXT_KEY_DN_PER11",  "TXT_KEY_DN_PER12",  "TXT_KEY_DN_PER13",  "TXT_KEY_DN_PER14",  "TXT_KEY_DN_PER15",  "TXT_KEY_DN_PER16",  "TXT_KEY_DN_PER17",  "TXT_KEY_DN_PER18",  "TXT_KEY_DN_PER19",  "TXT_KEY_DN_PER20",  "TXT_KEY_DN_PER21" },
//Carthage
	{	 "TXT_KEY_DN_CAR00", "TXT_KEY_DN_CAR01", "TXT_KEY_DN_CAR02", "TXT_KEY_DN_CAR03",  "TXT_KEY_DN_CAR04",  "TXT_KEY_DN_CAR05",  "TXT_KEY_DN_CAR06",  "TXT_KEY_DN_CAR07",  "TXT_KEY_DN_CAR08",  "TXT_KEY_DN_CAR09",  "TXT_KEY_DN_CAR10",  "TXT_KEY_DN_CAR11",  "TXT_KEY_DN_CAR12",  "TXT_KEY_DN_CAR13",  "TXT_KEY_DN_CAR14",  "TXT_KEY_DN_CAR15",  "TXT_KEY_DN_CAR16",  "TXT_KEY_DN_CAR17",  "TXT_KEY_DN_CAR18",  "TXT_KEY_DN_CAR19",  "TXT_KEY_DN_CAR20",  "TXT_KEY_DN_CAR21" },
//Rome
	{	 "TXT_KEY_DN_ROM00", "TXT_KEY_DN_ROM01", "TXT_KEY_DN_ROM02", "TXT_KEY_DN_ROM03",  "TXT_KEY_DN_ROM04",  "TXT_KEY_DN_ROM05",  "TXT_KEY_DN_ROM06",  "TXT_KEY_DN_ROM07",  "TXT_KEY_DN_ROM08",  "TXT_KEY_DN_ROM09",  "TXT_KEY_DN_ROM10",  "TXT_KEY_DN_ROM11",  "TXT_KEY_DN_ROM12",  "TXT_KEY_DN_ROM13",  "TXT_KEY_DN_ROM14",  "TXT_KEY_DN_ROM15",  "TXT_KEY_DN_ROM16",  "TXT_KEY_DN_ROM17",  "TXT_KEY_DN_ROM18",  "TXT_KEY_DN_ROM19",  "TXT_KEY_DN_ROM20",  "TXT_KEY_DN_ROM21" },
//Japan
	{	 "TXT_KEY_DN_JAP00", "TXT_KEY_DN_JAP01", "TXT_KEY_DN_JAP02", "TXT_KEY_DN_JAP03",  "TXT_KEY_DN_JAP04",  "TXT_KEY_DN_JAP05",  "TXT_KEY_DN_JAP06",  "TXT_KEY_DN_JAP07",  "TXT_KEY_DN_JAP08",  "TXT_KEY_DN_JAP09",  "TXT_KEY_DN_JAP10",  "TXT_KEY_DN_JAP11",  "TXT_KEY_DN_JAP12",  "TXT_KEY_DN_JAP13",  "TXT_KEY_DN_JAP14",  "TXT_KEY_DN_JAP15",  "TXT_KEY_DN_JAP16",  "TXT_KEY_DN_JAP17",  "TXT_KEY_DN_JAP18",  "TXT_KEY_DN_JAP19",  "TXT_KEY_DN_JAP20",  "TXT_KEY_DN_JAP21" },
//Ethiopia
	{	 "TXT_KEY_DN_ETH00", "TXT_KEY_DN_ETH01", "TXT_KEY_DN_ETH02", "TXT_KEY_DN_ETH03",  "TXT_KEY_DN_ETH04",  "TXT_KEY_DN_ETH05",  "TXT_KEY_DN_ETH06",  "TXT_KEY_DN_ETH07",  "TXT_KEY_DN_ETH08",  "TXT_KEY_DN_ETH09",  "TXT_KEY_DN_ETH10",  "TXT_KEY_DN_ETH11",  "TXT_KEY_DN_ETH12",  "TXT_KEY_DN_ETH13",  "TXT_KEY_DN_ETH14",  "TXT_KEY_DN_ETH15",  "TXT_KEY_DN_ETH16",  "TXT_KEY_DN_ETH17",  "TXT_KEY_DN_ETH18",  "TXT_KEY_DN_ETH19",  "TXT_KEY_DN_ETH20",  "TXT_KEY_DN_ETH21" },
//Maya
	{	 "TXT_KEY_DN_MAY00", "TXT_KEY_DN_MAY01", "TXT_KEY_DN_MAY02", "TXT_KEY_DN_MAY03",  "TXT_KEY_DN_MAY04",  "TXT_KEY_DN_MAY05",  "TXT_KEY_DN_MAY06",  "TXT_KEY_DN_MAY07",  "TXT_KEY_DN_MAY08",  "TXT_KEY_DN_MAY09",  "TXT_KEY_DN_MAY10",  "TXT_KEY_DN_MAY11",  "TXT_KEY_DN_MAY12",  "TXT_KEY_DN_MAY13",  "TXT_KEY_DN_MAY14",  "TXT_KEY_DN_MAY15",  "TXT_KEY_DN_MAY16",  "TXT_KEY_DN_MAY17",  "TXT_KEY_DN_MAY18",  "TXT_KEY_DN_MAY19",  "TXT_KEY_DN_MAY20",  "TXT_KEY_DN_MAY21" },
//Viking
	{	 "TXT_KEY_DN_VIK00", "TXT_KEY_DN_VIK01", "TXT_KEY_DN_VIK02", "TXT_KEY_DN_VIK03",  "TXT_KEY_DN_VIK04",  "TXT_KEY_DN_VIK05",  "TXT_KEY_DN_VIK06",  "TXT_KEY_DN_VIK07",  "TXT_KEY_DN_VIK08",  "TXT_KEY_DN_VIK09",  "TXT_KEY_DN_VIK10",  "TXT_KEY_DN_VIK11",  "TXT_KEY_DN_VIK12",  "TXT_KEY_DN_VIK13",  "TXT_KEY_DN_VIK14",  "TXT_KEY_DN_VIK15",  "TXT_KEY_DN_VIK16",  "TXT_KEY_DN_VIK17",  "TXT_KEY_DN_VIK18",  "TXT_KEY_DN_VIK19",  "TXT_KEY_DN_VIK20",  "TXT_KEY_DN_VIK21" },
//Arabia
	{	 "TXT_KEY_DN_ARA00", "TXT_KEY_DN_ARA01", "TXT_KEY_DN_ARA02", "TXT_KEY_DN_ARA03",  "TXT_KEY_DN_ARA04",  "TXT_KEY_DN_ARA05",  "TXT_KEY_DN_ARA06",  "TXT_KEY_DN_ARA07",  "TXT_KEY_DN_ARA08",  "TXT_KEY_DN_ARA09",  "TXT_KEY_DN_ARA10",  "TXT_KEY_DN_ARA11",  "TXT_KEY_DN_ARA12",  "TXT_KEY_DN_ARA13",  "TXT_KEY_DN_ARA14",  "TXT_KEY_DN_ARA15",  "TXT_KEY_DN_ARA16",  "TXT_KEY_DN_ARA17",  "TXT_KEY_DN_ARA18",  "TXT_KEY_DN_ARA19",  "TXT_KEY_DN_ARA20",  "TXT_KEY_DN_ARA21" },
//Khmer
	{	 "TXT_KEY_DN_KHM00", "TXT_KEY_DN_KHM01", "TXT_KEY_DN_KHM02", "TXT_KEY_DN_KHM03",  "TXT_KEY_DN_KHM04",  "TXT_KEY_DN_KHM05",  "TXT_KEY_DN_KHM06",  "TXT_KEY_DN_KHM07",  "TXT_KEY_DN_KHM08",  "TXT_KEY_DN_KHM09",  "TXT_KEY_DN_KHM10",  "TXT_KEY_DN_KHM11",  "TXT_KEY_DN_KHM12",  "TXT_KEY_DN_KHM13",  "TXT_KEY_DN_KHM14",  "TXT_KEY_DN_KHM15",  "TXT_KEY_DN_KHM16",  "TXT_KEY_DN_KHM17",  "TXT_KEY_DN_KHM18",  "TXT_KEY_DN_KHM19",  "TXT_KEY_DN_KHM20",  "TXT_KEY_DN_KHM21" },
//Spain
	{	 "TXT_KEY_DN_SPA00", "TXT_KEY_DN_SPA01", "TXT_KEY_DN_SPA02", "TXT_KEY_DN_SPA03",  "TXT_KEY_DN_SPA04",  "TXT_KEY_DN_SPA05",  "TXT_KEY_DN_SPA06",  "TXT_KEY_DN_SPA07",  "TXT_KEY_DN_SPA08",  "TXT_KEY_DN_SPA09",  "TXT_KEY_DN_SPA10",  "TXT_KEY_DN_SPA11",  "TXT_KEY_DN_SPA12",  "TXT_KEY_DN_SPA13",  "TXT_KEY_DN_SPA14",  "TXT_KEY_DN_SPA15",  "TXT_KEY_DN_SPA16",  "TXT_KEY_DN_SPA17",  "TXT_KEY_DN_SPA18",  "TXT_KEY_DN_SPA19",  "TXT_KEY_DN_SPA20",  "TXT_KEY_DN_SPA21" },
//France
	{	 "TXT_KEY_DN_FRA00", "TXT_KEY_DN_FRA01", "TXT_KEY_DN_FRA02", "TXT_KEY_DN_FRA03",  "TXT_KEY_DN_FRA04",  "TXT_KEY_DN_FRA05",  "TXT_KEY_DN_FRA06",  "TXT_KEY_DN_FRA07",  "TXT_KEY_DN_FRA08",  "TXT_KEY_DN_FRA09",  "TXT_KEY_DN_FRA10",  "TXT_KEY_DN_FRA11",  "TXT_KEY_DN_FRA12",  "TXT_KEY_DN_FRA13",  "TXT_KEY_DN_FRA14",  "TXT_KEY_DN_FRA15",  "TXT_KEY_DN_FRA16",  "TXT_KEY_DN_FRA17",  "TXT_KEY_DN_FRA18",  "TXT_KEY_DN_FRA19",  "TXT_KEY_DN_FRA20",  "TXT_KEY_DN_FRA21" },
//England
	{	 "TXT_KEY_DN_ENG00", "TXT_KEY_DN_ENG01", "TXT_KEY_DN_ENG02", "TXT_KEY_DN_ENG03",  "TXT_KEY_DN_ENG04",  "TXT_KEY_DN_ENG05",  "TXT_KEY_DN_ENG06",  "TXT_KEY_DN_ENG07",  "TXT_KEY_DN_ENG08",  "TXT_KEY_DN_ENG09",  "TXT_KEY_DN_ENG10",  "TXT_KEY_DN_ENG11",  "TXT_KEY_DN_ENG12",  "TXT_KEY_DN_ENG13",  "TXT_KEY_DN_ENG14",  "TXT_KEY_DN_ENG15",  "TXT_KEY_DN_ENG16",  "TXT_KEY_DN_ENG17",  "TXT_KEY_DN_ENG18",  "TXT_KEY_DN_ENG19",  "TXT_KEY_DN_ENG20",  "TXT_KEY_DN_ENG21" },
//Germany
	{	 "TXT_KEY_DN_GER00", "TXT_KEY_DN_GER01", "TXT_KEY_DN_GER02", "TXT_KEY_DN_GER03",  "TXT_KEY_DN_GER04",  "TXT_KEY_DN_GER05",  "TXT_KEY_DN_GER06",  "TXT_KEY_DN_GER07",  "TXT_KEY_DN_GER08",  "TXT_KEY_DN_GER09",  "TXT_KEY_DN_GER10",  "TXT_KEY_DN_GER11",  "TXT_KEY_DN_GER12",  "TXT_KEY_DN_GER13",  "TXT_KEY_DN_GER14",  "TXT_KEY_DN_GER15",  "TXT_KEY_DN_GER16",  "TXT_KEY_DN_GER17",  "TXT_KEY_DN_GER18",  "TXT_KEY_DN_GER19",  "TXT_KEY_DN_GER20",  "TXT_KEY_DN_GER21" },
//Russia
	{	 "TXT_KEY_DN_RUS00", "TXT_KEY_DN_RUS01", "TXT_KEY_DN_RUS02", "TXT_KEY_DN_RUS03",  "TXT_KEY_DN_RUS04",  "TXT_KEY_DN_RUS05",  "TXT_KEY_DN_RUS06",  "TXT_KEY_DN_RUS07",  "TXT_KEY_DN_RUS08",  "TXT_KEY_DN_RUS09",  "TXT_KEY_DN_RUS10",  "TXT_KEY_DN_RUS11",  "TXT_KEY_DN_RUS12",  "TXT_KEY_DN_RUS13",  "TXT_KEY_DN_RUS14",  "TXT_KEY_DN_RUS15",  "TXT_KEY_DN_RUS16",  "TXT_KEY_DN_RUS17",  "TXT_KEY_DN_RUS18",  "TXT_KEY_DN_RUS19",  "TXT_KEY_DN_RUS20",  "TXT_KEY_DN_RUS21" },
//Holland
	{	 "TXT_KEY_DN_NED00", "TXT_KEY_DN_NED01", "TXT_KEY_DN_NED02", "TXT_KEY_DN_NED03",  "TXT_KEY_DN_NED04",  "TXT_KEY_DN_NED05",  "TXT_KEY_DN_NED06",  "TXT_KEY_DN_NED07",  "TXT_KEY_DN_NED08",  "TXT_KEY_DN_NED09",  "TXT_KEY_DN_NED10",  "TXT_KEY_DN_NED11",  "TXT_KEY_DN_NED12",  "TXT_KEY_DN_NED13",  "TXT_KEY_DN_NED14",  "TXT_KEY_DN_NED15",  "TXT_KEY_DN_NED16",  "TXT_KEY_DN_NED17",  "TXT_KEY_DN_NED18",  "TXT_KEY_DN_NED19",  "TXT_KEY_DN_NED20",  "TXT_KEY_DN_NED21" },
//Mali
	{	 "TXT_KEY_DN_MAL00", "TXT_KEY_DN_MAL01", "TXT_KEY_DN_MAL02", "TXT_KEY_DN_MAL03",  "TXT_KEY_DN_MAL04",  "TXT_KEY_DN_MAL05",  "TXT_KEY_DN_MAL06",  "TXT_KEY_DN_MAL07",  "TXT_KEY_DN_MAL08",  "TXT_KEY_DN_MAL09",  "TXT_KEY_DN_MAL10",  "TXT_KEY_DN_MAL11",  "TXT_KEY_DN_MAL12",  "TXT_KEY_DN_MAL13",  "TXT_KEY_DN_MAL14",  "TXT_KEY_DN_MAL15",  "TXT_KEY_DN_MAL16",  "TXT_KEY_DN_MAL17",  "TXT_KEY_DN_MAL18",  "TXT_KEY_DN_MAL19",  "TXT_KEY_DN_MAL20",  "TXT_KEY_DN_MAL21" },
//Portugal
	{	 "TXT_KEY_DN_POR00", "TXT_KEY_DN_POR01", "TXT_KEY_DN_POR02", "TXT_KEY_DN_POR03",  "TXT_KEY_DN_POR04",  "TXT_KEY_DN_POR05",  "TXT_KEY_DN_POR06",  "TXT_KEY_DN_POR07",  "TXT_KEY_DN_POR08",  "TXT_KEY_DN_POR09",  "TXT_KEY_DN_POR10",  "TXT_KEY_DN_POR11",  "TXT_KEY_DN_POR12",  "TXT_KEY_DN_POR13",  "TXT_KEY_DN_POR14",  "TXT_KEY_DN_POR15",  "TXT_KEY_DN_POR16",  "TXT_KEY_DN_POR17",  "TXT_KEY_DN_POR18",  "TXT_KEY_DN_POR19",  "TXT_KEY_DN_POR20",  "TXT_KEY_DN_POR21" },
//Inca
	{	 "TXT_KEY_DN_INC00", "TXT_KEY_DN_INC01", "TXT_KEY_DN_INC02", "TXT_KEY_DN_INC03",  "TXT_KEY_DN_INC04",  "TXT_KEY_DN_INC05",  "TXT_KEY_DN_INC06",  "TXT_KEY_DN_INC07",  "TXT_KEY_DN_INC08",  "TXT_KEY_DN_INC09",  "TXT_KEY_DN_INC10",  "TXT_KEY_DN_INC11",  "TXT_KEY_DN_INC12",  "TXT_KEY_DN_INC13",  "TXT_KEY_DN_INC14",  "TXT_KEY_DN_INC15",  "TXT_KEY_DN_INC16",  "TXT_KEY_DN_INC17",  "TXT_KEY_DN_INC18",  "TXT_KEY_DN_INC19",  "TXT_KEY_DN_INC20",  "TXT_KEY_DN_INC21" },
//Mongolia
	{	 "TXT_KEY_DN_MON00", "TXT_KEY_DN_MON01", "TXT_KEY_DN_MON02", "TXT_KEY_DN_MON03",  "TXT_KEY_DN_MON04",  "TXT_KEY_DN_MON05",  "TXT_KEY_DN_MON06",  "TXT_KEY_DN_MON07",  "TXT_KEY_DN_MON08",  "TXT_KEY_DN_MON09",  "TXT_KEY_DN_MON10",  "TXT_KEY_DN_MON11",  "TXT_KEY_DN_MON12",  "TXT_KEY_DN_MON13",  "TXT_KEY_DN_MON14",  "TXT_KEY_DN_MON15",  "TXT_KEY_DN_MON16",  "TXT_KEY_DN_MON17",  "TXT_KEY_DN_MON18",  "TXT_KEY_DN_MON19",  "TXT_KEY_DN_MON20",  "TXT_KEY_DN_MON21" },
//Aztec
	{	 "TXT_KEY_DN_AZT00", "TXT_KEY_DN_AZT01", "TXT_KEY_DN_AZT02", "TXT_KEY_DN_AZT03",  "TXT_KEY_DN_AZT04",  "TXT_KEY_DN_AZT05",  "TXT_KEY_DN_AZT06",  "TXT_KEY_DN_AZT07",  "TXT_KEY_DN_AZT08",  "TXT_KEY_DN_AZT09",  "TXT_KEY_DN_AZT10",  "TXT_KEY_DN_AZT11",  "TXT_KEY_DN_AZT12",  "TXT_KEY_DN_AZT13",  "TXT_KEY_DN_AZT14",  "TXT_KEY_DN_AZT15",  "TXT_KEY_DN_AZT16",  "TXT_KEY_DN_AZT17",  "TXT_KEY_DN_AZT18",  "TXT_KEY_DN_AZT19",  "TXT_KEY_DN_AZT20",  "TXT_KEY_DN_AZT21" },
//Turkey
	{	 "TXT_KEY_DN_TUR00", "TXT_KEY_DN_TUR01", "TXT_KEY_DN_TUR02", "TXT_KEY_DN_TUR03",  "TXT_KEY_DN_TUR04",  "TXT_KEY_DN_TUR05",  "TXT_KEY_DN_TUR06",  "TXT_KEY_DN_TUR07",  "TXT_KEY_DN_TUR08",  "TXT_KEY_DN_TUR09",  "TXT_KEY_DN_TUR10",  "TXT_KEY_DN_TUR11",  "TXT_KEY_DN_TUR12",  "TXT_KEY_DN_TUR13",  "TXT_KEY_DN_TUR14",  "TXT_KEY_DN_TUR15",  "TXT_KEY_DN_TUR16",  "TXT_KEY_DN_TUR17",  "TXT_KEY_DN_TUR18",  "TXT_KEY_DN_TUR19",  "TXT_KEY_DN_TUR20",  "TXT_KEY_DN_TUR21" },
//America
	{	 "TXT_KEY_DN_AME00", "TXT_KEY_DN_AME01", "TXT_KEY_DN_AME02", "TXT_KEY_DN_AME03",  "TXT_KEY_DN_AME04",  "TXT_KEY_DN_AME05",  "TXT_KEY_DN_AME06",  "TXT_KEY_DN_AME07",  "TXT_KEY_DN_AME08",  "TXT_KEY_DN_AME09",  "TXT_KEY_DN_AME10",  "TXT_KEY_DN_AME11",  "TXT_KEY_DN_AME12",  "TXT_KEY_DN_AME13",  "TXT_KEY_DN_AME14",  "TXT_KEY_DN_AME15",  "TXT_KEY_DN_AME16",  "TXT_KEY_DN_AME17",  "TXT_KEY_DN_AME18",  "TXT_KEY_DN_AME19",  "TXT_KEY_DN_AME20",  "TXT_KEY_DN_AME21" }};


int civDynamicNamesFlag[27] = 	{	 1,  1,  0,  1,  0,  1,  1,  0,  0,  1,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  1,  0 };
//									EGY	IND CHI BAB GRE PER CAR ROM JAP ETH MAY VIK ARA KHM SPA FRA ENG GER RUS HOL MAL POR INC MON AZT TUR AME
// 1 = REL, 0 = GOV

int civDynamicNamesEraThreshold[27] = { 2,  3,  4,  2,  2,  3,  2,  3,  4,  3,  3,  3,  4,  4,  4,  4,  4,  4,  4,  4,  3,  4,  3,  3,  3,  3,  4};


int startingLocationsClustering[27][27] = {  //RFCRAND -2 to +2
//		 EGY  IND  CHI  BAB  GRE  PER  CAR  ROM  JAP  ETH  MAY  VIK  ARA  KHM  SPA  FRA  ENG  GER  RUS  HOL  MAL  POR  INC  MON  AZT  TUR  AME
//Egypt
	{	  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//India
	{	  1,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//China
	{	 -1,   1,   0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Babylonia
	{	  2,   1,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Greece
	{	  1,   0,  -2,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Persia
	{	  1,   2,  -1,   2,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Carthage
	{	  2,  -1,  -2,   0,   1,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Rome
	{	  1,  -1,  -2,   0,   2,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Japan
	{	 -2,  -1,   2,  -2,  -2,  -2,  -2,  -2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Ethiopia
	{	  2,   0,  -2,   0,  -1,  -1,   0,  -1,  -2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Maya
	{	 -1,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Viking
	{	 -1,  -2,  -2,  -1,   0,  -1,  -1,   1,  -2,  -2,  -2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Arabia
	{	  2,   1,  -1,   2,   0,   1,   1,   0,  -2,   1,  -2,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Khmer
	{	 -1,   2,   1,  -1,  -2,   0,  -2,  -2,   1,  -1,  -2,  -2,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Spain
	{	 -1,  -1,  -2,  -1,   0,  -1,   1,   2,  -2,  -2,  -2,   0,   0,  -2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//France
	{	 -1,  -1,  -2,  -1,   0,  -1,   0,   2,  -2,  -2,  -2,   1,   0,  -2,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//England
	{	 -1,  -1,  -2,  -1,   0,  -1,   0,   1,  -2,  -2,  -2,   2,  -1,  -2,   1,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Germany
	{	 -1,  -1,  -2,  -1,   1,  -1,  -1,   2,  -2,  -2,  -2,   2,  -1,  -2,   1,   2,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Russia
	{	 -1,  -1,   0,   0,   2,   1,  -2,   0,   0,  -2,  -2,   2,   0,  -2,   0,   1,   1,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Holland
	{	 -1,  -1,  -2,  -1,   1,  -1,  -1,   1,  -2,  -2,  -2,   2,  -1,  -2,   1,   2,   2,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0 },
//Mali
	{	  2,  -1,  -2,   0,   0,  -1,   2,   0,  -2,   2,  -2,  -2,   0,  -2,   0,  -1,  -2,  -2,  -2,  -2,   0,   0,   0,   0,   0,   0,   0 },
//Portugal
	{	 -1,  -1,  -2,  -1,   0,  -1,   1,   1,  -2,  -2,  -2,   0,   0,  -2,   2,   2,   2,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0 },
//Inca
	{	 -1,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,   0,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,   0,   0,   0,   0,   0 },
//Mongolia
	{	 -1,   1,   2,  -1,  -1,   2,  -2,  -1,   2,  -2,  -2,  -1,   0,   1,  -2,  -2,  -2,  -1,   2,  -2,  -2,  -2,  -2,   0,   0,   0,   0 },
//Aztec
	{	 -1,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,   1,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,  -2,   0,  -2,   0,   0,   0 },
//Turkey
	{	  2,   0,  -1,   2,   2,   1,   0,   0,  -2,   0,  -2,  -1,   1,  -2,   0,   0,  -1,   0,   1,  -1,  -1,   0,  -2,   1,  -2,   0,   0 },
//America
	{	  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0 }
};
//		 EGY  IND  CHI  BAB  GRE  PER  CAR  ROM  JAP  ETH  MAY  VIK  ARA  KHM  SPA  FRA  ENG  GER  RUS  HOL  MAL  POR  INC  MON  AZT  TUR  AME


int settlersCoords[27][8] = { //RFCRAND
//		minlatSL	maxlatSL	minlat		maxlat		long		coastSL(0-5) targetcity   centrality
//coastSL: 0=very distant; 1=not coastal; 2=close to coastal; 3=coastal; 4=close to ocean; 5=coastal ocean
//Egypt
{         10,         30,         10,         35,         20,         2,         5,         0},
//India
{         00,         25,         00,         30,         40,         1,         5,         1},
//China
{         25,         55,         25,         60,         50,         1,         6,        -2},
//Babylonia
{         10,         30,         10,         35,         15,         1,         3,         1},
//Greece
{         20,         35,         10,         50,         50,         3,         5,         1}, //maxlatSL lowered from 40 to 35 because they'd end up too morth  //centrality should be 0 but they risk to steal a spot on the edge of the ocean to euro civs
//Persia
{         10,         30,         10,         40,         40,         0,         6,         1}, //coastSL 1 instead of 0, for ensuring space for Mediterranean civs
//Carthage
{         10,         30,         00,         50,         50,         3,         5,         1}, //centrality should be -1 but they risk to steal a spot on the edge of the ocean to euro civs
//Rome
{         20,         45,         30,         70,         50,         2,         6,         1},
//Japan
{         40,         70,         00,         70,         40,         3,         5,        -2},
//Ethiopia
{         00,         20,         00,         25,         15,         0,         3,         0},
//Maya
{         00,         20,         00,         25,         15,         0,         3,         0}, //coastSL 0 instead of 1, for ensuring free American coasts
//Viking
{         60,         80,         40,         90,        100,         3,         5,         0}, //centrality should be -1 but this will help Russian position
//Arabia
{         10,         30,         00,         45,         70,         1,         6,         1},
//Khmer
{         00,         20,         00,         25,         15,         0,         3,        -1},
//Spain
{         25,         55,         00,         75,        100,         4,         4,        -2},
//France
{         30,         65,         10,         85,        100,         4,         4,        -1},
//England
{         40,         70,         20,         85,        100,         5,         4,        -2},
//Germany
{         40,         70,         35,         80,        100,         0,         6,         2},
//Russia
{         50,         80,         40,         90,         70,         0,         7,         2},
//Netherlands
{         35,         65,         00,         75,        100,         5,         2,        -2},
//Mali
{         00,         35,         00,         35,         15,         0,         3,         0},
//Portugal
{         25,         55,         00,         65,        100,         5,         2,        -2},
//Inca
{         00,         35,         00,         45,         20,         0,         5,         0}, //coastSL 0 instead of 2, for ensuring free American coasts
//Mongolia
{         30,         80,         10,         80,         70,         0,         7,         2},
//Aztec
{         00,         30,         00,         30,         15,         0,         3,         0}, //coastSL 0 instead of 1, for ensuring free American coasts
//Turkey
{         10,         40,         10,         45,         60,         1,         6,         1},
//America
{         40,         65,         25,         90,        100,         3,         6,         0}
};

int settlersModifiers[27][7] = { //RFCRAND
// continent	coast	river	mount	jungle	  desert	tundra
//Egypt
{     150,     100,     140,     100,      80,     160,      50}, //low jungle for allowing India to find a good spot
//India
{     130,     100,     120,     100,     140,      80,      50}, //low desert for allowing Babylonia to find a good spot
//China
{     150,     100,     100,     100,      90,      70,      50}, //low desert for allowing Babylonia to find a good spot
//Babylonia
{     150,      60,     140,     100,      80,     160,      50},
//Greece
{      70,     160,     100,     100,      80,      80,      50}, //low desert for allowing Persia to find a good spot
//Persia
{      80,      60,     100,     100,      80,     130,      50},
//Carthage
{      70,     160,     100,     100,      80,     100,      50},
//Rome
{     100,     110,     100,     100,      80,      80,      50},
//Japan
{      70,     120,     100,     100,      80,      80,      60},
//Ethiopia
{     150,      90,      70,     130,     130,     140,      50},
//Maya
{     150,      60,     100,      60,     130,     100,      50}, //coast 60 instead of 100, for ensuring free American coasts
//Viking
{      50,     120,     100,     130,      70,      50,     110},
//Arabia
{      80,     100,      70,     100,      70,     170,      50},
//Khmer
{     140,      90,     100,     100,     140,     100,      50},
//Spain
{      50,     140,     100,     100,      90,     100,      50},
//France
{      60,     140,     100,     100,      90,     100,      50},
//England
{      50,     160,     100,     100,      90,     100,      60},
//Germany
{     130,      90,     100,     100,      80,     100,      60},
//Russia
{     140,      70,     100,     100,      70,     100,      70},
//Netherlands
{      40,     160,     100,      80,      90,     100,      50},
//Mali
{     150,      90,     140,     100,     110,     150,      50},
//Portugal
{      40,     160,     100,     100,      90,     100,      50},
//Inca
{     150,      70,     100,     180,     110,     130,      50}, //coast 70 instead of 130, for ensuring free American coasts
//Mongolia
{     140,      70,     100,     100,      90,     130,      70},
//Aztec
{     150,      60,     100,     100,     130,     100,      50}, //coast 60 instead of 100, for ensuring free American coasts
//Turkey
{      80,     110,     100,     120,      80,     120,      50},
//America
{     100,     100,     100,     100,      90,     100,      60}
};


