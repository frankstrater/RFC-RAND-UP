//Rhye
#ifndef CVRHYES_H
#define CVRHYES_H

// rhyes.h
//Rhye - RFCRAND
//#define EARTH_X					(124)
//#define EARTH_Y					(68)


#define MAX_COM_SHRINE			(20)


#define EGYPT					(0)
#define INDIA					(1)
#define CHINA					(2)
#define BABYLONIA				(3)
#define GREECE					(4)
#define PERSIA					(5)
#define CARTHAGE				(6)
#define ROME					(7)
#define JAPAN					(8)
#define ETHIOPIA				(9)
#define MAYA					(10)
#define VIKING					(11)
#define ARABIA					(12)
#define KHMER					(13)
#define SPAIN					(14)
#define FRANCE					(15)
#define ENGLAND					(16)
#define GERMANY					(17)
#define RUSSIA					(18)
#define NETHERLANDS				(19)
#define MALI					(20)
#define PORTUGAL				(21)
#define INCA					(22)
#define MONGOLIA				(23)
#define AZTEC					(24)
#define TURKEY					(25)
#define AMERICA					(26)
#define NUM_MAJOR_PLAYERS		(27)
#define INDEPENDENT				(27)
#define INDEPENDENT2			(28)
#define NATIVE					(29)
#define CELTIA					(30)
#define BARBARIAN				(31)


#define MEDITATION				(1)
#define POLYTHEISM				(2)
#define PRIESTHOOD				(3)
#define MONOTHEISM				(4)
#define MONARCHY				(5)
#define LITERATURE				(6)
#define CODEOFLAWS				(7)
#define DRAMA					(8)
#define FEUDALISM				(9)
#define THEOLOGY				(10)
#define MUSIC					(11)
#define CIVIL_SERVICE			(12)
#define GUILDS					(13)
#define DIVINERIGHT				(14)
#define NATIONALISM				(15)
#define MILITARY_TRADITION		(16)
#define LIBERALISM				(18)
#define FASCISM					(21)
#define COMMUNISM				(22)
#define MASS_MEDIA				(23)

#define FISHING					(25)
#define POTTERY					(28)
#define AESTHETICS				(29)
#define SAILING					(30)
#define WRITING					(31)
#define MATHEMATICS				(32)
#define ALPHABET				(33)
#define CALENDAR				(34)
#define CURRENCY				(35)
#define PHILOSOPHY				(36)
#define PAPER					(37)
#define PRINTING_PRESS			(40)
#define ECONOMICS				(41)
#define ASTRONOMY				(42)
#define CHEMISTRY				(43)
#define ELECTRICITY				(48)
#define FISSION					(50)
#define FIBER_OPTICS			(57)

#define HUNTING					(59)
#define ARCHERY					(61)
#define MASONRY					(62)
#define BRONZEWORKING			(64)
#define IRONWORKING				(66)
#define METALCASTING			(67)
#define COMPASS					(68)
#define CONSTRUCTION			(69)
#define MACHINERY				(70)
#define ENGINEERING				(71)
#define OPTICS					(72)
#define GUNPOWDER				(73)
#define MILITARY_SCIENCE		(75)
#define RIFLING					(76)
#define ASSEMBLY_LINE			(79)
#define INDUSTRIALISM			(82)
#define ROBOTICS				(90)



#define GREATPALACE				(1)
#define SUMMERPALACE			(1)
#define VERSAILLES				(2)
#define FORBIDDENPALACE			(2)

#define HEROICEPIC				(105)
#define FLAVIANAMPHITHEATRE		(105)
#define NATIONALEPIC			(106)
#define TRIUMPHALARCH			(106)
#define GLOBETHEATRE			(107)
#define HERMITAGE				(109)
#define NATIONALGALLERY			(109)
#define CHANNELTUNNEL			(110)
#define WALLSTREET				(111)
#define IRONWORKS				(112)
#define TRADINGCOMPANY			(113)
#define MTRUSHMORE				(114)
#define REDCROSS				(115)
#define INTERPOL				(116)
#define SCOTLANDYARD			(116)
#define PYRAMID					(117)
#define STONEHENGE				(118)
#define GREATLIBRARY			(119)
#define GREATLIGHTHOUSE			(120)
#define HANGINGGARDEN			(121)
#define COLOSSUS				(122)
#define ORACLE					(123)
#define PARTHENON				(124)
#define ANGKORWAT				(125)
#define HAGIASOPHIA				(126)
#define CHICHENITZA				(127)
#define TEMPLEOFKUKULKAN		(127)
#define SISTINECHAPEL			(128)
#define SPIRALMINARET			(129)
#define NOTREDAME				(130)
#define TAJMAHAL				(131)
#define KREMLIN					(132)
#define EIFFELTOWER				(133)
#define STATUEOFLIBERTY			(134)
#define BROADWAY				(135)
#define WEMBLEY					(135)
#define ROCKNROLL				(136)
#define GRACELAND				(136)
#define HOLLYWOOD				(137)
#define GREATDAM				(138)
#define PENTAGON				(139)
#define UNITEDNATIONS			(140)
#define SPACEELEVATOR			(141)
#define ARTEMIS					(143)
#define SANKORE					(144)
#define GREATWALL				(145)
#define ZEUS					(146)
#define MAUSOLLOS				(147)
#define CRISTO					(148)
#define PAYA					(149)
#define MOAI					(150)
#define APOSTOLIC				(158)
#define LEANINGTOWER			(159)
#define OLYMPICPARK				(160)

#define NUM_BUILDINGS_PLAGUE	(162)

#define NUM_BUILDINGTYPES_PLAGUE	(128)

#endif	// CVRHYES_H


//Rhye - RFCRAND
//extern int EARTH_X;
//extern int EARTH_Y;
extern int assignedCiv[];
extern int assignedEarlyLeader[];

extern int startingTurn[];
extern int startingRange[27][2];
extern char loadingTime[34][4];
extern char loadingTime600AD[34][4];
extern char startingYear[34][6];
extern bool startingEra[34];
extern char startingYear600AD[34][6];
extern bool startingEra600AD[34];
//extern int militaryBonus[2][18];
extern char uniquePower[34][2][16];
extern char uniqueGoals[34][3][18];
extern char rating[34][6][15];

extern int turnPlayed[32];
extern int civSpreadFactor[32][7];
extern int borders[27][27];
extern CvWString civDynamicNames[27][22]; //(dynamic civ names - not jdog's)
extern int civDynamicNamesFlag[27];
extern int civDynamicNamesEraThreshold[27];
extern int startingLocationsClustering[27][27]; //RFCRAND
extern int settlersCoords[][8]; //RFCRAND
extern int settlersModifiers[][7]; //RFCRAND


