# Rhye's and Fall of Civilization - Constants


# globals

from CvPythonExtensions import *
gc = CyGlobalContext()

l0Array =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l0ArrayActive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l0ArrayTotal =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lm1Array =      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# initialise player variables to player IDs from WBS
iEgypt = 0
iIndia = 1
iChina = 2
iBabylonia = 3
iGreece = 4
iPersia = 5
iCarthage = 6
iRome = 7
iJapan = 8
iEthiopia = 9
iMaya = 10
iVikings = 11
iArabia = 12
iKhmer = 13
iSpain = 14
iFrance = 15
iEngland = 16
iGermany = 17
iRussia = 18
iNetherlands = 19
iHolland = 19
iMali = 20
iPortugal = 21
iInca = 22
iMongolia = 23
iAztecs = 24
iTurkey = 25
iAmerica = 26
iNumPlayers = 27
iNumMajorPlayers = 27
iNumActivePlayers = 27
iIndependent = 27
iIndependent2 = 28
iNative = 29
iCeltia = 30
iNumTotalPlayers = 31
iBarbarian = 31
iNumTotalPlayersB = 32

#RFCRAND
lEquatorDivisionN = [iEngland, iPortugal, iNetherlands, iSpain, iFrance, iGermany, iRome, iVikings, iGreece, iRussia, iTurkey, iMongolia, iChina, iJapan, iCarthage, iEgypt, iArabia, iBabylonia, iPersia, iAztecs, iMaya]
lEquatorDivisionS = [iMali, iEthiopia, iIndia, iKhmer, iInca]
lHorizontalDivisionN = [iEngland, iPortugal, iNetherlands, iSpain, iFrance, iGermany, iRome, iVikings, iGreece, iRussia, iTurkey, iMongolia, iChina, iJapan]
lHorizontalDivisionS = [iCarthage, iMali, iEgypt, iEthiopia, iArabia, iBabylonia, iPersia, iIndia, iKhmer]
lVerticalDivisionW = [iEngland, iPortugal, iNetherlands, iSpain, iFrance, iGermany, iRome, iVikings, iGreece, iRussia, iCarthage, iMali, iEgypt, iEthiopia]
lVerticalDivisionE = [iTurkey, iArabia, iBabylonia, iPersia, iIndia, iKhmer, iMongolia, iChina, iJapan]

#RFCRAND
iTemperate = 0
iTropical = 1
iArid = 2
iRocky = 4
iCold = 3

#RFCRAND #in the DLL (CvGameTextMgr) it's assumed always 5
tRadius = (
5, #Egypt
5, #India
5, #China 
5, #Babylonia
4, #Greece
5, #Persia
5, #Carthage
4, #Rome
4, #Japan
4, #Ethiopia
4, #Maya
4, #Vikings
5, #Arabia
4, #Khmer
5, #Spain
5, #France
5, #England
5, #Germany
5, #Russia
4, #Holland
4, #Mali
4, #Portugal
5, #Inca
5, #Mongolia
5, #Aztecs
5, #Turkey
5 #America
) 


#for Congresses and Victory (other uses in RFCRAND too)
lCivGroups = [[iGreece, iRome, iVikings, iSpain, iFrance, iEngland, iGermany, iRussia, iNetherlands, iPortugal],  #Euros
                [iIndia, iChina, iPersia, iJapan, iKhmer, iRussia, iMongolia], #Asian
                [iEgypt, iBabylonia, iPersia, iArabia, iTurkey], #MiddleEastern
                [iEgypt, iGreece, iCarthage, iRome], #Mediterranean
                [iEgypt, iCarthage, iEthiopia, iMali], #African
                [iMaya, iInca, iAztecs, iAmerica], #American
                [iChina, iJapan, iKhmer]] #far east #RDFRAND added for Barbs.py; this group is ignored in the other uses
                

lCivStabilityGroups = [[iVikings, iSpain, iFrance, iEngland, iGermany, iRussia, iNetherlands, iPortugal],  #Euros
                [iIndia, iChina, iJapan, iKhmer, iMongolia], #Asian
                [iBabylonia, iPersia, iArabia, iTurkey], #MiddleEastern
                [iEgypt, iGreece, iCarthage, iRome, iEthiopia, iMali], #Mediterranean
                [iMaya, iInca, iAztecs, iAmerica]] #American


lCivBioOldWorld = [iEgypt, iIndia, iChina, iBabylonia, iGreece, iPersia, iCarthage, iRome, iJapan, \
                   iEthiopia, iVikings, iArabia, iKhmer, iSpain, iFrance, iEngland, iGermany, iRussia, \
                   iNetherlands, iMali, iTurkey, iPortugal, iMongolia, iAmerica, \
                   iIndependent, iIndependent2, iCeltia, iBarbarian]
lCivBioNewWorld = [iMaya, iInca, iAztecs] #, iNative]


#for Victory and the handler
tAmericasTL = (3, 0)
tAmericasBR = (43, 63)


#for messages
iDuration = 14
iWhite = 0
iRed = 7
iGreen = 8
iBlue = 9
iLightBlue = 10
iYellow = 11
iDarkPink = 12
iLightRed = 20
iPurple = 25
iCyan = 44
iBrown = 55
iOrange = 88
iTan = 90
iLime = 100

#neighbours
lNeighbours = [
[iBabylonia, iGreece, iPersia, iCarthage, iRome, iEthiopia, iArabia, iTurkey], #Egypt
[iChina, iPersia, iKhmer, iMongolia], #India
[iIndia, iJapan, iKhmer, iMongolia], #China
[iEgypt, iGreece, iPersia, iTurkey, iMongolia], #Babylonia
[iPersia, iCarthage, iRome, iGermany, iRussia, iTurkey], #Greece
[iIndia, iBabylonia, iGreece, iTurkey, iMongolia], #Persia
[iEgypt, iGreece, iRome, iSpain, iMali, iPortugal], #Carthage
[iEgypt, iBabylonia, iGreece, iCarthage, iSpain, iFrance, iGermany, iPortugal], #Rome
[iChina, iKhmer, iMongolia], #Japan
[iEgypt, iArabia, iMali], #Ethiopia
[iSpain, iInca, iAztecs, iAmerica], #Maya
[iFrance, iEngland, iGermany, iRussia, iNetherlands], #Vikings
[iEgypt, iBabylonia, iPersia, iEthiopia, iTurkey], #Arabia
[iIndia, iChina, iJapan], #Khmer
[iCarthage, iRome, iFrance, iEngland, iPortugal], #Spain
[iRome, iVikings, iSpain, iEngland, iGermany, iNetherlands, iPortugal], #France
[iRome, iVikings, iSpain, iFrance, iGermany, iNetherlands], #England
[iRome, iVikings, iFrance, iEngland, iRussia, iNetherlands], #Germany
[iPersia, iVikings, iGermany, iTurkey, iMongolia], #Russia
[iVikings, iFrance, iEngland, iGermany], #Netherlands
[iEgypt, iCarthage, iEthiopia], #Mali
[iCarthage, iRome, iSpain, iFrance], #Portugal
[iSpain, iAztecs, iAmerica], #Inca
[iIndia, iChina, iPersia, iJapan, iRussia, iTurkey], #Mongolia
[iSpain, iInca, iAmerica], #Aztec
[iBabylonia, iGreece, iPersia, iRussia, iMongolia], #Turkey
[iJapan, iSpain, iFrance, iEngland, iRussia, iInca, iAztecs] #America
]

#for stability hit on spawn
lOlderNeighbours = [
[], #Egypt
[], #India
[], #China
[], #Babylonia
[iEgypt, iBabylonia], #Greece
[iEgypt, iBabylonia, iGreece], #Persia
[iEgypt], #Carthage
[iEgypt, iGreece, iCarthage], #Rome
[], #Japan
[iEgypt], #Ethiopia
[], #Maya
[], #Vikings
[iEgypt, iPersia], #Arabia
[iIndia], #Khmer
[iCarthage, iRome], #Spain
[iRome], #France
[], #England
[iGreece, iRome, iVikings], #Germany
[iPersia, iGreece], #Russia
[iRome, iGermany], #Netherlands
[iCarthage, iEthiopia], #Mali
[iCarthage, iRome], #Portugal
[], #Inca
[iChina, iJapan, iKhmer, iRussia], #Mongolia
[iMaya], #Aztec
[iBabylonia, iGreece, iPersia], #Turkey
[iSpain, iFrance, iEngland, iNetherlands, iPortugal, iAztecs, iMaya] #America
]

# civ birth dates

tBirth = [
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0, 
0,
0,
0,
0,
0, #America 
0,
0,
0,
0,
0]


tYear = (
("3000 ", "TXT_KEY_BC"),
("3000 ", "TXT_KEY_BC"),
("3000 ", "TXT_KEY_BC"),
("3000 ", "TXT_KEY_BC"),
("1600 ", "TXT_KEY_BC"),
("850 ", "TXT_KEY_BC"),
("820 ", "TXT_KEY_BC"),
("760 ", "TXT_KEY_BC"),
("655 ", "TXT_KEY_BC"),
("295 ", "TXT_KEY_BC"),
("65 ", "TXT_KEY_AD"),
("545 ", "TXT_KEY_AD"),
("620 ", "TXT_KEY_AD"),
("660 ", "TXT_KEY_AD"),
("720 ", "TXT_KEY_AD"),
("750 ", "TXT_KEY_AD"),
("820 ", "TXT_KEY_AD"),
("840 ", "TXT_KEY_AD"),
("860 ", "TXT_KEY_AD"),
("920 ", "TXT_KEY_AD"),
("980 ", "TXT_KEY_AD"),
("1130 ", "TXT_KEY_AD"),
("1150 ", "TXT_KEY_AD"),
("1190 ", "TXT_KEY_AD"),
("1200 ", "TXT_KEY_AD"),
("1280 ", "TXT_KEY_AD"),
("1775 ", "TXT_KEY_AD"))


#RFCRAND
tScout = (0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0)

tGoals = (
("TXT_KEY_UHV_EGY1", "TXT_KEY_UHV_EGY2", "TXT_KEY_UHV_EGY3"),
("TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"),
("TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"),
("TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2", "TXT_KEY_UHV_BAB3"),
("TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2", "TXT_KEY_UHV_GRE3"),
("TXT_KEY_UHV_PER1", "TXT_KEY_UHV_PER2", "TXT_KEY_UHV_PER3"),
("TXT_KEY_UHV_CAR1", "TXT_KEY_UHV_CAR2", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_ROM1", "TXT_KEY_UHV_ROM2", "TXT_KEY_UHV_ROM3"),
("TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"),
("TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"),
("TXT_KEY_UHV_MAY1", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"),
("TXT_KEY_UHV_VIK1", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_KHM1", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"),
("TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"),
("TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"),
("TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"),
("TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"),
("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2", "TXT_KEY_UHV_MAL3"),
("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
("TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2", "TXT_KEY_UHV_INC3"),
("TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"),
("TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"),
("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
("TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3")
)


# date waypoints

i3000BC = 0
i2250BC = 25
i2085BC = 31
i2000BC = 34
i1800BC = 42
i1600BC = 50
i1000BC = 74
i850BC = 84
i700BC = 94
i650BC = 97
i600BC = 101
i483BC = 108
i479BC = 109
i400BC = 114 #new timeline
i350BC = 117
i250BC = 124 #new timeline
i210BC = 127
i110BC = 133
i100BC = 134 #new timeline
i10BC = 140
i33AD = 143
i50AD = 144
i140AD = 150 #new timeline
i170AD = 152
i190AD = 153
i200AD = 154 #new timeline
i250AD = 157
i300AD = 161
i350AD = 164
i450AD = 171
i470AD = 172 #new timeline
i476AD = 172
i500AD = 174 #new timeline
i550AD = 177
i600AD = 181
i622AD = 183
i690AD = 190
i700AD = 191
i860AD = 207
i900AD = 211
i920AD = 213
i1000AD = 221
i1100AD = 231
i1140AD = 235
i1190AD = 240
i1200AD = 241
i1250AD = 246
i1300AD = 251
i1350AD = 256
i1400AD = 261
i1450AD = 271
i1500AD = 281
i1600AD = 301
i1607AD = 302
i1650AD = 311
i1700AD = 321
i1715AD = 326
i1730AD = 331
i1745AD = 336
i1760AD = 341
i1775AD = 346
i1800AD = 355
i1820AD = 361
i1850AD = 372
i1860AD = 377
i1870AD = 382
i1880AD = 387
i1900AD = 397
i1910AD = 402
i1918AD = 406
i1930AD = 412
i1940AD = 420
i1950AD = 430
i2000AD = 480


#RFCRAND - start
# starting locations coordinates
tCapitals = [
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0],
[0, 0]
] 

#for minor civs
tReserveCapitals = (
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(),
(),
(),
(),
(), 
)

#core areas (for RiseAndFall and Victory)
#RFCRAND (here are % of width and height)
tCoreAreasTL = (
(53, 39), #Egypt
(77, 36), #India
(87, 52), #China 
(68, 50), #Babylonia
(57, 55), #Greece
(73, 43), #Persia
(40, 45), #Carthage
(50, 55), #Rome
(93, 53), #Japan
(60, 29), #Ethiopia
(14, 49), #Maya
(46, 83), #Vikings
(64, 39), #Arabia
(85, 34), #Khmer
(41, 55), #Spain
(43, 64), #France
(37, 73), #England
(53, 68), #Germany
(64, 73), #Russia
(47, 73), #Holland
(40, 37), #Mali
(38, 55), #Portugal
(14, 18), #Inca
(79, 59), #Mongolia
(10, 52), #Aztecs
(64, 57), #Turkey
(20, 56) #America
) 

tCoreAreasBR = (
(61, 51), #Egypt
(82, 51), #India
(90, 61), #China
(73, 57), #Babylonia
(61, 66), #Greece
(78, 57), #Persia
(54, 51), #Carthage
(55, 67), #Rome
(98, 73), #Japan
(67, 38), #Ethiopia
(22, 77), #Maya
(59, 94), #Vikings
(71, 49), #Arabia
(90, 45), #Khmer
(47, 64), #Spain
(50, 72), #France
(44, 92), #England
(60, 80), #Germany
(75, 83), #Russia
(52, 80), #Holland
(52, 44), #Mali
(40, 65), #Portugal
(19, 45), #Inca
(88, 67), #Mongolia
(18, 58), #Aztecs
(75, 63), #Turkey
(29, 82) #America
) 


tExceptions = (  #for RiseAndFall
(), #Egypt
(), #India
(), #China
(), #Babylonia
(), #Greece
(), #Persia
(), #Carthage
(), #Rome
(), #Japan
(), #Ethiopia
(), #Maya
(), #Vikings
(),  #Arabia
(), #Khmer
(), #Spain
(), #France
(), #England
(),  #Germany
(), #Russia
(), #Holland
(), #Mali
(), #Portugal
(), #Inca
(), #Mongolia
(), #Aztecs
(), #Turkey
() #America
)


#normal areas (for Victory and resurrection)
#RFCRAND
tNormalAreasTL = [
[0, 0], #Egypt
[0, 0], #India
[0, 0], #China
[0, 0], #Babylonia
[0, 0], #Greece
[0, 0], #Persia
[0, 0], #Carthage
[0, 0], #Rome
[0, 0], #Japan
[0, 0], #Ethiopia
[0, 0], #Maya
[0, 0], #Vikings
[0, 0], #Arabia
[0, 0], #Khmer
[0, 0], #Spain
[0, 0], #France
[0, 0], #England
[0, 0], #Germany
[0, 0], #Russia
[0, 0], #Holland
[0, 0], #Mali
[0, 0], #Portugal
[0, 0], #Inca
[0, 0], #Mongolia
[0, 0], #Aztecs
[0, 0], #Turkey
[0, 0]  #America
] 

tNormalAreasBR = [
[0, 0], #Egypt
[0, 0], #India
[0, 0], #China
[0, 0], #Babylonia
[0, 0], #Greece
[0, 0], #Persia
[0, 0], #Carthage
[0, 0], #Rome
[0, 0], #Japan
[0, 0], #Ethiopia
[0, 0], #Maya
[0, 0], #Vikings
[0, 0], #Arabia
[0, 0], #Khmer
[0, 0], #Spain
[0, 0], #France
[0, 0], #England
[0, 0], #Germany
[0, 0], #Russia
[0, 0], #Holland
[0, 0], #Mali
[0, 0], #Portugal
[0, 0], #Inca
[0, 0], #Mongolia
[0, 0], #Aztecs
[0, 0], #Turkey
[0, 0]  #America
] 


tNormalAreasSubtract = (  #for resurrection and stability
(), #Egypt
(), #India
(), #China
(), #Babylonia
(), #Greece
(), #Persia
(), #Carthage
(), #Rome
(), #Japan
(), #Ethiopia
(), #Maya
(), #Vikings
(),  #Arabia
(), #Khmer
(), #Spain
(), #France
(), #England
(),  #Germany
(), #Russia
(), #Holland
(), #Mali
(), #Portugal
(), #Inca
(), #Mongolia
(), #Aztecs
(), #Turkey
() #America
)
#RFCRAND - end


# broader areas coordinates (top left and bottom right) (for RiseAndFall)

tBroaderAreasTL = (
(60, 26), #Egypt
(85, 28), #India
(95, 38), #China
(72, 37), #Babylonia
(62, 39), #Greece
(70, 37), #Persia
(49, 35), #Carthage
(49, 35), #Rome
(110, 40), #Japan
(67, 21), #Ethiopia
(19, 30), #Maya
(57, 55), #Vikings
(64, 30), #Arabia
(97, 25), #Khmer
(49, 38), #Spain
(49, 44), #France
(48, 53), #England
(55, 46), #Germany
(65, 48), #Russia
(56, 51), #Holland
(48, 21), #Mali
(49, 40), #Portugal
(24, 14), #Inca
(82, 44), #Mongolia
(14, 32), #Aztecs
(68, 42), #Turkey
(10, 42) #America
)

tBroaderAreasBR = (
(74, 38), #Egypt
(99, 43), #India
(107, 50), #China
(78, 44), #Babylonia
(77, 47), #Greece
(87, 49), #Persia
(59, 41), #Carthage
(73, 50), #Rome
(116, 56), #Japan
(77, 30), #Ethiopia
(26, 37), #Maya
(71, 65), #Vikings
(85, 44), #Arabia
(105, 39), #Khmer
(55, 46), #Spain
(61, 52), #France
(54, 60), #England
(67, 56), #Germany
(92, 59), #Russia
(58, 53), #Holland
(67, 32), #Mali
(51, 45), #Portugal
(30, 27), #Inca
(110, 62), #Mongolia
(24, 43), #Aztecs
(86, 49), #Turkey
(37, 56)) #America



#Mercenaries. Higher number = less likely to hire
tHire = (
10, #Egypt
30, #India
30, #China
30, #Babylonia
50, #Greece
20, #Persia
10, #Carthage
30, #Rome
60, #Japan
30, #Ethiopia
30, #Maya
60, #Viking
50, #Arabia
30, #Ethiopia
50, #Spain
50, #France
50, #England
60, #Germany
60, #Russia
10, #Holland
30, #Mali
60, #Portugal
30, #Inca
70, #Mongolia
30, #Aztec
50, #Turkey
50, #America
100,
100,
100,
100,
100) #Barbs



#rnf. Some civs have a double entry, for a higher chance
lEnemyCivsOnSpawn = [
[], #Egypt
[], #India
[iIndependent,iIndependent2,iIndependent2], #China
[iIndependent,iIndependent2], #Babylonia
[iIndependent,iIndependent2,iBabylonia], #Greece
[iBabylonia,iBabylonia,iGreece], #Persia
[], #Carthage
[iEgypt,iGreece,iGreece,iCarthage,iCarthage], #Rome
[], #Japan
[], #Ethiopia
[], #Maya
[iRome,iArabia,iSpain,iEngland,iEngland,iFrance,iFrance,iGermany,iGermany,iNetherlands,iCeltia,iIndependent,iIndependent2], #Vikings
[iEgypt,iBabylonia,iBabylonia,iGreece,iPersia,iCarthage,iRome,iSpain,iFrance,iCeltia,iCeltia,iIndependent,iIndependent2], #Arabia
[], #Khmer
[iArabia], #Spain
[iArabia], #France
[], #England
[iRome], #Germany
[], #Russia
[], #Netherlands
[], #Mali
[], #Portugal
[], #Inca
[iIndia,iChina,iChina,iJapan,iPersia,iKhmer,iRussia,iRussia,iIndependent,iIndependent,iIndependent2,iIndependent2], #Mongolia
[iMaya], #Aztec
[iEgypt,iBabylonia,iGreece,iGreece,iCeltia,iCeltia], #Turkey
[iIndependent,iIndependent2] #America
]


#AIWars
tAggressionLevel = (
0, #Egypt
0, #India
1, #China
1, #Babylonia
1, #Greece
2, #Persia
0, #Carthage
2, #Rome
1, #Japan
0, #Ethiopia
1, #Maya
2, #Viking
2, #Arabia
1, #Khmer
2, #Spain
1, #France
1, #England
2, #Germany
1, #Russia
0, #Holland
0, #Mali
0, #Portugal
1, #Inca
2, #Mongolia
1, #Aztec
2, #Turkey
2, #America
0) #Barbs


#war during rise of new civs
tAIStopBirthThreshold = (
    80, #Egypt
    80, #India
    60, #China
    50, #Babylonia
    50, #Greece #would be 80 but with Turks must be lower
    70, #Persia
    80, #Carthage
    80, #Rome
    80, #Japan
    80, #Ethiopia
    80, #Maya
    80, #Viking
    80, #Arabia
    80, #Khmer
    80, #Spain  #60 in vanilla and Warlords
    80, #France #60 in vanilla and Warlords
    50, #England
    80, #Germany #70 in vanilla and Warlords
    50, #Russia
    80, #Holland
    70, #Mali
    60, #Portugal
    70, #Inca
    70, #Mongolia
    50, #Aztec
    70, #Turkey
    50, #America
    100,
    100,
    100,
    100,
    100)


#RiseAndFall
tResurrectionProb = (
80, #Egypt
100, #India
100, #China
30, #Babylonia
60, #Greece
60, #Persia
30, #Carthage
65, #Rome
100, #Japan
80, #Ethopia
30, #Maya
60, #Viking
100, #Arabia
60, #Khmer
100, #Spain
100, #France
100, #England
100, #Germany
100, #Russia
100, #Holland
30, #Mali
100, #Portugal
70, #Inca
80, #Mongolia
70, #Aztec
100, #Turkey
100, #America
#    100, #Holland
#    100, #Portugal
100) #Barbs 


#Congresses.
tPatienceThreshold = (
30, #Egypt
50, #India
30, #China
30, #Babylonia
35, #Greece
30, #Persia
35, #Carthage
25, #Rome
25, #Japan
20, #Ethopia
35, #Maya
30, #Viking
30, #Arabia
30, #Khmer
20, #Spain
20, #France
20, #England
20, #Germany
30, #Russia
30, #Holland
35, #Mali
30, #Portugal
35, #Inca
20, #Mongolia
30, #Aztec
35, #Turkey
30, #America
100) #Barbs


#RnF Colonists
tMaxColonists = (
0, #Egypt
0, #India
0, #China
0, #Babylonia
0, #Greece
0, #Persia
0, #Carthage
0, #Rome
0, #Japan
0, #Ethopia
0, #Maya
1, #Viking
0, #Arabia
0, #Khmer
6, #Spain
6, #France
6, #England
1, #Germany
0, #Russia
6, #Holland
0, #Mali
6, #Portugal
0, #Inca
0, #Mongolia
0, #Aztec
0, #Turkey
0) #America


# initialise religion variables to religion indices from XML
iJudaism = 0
iChristianity = 1
iIslam = 2
iHinduism = 3
iBuddhism = 4
iConfucianism = 5
iTaoism = 6
iNumReligions = 7


# initialise tech variables to unit indices from XML

iMysticism = 0
iMeditation = 1
iPolytheism = 2
iPriesthood = 3
iMonotheism = 4
iMonarchy = 5
iLiterature = 6
iCodeOfLaws = 7
iDrama = 8
iFeudalism = 9
iTheology = 10
iMusic = 11
iCivilService = 12
iGuilds = 13
iDivineRight = 14
iNationalism = 15
iMilitaryTradition = 16
iConstitution = 17
iLiberalism = 18
iDemocracy = 19
iCorporation = 20
iFascism = 21
iUtopia = 22
iCommunism = 22 #
iMassMedia = 23
iEcology = 24

iFishing = 25
iTheWheel = 26
iAgriculture = 27
iPottery = 28
iAesthetics = 29
iSailing = 30
iWriting = 31
iMathematics = 32
iAlphabet = 33
iCalendar = 34
iCurrency = 35
iPhilosophy = 36
iPaper = 37
iBanking = 38
iEducation = 39
iPrintingPress = 40
iEconomics = 41
iAstronomy = 42
iChemistry = 43
iScientificMethod = 44
iPhysics = 45
iBiology = 46
iMedicine = 47
iElectricity = 48
iCombustion = 49
iFission = 50
iFlight = 51
iAdvancedFlight = 52
iPlastics = 53
iComposites = 54
iStealth = 55
iGenetics = 56
iFiberOptics = 57
iFusion = 58

iHunting = 59
iMining = 60
iArchery = 61
iMasonry = 62
iAnimalHusbandry = 63
iBronzeWorking = 64
iHorsebackRiding = 65
iIronWorking = 66
iMetalCasting = 67
iCompass = 68
iConstruction = 69
iMachinery = 70
iEngineering = 71
iOptics = 72
iGunpowder = 73
iReplaceableParts = 74
iMilitaryScience = 75
iRifling = 76
iSteamPower = 77
iSteel = 78
iAssemblyLine = 79
iRailroad = 80
iArtillery = 81
iIndustrialism = 82
iRadio = 83
iRefrigeration = 84
iSuperconductors = 85
iComputers = 86
iLaser = 87
iRocketry = 88
iSatellites = 89
iRobotics = 90

iNumTechs = 91
iFutureTech = 91

iNumTechsFuture = 92


# initialise unit variables to unit indices from XML

iLion = 0
iBear = 1
iPanther = 2
iWolf = 3
iSettler = 4
iWorker = 5
iIndianFastWorker = 6
iScout = 7
iExplorer = 8
iSpy = 9
iExecutive1 = 10
iExecutive2 = 11
iExecutive3 = 12
iExecutive4 = 13
iExecutive5 = 14
iExecutive6 = 15
iExecutive7 = 16
iJewishMissionary = 17
iChristianMissionary = 18
iIslamicMissionary = 19
iHinduMissionary = 20
iBuddhistMissionary = 21
iConfucianMissionary = 22
iTaoistMissionary = 23
iWarrior = 24
iIncanQuechua = 25
iSwordsman = 26
iAztecJaguar = 27
iCelticGallicWarrior = 28
iRomePraetorian = 29
iAxeman = 30
iGreekPhalanx = 31
iSumerianVulture = 32
iNativeAmericaDogSoldier = 33
iMaceman = 34
iJapanSamurai = 35
iVikingBeserker = 36
iSpearman = 37
iZuluImpi = 38
iMayaHolkan = 39
iPikeman = 40
iHolyRomanLandsknecht = 41
iMusketman = 42
iFrenchMusketeer = 43
iOttomanJanissary = 44
iEthiopianOromoWarrior = 45
iRifleman = 46
iEnglishRedcoat = 47
iGrenadier = 48
iAtInfantry = 49
iInfantry = 50
iSamInfantry = 51
iMobileSam = 52
iMarine = 53
iAmericanNavySeal = 54
iParatrooper = 55
iMechanizedInfantry = 56
iArcher = 57
iMaliSkirmisher = 58
iBabylonBowman = 59
iLongbowman = 60
iCrossbowman = 61
iChinaChokonu = 62
iChariot = 63
iEgyptWarchariot = 64
iPersiaImmortal = 65
iHorseArcher = 66
iCarthageNumidianCavalry = 67
iMongolKeshik = 68
iKnight = 69
iArabiaCamelarcher = 70
iCamelArcher = 70 #
iByzantineCataphract = 71
iSpanishConquistador = 72
iConquistador = 72 #
iCuirassier = 73
iCavalry = 74
iRussiaCossack = 75
iWarElephant = 76
iKhmerBallistaElephant = 77
iTank = 78
iGermanPanzer = 79
iModernArmor = 80
iGunship = 81
iCatapult = 82
iKoreanHwacha = 83
iTrebuchet = 84
iCannon = 85
iMachineGun = 86
iArtillery = 87
iMobileArtillery = 88
iWorkboat = 89
iWorkBoat = 89 #
iGalley = 90
iTrireme = 91
iCaravel = 92
iPortugalCarrack = 93
iGalleon = 94
iNetherlandsOostindievaarder = 95
iPrivateer = 96
iFrigate = 97
iShipOfTheLine = 98
iIronclad = 99
iTransport = 100
iDestroyer = 101
iBattleship = 102
iMissileCruiser = 103
iStealthDestroyer = 104
iSubmarine = 105
iAttackSubmarine = 106
iCarrier = 107
iAirship = 108
iFighter = 109
iJetFighter = 110
iBomber = 111
iStealthBomber = 112
iGuidedMissile = 113
iTacticalNuke = 114
iIcbm = 115
iProphet = 116
iArtist = 117
iScientist = 118
iMerchant = 119
iEngineer = 120
iGreatGeneral = 121
iGreatSpy = 122






# initialise bonuses variables to bonuses IDs from WBS
iAluminium = 0
iCoal = 1
iCopper = 2
iHorse = 3
iIron = 4
iMarble = 5
iOil = 6 
iStone = 7
iUranium = 8
iBanana = 9
iClam = 10
iCorn = 11
iCow = 12
iCrab = 13
iDeer = 14
iFish = 15
iPig = 16
iRice = 17
iSheep = 18
iWheat = 19
iDye = 20
iFur = 21
iGems = 22
iGold = 23
iIncense = 24
iIvory = 25
iSilk = 26
iSilver = 27
iSpices = 28
iSugar = 29
iWine = 30
iWhales = 31
iCotton = 35


#Buildings (update Persian UHV every time this is changed)
iTemple = 77 #generic
iCathedral = 78 #generic
iShrine = 80 #generic


iPalace = 0
iGreatPalace = 1
iSummerPalace = 1 #
iVersailles = 2
iForbiddenPalace = 2 #
iWalls = 3
iCelticDun = 4
iCastle = 5
iSpanishCitadel = 6
iBarracks = 7
iZuluIkhanda = 8
iStable = 9
iMongolGer = 10
iBunker = 11
iBombShelter = 12
iGranary = 13
iIncanTerrace = 14
iAqueduct = 15
iOttomanHammam = 16
iKhmerBaray = 17
iHospital = 18
iRecyclingCenter = 19
iLighthouse = 20
iVikingTradingPost = 21
iHarbor = 22
iCarthageCothon = 23
iCustomHouse = 24
iPortugalFeitoria = 25
iDrydock = 26
iAirport = 27
iForge = 28
iMaliMint = 29
iFactory = 30
iGermanAssemblyPlant = 31
iCoalPlant = 32
iJapaneseShalePlant = 33
iHydroPlant = 34
iNuclearPlant = 35
iIndustrialPark = 36
iObelisk = 37
iEgyptianObelisk = 38
iEthiopianStele = 39
iNativeAmericaTotem = 40
iPublicTransportation = 41
iAcademy = 42
iLibrary = 43
iArabianMadrassa = 44
iUniversity = 45
iKoreanSeowon = 46
iObservatory = 47
iFrenchSalon = 48
iLaboratory = 49
iRussianResearchInstitute = 50
iTheatre = 51
iChinesePavillion = 52
iByzantineHippodrome = 53
iColosseum = 54
iGreekOdeon = 55
iMayaBallCourt = 56
iBabylonGarden = 57
iBroadcastTower = 58
iMarket = 59
iRomanForum = 60
iGrocer = 61
iPersianApothecary = 62
iBank = 63
iEnglishStockExchange = 64
iSupermarket = 65
iAmericanMall = 66
iCourthouse = 67
iAztecSacrificialAltar = 68
iHolyRomanRathaus = 69
iSumerianZiggurat = 70
iJail = 71
iIndianMausoleum = 72
iLevee = 73
iNetherlandsDike = 74
iIntelligenceAgency = 75
iNationalSecurity = 76
iJewishTemple = 77
iJewishCathedral = 78
iJewishMonastery = 79
iJewishShrine = 80
iChristianTemple = 81
iChristianCathedral = 82
iChristianMonastery = 83
iChristianShrine = 84
iIslamicTemple = 85
iIslamicCathedral = 86
iIslamicMonastery = 87
iIslamicShrine = 88
iHinduTemple = 89
iHinduCathedral = 90
iHinduMonastery = 91
iHinduShrine = 92
iBuddhistTemple = 93
iBuddhistCathedral = 94
iBuddhistMonastery = 95
iBuddhistShrine = 96
iConfucianTemple = 97
iConfucianCathedral = 98
iConfucianMonastery = 99
iConfucianShrine = 100
iTaoistTemple = 101
iTaoistCathedral = 102
iTaoistMonastery = 103
iTaoistShrine = 104
iHeroicEpic = 105 #
iFlavianAmphitheatre = 105
iNationalEpic = 106
iTriumphalArch = 106 #
iGlobeTheatre = 107
iNationalPark = 108
iHermitage = 109
iNationalGallery = 109 #
iChannelTunnel = 110
iWallStreet = 111
iIronWorks = 112
iTradingCompany = 113
iMtRushmore = 114
iRedCross = 115
iScotlandYard = 116
iInterpol = 116 #
iPyramid = 117
iStonehenge = 118
iGreatLibrary = 119
iGreatLighthouse = 120
iHangingGarden = 121
iColossus = 122
iOracle = 123
iParthenon = 124
iAngkorWat = 125
iHagiaSophia = 126
iChichenItza = 127
iTempleOfKukulkan = 127 #
iSistineChapel = 128
iSpiralMinaret = 129
iNotreDame = 130
iTajMahal = 131
iKremlin = 132
iEiffelTower = 133
iStatueOfLiberty = 134
iBroadway = 135
iWembley = 135 #
iRocknroll = 136
iGraceland = 136 #
iHollywood = 137
iGreatDam = 138
iPentagon = 139
iUnitedNations = 140
iSpaceElevator = 141
iMilitaryAcademy = 142
iArtemis = 143
iSankore = 144
iGreatWall = 145
iStatueOfZeus = 146
iMausoleumOfMaussollos = 147
iCristoRedentor = 148
iShwedagonPaya = 149
iMoaiStatues = 150
iCorporation1 = 151
iCorporation2 = 152
iCorporation3 = 153
iCorporation4 = 154
iCorporation5 = 155
iCorporation6 = 156
iCorporation7 = 157
iApostolicPalace = 158
iLeaningTower = 159
iOlympicPark = 160

iNumBuildings = 161 
iPlague = 161
iNumBuildingsPlague = 162

iEgyEmbassy = 162
iIndEmbassy = 163
iChiEmbassy = 164
iBabEmbassy = 165
iGreEmbassy = 166
iPerEmbassy = 167
iCarEmbassy = 168
iRomEmbassy = 169
iJapEmbassy = 170
iEthEmbassy = 171
iMayEmbassy = 172
iVikEmbassy = 173
iAraEmbassy = 174
iKhmEmbassy = 175
iSpaEmbassy = 176
iFraEmbassy = 177
iEngEmbassy = 178
iGerEmbassy = 179
iRusEmbassy = 180
iHolEmbassy = 181
iMalEmbassy = 182
iPorEmbassy = 183
iIncEmbassy = 184
iMonEmbassy = 185
iAztEmbassy = 186
iTurEmbassy = 187
iAmeEmbassy = 188

iNumBuildingsEmbassy = 189


#Projects

iManhattanProject = 0
iTheInternet = 1
iSDI = 2
iApolloProgram = 3
iSSCasing = 4
iSSThrusters = 5
iSSEngine = 6
iSSDockingBay = 7
iSSCockpit = 8
iSSLifeSupport = 9
iSSStasisChamber = 10


#Eras

iAncient = 0
iClassical = 1
iMedieval = 2
iRenaissance = 3
iIndustrial = 4
iModern = 5
iFuture = 6


#Improvements

iHut = 3
iCottage = 19
iHamlet = 20
iVillage = 21
iTown = 22

#feature & terrain

iSeaIce = 0
iJungle = 1
iOasis = 2
iFloodPlains = 3
iForest = 4
iFallout = 5
iMud = 6

iGrass = 0
iPlains = 1
iDesert = 2
iTundra = 3
iSnow = 4
iCoast = 5
iOcean = 6
iTerrainPeak = 7
iTerrainHills = 8
iMarsh = 9

iSwamp = 36 #bonus


#Stability Parameters

iParCities3 = 0
iParCitiesE = 1
iParCivics3 = 2
iParCivics1 = 3
iParCivicsE = 4
iParDiplomacy3 = 5
iParDiplomacyE = 6
iParEconomy3 = 7
iParEconomy1 = 8
iParEconomyE = 9
iParExpansion3 = 10
iParExpansion1 = 11
iParExpansionE = 12
iNumStabilityParameters = 13

#Plague
iImmunity = 20


#leaders
iLeaderBarbarian = 0
iAlexander = 1
iAsoka = 2
iAugustus = 3
iBismarck = 4
iBoudica = 5
iBrennus = 6
iCatherine = 7
iCharlemagne = 8
iOttoI = 8
iChurchill = 9
iCyrus = 10
iDarius = 11
iDe_Gaulle = 12
iElizabeth = 13
iFrederick = 14
iGandhi = 15
iGenghis_Khan = 16
iGilgamesh = 17
iHammurabi = 18
iHannibal = 19
iHatshepsut = 20
iHuayna_Capac = 21
iIsabella = 22
iJoao = 23
iJulius_Caesar = 24
iJustinian = 25
iKublai_Khan = 26
iLincoln = 27
iLouis_Xiv = 28
iMansa_Musa = 29
iMao = 30
iMehmed = 31
iMontezuma = 32
iNapoleon = 33
iPacal = 34
iPericles = 35
iPeter = 36
iQin_Shi_Huang = 37
iRamesses = 38
iRagnar = 39
iFranklin_Roosevelt = 40
iSaladin = 41
iShaka = 42
iSitting_Bull = 43
iStalin = 44
iSuleiman = 45
iSuryavarman = 46
iTokugawa = 47
iVictoria = 48
iWangkon = 49
iMing_Tai_Zu = 49
iWashington = 50
iWillem_Van_Oranje = 51
iZara_Yaqob = 52
iIndependentLeader = 53 #RFCRAND


tLeaders = (
(iRamesses,), #iHatshepsut),
(iAsoka, iGandhi),
(iQin_Shi_Huang, iMing_Tai_Zu, iMao),
(iHammurabi, iGilgamesh),
(iPericles, iAlexander,),
(iCyrus, iDarius),
(iHannibal,),
(iAugustus, iJulius_Caesar, iJustinian),
(iTokugawa,),
(iZara_Yaqob,),
(iPacal,),
(iRagnar,),
(iSaladin,),
(iSuryavarman,),
(iIsabella,),
(iLouis_Xiv, iNapoleon, iDe_Gaulle),
(iVictoria, iElizabeth, iChurchill),
(iBismarck, iOttoI, iFrederick),
(iStalin, iPeter, iCatherine),
(iWillem_Van_Oranje,),
(iMansa_Musa,),
(iJoao,),
(iHuayna_Capac,),
(iGenghis_Khan, iKublai_Khan),
(iMontezuma,),
(iMehmed, iSuleiman),
(iFranklin_Roosevelt, iWashington, iLincoln))

tEarlyLeaders = (
(iRamesses), 
(iAsoka),
(iQin_Shi_Huang),
(iGilgamesh),
(iPericles),
(iCyrus),
(iHannibal),
(iJulius_Caesar),
(iTokugawa),
(iZara_Yaqob),
(iPacal),
(iRagnar),
(iSaladin),
(iSuryavarman),
(iIsabella),
(iLouis_Xiv),
(iElizabeth),
(iOttoI),
(iPeter),
(iWillem_Van_Oranje),
(iMansa_Musa),
(iJoao),
(iHuayna_Capac),
(iGenghis_Khan),
(iMontezuma),
(iMehmed),
(iWashington),
(iIndependentLeader),#RFCRAND
(iIndependentLeader),#RFCRAND
(iShaka),#RFCRAND
(iBrennus))#RFCRAND


if (gc.getPlayer(0).isPlayable()): #late start condition
        tRomanLateLeaders = (iAugustus, i50AD, 5, 2, iJustinian, i1000AD, 10, 3)
else: 
        tRomanLateLeaders = (iAugustus, i50AD, 5, 2)


tLateLeaders = ( #all up to 300 turns earlier because the switch is triggered after a few years
(iRamesses,), 
(iGandhi, i1700AD, 5, 4),
(iMing_Tai_Zu, i1400AD, 10, 3, iMao, i1800AD, 10, 5),
(iHammurabi, i1600BC, 10, 1),
(iAlexander, i10BC, 5, 2),
(iDarius, i10BC, 5, 2),
(iHannibal,),
tRomanLateLeaders,
(iTokugawa,),
(iZara_Yaqob,),
(iPacal,),
(iRagnar,),
(iSaladin,),
(iSuryavarman,),
(iIsabella,),
(iNapoleon, i1700AD, 10, 4, iDe_Gaulle, i1940AD, 10, 5),
(iVictoria, i1600AD, 15, 3, iChurchill, i1930AD, 10, 5),
(iFrederick, i1500AD, 10, 3, iBismarck, i1760AD, 10, 4),
(iCatherine, i1600AD, 15, 4, iStalin, i1800AD, 15, 5),
(iWillem_Van_Oranje,),
(iMansa_Musa,),
(iJoao,),
(iHuayna_Capac,),
(iKublai_Khan, i1500AD, 10, 3),
(iMontezuma,),
(iSuleiman, i1500AD, 10, 3),
(iLincoln, i1800AD, 15, 5, iFranklin_Roosevelt, i1900AD, 15, 5))
