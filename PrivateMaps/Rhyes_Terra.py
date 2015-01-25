#
#	FILE:	 Terra.py
#	AUTHOR:  Bob Thomas (Sirian)
#	PURPOSE: Global map script - Simulates Terran (Earth-like) worlds
#-----------------------------------------------------------------------------
#	Copyright (c) 2005 Firaxis Games, Inc. All rights reserved.
#-----------------------------------------------------------------------------
#

from CvPythonExtensions import *
import CvUtil
import CvMapGeneratorUtil
from CvMapGeneratorUtil import MultilayeredFractal
from CvMapGeneratorUtil import TerrainGenerator
from CvMapGeneratorUtil import FeatureGenerator
from CvMapGeneratorUtil import BonusBalancer
from CvMapGeneratorUtil import FractalWorld #Rhye

import RFCUtils #Rhye
utils = RFCUtils.RFCUtils() #Rhye
import StoredData #Rhye
import pickle  #Rhye
gc = CyGlobalContext() #Rhye
import Consts as con #Rhye

balancer = BonusBalancer()



'''
MULTILAYERED FRACTAL NOTES

The MultilayeredFractal class was created for use with this script.

I worked to make it adaptable to other scripts, though, and eventually it
migrated in to the MapUtil file along with the other primary map classes.

- Bob Thomas   July 13, 2005


TERRA NOTES

Terra turns out to be our largest size map. This is the only map script
in the original release of Civ4 where the grids are this large!

This script is also the one that got me started in to map scripting. I had 
this idea early in the development cycle and just kept pestering until Soren 
turned me loose on it, finally. Once I got going, I just kept on going!

- Bob Thomas   September 20, 2005
'''

#def beforeGeneration():
#        StoredData.StoredData().setupScriptData() #Rhye

def getDescription():
	return "TXT_KEY_MAP_SCRIPT_TERRA_DESCR"

def isAdvancedMap():
	"This map should show up in simple mode"
	return 0

def getWrapX():
	map = CyMap()
	#Rhye
	if (utils.getWrap(0) != -1):
                return utils.getWrap(0)
	likeness = int(map.getSeaLevel())
	if (likeness <= 1):
                utils.setWrap(0,True)
                utils.setWrap(1,False)
        else: #less the likeness, more strange setting is likely to happen
                if (gc.getGame().getSorenRandNum(9-likeness, '') == 0):
                        utils.setWrap(0,True)
                        utils.setWrap(1,True)
                elif (gc.getGame().getSorenRandNum(9-likeness, '') == 1):
                        utils.setWrap(0,False)
                        utils.setWrap(1,False)
                        if (gc.getGame().isVictoryValid(7)):
                                iHuman = utils.getHumanID()
                                if (iHuman == con.iGreece or iHuman == con.iCarthage or iHuman == con.iEngland):
                                        utils.setWrap(0,True)
                                        utils.setWrap(1,True)                                        
                elif (gc.getGame().getSorenRandNum(9-likeness, '') == 2):
                        utils.setWrap(0,False)
                        utils.setWrap(1,True)
                else:
                        utils.setWrap(0,True)
                        utils.setWrap(1,False)
        #debug
        #utils.setWrap(0,False)
        #utils.setWrap(1,False)
        return utils.getWrap(0)
	
def getWrapY():
	map = CyMap()
	#Rhye
	if (utils.getWrap(1) != -1):
                return utils.getWrap(1)
        return False


def getGridSize(argsList):
        StoredData.StoredData().setupScriptData() #Rhye - this is called before anything else, including getWrapX()
        #we must keep overriding, so that we can do the early initialization of stored data
	grid_sizes = {
##		WorldSizeTypes.WORLDSIZE_DUEL:		(13,8),
##		WorldSizeTypes.WORLDSIZE_TINY:		(16,10),
##		WorldSizeTypes.WORLDSIZE_SMALL:		(21,13),
		WorldSizeTypes.WORLDSIZE_STANDARD:	(22,13),
		WorldSizeTypes.WORLDSIZE_LARGE:		(25,15),
		WorldSizeTypes.WORLDSIZE_HUGE:		(29,17)
	}

def minStartingDistanceModifier():
	return -20

def findStartingPlot(argsList):
	[playerID] = argsList

	def isValid(playerID, x, y):
                #return False #Rhye
		map = CyMap()
		pPlot = map
		
		if (pPlot.getArea() != map.findBiggestArea(False).getID()):
			return False

		return True
	
	return CvMapGeneratorUtil.findStartingPlot(playerID, isValid)
        #return CvMapGeneratorUtil.findStartingPlot(playerID, utils.isValid) #Rhye (it's the same)

class TerraMultilayeredFractal(CvMapGeneratorUtil.MultilayeredFractal):


        
	# Subclass. Only the controlling function overridden in this case.
	def generatePlotsByRegion(self):                
		
		#StoredData.StoredData().setupScriptData() #moved to getGridSize()

		# Sea Level adjustment (from user input), limited to value of 5%.
		sea = self.gc.getSeaLevelInfo(self.map.getSeaLevel()).getSeaLevelChange()
		#sea = min(sea, 5) #Rhye
		#sea = max(sea, -5) #Rhye
                likelihood = int(self.map.getSeaLevel())

                # Dice rolls
                roll5 = self.dice.get(2, "Divided Eurasia - Terra PYTHON")
                roll1 = self.dice.get(2, "Eurasian Hemisphere N/S - Terra PYTHON")
                #roll1 = 1 #debug
                roll2 = self.dice.get(2, "Eurasian Hemisphere E/W - Terra PYTHON")
                #roll2=1 #debug
                roll3 = self.dice.get(2, "American Hemisphere N/S - Terra PYTHON")
                roll4 = self.dice.get(3, "Central America shape - Terra PYTHON")
                #roll4=1 #debug
                roll6 = self.dice.get(2, "Extra oceanian territory")
                roll7 = self.dice.get(5, "African position - Terra PYTHON")
                if (roll7 == 2):
                        roll6 = 0
                roll8 = self.dice.get(5, "British/Japanese isles - Terra PYTHON")
                roll9 = self.dice.get(4, "Force spawn regions")

                if (likelihood == 0 or likelihood == 1): #high
                        roll5 = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll6 = 1
                        roll7 = 0
                        roll8 = 4
                        roll9 = 1
                if (likelihood >= 3): #low
                        roll9 = 0



		

                
		if (likelihood == 0): #very high
                        # Sirian's MultilayeredFractal class, controlling function.
                        # You -MUST- customize this function for each use of the class.
                        #
                        # The following grain matrix is specific to Terra.py
                        sizekey = self.map.getWorldSize()
                        sizevalues = {
                                #Rhye RFCRAND
##                                WorldSizeTypes.WORLDSIZE_DUEL:      (3,2,1),
##                                WorldSizeTypes.WORLDSIZE_TINY:      (3,2,1),
##                                WorldSizeTypes.WORLDSIZE_SMALL:     (4,2,1),
                                WorldSizeTypes.WORLDSIZE_STANDARD:  (4,2,1),
                                WorldSizeTypes.WORLDSIZE_LARGE:     (4,2,1),
                                WorldSizeTypes.WORLDSIZE_HUGE:      (5,2,1)
                                }
                        (ScatterGrain, BalanceGrain, GatherGrain) = sizevalues[sizekey]
                        

                        # The following regions are specific to Earth2.py

                        NATundraWestLon = 0.03 #0.05
                        NATundraEastLon = 0.20 #0.21
                        GreenlandWestLon = 0.24 #0.26
                        GreenlandEastLon = 0.31 #0.39
                        QuebecWestLon = 0.24 #Rhye
                        QuebecEastLon = 0.29 #Rhye
                        NAmericasWestLon = 0.07 #0.10
                        NAmericasEastLon = 0.26 #0.29
                        FloridaWestLon = 0.23 #0.28
                        FloridaEastLon = 0.25 #0.30                        
                        MexicoWestLon = 0.10 #0.12
                        MexicoEastLon = 0.18 #0.20
                        CAmericasWestLon = 0.11 #0.13
                        CAmericasEastLon = 0.23 #0.25
                        PanamaWestLon = 0.17 #0.21
                        PanamaEastLon = 0.21 #0.25
                        CaribWestLon = 0.14 #0.17
                        CaribEastLon = 0.31 #0.35
                        SAmericasWestLon = 0.14 #0.19
                        SAmericasEastLon = 0.31 #0.33                        
                        BrazilWestLon = 0.14 #0.21
                        BrazilEastLon = 0.33 #0.37
                        atlanticLine = BrazilEastLon #Rhye
                        AndesWestLon = 0.17 #0.23
                        AndesEastLon = 0.22 #0.26
                        
                        EmeraldWestLon = 0.37 #0.54
                        EmeraldEastLon = 0.44 #0.58
                        ScandinaviaWestLon = 0.46 #0.60
                        ScandinaviaEastLon = 0.66 #0.68
                        NEuropeWestLon = 0.47 #Rhye
                        NEuropeEastLon = 0.63 #Rhye
                        CEuropeWestLon = 0.43 #0.54
                        CEuropeEastLon = 0.64 #0.68
                        EEuropeWestLon = 0.62 #Rhye
                        EEuropeEastLon = 0.71 #Rhye
                        IberiaWestLon = 0.38 #0.51
                        IberiaEastLon = 0.47 #0.55
                        ItalyWestLon = 0.50 #Rhye
                        ItalyEastLon = 0.55 #Rhye
                        MediWestLon = 0.57 #0.54
                        MediEastLon = 0.64 #0.68
                        NumidiaWestLon = 0.40 #0.50
                        NumidiaEastLon = 0.54 #0.58
                        AfricaWestLon = 0.50
                        AfricaEastLon = 0.63 #0.68
                        CAfricaWestLon = 0.52 #0.58
                        CAfricaEastLon = 0.63 #0.68
                        EAfricaWestLon = 0.60 #Rhye
                        EAfricaEastLon = 0.67 #Rhye                       
                        SAfricaWestLon = 0.54 #0.60
                        SAfricaEastLon = 0.60 #0.66
                        SiberiaWestLon = 0.63 #0.67
                        SiberiaEastLon = 0.95 #0.95
                        SteppeWestLon = 0.70 #0.67
                        SteppeEastLon = 0.90 #0.92
                        NearEastWestLon = 0.62 #0.67
                        NearEastEastLon = 0.78 #0.75
                        ArabiaWestLon = 0.63 #0.68
                        ArabiaEastLon = 0.71 #0.73
                        PersiaWestLon = 0.73 #Rhye
                        PersiaEastLon = 0.79 #Rhye
                        IndiaWestLon = 0.78 #0.73
                        IndiaEastLon = 0.83 #0.81
                        ChinaWestLon = 0.80
                        ChinaEastLon = 0.90 #0.89
                        IndoChinaWestLon = 0.85 #Rhye
                        IndoChinaEastLon = 0.89 #Rhye
                        IndonesiaWestLon = 0.85 #0.80
                        IndonesiaEastLon = 0.96 #0.94
                        JapanWestLon = 0.92 #0.91
                        JapanEastLon = 0.97 #0.94
                        AustraliaWestLon = 0.83 #0.84
                        AustraliaEastLon = 0.99 #0.96
                        SouthPacificWestLon = 0.00 #0.01
                        SouthPacificEastLon = 0.06 #0.20
                        
                        
                        NATundraNorthLat = 0.95 #0.94
                        NATundraSouthLat = 0.81 #0.80
                        GreenlandNorthLat = 0.99 #0.90
                        GreenlandSouthLat = 0.91 #0.78
                        QuebecNorthLat = 0.88 #Rhye
                        QuebecSouthLat = 0.77 #Rhye
                        NAmericasNorthLat = 0.83 #0.82
                        NAmericasSouthLat = 0.60 #0.63
                        FloridaNorthLat = 0.64
                        FloridaSouthLat = 0.56 #0.64
                        MexicoNorthLat = 0.70
                        MexicoSouthLat = 0.52 #0.60
                        CAmericasNorthLat = 0.60 #0.65
                        CAmericasSouthLat = 0.49 #0.54
                        PanamaNorthLat = 0.50 #0.55
                        PanamaSouthLat = 0.49 #0.54
                        CaribNorthLat = 0.61 #0.66
                        CaribSouthLat = 0.45 #0.50
                        SAmericasNorthLat = 0.50 #0.55
                        SAmericasSouthLat = 0.18 #0.25
                        BrazilNorthLat = 0.44 #0.50
                        BrazilSouthLat = 0.32 #0.40
                        AndesNorthLat = 0.51 #0.56
                        AndesSouthLat = 0.09 #0.14
                        
                        EmeraldNorthLat = 0.92 #0.86
                        EmeraldSouthLat = 0.73 #0.81
                        ScandinaviaNorthLat = 0.94 #0.92
                        ScandinaviaSouthLat = 0.81 #0.80
                        NEuropeNorthLat = 0.80 #Rhye
                        NEuropeSouthLat = 0.65 #Rhye
                        CEuropeNorthLat = 0.72 #0.80
                        CEuropeSouthLat = 0.62 #0.72
                        EEuropeNorthLat = 0.85 #Rhye
                        EEuropeSouthLat = 0.68 #Rhye
                        IberiaNorthLat = 0.65 #0.74
                        IberiaSouthLat = 0.55 #0.68
                        ItalyNorthLat = 0.65 #Rhye
                        ItalySouthLat = 0.54 #Rhye
                        MediNorthLat = 0.65 #0.75
                        MediSouthLat = 0.55 #0.60
                        AfricaNorthLat = 0.50 #0.60
                        AfricaSouthLat = 0.39 #0.44
                        NumidiaNorthLat = 0.51 #0.64
                        NumidiaSouthLat = 0.37 #0.55
                        CAfricaNorthLat = 0.41 #0.46
                        CAfricaSouthLat = 0.20 #0.25
                        EAfricaNorthLat = 0.36 #Rhye
                        EAfricaSouthLat = 0.29 #Rhye                       
                        SAfricaNorthLat = 0.25 #0.30
                        SAfricaSouthLat = 0.12 #0.18
                        SiberiaNorthLat = 0.96 #0.94
                        SiberiaSouthLat = 0.81 #0.82
                        SteppeNorthLat = 0.85
                        SteppeSouthLat = 0.60 #0.70
                        NearEastNorthLat = 0.60 #0.75
                        NearEastSouthLat = 0.50 #0.59
                        ArabiaNorthLat = 0.55 #0.60
                        ArabiaSouthLat = 0.39 #0.55
                        PersiaNorthLat = 0.54 #Rhye
                        PersiaSouthLat = 0.43 #Rhye
                        IndiaNorthLat = 0.65 #0.75
                        IndiaSouthLat = 0.36 #0.47
                        ChinaNorthLat = 0.63 #0.75
                        ChinaSouthLat = 0.42 #0.50
                        IndoChinaNorthLat = 0.51 #Rhye
                        IndoChinaSouthLat = 0.37 #Rhye
                        IndonesiaNorthLat = 0.52 #0.55
                        IndonesiaSouthLat = 0.28 #0.32
                        JapanNorthLat = 0.79 #0.75
                        JapanSouthLat = 0.50 #0.65
                        AustraliaNorthLat = 0.30
                        AustraliaSouthLat = 0.11 #0.15
                        SouthPacificNorthLat = 0.45
                        SouthPacificSouthLat = 0.09 #0.15

                        # Simulate the Western Hemisphere - North American Tundra.
                        NiTextOut("Generating North America (Python Earth2) ...")
                        # Set dimensions of North American Tundra
                        NATundraWestX = int(self.iW * NATundraWestLon)
                        NATundraEastX = int(self.iW * NATundraEastLon)
                        NATundraNorthY = int(self.iH * NATundraNorthLat)
                        NATundraSouthY = int(self.iH * NATundraSouthLat)
                        NATundraWidth = NATundraEastX - NATundraWestX + 1
                        NATundraHeight = NATundraNorthY - NATundraSouthY + 1

                        NATundraWater = 35+sea
                        
                        self.generatePlotsInRegion(NATundraWater,
                                                   NATundraWidth, NATundraHeight,
                                                   NATundraWestX, NATundraSouthY,
                                                   BalanceGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                    
                        # Simulate the Western Hemisphere - North American Tundra.
                        NiTextOut("Generating North America (Python Earth2) ...")
                        # Set dimensions of Greenland
                        GreenlandWestX = int(self.iW * GreenlandWestLon)
                        GreenlandEastX = int(self.iW * GreenlandEastLon)
                        GreenlandNorthY = int(self.iH * GreenlandNorthLat)
                        GreenlandSouthY = int(self.iH * GreenlandSouthLat)
                        GreenlandWidth = GreenlandEastX - GreenlandWestX + 1
                        GreenlandHeight = GreenlandNorthY - GreenlandSouthY + 1

                        GreenlandWater = 45+sea #Rhye 70+sea
                        
                        self.generatePlotsInRegion(GreenlandWater,
                                                   GreenlandWidth, GreenlandHeight,
                                                   GreenlandWestX, GreenlandSouthY,
                                                   ScatterGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   1, True,
                                                   False
                                                   )

                        self.generatePlotsInRegion(GreenlandWater,
                                                   GreenlandWidth, GreenlandHeight,
                                                   GreenlandWestX, GreenlandSouthY,
                                                   ScatterGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   1, True,
                                                   False
                                                   )

                        #Rhye
                        # Simulate the Western Hemisphere - Quebec
                        NiTextOut("Generating North America (Python Earth2) ...")
                        # Set dimensions of Quebec
                        QuebecWestX = int(self.iW * QuebecWestLon)
                        QuebecEastX = int(self.iW * QuebecEastLon)
                        QuebecNorthY = int(self.iH * QuebecNorthLat)
                        QuebecSouthY = int(self.iH * QuebecSouthLat)
                        QuebecWidth = QuebecEastX - QuebecWestX + 1
                        QuebecHeight = QuebecNorthY - QuebecSouthY + 1

                        QuebecWater = 45+sea #Rhye 70+sea
                        
                        self.generatePlotsInRegion(QuebecWater,
                                                   QuebecWidth, QuebecHeight,
                                                   QuebecWestX, QuebecSouthY,
                                                   ScatterGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   1, True,
                                                   False
                                                   )

                        self.generatePlotsInRegion(QuebecWater,
                                                   QuebecWidth, QuebecHeight,
                                                   QuebecWestX, QuebecSouthY,
                                                   ScatterGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   1, True,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - North America Mainland.
                        NiTextOut("Generating North America (Python Earth2) ...")
                        # Set dimensions of North America Mainland
                        NAmericasWestX = int(self.iW * NAmericasWestLon)
                        NAmericasEastX = int(self.iW * NAmericasEastLon)
                        NAmericasNorthY = int(self.iH * NAmericasNorthLat)
                        NAmericasSouthY = int(self.iH * NAmericasSouthLat)
                        NAmericasWidth = NAmericasEastX - NAmericasWestX + 1
                        NAmericasHeight = NAmericasNorthY - NAmericasSouthY + 1

                        NAmericasWater = 40+sea
                        
                        self.generatePlotsInRegion(NAmericasWater,
                                                   NAmericasWidth, NAmericasHeight,
                                                   NAmericasWestX, NAmericasSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(NAmericasWater,
                                                   NAmericasWidth, NAmericasHeight,
                                                   NAmericasWestX, NAmericasSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - Florida.
                        NiTextOut("Generating North America (Python Earth2) ...")
                        # Set dimensions of Florida
                        FloridaWestX = int(self.iW * FloridaWestLon)
                        FloridaEastX = int(self.iW * FloridaEastLon)
                        FloridaNorthY = int(self.iH * FloridaNorthLat)
                        FloridaSouthY = int(self.iH * FloridaSouthLat)
                        FloridaWidth = FloridaEastX - FloridaWestX + 1
                        FloridaHeight = FloridaNorthY - FloridaSouthY + 1

                        FloridaWater = 40+sea
                        
                        self.generatePlotsInRegion(FloridaWater,
                                                   FloridaWidth, FloridaHeight,
                                                   FloridaWestX, FloridaSouthY,
                                                   GatherGrain, ScatterGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - Mexico.
                        NiTextOut("Generating Central America (Python Earth2) ...")
                        # Set dimensions of Mexico
                        MexicoWestX = int(self.iW * MexicoWestLon)
                        MexicoEastX = int(self.iW * MexicoEastLon)
                        MexicoNorthY = int(self.iH * MexicoNorthLat)
                        MexicoSouthY = int(self.iH * MexicoSouthLat)
                        MexicoWidth = MexicoEastX - MexicoWestX + 1
                        MexicoHeight = MexicoNorthY - MexicoSouthY + 1

                        MexicoWater = 30+sea
                        
                        self.generatePlotsInRegion(MexicoWater,
                                                   MexicoWidth, MexicoHeight,
                                                   MexicoWestX, MexicoSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - Central America.
                        NiTextOut("Generating Central America (Python Earth2) ...")
                        # Set dimensions of Central America
                        CAmericasWestX = int(self.iW * CAmericasWestLon)
                        CAmericasEastX = int(self.iW * CAmericasEastLon)
                        CAmericasNorthY = int(self.iH * CAmericasNorthLat)
                        CAmericasSouthY = int(self.iH * CAmericasSouthLat)
                        CAmericasWidth = CAmericasEastX - CAmericasWestX + 1
                        CAmericasHeight = CAmericasNorthY - CAmericasSouthY + 1

                        CAmericasWater = 80+sea
                        
                        self.generatePlotsInRegion(CAmericasWater,
                                                   CAmericasWidth, CAmericasHeight,
                                                   CAmericasWestX, CAmericasSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - Panama.
                        NiTextOut("Generating Central America (Python Earth2) ...")
                        # Set dimensions of Panama
                        PanamaWestX = int(self.iW * PanamaWestLon)
                        PanamaEastX = int(self.iW * PanamaEastLon)
                        PanamaNorthY = int(self.iH * PanamaNorthLat)
                        PanamaSouthY = int(self.iH * PanamaSouthLat)
                        PanamaWidth = PanamaEastX - PanamaWestX + 1
                        PanamaHeight = PanamaNorthY - PanamaSouthY + 1

                        PanamaWater = 85+sea
                        
                        self.generatePlotsInRegion(PanamaWater,
                                                   PanamaWidth, PanamaHeight,
                                                   PanamaWestX, PanamaSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iHorzFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - The Caribbean.
                        NiTextOut("Generating Central America (Python Earth2) ...")
                        # Set dimensions of The Caribbean
                        CaribWestX = int(self.iW * CaribWestLon)
                        CaribEastX = int(self.iW * CaribEastLon)
                        CaribNorthY = int(self.iH * CaribNorthLat)
                        CaribSouthY = int(self.iH * CaribSouthLat)
                        CaribWidth = CaribEastX - CaribWestX + 1
                        CaribHeight = CaribNorthY - CaribSouthY + 1

                        CaribWater = 90+sea
                        
                        self.generatePlotsInRegion(CaribWater,
                                                   CaribWidth, CaribHeight,
                                                   CaribWestX, CaribSouthY,
                                                   ScatterGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - South America.
                        NiTextOut("Generating South America (Python Earth2) ...")
                        # Set dimensions of South America
                        SAmericasWestX = int(self.iW * SAmericasWestLon)
                        SAmericasEastX = int(self.iW * SAmericasEastLon)
                        SAmericasNorthY = int(self.iH * SAmericasNorthLat)
                        SAmericasSouthY = int(self.iH * SAmericasSouthLat)
                        SAmericasWidth = SAmericasEastX - SAmericasWestX + 1
                        SAmericasHeight = SAmericasNorthY - SAmericasSouthY + 1

                        SAmericasWater = 65+sea
                        
                        self.generatePlotsInRegion(SAmericasWater,
                                                   SAmericasWidth, SAmericasHeight,
                                                   SAmericasWestX, SAmericasSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(SAmericasWater,
                                                   SAmericasWidth, SAmericasHeight,
                                                   SAmericasWestX, SAmericasSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - Brazil.
                        NiTextOut("Generating South America (Python Earth2) ...")
                        # Set dimensions of Brazil
                        BrazilWestX = int(self.iW * BrazilWestLon)
                        BrazilEastX = int(self.iW * BrazilEastLon)
                        BrazilNorthY = int(self.iH * BrazilNorthLat)
                        BrazilSouthY = int(self.iH * BrazilSouthLat)
                        BrazilWidth = BrazilEastX - BrazilWestX + 1
                        BrazilHeight = BrazilNorthY - BrazilSouthY + 1

                        BrazilWater = 45+sea
                        
                        self.generatePlotsInRegion(BrazilWater,
                                                   BrazilWidth, BrazilHeight,
                                                   BrazilWestX, BrazilSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(BrazilWater,
                                                   BrazilWidth, BrazilHeight,
                                                   BrazilWestX, BrazilSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iHorzFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Western Hemisphere - Andes.
                        NiTextOut("Generating South America (Python Earth2) ...")
                        # Set dimensions of Andes
                        AndesWestX = int(self.iW * AndesWestLon)
                        AndesEastX = int(self.iW * AndesEastLon)
                        AndesNorthY = int(self.iH * AndesNorthLat)
                        AndesSouthY = int(self.iH * AndesSouthLat)
                        AndesWidth = AndesEastX - AndesWestX + 1
                        AndesHeight = AndesNorthY - AndesSouthY + 1

                        AndesWater = 35+sea
                        
                        self.generatePlotsInRegion(AndesWater,
                                                   AndesWidth, AndesHeight,
                                                   AndesWestX, AndesSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        self.setAmericaInfo(0,NATundraWestX)
                        self.setAmericaInfo(1,BrazilEastX)
                        self.setAmericaInfo(2,AndesSouthY)
                        self.setAmericaInfo(3,NATundraNorthY)

                        # Simulate the Eastern Hemisphere - British Isles.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of British Isles
                        EmeraldWestX = int(self.iW * EmeraldWestLon)
                        EmeraldEastX = int(self.iW * EmeraldEastLon)
                        EmeraldNorthY = int(self.iH * EmeraldNorthLat)
                        EmeraldSouthY = int(self.iH * EmeraldSouthLat)
                        EmeraldWidth = EmeraldEastX - EmeraldWestX + 1
                        EmeraldHeight = EmeraldNorthY - EmeraldSouthY + 1

                        EmeraldWater = 60+sea #80+sea
                        
                        self.generatePlotsInRegion(EmeraldWater,
                                                   EmeraldWidth, EmeraldHeight,
                                                   EmeraldWestX, EmeraldSouthY,
                                                   BalanceGrain, ScatterGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(EmeraldWater,
                                                   EmeraldWidth, EmeraldHeight,
                                                   EmeraldWestX, EmeraldSouthY,
                                                   BalanceGrain, ScatterGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   1, False,
                                                   False
                                                   )


                        #Rhye
                        self.setIsland1Info(0,EmeraldWestX)
                        self.setIsland1Info(1,EmeraldEastX)
                        self.setIsland1Info(2,EmeraldSouthY)
                        self.setIsland1Info(3,EmeraldNorthY)

                        #Rhye
                        # Simulate the Eastern Hemisphere - Scandinavia.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of Scandinavia
                        ScandinaviaWestX = int(self.iW * ScandinaviaWestLon)
                        ScandinaviaEastX = int(self.iW * ScandinaviaEastLon)
                        ScandinaviaNorthY = int(self.iH * ScandinaviaNorthLat)
                        ScandinaviaSouthY = int(self.iH * ScandinaviaSouthLat)
                        ScandinaviaWidth = ScandinaviaEastX - ScandinaviaWestX + 1
                        ScandinaviaHeight = ScandinaviaNorthY - ScandinaviaSouthY + 1

                        ScandinaviaWater = 50+sea
                        
                        self.generatePlotsInRegion(ScandinaviaWater,
                                                   ScandinaviaWidth, ScandinaviaHeight,
                                                   ScandinaviaWestX, ScandinaviaSouthY,
                                                   BalanceGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Northern Europe.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of Northern Europe
                        NEuropeWestX = int(self.iW * NEuropeWestLon)
                        NEuropeEastX = int(self.iW * NEuropeEastLon)
                        NEuropeNorthY = int(self.iH * NEuropeNorthLat)
                        NEuropeSouthY = int(self.iH * NEuropeSouthLat)
                        NEuropeWidth = NEuropeEastX - NEuropeWestX + 1
                        NEuropeHeight = NEuropeNorthY - NEuropeSouthY + 1

                        NEuropeWater = 40+sea #50+sea
                        
                        self.generatePlotsInRegion(NEuropeWater,
                                                   NEuropeWidth, NEuropeHeight,
                                                   NEuropeWestX, NEuropeSouthY,
                                                   BalanceGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Central Europe.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of Central Europe
                        CEuropeWestX = int(self.iW * CEuropeWestLon)
                        CEuropeEastX = int(self.iW * CEuropeEastLon)
                        CEuropeNorthY = int(self.iH * CEuropeNorthLat)
                        CEuropeSouthY = int(self.iH * CEuropeSouthLat)
                        CEuropeWidth = CEuropeEastX - CEuropeWestX + 1
                        CEuropeHeight = CEuropeNorthY - CEuropeSouthY + 1

                        CEuropeWater = 35+sea
                        
                        self.generatePlotsInRegion(CEuropeWater,
                                                   CEuropeWidth, CEuropeHeight,
                                                   CEuropeWestX, CEuropeSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(CEuropeWater,
                                                   CEuropeWidth, CEuropeHeight,
                                                   CEuropeWestX, CEuropeSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        # Simulate the Eastern Hemisphere - Eastern Europe.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of Eastern Europe
                        EEuropeWestX = int(self.iW * EEuropeWestLon)
                        EEuropeEastX = int(self.iW * EEuropeEastLon)
                        EEuropeNorthY = int(self.iH * EEuropeNorthLat)
                        EEuropeSouthY = int(self.iH * EEuropeSouthLat)
                        EEuropeWidth = EEuropeEastX - EEuropeWestX + 1
                        EEuropeHeight = EEuropeNorthY - EEuropeSouthY + 1

                        EEuropeWater = 35+sea
                        
                        self.generatePlotsInRegion(EEuropeWater,
                                                   EEuropeWidth, EEuropeHeight,
                                                   EEuropeWestX, EEuropeSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(EEuropeWater,
                                                   EEuropeWidth, EEuropeHeight,
                                                   EEuropeWestX, EEuropeSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Iberia.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of Iberia
                        IberiaWestX = int(self.iW * IberiaWestLon)
                        IberiaEastX = int(self.iW * IberiaEastLon)
                        IberiaNorthY = int(self.iH * IberiaNorthLat)
                        IberiaSouthY = int(self.iH * IberiaSouthLat)
                        IberiaWidth = IberiaEastX - IberiaWestX + 1
                        IberiaHeight = IberiaNorthY - IberiaSouthY + 1

                        IberiaWater = 10+sea #Rhye 20+sea
                        
                        self.generatePlotsInRegion(IberiaWater,
                                                   IberiaWidth, IberiaHeight,
                                                   IberiaWestX, IberiaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   0, self.iTerrainFlags, #self.iRoundFlags, self.iTerrainFlags, #Rhye
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        # Simulate the Eastern Hemisphere - Italy.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of Italy
                        ItalyWestX = int(self.iW * ItalyWestLon)
                        ItalyEastX = int(self.iW * ItalyEastLon)
                        ItalyNorthY = int(self.iH * ItalyNorthLat)
                        ItalySouthY = int(self.iH * ItalySouthLat)
                        ItalyWidth = ItalyEastX - ItalyWestX + 1
                        ItalyHeight = ItalyNorthY - ItalySouthY + 1

                        ItalyWater = 45+sea
                        
                        self.generatePlotsInRegion(ItalyWater,
                                                   ItalyWidth, ItalyHeight,
                                                   ItalyWestX, ItalySouthY,
                                                   ScatterGrain, ScatterGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )


                        # Simulate the Eastern Hemisphere - Mediterranean.
                        NiTextOut("Generating Europe (Python Earth2) ...")
                        # Set dimensions of Mediterranean
                        MediWestX = int(self.iW * MediWestLon)
                        MediEastX = int(self.iW * MediEastLon)
                        MediNorthY = int(self.iH * MediNorthLat)
                        MediSouthY = int(self.iH * MediSouthLat)
                        MediWidth = MediEastX - MediWestX + 1
                        MediHeight = MediNorthY - MediSouthY + 1

                        MediWater = 60+sea #Rhye 80+sea
                        
                        self.generatePlotsInRegion(MediWater,
                                                   MediWidth, MediHeight,
                                                   MediWestX, MediSouthY,
                                                   ScatterGrain, ScatterGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - North Africa.
                        NiTextOut("Generating Africa (Python Earth2) ...")
                        # Set dimensions of North Africa
                        AfricaWestX = int(self.iW * AfricaWestLon)
                        AfricaEastX = int(self.iW * AfricaEastLon)
                        AfricaNorthY = int(self.iH * AfricaNorthLat)
                        AfricaSouthY = int(self.iH * AfricaSouthLat)
                        AfricaWidth = AfricaEastX - AfricaWestX + 1
                        AfricaHeight = AfricaNorthY - AfricaSouthY + 1

                        AfricaWater = 50+sea
                        
                        self.generatePlotsInRegion(AfricaWater,
                                                   AfricaWidth, AfricaHeight,
                                                   AfricaWestX, AfricaSouthY,
                                                   GatherGrain, ScatterGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )
                        
                        self.generatePlotsInRegion(AfricaWater,
                                                   AfricaWidth, AfricaHeight,
                                                   AfricaWestX, AfricaSouthY,
                                                   GatherGrain, ScatterGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(AfricaWater,
                                                   AfricaWidth, AfricaHeight,
                                                   AfricaWestX, AfricaSouthY,
                                                   GatherGrain, ScatterGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Numidia.
                        NiTextOut("Generating Africa (Python Earth2) ...")
                        # Set dimensions of Numidia
                        NumidiaWestX = int(self.iW * NumidiaWestLon)
                        NumidiaEastX = int(self.iW * NumidiaEastLon)
                        NumidiaNorthY = int(self.iH * NumidiaNorthLat)
                        NumidiaSouthY = int(self.iH * NumidiaSouthLat)
                        NumidiaWidth = NumidiaEastX - NumidiaWestX + 1
                        NumidiaHeight = NumidiaNorthY - NumidiaSouthY + 1

                        NumidiaWater = 10+sea #Rhye 20+sea
                        
                        self.generatePlotsInRegion(NumidiaWater,
                                                   NumidiaWidth, NumidiaHeight,
                                                   NumidiaWestX, NumidiaSouthY,
                                                   GatherGrain, GatherGrain,
                                                   0, self.iTerrainFlags, #self.iRoundFlags, self.iTerrainFlags, #Rhye
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Central Africa.
                        NiTextOut("Generating Africa (Python Earth2) ...")
                        # Set dimensions of Central Africa
                        CAfricaWestX = int(self.iW * CAfricaWestLon)
                        CAfricaEastX = int(self.iW * CAfricaEastLon)
                        CAfricaNorthY = int(self.iH * CAfricaNorthLat)
                        CAfricaSouthY = int(self.iH * CAfricaSouthLat)
                        CAfricaWidth = CAfricaEastX - CAfricaWestX + 1
                        CAfricaHeight = CAfricaNorthY - CAfricaSouthY + 1

                        CAfricaWater = 35+sea
                        
                        self.generatePlotsInRegion(CAfricaWater,
                                                   CAfricaWidth, CAfricaHeight,
                                                   CAfricaWestX, CAfricaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(CAfricaWater,
                                                   CAfricaWidth, CAfricaHeight,
                                                   CAfricaWestX, CAfricaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        # Simulate the Eastern Hemisphere - East Africa.
                        NiTextOut("Generating Africa (Python Earth2) ...")
                        # Set dimensions of East Africa
                        EAfricaWestX = int(self.iW * EAfricaWestLon)
                        EAfricaEastX = int(self.iW * EAfricaEastLon)
                        EAfricaNorthY = int(self.iH * EAfricaNorthLat)
                        EAfricaSouthY = int(self.iH * EAfricaSouthLat)
                        EAfricaWidth = EAfricaEastX - EAfricaWestX + 1
                        EAfricaHeight = EAfricaNorthY - EAfricaSouthY + 1

                        EAfricaWater = 45+sea
                        
                        self.generatePlotsInRegion(EAfricaWater,
                                                   EAfricaWidth, EAfricaHeight,
                                                   EAfricaWestX, EAfricaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(EAfricaWater,
                                                   EAfricaWidth, EAfricaHeight,
                                                   EAfricaWestX, EAfricaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - South Africa.
                        NiTextOut("Generating Africa (Python Earth2) ...")
                        # Set dimensions of South Africa
                        SAfricaWestX = int(self.iW * SAfricaWestLon)
                        SAfricaEastX = int(self.iW * SAfricaEastLon)
                        SAfricaNorthY = int(self.iH * SAfricaNorthLat)
                        SAfricaSouthY = int(self.iH * SAfricaSouthLat)
                        SAfricaWidth = SAfricaEastX - SAfricaWestX + 1
                        SAfricaHeight = SAfricaNorthY - SAfricaSouthY + 1

                        SAfricaWater = 45+sea
                        
                        self.generatePlotsInRegion(SAfricaWater,
                                                   SAfricaWidth, SAfricaHeight,
                                                   SAfricaWestX, SAfricaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(SAfricaWater,
                                                   SAfricaWidth, SAfricaHeight,
                                                   SAfricaWestX, SAfricaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        self.setAfricaInfo(0,NumidiaWestX)
                        self.setAfricaInfo(1,CAfricaEastX)
                        self.setAfricaInfo(2,SAfricaSouthY)
                        self.setAfricaInfo(3,AfricaNorthY)

                        # Simulate the Eastern Hemisphere - Siberia.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of Siberia
                        SiberiaWestX = int(self.iW * SiberiaWestLon)
                        SiberiaEastX = int(self.iW * SiberiaEastLon)
                        SiberiaNorthY = int(self.iH * SiberiaNorthLat)
                        SiberiaSouthY = int(self.iH * SiberiaSouthLat)
                        SiberiaWidth = SiberiaEastX - SiberiaWestX + 1
                        SiberiaHeight = SiberiaNorthY - SiberiaSouthY + 1

                        SiberiaWater = 25+sea
                        
                        self.generatePlotsInRegion(SiberiaWater,
                                                   SiberiaWidth, SiberiaHeight,
                                                   SiberiaWestX, SiberiaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Steppe.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of Steppe
                        SteppeWestX = int(self.iW * SteppeWestLon)
                        SteppeEastX = int(self.iW * SteppeEastLon)
                        SteppeNorthY = int(self.iH * SteppeNorthLat)
                        SteppeSouthY = int(self.iH * SteppeSouthLat)
                        SteppeWidth = SteppeEastX - SteppeWestX + 1
                        SteppeHeight = SteppeNorthY - SteppeSouthY + 1

                        SteppeWater = 6+sea
                        
                        self.generatePlotsInRegion(SteppeWater,
                                                   SteppeWidth, SteppeHeight,
                                                   SteppeWestX, SteppeSouthY,
                                                   GatherGrain, GatherGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Near East.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of Near East
                        NearEastWestX = int(self.iW * NearEastWestLon)
                        NearEastEastX = int(self.iW * NearEastEastLon)
                        NearEastNorthY = int(self.iH * NearEastNorthLat)
                        NearEastSouthY = int(self.iH * NearEastSouthLat)
                        NearEastWidth = NearEastEastX - NearEastWestX + 1
                        NearEastHeight = NearEastNorthY - NearEastSouthY + 1

                        NearEastWater = 50+sea
                        
                        self.generatePlotsInRegion(NearEastWater,
                                                   NearEastWidth, NearEastHeight,
                                                   NearEastWestX, NearEastSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(NearEastWater,
                                                   NearEastWidth, NearEastHeight,
                                                   NearEastWestX, NearEastSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Arabia.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of Arabia
                        ArabiaWestX = int(self.iW * ArabiaWestLon)
                        ArabiaEastX = int(self.iW * ArabiaEastLon)
                        ArabiaNorthY = int(self.iH * ArabiaNorthLat)
                        ArabiaSouthY = int(self.iH * ArabiaSouthLat)
                        ArabiaWidth = ArabiaEastX - ArabiaWestX + 1
                        ArabiaHeight = ArabiaNorthY - ArabiaSouthY + 1

                        ArabiaWater = 30+sea #Rhye 50+sea
                        
                        self.generatePlotsInRegion(ArabiaWater,
                                                   ArabiaWidth, ArabiaHeight,
                                                   ArabiaWestX, ArabiaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        # Simulate the Eastern Hemisphere - Persia
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of Persia
                        PersiaWestX = int(self.iW * PersiaWestLon)
                        PersiaEastX = int(self.iW * PersiaEastLon)
                        PersiaNorthY = int(self.iH * PersiaNorthLat)
                        PersiaSouthY = int(self.iH * PersiaSouthLat)
                        PersiaWidth = PersiaEastX - PersiaWestX + 1
                        PersiaHeight = PersiaNorthY - PersiaSouthY + 1

                        PersiaWater = 40+sea
                        
                        self.generatePlotsInRegion(PersiaWater,
                                                   PersiaWidth, PersiaHeight,
                                                   PersiaWestX, PersiaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )
                        
                        self.generatePlotsInRegion(PersiaWater,
                                                   PersiaWidth, PersiaHeight,
                                                   PersiaWestX, PersiaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )


                        # Simulate the Eastern Hemisphere - India.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of India
                        IndiaWestX = int(self.iW * IndiaWestLon)
                        IndiaEastX = int(self.iW * IndiaEastLon)
                        IndiaNorthY = int(self.iH * IndiaNorthLat)
                        IndiaSouthY = int(self.iH * IndiaSouthLat)
                        IndiaWidth = IndiaEastX - IndiaWestX + 1
                        IndiaHeight = IndiaNorthY - IndiaSouthY + 1

                        IndiaWater = 33+sea
                        
                        self.generatePlotsInRegion(IndiaWater,
                                                   IndiaWidth, IndiaHeight,
                                                   IndiaWestX, IndiaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )
                        
                        self.generatePlotsInRegion(IndiaWater,
                                                   IndiaWidth, IndiaHeight,
                                                   IndiaWestX, IndiaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - China.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of China
                        ChinaWestX = int(self.iW * ChinaWestLon)
                        ChinaEastX = int(self.iW * ChinaEastLon)
                        ChinaNorthY = int(self.iH * ChinaNorthLat)
                        ChinaSouthY = int(self.iH * ChinaSouthLat)
                        ChinaWidth = ChinaEastX - ChinaWestX + 1
                        ChinaHeight = ChinaNorthY - ChinaSouthY + 1

                        ChinaWater = 65+sea
                        
                        self.generatePlotsInRegion(ChinaWater,
                                                   ChinaWidth, ChinaHeight,
                                                   ChinaWestX, ChinaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )
                        
                        self.generatePlotsInRegion(ChinaWater,
                                                   ChinaWidth, ChinaHeight,
                                                   ChinaWestX, ChinaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iHorzFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(ChinaWater,
                                                   ChinaWidth, ChinaHeight,
                                                   ChinaWestX, ChinaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iHorzFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        # Simulate the Eastern Hemisphere - IndoChina.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of IndoChina
                        IndoChinaWestX = int(self.iW * IndoChinaWestLon)
                        IndoChinaEastX = int(self.iW * IndoChinaEastLon)
                        IndoChinaNorthY = int(self.iH * IndoChinaNorthLat)
                        IndoChinaSouthY = int(self.iH * IndoChinaSouthLat)
                        IndoChinaWidth = IndoChinaEastX - IndoChinaWestX + 1
                        IndoChinaHeight = IndoChinaNorthY - IndoChinaSouthY + 1

                        IndoChinaWater = 60+sea
                        
                        self.generatePlotsInRegion(IndoChinaWater,
                                                   IndoChinaWidth, IndoChinaHeight,
                                                   IndoChinaWestX, IndoChinaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )
                        
                        self.generatePlotsInRegion(IndoChinaWater,
                                                   IndoChinaWidth, IndoChinaHeight,
                                                   IndoChinaWestX, IndoChinaSouthY,
                                                   ScatterGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the Eastern Hemisphere - Indonesia.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of Indonesia
                        IndonesiaWestX = int(self.iW * IndonesiaWestLon)
                        IndonesiaEastX = int(self.iW * IndonesiaEastLon)
                        IndonesiaNorthY = int(self.iH * IndonesiaNorthLat)
                        IndonesiaSouthY = int(self.iH * IndonesiaSouthLat)
                        IndonesiaWidth = IndonesiaEastX - IndonesiaWestX + 1
                        IndonesiaHeight = IndonesiaNorthY - IndonesiaSouthY + 1

                        IndonesiaWater = 82+sea
                        
                        self.generatePlotsInRegion(IndonesiaWater,
                                                   IndonesiaWidth, IndonesiaHeight,
                                                   IndonesiaWestX, IndonesiaSouthY,
                                                   ScatterGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )
                        
                        self.generatePlotsInRegion(IndonesiaWater,
                                                   IndonesiaWidth, IndonesiaHeight,
                                                   IndonesiaWestX, IndonesiaSouthY,
                                                   ScatterGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        #Rhye
                        self.setEurasiaInfo(0,IberiaWestX)
                        self.setEurasiaInfo(1,ChinaEastX)
                        self.setEurasiaInfo(2,IndiaSouthY)
                        self.setEurasiaInfo(3,NEuropeNorthY)
                        

                        # Simulate the Eastern Hemisphere - Japan.
                        NiTextOut("Generating Asia (Python Earth2) ...")
                        # Set dimensions of Japan
                        JapanWestX = int(self.iW * JapanWestLon)
                        JapanEastX = int(self.iW * JapanEastLon)
                        JapanNorthY = int(self.iH * JapanNorthLat)
                        JapanSouthY = int(self.iH * JapanSouthLat)
                        JapanWidth = JapanEastX - JapanWestX + 1
                        JapanHeight = JapanNorthY - JapanSouthY + 1

                        JapanWater = 63+sea #Rhye 92+sea
                        
                        self.generatePlotsInRegion(JapanWater,
                                                   JapanWidth, JapanHeight,
                                                   JapanWestX, JapanSouthY,
                                                   BalanceGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(JapanWater,
                                                   JapanWidth, JapanHeight,
                                                   JapanWestX, JapanSouthY,
                                                   BalanceGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )


                        #Rhye
                        self.setIsland2Info(0,JapanWestX)
                        self.setIsland2Info(1,JapanEastX)
                        self.setIsland2Info(2,JapanSouthY)
                        self.setIsland2Info(3,JapanNorthY)

                        
                        

                        # Simulate the Eastern Hemisphere - Australia.
                        NiTextOut("Generating Australia (Python Earth2) ...")
                        # Set dimensions of Australia
                        AustraliaWestX = int(self.iW * AustraliaWestLon)
                        AustraliaEastX = int(self.iW * AustraliaEastLon)
                        AustraliaNorthY = int(self.iH * AustraliaNorthLat)
                        AustraliaSouthY = int(self.iH * AustraliaSouthLat)
                        AustraliaWidth = AustraliaEastX - AustraliaWestX + 1
                        AustraliaHeight = AustraliaNorthY - AustraliaSouthY + 1

                        AustraliaWater = 50+sea #Rhye 45+sea
                        
                        self.generatePlotsInRegion(AustraliaWater,
                                                   AustraliaWidth, AustraliaHeight,
                                                   AustraliaWestX, AustraliaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        self.generatePlotsInRegion(AustraliaWater,
                                                   AustraliaWidth, AustraliaHeight,
                                                   AustraliaWestX, AustraliaSouthY,
                                                   GatherGrain, BalanceGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )

                        # Simulate the South Pacific - South Pacific.
                        NiTextOut("Generating Pacific (Python Earth2) ...")
                        # Set dimensions of South Pacific
                        SouthPacificWestX = int(self.iW * SouthPacificWestLon)
                        SouthPacificEastX = int(self.iW * SouthPacificEastLon)
                        SouthPacificNorthY = int(self.iH * SouthPacificNorthLat)
                        SouthPacificSouthY = int(self.iH * SouthPacificSouthLat)
                        SouthPacificWidth = SouthPacificEastX - SouthPacificWestX + 1
                        SouthPacificHeight = SouthPacificNorthY - SouthPacificSouthY + 1

                        SouthPacificWater = 91+sea #94+sea
                        
                        self.generatePlotsInRegion(SouthPacificWater,
                                                   SouthPacificWidth, SouthPacificHeight,
                                                   SouthPacificWestX, SouthPacificSouthY,
                                                   ScatterGrain, ScatterGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   5, 5,
                                                   True, 5,
                                                   -1, False,
                                                   False
                                                   )


                        self.setWorldShapeInfo(0,roll1)
                        self.setWorldShapeInfo(1,roll2)
                        self.setWorldShapeInfo(2,roll3)
                        self.setWorldShapeInfo(3,roll4)
                        self.setWorldShapeInfo(4,roll5)
                        self.setWorldShapeInfo(5,roll6)
                        self.setWorldShapeInfo(6,roll7)
                        self.setWorldShapeInfo(7,roll8)
                        self.setWorldShapeInfo(8,roll9)
                        self.setWorldShapeInfo(9,atlanticLine-0.01)


                        

                        # All regions have been processed. Plot Type generation completed.
                        return self.wholeworldPlotTypes


                    
		elif (likelihood == 1 or likelihood == 2): #high or medium
                        # Sirian's MultilayeredFractal class, controlling function.
                        # You -MUST- customize this function for each use of the class.
                        #
                        # The following grain matrix is specific to Terra.py
                        sizekey = self.map.getWorldSize()
                        sizevalues = {
                                #Rhye RFCRAND
        ##			WorldSizeTypes.WORLDSIZE_DUEL:      (3,2,1,2),
        ##			WorldSizeTypes.WORLDSIZE_TINY:      (3,2,1,2),
        ##			WorldSizeTypes.WORLDSIZE_SMALL:     (4,2,1,2),
                                WorldSizeTypes.WORLDSIZE_STANDARD:  (4,2,1,2),
                                WorldSizeTypes.WORLDSIZE_LARGE:     (4,2,1,2),
                                WorldSizeTypes.WORLDSIZE_HUGE:      (4,2,1,2)
                                }
                        (archGrain, contGrain, gaeaGrain, eurasiaGrain) = sizevalues[sizekey]

                        newworldWestLon = 0.00 #Rhye (05)
                        newworldEastLon = 0.35 #Rhye (35)
                        atlanticLine = newworldEastLon #Rhye
                        eurasiaWestLon = atlanticLine #+0.01 #43 #Rhye (45)
                        eurasiaEastLon = 1.00 #97 #Rhye (95)
                        eurasiaNorthLat = 0.99
                        eurasiaSouthLat = 0.36
                        thirdworldDimension = 0.17 #Rhye (125)
                        #thirdworldNorthLat = 0.27 #Rhye (35)
                        #thirdworldSouthLat = 0.08 #Rhye (05)
                        subcontinentLargeHorz = 0.25 #Rhye (20)
                        subcontinentLargeVert = 0.32
                        subcontinentLargeNorthLat = 0.6
                        subcontinentLargeSouthLat = 0.28
                        subcontinentSmallDimension = 0.14 #Rhye (125)
                        subcontinentSmallNorthLat = 0.525
                        subcontinentSmallSouthLat = 0.4
                        island1SouthLat = 0.61
                        island2SouthLat = 0.59
                        #islandsWidth = 0.10
                        islandsHeight = 0.28
                        islandsEurasiaFraction = 9
                        
                        iNorthAmericaTop = 0.90  #Rhye (85)
                        iNorthAmericaBottom = 0.52  
                        iArcticAmericaTop = 0.975
                        iArcticAmericaBottom = 0.82 #Rhye 0.85
                        iCaribbeanAmericaTop = 0.55
                        iCaribbeanAmericaBottom = 0.47
                        iCentralAmericaTop = 0.6
                        iCentralAmericaBottom = 0.42
                        iYukonAmericaTop = 0.97 #Rhye (93)
                        iYukonAmericaBottom = 0.73 #Rhye (75)
                        iSouthAmericaTop1 = 0.47
                        iSouthAmericaBottom1 = 0.22 #Rhye (25)
                        iSouthAmericaTop2 = 0.3
                        iSouthAmericaBottom2 = 0.10 #Rhye (18)


                                


                        
                        eurasiaStandardSouthLat = eurasiaSouthLat
                        eurasiaStandardNorthLat = eurasiaNorthLat
                        if roll5 == 1:                        
                                eurasiaSouthLat = 0.32
                                eurasiaNorthLat = 0.99
                        if roll1 == 1:
                                eurasiaNorthLat -= (eurasiaSouthLat)#-0.01)
                                eurasiaSouthLat -= (eurasiaSouthLat)#-0.01) #that is, 0.00
                                subcontinentLargeNorthLat += 0.12
                                subcontinentLargeSouthLat += 0.12
                                subcontinentSmallNorthLat += 0.075
                                subcontinentSmallSouthLat += 0.075
                                island1SouthLat = 1 - island1SouthLat - islandsHeight
                                island2SouthLat = 1 - island2SouthLat - islandsHeight
                        if roll2 == 1:
                                eurasiaWestLon -= (atlanticLine); eurasiaEastLon -= (atlanticLine)
                                atlanticLine = 1 - (atlanticLine)
                                newworldWestLon += atlanticLine; newworldEastLon += atlanticLine
                        if roll7 == 2:
                                roll6 = 0
        		if roll3 == 1:
                                temp = iNorthAmericaTop
                                iNorthAmericaTop = 1 - iNorthAmericaBottom
                                iNorthAmericaBottom = 1 - temp  
                                temp = iArcticAmericaTop
                                iArcticAmericaTop = 1 - iArcticAmericaBottom
                                iArcticAmericaBottom = 1 - temp
                                temp = iCentralAmericaTop
                                iCentralAmericaTop = 1 - iCentralAmericaBottom
                                iCentralAmericaBottom = 1 - temp
                                temp = iYukonAmericaTop
                                iYukonAmericaTop = 1 - iYukonAmericaBottom
                                iYukonAmericaBottom = 1 - temp
                                temp = iSouthAmericaTop1
                                iSouthAmericaTop1 = 1 - iSouthAmericaBottom1
                                iSouthAmericaBottom1 = 1 - temp
                                temp = iSouthAmericaTop2
                                iSouthAmericaTop2 = 1 - iSouthAmericaBottom2
                                iSouthAmericaBottom2 = 1 - temp


                                
                        print ("roll1 (Eurasia N/S)", roll1, "roll2 (E/W)", roll2, "roll3 (America N/S)", roll3, "roll4 (Central Am shape)", roll4)
                        print ("roll5 (Divided Eurasia)", roll5, "roll6 (Oceania 3rd)", roll6, "roll7 (Africa X)", roll7, "roll8 (UK/Jap)", roll8)


                    

                        # Simulate the Old World - a large continent akin to Earth's Eurasia.
                        NiTextOut("Generating the Old World (Python Terra) ...")
                        # Set dimensions of the Old World region (specific to Terra.py)
                        eurasiaWestX = int(self.iW * eurasiaWestLon)
                        eurasiaEastX = int(self.iW * eurasiaEastLon)
                        eurasiaNorthY = int(self.iH * eurasiaNorthLat)
                        eurasiaSouthY = int(self.iH * eurasiaSouthLat)
                        eurasiaWidth = eurasiaEastX - eurasiaWestX + 1
                        eurasiaHeight = eurasiaNorthY - eurasiaSouthY + 1

                        print ("eurasiaWestX", eurasiaWestX, "eurasiaEastX", eurasiaEastX, "eurasiaNorthY", eurasiaNorthY, "eurasiaSouthY", eurasiaSouthY, "eurasiaWidth", eurasiaWidth, "eurasiaHeight", eurasiaHeight)


                        eurasiaStandardWestX = eurasiaWestX #Rhye
                        eurasiaStandardEastX = eurasiaEastX #Rhye
                        eurasiaStandardWidth = eurasiaWidth #Rhye
                        eurasiaStandardNorthY = int(self.iH * eurasiaStandardNorthLat) #Rhye
                        eurasiaStandardSouthY = int(self.iH * eurasiaStandardSouthLat) #Rhye
                        eurasiaStandardHeight = eurasiaStandardNorthY - eurasiaStandardSouthY + 1 #Rhye

                        #eurasiaWater = 55+sea #Rhye
                        eurasiaWater = 55+sea #50

                        if roll8 == 2:
                                eurasiaWestX += (eurasiaStandardWidth/islandsEurasiaFraction -1)
                                eurasiaWidth -= (eurasiaStandardWidth/islandsEurasiaFraction -1)
                                print ("eurasiaWestX", eurasiaWestX, "eurasiaWidth", eurasiaWidth)
                        elif roll8 == 3:
                                eurasiaEastX -= (eurasiaStandardWidth/islandsEurasiaFraction -1)
                                eurasiaWidth -= (eurasiaStandardWidth/islandsEurasiaFraction -1)
                                print ("eurasiaEastX", eurasiaEastX, "eurasiaWidth", eurasiaWidth)
                        elif roll8 == 4:
                                eurasiaWestX += (eurasiaStandardWidth/islandsEurasiaFraction -1)
                                eurasiaEastX -= (eurasiaStandardWidth/islandsEurasiaFraction -1)
                                eurasiaWidth -= 2*(eurasiaStandardWidth/islandsEurasiaFraction -1)
                                print ("eurasiaWestX", eurasiaWestX, "eurasiaEastX", eurasiaEastX, "eurasiaWidth", eurasiaWidth)


                        #Rhye
                        self.setEurasiaInfo(0,eurasiaWestX)
                        self.setEurasiaInfo(1,eurasiaEastX)
                        self.setEurasiaInfo(2,eurasiaSouthY)
                        self.setEurasiaInfo(3,eurasiaNorthY)
                        eurasiaRift = -1 #twRift = 2
                        
                            
                        self.generatePlotsInRegionPre(eurasiaWater,
                                                   eurasiaWidth, eurasiaHeight,
                                                   eurasiaWestX, eurasiaSouthY,
                                                   eurasiaGrain, archGrain,
                                                   self.iHorzFlags, self.iTerrainFlags,
                                                   -1, -1,
                                                   True, 11,
                                                   eurasiaRift, False,
                                                   False
                                                   )


                        # Eurasia, second layer (to increase pangaea-like cohesion).
                        twHeight = eurasiaHeight/2
                        twWestX = eurasiaWestX + eurasiaWidth/islandsEurasiaFraction
                        twEastX = eurasiaEastX - eurasiaWidth/islandsEurasiaFraction
                        twWidth = twEastX - twWestX + 1
                        twNorthY = eurasiaNorthY - eurasiaHeight/4
                        twSouthY = eurasiaSouthY + eurasiaHeight/4

                        #twWater = 60+sea; twGrain = 1; twRift = 2 #Rhye
                        twWater = 65+sea; twGrain = 1; twRift = 2

                        if roll5 == 0: #Rhye
                                self.generatePlotsInRegionPre(twWater,
                                                           twWidth, twHeight,
                                                           twWestX, twSouthY,
                                                           twGrain, archGrain,
                                                           self.iHorzFlags, self.iTerrainFlags,
                                                           -1, -1,
                                                           True, 11,
                                                           twRift, False,
                                                           False
                                                           )

                        #Rhye - start (Islands like Britain (1) and Japan (2))
                        if roll8 >= 2:
                                iWidth = eurasiaStandardWidth/islandsEurasiaFraction +2
                                iHeight = int(islandsHeight * self.iH)
                                i1WestX = eurasiaStandardWestX - 1
                                i2WestX = eurasiaEastX + 1 -2
                                i1SouthY = int(self.iH * island1SouthLat)
                                i2SouthY = int(self.iH * island2SouthLat)
                                i1Water = 60+sea; i1Grain = 2; i1Rift = -1 #2
                                i2Water = 60+sea; i2Grain = 2; i2Rift = -1 #1
                                
                                self.setIsland1Info(0,i1WestX)
                                self.setIsland1Info(1,i1WestX+iWidth)
                                self.setIsland1Info(2,i1SouthY)
                                self.setIsland1Info(3,i1SouthY+iHeight)
                                self.setIsland2Info(0,i2WestX)
                                self.setIsland2Info(1,i2WestX+iWidth)
                                self.setIsland2Info(2,i2SouthY)
                                self.setIsland2Info(3,i2SouthY+iHeight)

                        if roll8 == 2 or roll8 == 4 :
                                self.generatePlotsInRegionPre(i1Water,
                                                           iWidth, iHeight,
                                                           i1WestX, i1SouthY,
                                                           i1Grain, archGrain,
                                                           self.iVertFlags, self.iTerrainFlags,
                                                           5, 5,
                                                           True, 5,
                                                           i1Rift, False,
                                                           False
                                                           )
                        if roll8 == 3 or roll8 == 4 :
                                self.generatePlotsInRegionPre(i2Water,
                                                           iWidth, iHeight,
                                                           i2WestX, i2SouthY,
                                                           i2Grain, archGrain,
                                                           self.iVertFlags, self.iTerrainFlags,
                                                           5, 5,
                                                           True, 5,
                                                           i2Rift, False,
                                                           False
                                                           )                     



                        # Simulate the New World - land masses akin to Earth's American continents.
                        # First simulate North America

                        NiTextOut("Generating the New World (Python Terra) ...")
                        nwWestX = int(self.iW * newworldWestLon)
                        nwEastX = int(self.iW * newworldEastLon)
                        nwNorthY = int(self.iH * iNorthAmericaTop)
                        nwSouthY = int(self.iH * iNorthAmericaBottom)
                        nwWidth = nwEastX - nwWestX + 1
                        nwHeight = nwNorthY - nwSouthY + 1

                        nwWater = 61+sea; nwGrain = 1; nwRift = -1
                        
                        self.generatePlotsInRegionPre(nwWater,
                                                   nwWidth, nwHeight,
                                                   nwWestX, nwSouthY,
                                                   nwGrain, archGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   6, 6,
                                                   True, 7,
                                                   nwRift, False,
                                                   False
                                                   )

                        # Now simulate South America
                        #Rhye - start
                                
                        nwsRoll = self.dice.get(2, "New World South E/W - Terra PYTHON")
                        if (CyMap().getSeaLevel() == 0):
                                nwsRoll = 0
                        nwsVar = 0.0
                        if nwsRoll == 1: nwsVar = 0.05                        
                        nwsWestX = nwWestX + int(self.iW * (0.07 - nwsVar)) # Not as wide as the north  #Rhye (0.08)
                        nwsEastX = nwEastX - int(self.iW * (0.02 + nwsVar)) #Rhye (0.03)
                        nwsNorthY = int(self.iH * iSouthAmericaTop1)
                        nwsSouthY = int(self.iH * iSouthAmericaBottom1)
                        nwsWidth = nwsEastX - nwsWestX + 1
                        nwsHeight = nwsNorthY - nwsSouthY + 1

                        nwsWater = 55+sea; nwsGrain = 1; nwsRift = -1
                        
                        self.generatePlotsInRegionPre(nwsWater,
                                                   nwsWidth, nwsHeight,
                                                   nwsWestX, nwsSouthY,
                                                   nwsGrain, archGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   6, 6,
                                                   True, 5,
                                                   nwsRift, False,
                                                   False
                                                   )

                        nwpWestX = nwWestX + int(self.iW * (0.1 - nwsVar)) # Not as wide as the north
                        nwpEastX = nwEastX - int(self.iW * (0.07 + nwsVar))
                        nwpNorthY = int(self.iH * iSouthAmericaTop2)
                        nwpSouthY = int(self.iH * iSouthAmericaBottom2)
                        nwpWidth = nwpEastX - nwpWestX + 1
                        nwpHeight = nwpNorthY - nwpSouthY + 1

                        nwpWater = 67+sea; nwpGrain = 1; nwpRift = -1
                        
                        self.generatePlotsInRegionPre(nwpWater,
                                                   nwpWidth, nwpHeight,
                                                   nwpWestX, nwpSouthY,
                                                   nwpGrain, archGrain,
                                                   self.iVertFlags, self.iTerrainFlags,
                                                   6, 5,
                                                   True, 3,
                                                   nwpRift, False,
                                                   False
                                                   )

                        #Rhye
                        self.setAmericaInfo(0,nwWestX)
                        self.setAmericaInfo(1,nwEastX)
                        if roll3 == 0:
                                self.setAmericaInfo(2,nwpSouthY)
                                self.setAmericaInfo(3,nwNorthY)
                                print ("AmericaWestX", nwWestX, "AmericaEast", nwEastX, "AmericaSouthY", nwpSouthY, "AmericaNorthY", nwNorthY)
                        if roll3 == 1:
                                self.setAmericaInfo(2,nwSouthY)
                                self.setAmericaInfo(3,nwpNorthY)
                                print ("AmericaWestX", nwSouthY, "AmericaEast", nwWestX, "AmericaSouthY", nwEastX, "AmericaNorthY", nwpNorthY)

                        # Now the Yukon

                        twWidth = int(self.iW * 0.14) #Rhye
                        twWestX = nwWestX +3 #Rhye
                        boreal = self.dice.get(2, "New World North E/W - Terra PYTHON")
                        if boreal == 1: twWestX += int(self.iW * 0.15) -3 #Rhye
                        twEastX = twWestX + twWidth
                        twNorthY = int(self.iH * iYukonAmericaTop)
                        twSouthY = int(self.iH * iYukonAmericaBottom)
                        twHeight = abs(twNorthY - twSouthY) + 1

                        twWater = 68+sea; twGrain = 2; twRift = -1
                        
                        self.generatePlotsInRegionPre(twWater,
                                                   twWidth, twHeight,
                                                   twWestX, twSouthY,
                                                   twGrain, archGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   6, 5,
                                                   True, 5,
                                                   twRift, False,
                                                   False
                                                   )
                        print ("Yukon", "twWestX", twWestX, "twSouthY", twSouthY, "twWidth", twWidth, "twHeight", twHeight, "boreal", boreal)

                        # Now add a random region of arctic islands

                        twWidth = int(0.14 * self.iW) #Rhye thirdworldDimension 0.17
                        twHeight = int(thirdworldDimension * self.iH)
                        if boreal == 0: 
                                twEastX = nwEastX
                                twWestX = twEastX - twWidth -2 #Rhye
                        else:
                                twWestX = nwWestX +2 #Rhye
                                twEastX = twWestX + twWidth
                        twNorthY = int(self.iH * iArcticAmericaTop)
                        twSouthY = int(self.iH * iArcticAmericaBottom)

                        twWater = 76+sea; twGrain = archGrain; twRift = -1
                        
                        self.generatePlotsInRegionPre(twWater,
                                                   twWidth, twHeight,
                                                   twWestX, twSouthY,
                                                   twGrain, archGrain,
                                                   self.iHorzFlags, self.iTerrainFlags,
                                                   6, 5,
                                                   True, 5,
                                                   twRift, False,
                                                   False
                                                   )
                        print ("Arctic", "twWestX", twWestX, "twSouthY", twSouthY, "twWidth", twWidth, "twHeight", twHeight)

                        # Now simulate Central America

                        nwcVar = 0.0
                        if nwsRoll == 1: nwcVar = 0.04
                        nwcWidth = int(self.iW * 0.07) #Rhye (0.06)
                        nwcRoll = self.dice.get(2, "Central America and Carribean Placement - Terra PYTHON")
                        nwcWestX = nwWestX + int(self.iW * (0.1 + nwcVar))
                        nwcEastX = nwcWestX + nwcWidth
                        nwcNorthY = int(self.iH * iCentralAmericaTop)
                        nwcSouthY = int(self.iH * iCentralAmericaBottom)
                        nwcHeight = nwcNorthY - nwcSouthY + 1

                        nwcWater = 60+sea; nwcGrain = 1; nwcRift = -1

                        if roll4 == 2: #Rhye
                                nwcWestX = nwsWestX
                                nwcEastX = nwsEastX
                                nwcWidth = nwcEastX-nwcWestX
                                #nwcWater = 60+sea
                                nwcGrain = 1
                                

                        if roll4 == 0 or roll4 == 2: #Rhye
                                self.generatePlotsInRegionPre(nwcWater,
                                                           nwcWidth, nwcHeight,
                                                           nwcWestX, nwcSouthY,
                                                           nwcGrain, archGrain,
                                                           self.iVertFlags, self.iTerrainFlags,
                                                           6, 5,
                                                           True, 5,
                                                           nwcRift, False,
                                                           False
                                                           )

                                print ("Central America", "nwcWestX", nwcWestX, "nwcSouthY", nwcSouthY, "nwcWidth", nwcWidth, "nwcHeight", nwcHeight)

                        # Now the Carribean islands

                        carVar = 0.05
                        if nwsRoll == 1: carVar = 0.18
                        twWidth = int(0.15 * self.iW)
                        twEastX = nwEastX - int(carVar * self.iW)
                        twWestX = twEastX - twWidth
                        twNorthY = int(self.iH * iCaribbeanAmericaTop)
                        twSouthY = int(self.iH * iCaribbeanAmericaBottom)
                        twHeight = twNorthY - twSouthY + 1

                        twWater = 75+sea; twGrain = archGrain + 1; twRift = -1

                        if roll4 == 1: #Rhye
                                twWestX = nwsWestX
                                twEastX = nwsEastX
                                twWidth = twEastX-twWestX
                        
                        if roll4 <= 1: #Rhye                            
                                self.generatePlotsInRegionPre(twWater,
                                                           twWidth, twHeight,
                                                           twWestX, twSouthY,
                                                           twGrain, archGrain,
                                                           0, self.iTerrainFlags,
                                                           6, 5,
                                                           True, 3,
                                                           twRift, False,
                                                           False
                                                           )
                                print ("Caribbean",  "twWestX", twWestX, "twSouthY", twSouthY, "twWidth", twWidth, "twHeight", twHeight)

                        # Add subcontinents to the Old World, one large, one small. (Terra.py)
                        # Subcontinents can be akin to pangaea, continents, or archipelago.
                        # The large adds an amount of land akin to subSaharan Africa.
                        # The small adds an amount of land akin to South Pacific islands.
                        NiTextOut("Generating the Third World (Python Terra) ...")
                        scLargeWidth = int(subcontinentLargeHorz * self.iW)
                        scLargeHeight = int(subcontinentLargeVert * self.iH)
                        scRoll = self.dice.get((eurasiaStandardWidth - scLargeWidth), "Large Subcontinent Placement - Terra PYTHON")
                        scWestX = eurasiaStandardWestX + scRoll
                        scEastX = scWestX + scLargeWidth
                        scNorthY = int(self.iH * subcontinentLargeNorthLat)
                        scSouthY = int(self.iH * subcontinentLargeSouthLat)

                        scShape = self.dice.get(4, "Large Subcontinent Shape - Terra PYTHON")
                        if scShape > 1: # Massive subcontinent! (Africa style)
                                scWater = 55+sea; scGrain = 1; scRift = 2
                        elif scShape == 1: # Standard subcontinent.
                                scWater = 66+sea; scGrain = 2; scRift = 2
                        else: # scShape == 0, Archipelago subcontinent.
                                scWater = 77+sea; scGrain = archGrain; scRift = -1
                        
                        self.generatePlotsInRegionPre(scWater,
                                                   scLargeWidth, scLargeHeight,
                                                   scWestX, scSouthY,
                                                   scGrain, archGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   6, 6,
                                                   True, 7,
                                                   scRift, False,
                                                   False
                                                   )

                        scSmallWidth = int(subcontinentSmallDimension * self.iW)
                        scSmallHeight = int(subcontinentSmallDimension * self.iH)
                        endless = 1
                        while endless == 1: # Prevent excessive overlap of the two subcontinents.
                                scsRoll = self.dice.get((eurasiaStandardWidth - scSmallWidth), "Small Subcontinent Placement - Terra PYTHON")
                                scsWestX = eurasiaStandardWestX + scsRoll
                                if abs((scsWestX + self.iW/12) - scWestX) > self.iW/8: break
                        scsEastX = scsWestX + scSmallWidth
                        scsNorthY = int(self.iH * subcontinentSmallNorthLat)
                        scsSouthY = int(self.iH * subcontinentSmallSouthLat)

                        scsShape = self.dice.get(4, "Small Subcontinent Shape - Terra PYTHON")
                        if scsShape == 2: # Massive subcontinent!
                                scsWater = 55+sea; scsGrain = 1; scsRift = 2
                        elif scsShape == 1: # Standard subcontinent. (India style).
                                scsWater = 66+sea; scsGrain = 2; scsRift = 2
                        else: # scsShape == 0 or 3, Archipelago subcontinent (East Indies style).
                                scsWater = 77+sea; scsGrain = archGrain; scsRift = -1
                        
                        self.generatePlotsInRegionPre(scsWater,
                                                   scSmallWidth, scSmallHeight,
                                                   scsWestX, scsSouthY,
                                                   scsGrain, archGrain,
                                                   self.iHorzFlags, self.iTerrainFlags,
                                                   6, 5,
                                                   True, 5,
                                                   scsRift, False,
                                                   False
                                                   )



                        #Rhye - start
                        #Africa
                        aHeight = eurasiaStandardHeight*78/100
                        aWestX = eurasiaStandardWestX - eurasiaStandardWidth/16 #+ eurasiaStandardWidth/25
                        aEastX = eurasiaStandardEastX + eurasiaStandardWidth/16 #- eurasiaStandardWidth/25
                        aWidth = (aEastX - aWestX) / 2

                        if roll7 >= 3:
                                aWestX += aWidth #right
                        elif roll7 == 2:
                                aWestX += aWidth/2 #central

                        aSouthY = 0
                        if roll1 == 0: 
                                aSouthY = eurasiaSouthY - aHeight + aHeight*25/100 #positive for attached, negative for detached from eurasia
                        else:
                                aSouthY = eurasiaNorthY - aHeight*30/100  #negative for attached, positive for detached from eurasia

                        aSouthY = max(5, min(self.iH-5, aSouthY))

                        aWater = 55+sea; aGrain = 1; twRift = -1 #twRift = 2
                        
                        self.generatePlotsInRegionPre(aWater,
                                                   aWidth, aHeight,
                                                   aWestX, aSouthY,
                                                   aGrain, archGrain,
                                                   self.iRoundFlags, self.iTerrainFlags,
                                                   6, 6,
                                                   True, 11,
                                                   twRift, False,
                                                   False
                                                   )

                        self.setAfricaInfo(0,aWestX)
                        self.setAfricaInfo(1,aWestX+aWidth)
                        self.setAfricaInfo(2,aSouthY)
                        self.setAfricaInfo(3,aSouthY+aHeight)
                        print ("afWestX", aWestX, "afSouthY", aSouthY, "afWidth", aWidth, "afHeight", aHeight)
                        

                        # Now simulate random lands akin to Australia and Antarctica
                        #extras = 2 + self.dice.get(3, "Number of Minor Regions - Terra PYTHON") # Two to four of these regions.
                        twNumber = 2
                        for loop in range(twNumber):

                                #roll7 >= 3: #oceania at left, africa at right
                                distFromPole = eurasiaStandardWidth*8/100
                                twWestX = eurasiaStandardWestX #-eurasiaStandardWidth*5/100
                                twWidth = eurasiaStandardWidth*45/100
                                
                                iCohesion = 13
                                iAdditionalThickness = 24
                                if roll1 == 0:
                                        twHeight = (min(eurasiaStandardHeight*87/100, eurasiaSouthY) / twNumber) + iAdditionalThickness*eurasiaStandardHeight/100 - distFromPole/2
                                        twSouthY = eurasiaSouthY - twHeight*twNumber + twHeight*loop +(iCohesion/3) + (iCohesion+2+self.map.getWorldSize())*self.dice.get(loop, "further coesion of Australia") + distFromPole
                                        if roll5 == 0: #undivided eurasia
                                                twSouthY -= eurasiaStandardHeight/12
                                        else: #divided
                                                twSouthY += eurasiaStandardHeight/20
                                else:
                                        twHeight = (min(eurasiaStandardHeight*87/100, self.iH-eurasiaNorthY) / twNumber) + iAdditionalThickness*eurasiaStandardHeight/100 - distFromPole/2
                                        twSouthY = eurasiaNorthY + twHeight*loop -(iCohesion/3) - (iCohesion+2+self.map.getWorldSize())*self.dice.get(loop, "further coesion of Australia")
                                        if (loop > 0):
                                                twSouthY -= eurasiaStandardHeight/20+self.dice.get(eurasiaStandardHeight/10, "further coesion of Australia") #further coesion of Australia when it's up north
                                        if roll5 == 0: #undivided eurasia
                                                twSouthY += eurasiaStandardHeight/12
                                        else: #divided
                                                twSouthY -= eurasiaStandardHeight/20


                                                
                                if roll7 == 2: #central Africa
                                        twWestX = eurasiaStandardWestX
                                        twWidth = eurasiaStandardWidth/2
                                        if loop == 1:
                                                twWestX = eurasiaStandardWestX + eurasiaStandardWidth*3/4
                                        #twSouthY = twSouthY - twHeight*loop
                                        if roll1 == 0:
                                                twSouthY = eurasiaSouthY - twHeight*twNumber +iCohesion
                                        else:
                                                twSouthY = eurasiaNorthY -iCohesion
                                        twHeight = twHeight*twNumber                                
                                elif roll7 <= 1: #africa at left, oceania at right
                                        twWestX = eurasiaStandardWestX + eurasiaStandardWidth/2 +eurasiaStandardWidth*7/100


                                twWidth -= twWidth/10
                                twHeight -= twWidth/10         
                                    
                                twXRoll = self.dice.get(eurasiaStandardWidth/12, "Minor Region Placement")
                                twWRoll = self.dice.get(eurasiaStandardWidth/12, "Minor Region Placement")
                                twSRoll = self.dice.get(twHeight/6, "Minor Region Placement")
                                twHRoll = self.dice.get(twHeight/6, "Minor Region Placement")
                                
                                twWestX = twWestX - eurasiaStandardWidth/24 + twXRoll                   
                                twWidth = twWidth - eurasiaStandardWidth/24 + twWRoll
                                twSouthY = twSouthY - twHeight/12 + twSRoll                        
                                twHeight += twHRoll



                                twShape = self.dice.get(3, "Minor Region Shape - Terra PYTHON")

                                if (likelihood == 0): #high
                                        if loop == 0:
                                                twShape = 2
                                        if loop == 1:
                                                twShape = 0
                        
                                        
                                if twShape == 2: # Massive subcontinent!
                                        twWater = 60+sea; twGrain = 1; twRift = -1 #twrift = 2
                                elif twShape == 1: # Standard subcontinent.
                                        twWater = 68+sea; twGrain = 2; twRift = -1 #twrift = 2       #68
                                else: # twShape == 0, Archipelago subcontinent. #Rhye
                                        twWater = 74+sea; twGrain = 3; twRift = -1 #Rhye    #76, archGrain
                        
                                self.generatePlotsInRegionPre(twWater,
                                                           twWidth, twHeight,
                                                           twWestX, twSouthY,
                                                           twGrain, archGrain,
                                                           self.iHorzFlags, self.iTerrainFlags,
                                                           6, 5,
                                                           True, 5,
                                                           twRift, False,
                                                           False
                                                           )
                                print ("Oceania", loop, "twWestX", twWestX, "twSouthY", twSouthY, "twWidth", twWidth, "twHeight", twHeight, "twShape", twShape)


                        self.setWorldShapeInfo(0,roll1)
                        self.setWorldShapeInfo(1,roll2)
                        self.setWorldShapeInfo(2,roll3)
                        self.setWorldShapeInfo(3,roll4)
                        self.setWorldShapeInfo(4,roll5)
                        self.setWorldShapeInfo(5,roll6)
                        self.setWorldShapeInfo(6,roll7)
                        self.setWorldShapeInfo(7,roll8)
                        self.setWorldShapeInfo(8,roll9)
                        self.setWorldShapeInfo(9,atlanticLine-0.01)

                        # All regions have been processed. Plot Type generation completed.
                        return self.wholeworldPlotTypes
                                
                elif (likelihood >= 3):  #low

                        sizekey = self.map.getWorldSize()
                        sizevalues = {
                                #Rhye RFCRAND
        ##			WorldSizeTypes.WORLDSIZE_DUEL:      (3,2,1,2),
        ##			WorldSizeTypes.WORLDSIZE_TINY:      (3,2,1,2),
        ##			WorldSizeTypes.WORLDSIZE_SMALL:     (4,2,1,2),
                                WorldSizeTypes.WORLDSIZE_STANDARD:  (4,2,1,2),
                                WorldSizeTypes.WORLDSIZE_LARGE:     (4,2,1,2),
                                WorldSizeTypes.WORLDSIZE_HUGE:      (4,2,1,2)
                                }
                        (archGrain, contGrain, gaeaGrain, eurasiaGrain) = sizevalues[sizekey]

                    
                        numContinentsX = 3
                        numContinentsY = 2
                        numLinks = 3
                        bArchipelagoWorld = 0
                        bInnerSea = 0
                        bForceContinents = 0
                        if (likelihood == 4): #very low
                                if (self.dice.get(16, "") == 0): #6.25% of inner sea
                                        bInnerSea = 1
                                if (self.dice.get(25, "") == 0): #4% of forcing continents, materially using "low"
                                        bForceContinents = 1
                                        bInnerSea = 0

                        skipContinent = -1
                        skipOdds = 12  #8% of skipping 1 out of 6 and adding 2 central regions (creates panagea in very low)
                        repeatContinent = -1
                        repeatOdds = 6 #15%
                        if (likelihood == 4 and bForceContinents == 0): #very low
                                skipOdds = 6 #15%
                                repeatOdds = 4 #25%

                                    
                        if (likelihood == 4 and bForceContinents == 0): #very low
                                numLinks = 2+self.dice.get(3, "")
                                if (self.dice.get(10, "") == 0): #10% of archipelago
                                        bArchipelagoWorld = 1
                                        numLinks = numLinks + 2

                        maxVariationPos = 5
                        if (likelihood == 4 and bForceContinents == 0): #very low
                                maxVariationPos = 9

                            
                        if (bInnerSea == 0):

                                if (self.dice.get(skipOdds, "") >= 0): 
                                        skipContinent = self.dice.get(numContinentsX*numContinentsY, "")
                                        if (utils.getWrap(1) == False):  #only with icy north
                                                if (skipContinent%2 == 1): #1 continent missing in the upper side
                                                        roll1 = 1 #better have jungles over there, with less land
                                                else: #lower side
                                                        roll1 = 0
                                        
                                if (self.dice.get(repeatOdds, "") == 0): 
                                        repeatContinent = self.dice.get(numContinentsX*numContinentsY, "")

                                
            
                                                
                                numBorders = 7

                                bordersList = [0, 1, 2, 3, 4, 5, 6]
                                #   1   3
                                # 4   5   6
                                #   0   2

                                #initialise coordinates
                                bordersListCoordinates = [[-1, -1, -1, -1], 
                                                          [-1, -1, -1, -1],
                                                          [-1, -1, -1, -1],
                                                          [-1, -1, -1, -1],
                                                          [-1, -1, -1, -1],
                                                          [-1, -1, -1, -1],
                                                          [-1, -1, -1, -1]]

                                
                                linksList = []
                                for i in range(numLinks): #repeat numLinks times
                                        iLink = self.dice.get(numBorders, "")
                                        while(iLink in linksList):
                                                iLink = self.dice.get(numBorders, "")
                                        linksList.append(iLink)


                                ##help unlikely combinations to be picked more often
                                odds = self.dice.get(100, "")
                                if (odds <= 10):
                                        linksList = [4, 5, 6]
                                elif (odds > 10 and odds <= 15):
                                        linksList = [0, 1, 6]
                                elif (odds > 15 and odds <= 20):
                                        linksList = [2, 3, 4]
                                elif (odds > 20 and odds <= 24):
                                        linksList = [1, 5, 2]
                                elif (odds > 24 and odds <= 28):
                                        linksList = [3, 5, 0]
                                
                                print("linksList", linksList)

                                continentLinks = [[0, 2],
                                                  [1, 3],
                                                  [2, 4],
                                                  [3, 5],
                                                  [0, 1],
                                                  [2, 3],
                                                  [4, 5]]
                                # continents:
                                # 1 3 5
                                # 0 2 4

        ##                        for i in range(7):
        ##                                if (i in linksList):
        ##                                        for j in range(len(continentLinks[i])):
        ##                                                self.setRandomContinents(continentLinks[i][j],0) #the rest is new world
                                                        
                                lOldWorldContinents = []   
                                for iContinent in range(6):
                                        lAdjacent = []
                                        for i in range(7):
                                                if (i in linksList):
                                                        for j in range(len(continentLinks[i])):
                                                                if (iContinent == continentLinks[i][j]):
                                                                        lAdjacent.append(continentLinks[i][(j+1)%len(continentLinks[i])])
                                        if (len(lAdjacent) >= 2):
                                                if (iContinent not in lOldWorldContinents):
                                                        lOldWorldContinents.append(iContinent)
                                                for k in lAdjacent:
                                                        if (k not in lOldWorldContinents):
                                                                lOldWorldContinents.append(k)

                                if (len(lOldWorldContinents) == 3): #with 3 continents already, a single one is enough
                                        for iContinent in range(6):
                                                iCounter = 0
                                                for i in range(7):
                                                        if (i in linksList):
                                                                for j in range(len(continentLinks[i])):
                                                                        if (iContinent == continentLinks[i][j]):
                                                                                iCounter = iCounter + 1
                                                if (iCounter == 0):
                                                        if (iContinent not in lOldWorldContinents):
                                                                lOldWorldContinents.append(iContinent)

                                                                
                                iAdjacentContinent = -1        
                                if (len(lOldWorldContinents) == 0): #they must be divided in 2/2/2
                                        iRandomContinent = self.dice.get(6, "Pick one random continent for the new world")
                                        for i in range(7):
                                                if (i in linksList):
                                                        for j in range(len(continentLinks[i])):
                                                                if (iRandomContinent == continentLinks[i][j]):
                                                                        iAdjacentContinent = continentLinks[i][(j+1)%len(continentLinks[i])]
                                                                        break
                                                                        break
                                        
                                        for iContinent in range(6):
                                                if (iContinent != iRandomContinent and iContinent != iAdjacentContinent): #both are new world
                                                        if (iContinent not in lOldWorldContinents):
                                                                lOldWorldContinents.append(iContinent)

                                print("Old World:", lOldWorldContinents)
                                
                                for iContinent in lOldWorldContinents:
                                        self.setRandomContinents(iContinent,0)
                                        

                                                      
                                continentWidth = int(self.iW/numContinentsX)                        
                                continentHeight = int(self.iH/numContinentsY)



                                #archGrain is 4
                                
                                for i in range(numContinentsX):
                                        variationPosX = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2
                                        continentWestX = 0 + i*continentWidth + continentWidth*variationPosX/10 #-20% to +20%
                                        for j in range(numContinentsY):
                                                if (skipContinent == i*numContinentsY+j):
                                                        print("skipping continent n.",skipContinent)
                                                        continue
                                                if (likelihood == 4 and bForceContinents == 0): #very low
                                                        variationWidth = self.dice.get(continentWidth/4, "variation")
                                                        variationHeight = self.dice.get(continentHeight/4, "variation")
                                                        continentWidth = continentWidth - continentWidth/8 + variationWidth 
                                                        continentHeight = continentHeight - continentHeight/8 + variationHeight 
                                        
                                                variationPosY = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2
                                                continentSouthY = 0 + j*continentHeight + continentHeight*variationPosY/10 #-20% to +20%

                                                continentGrain = self.dice.get(4, "Continent Grain") + 1 #1, 2, 3 or 4
                                                if (continentGrain >= 3):
                                                        continentGrain = self.dice.get(4, "Continent Grain") + 1 #roll again 1-4: 37.5, 37.5, 12.5, 12.5 odds
                                                if (continentGrain >= 3):
                                                        continentGrain = self.dice.get(4, "Continent Grain") + 1 #roll again 1-4: 43.75, 43.75, 6.25, 6.25 odds
                                                if (continentGrain == 3):
                                                        if (self.dice.get(100, "% Grain") > 50):
                                                                continentGrain = 1 # 46.875, 43.75, 6.25, 3.125 odds
                                                continentWater = 57 + self.dice.get(9, "Continent Water") + sea + continentGrain #(with little isles, it's better with more water)                                        print("continent", continentWater, continentGrain)
                                                    
                                                variationX = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2
                                                variationY = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2

                                                continentHeight2 = continentHeight
                                                continentSouthY2 = continentSouthY
                                                if (j == 0): #lower
                                                        continentHeight2 = continentHeight + self.iH/30
                                                else:
                                                        continentSouthY2 = continentSouthY + self.iH/30
                                                continentWidth2 = continentWidth - self.iW/50


                                                if (bArchipelagoWorld):
                                                        continentGrain = 4
                                                        continentWater = 75
                                                


                                                self.generatePlotsInRegionPre(continentWater,
                                                           continentWidth2 + continentWidth/8 + continentWidth*variationX/12, continentHeight2 + continentHeight/8 + continentHeight*variationY/12, #-16% to +16%
                                                           continentWestX - continentWidth/16, continentSouthY2 - continentHeight/24,
                                                           continentGrain, archGrain,
                                                           self.iRoundFlags, self.iTerrainFlags,
                                                           -1, -1,
                                                           True, 11,
                                                           -1, False,
                                                           False
                                                           )

                                                
                                                
                                                if (repeatContinent == i*numContinentsY+j and not bArchipelagoWorld):
                                                        #repeat
                                                        print("generating twice continent",i*numContinentsY+j)
                                                        self.generatePlotsInRegionPre(continentWater,
                                                                   continentWidth2 + continentWidth/13 + continentWidth*variationX/12, continentHeight2 + continentHeight/13 + continentHeight*variationY/12, #-16% to +16%
                                                                   continentWestX - continentWidth/26, continentSouthY2 - continentHeight/26,
                                                                   continentGrain, archGrain,
                                                                   self.iRoundFlags, self.iTerrainFlags,
                                                                   -1, -1,
                                                                   True, 11,
                                                                   -1, False,
                                                                   False
                                                                   )


                                                    

                                if (skipContinent != -1):

                                        centralContinentWidth = self.iW/5
                                        centralContinentHeight = self.iH/3
                                
                                        self.generatePlotsInRegionPre(continentWater,
                                                    centralContinentWidth + centralContinentWidth/8, centralContinentHeight + centralContinentHeight/8,
                                                    self.iW/5 - centralContinentWidth/16, self.iH/3 - centralContinentHeight/16,
                                                    continentGrain, archGrain,
                                                    self.iRoundFlags, self.iTerrainFlags,
                                                    -1, -1,
                                                    True, 11,
                                                    -1, False,
                                                    False
                                                    )
                                        self.generatePlotsInRegionPre(continentWater,
                                                    centralContinentWidth + centralContinentWidth/8, centralContinentHeight + centralContinentHeight/8,
                                                    self.iW*3/5 - centralContinentWidth/16, self.iH/3 - centralContinentHeight/16,
                                                    continentGrain, archGrain,
                                                    self.iRoundFlags, self.iTerrainFlags,
                                                    -1, -1,
                                                    True, 11,
                                                    -1, False,
                                                    False
                                                    )


                                    

                                
                                additionalLayer = self.dice.get(9, "additionalLayer")
                                layerCounter = 0   

                                borderCounter = 0         
                                for i in range(numContinentsX-1):                                
                                        variation = self.dice.get(5, "variation") +6
                                        subContinentWidth = continentWidth*variation/10
                                        subContinentWestX = 0 + i*continentWidth + subContinentWidth/2
                                        
                                        for j in range(numContinentsY):

                                                bordersListCoordinates[borderCounter][0] = 0 + (i+1)*continentWidth
                                                bordersListCoordinates[borderCounter][1] = 0 + (i+1)*continentWidth
                                                bordersListCoordinates[borderCounter][2] = 0 + j*continentHeight
                                                bordersListCoordinates[borderCounter][3] = 0 + (j+1)*continentHeight

                                                maxVariationPos = 5
                                                if (likelihood == 4 and bForceContinents == 0): #very low
                                                        maxVariationPos = 10
                                                
                                                variation = self.dice.get(4, "variation") +3
                                                variationPos = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2

                                                subContinentSouthY = 0 + j*continentHeight +continentHeight/(2*variation) +continentHeight*variationPos*2/10
                                                subContinentHeight = continentHeight -continentHeight/variation

                                                subContinentGrain = self.dice.get(3, "Continent Grain") + 2 #2, 3 or 4
                                                subContinentWater = 63 + self.dice.get(10, "Continent Water") + sea + continentGrain #(with little isles, it's better with more water)
                                                
                                                if (bArchipelagoWorld):
                                                        subcontinentGrain = 4
                                                        subcontinentWater = 75


                                                if (borderCounter in linksList):
                                                        self.generatePlotsInRegionPre(subContinentWater,
                                                                   subContinentWidth + subContinentWidth/12, subContinentHeight + subContinentHeight/12,
                                                                   subContinentWestX, subContinentSouthY,
                                                                   subContinentGrain, archGrain,
                                                                   self.iRoundFlags, self.iTerrainFlags,
                                                                   -1, -1,
                                                                   True, 11,
                                                                   -1, False,
                                                                   False
                                                                   )
                                                        
                                                        if (layerCounter == additionalLayer):
                                                                print("additionalLayer", additionalLayer)
                                                                self.generatePlotsInRegionPre(subContinentWater,
                                                                           subContinentWidth, subContinentHeight,
                                                                           subContinentWestX, subContinentSouthY,
                                                                           subContinentGrain, archGrain,
                                                                           self.iRoundFlags, self.iTerrainFlags,
                                                                           -1, -1,
                                                                           True, 11,
                                                                           -1, False,
                                                                           False
                                                                           )
                                                        layerCounter = layerCounter + 1
                                                                
                                                borderCounter = borderCounter + 1



                                                
                                for i in range(numContinentsX):                                
                                        variation = self.dice.get(4, "variation") +3
                                        variationPos = self.dice.get(5, "variation") -2
                                        
                                        subContinentWestX = 0 + i*continentWidth +continentWidth/(2*variation) +continentWidth*variationPos*2/10
                                        subContinentWidth = continentWidth -continentWidth/variation
                                        
                                        for j in range(numContinentsY-1):

                                                bordersListCoordinates[borderCounter][0] = 0 + i*continentWidth
                                                bordersListCoordinates[borderCounter][1] = 0 + (i+1)*continentWidth
                                                bordersListCoordinates[borderCounter][2] = 0 + (j+1)*continentHeight
                                                bordersListCoordinates[borderCounter][3] = 0 + (j+1)*continentHeight
                                                
                                                variation = self.dice.get(5, "variation") +6
                                                subContinentHeight = continentHeight*variation/10
                                                subContinentSouthY = 0 + j*continentHeight + subContinentHeight/2                                        

                                                subContinentWater = 63 + self.dice.get(10, "Continent Water") + sea
                                                subContinentGrain = self.dice.get(3, "Continent Grain") + 2 #2, 3 or 4

                                                if (bArchipelagoWorld):
                                                        subcontinentGrain = 4
                                                        subcontinentWater = 75

                                                if (borderCounter in linksList):
                                                        self.generatePlotsInRegionPre(subContinentWater,
                                                                   subContinentWidth + subContinentWidth/12, subContinentHeight + subContinentHeight/12,
                                                                   subContinentWestX, subContinentSouthY,
                                                                   subContinentGrain, archGrain,
                                                                   self.iRoundFlags, self.iTerrainFlags,
                                                                   -1, -1,
                                                                   True, 11,
                                                                   -1, False,
                                                                   False
                                                                   )

                                                        if (layerCounter == additionalLayer and not bArchipelagoWorld):
                                                                print("additionalLayer", additionalLayer)
                                                                self.generatePlotsInRegionPre(subContinentWater,
                                                                           subContinentWidth, subContinentHeight,
                                                                           subContinentWestX, subContinentSouthY,
                                                                           subContinentGrain, archGrain,
                                                                           self.iRoundFlags, self.iTerrainFlags,
                                                                           -1, -1,
                                                                           True, 11,
                                                                           -1, False,
                                                                           False
                                                                           )
                                                        layerCounter = layerCounter + 1

                                                borderCounter = borderCounter + 1




                                                        
                        
                                for iBorder in range(numBorders):
                                        if (iBorder not in linksList):
                                                self.setBordersCoordinates(iBorder, 0, bordersListCoordinates[iBorder][0])
                                                self.setBordersCoordinates(iBorder, 1, bordersListCoordinates[iBorder][1])
                                                self.setBordersCoordinates(iBorder, 2, bordersListCoordinates[iBorder][2])
                                                self.setBordersCoordinates(iBorder, 3, bordersListCoordinates[iBorder][3])


                        else: #inner sea
                                numContinentsX = 9
                                numContinentsY = numContinentsX
                                continentWidth = int(self.iW/numContinentsX)                     
                                continentHeight = int(self.iH/numContinentsY)

                                if (self.dice.get(skipOdds, "") >= 0): 
                                        skipContinent = self.dice.get(numContinentsX*numContinentsY, "")

                                innerContinentShapeRoll = self.dice.get(3, "")
                                print("innerContinentShapeRoll",innerContinentShapeRoll)

                                #pick areas in the 7x7 box
                                parameter1 = 7
                                parameter2 = 1
                                parameter3 = 0
                                if (innerContinentShapeRoll == 1):
                                        #pick areas in the 3x3 box
                                        parameter1 = 3
                                        parameter2 = 3
                                        parameter3 = 0
                                elif (innerContinentShapeRoll == 2):
                                        #pick areas in the 2 plots ring
                                        parameter1 = 2
                                        parameter2 = 4
                                        parameter3 = 2
    
                                

                                iRandomInnerContinent1X = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "left or right")*2-1)
                                iRandomInnerContinent1Y = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "up or down")*2-1)
                                iRandomInnerContinent2X = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "left or right")*2-1)
                                iRandomInnerContinent2Y = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "up or down")*2-1)
                                iRandomInnerContinent3X = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "left or right")*2-1)
                                iRandomInnerContinent3Y = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "up or down")*2-1)
                                iRandomInnerContinent4X = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "left or right")*2-1)
                                iRandomInnerContinent4Y = self.dice.get(parameter1, "") + parameter2+ parameter3*(self.dice.get(2, "up or down")*2-1)

                                print("random inner", iRandomInnerContinent1X ,iRandomInnerContinent1Y,iRandomInnerContinent2X ,iRandomInnerContinent2Y,iRandomInnerContinent3X ,iRandomInnerContinent3Y)

                                #near 0
                                if utils.getWrap(0) == 1:
                                        self.generatePlotsInRegionPre(20, 
                                                            continentWidth/2, self.iH,
                                                            0, 0,
                                                            1, archGrain,
                                                            self.iHorzFlags, self.iTerrainFlags,
                                                            -1, -1,
                                                            True, 11,
                                                            -1, False,
                                                            False
                                                            )
                                        self.generatePlotsInRegionPre(20, 
                                                            continentWidth/2, self.iH,
                                                            self.iW-continentWidth/2, 0,
                                                            1, archGrain,
                                                            self.iHorzFlags, self.iTerrainFlags,
                                                            -1, -1,
                                                            True, 11,
                                                            -1, False,
                                                            False
                                                            )
                                if self.getWrap(1) == 1:
                                        self.generatePlotsInRegionPre(10, 
                                                            self.iW, continentHeight*2/3,
                                                            0, 0,
                                                            1, archGrain,
                                                            0, self.iTerrainFlags,
                                                            -1, -1,
                                                            True, 11,
                                                            -1, False,
                                                            False
                                                            )
                                        self.generatePlotsInRegionPre(10, 
                                                            self.iW, continentHeight*2/3,
                                                            0, self.iH-continentHeight*2/3,
                                                            1, archGrain,
                                                            0, self.iTerrainFlags,
                                                            -1, -1,
                                                            True, 11,
                                                            -1, False,
                                                            False
                                                            )
                                
                                for i in range(numContinentsX):
                                        variationPosX = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2
                                        continentWestX = 0 + i*continentWidth + continentWidth*variationPosX/10 #-20% to +20%
                                        for j in range(numContinentsY):

                                                bRandomInnerContinent = False

                                                if (iRandomInnerContinent1X*numContinentsY+iRandomInnerContinent1Y == i*numContinentsY+j):
                                                        bRandomInnerContinent = True
                                                elif (iRandomInnerContinent2X*numContinentsY+iRandomInnerContinent2Y == i*numContinentsY+j):
                                                        bRandomInnerContinent = True
                                                elif (iRandomInnerContinent3X*numContinentsY+iRandomInnerContinent3Y == i*numContinentsY+j):
                                                        bRandomInnerContinent = True
                                                elif (iRandomInnerContinent4X*numContinentsY+iRandomInnerContinent4Y == i*numContinentsY+j):
                                                        bRandomInnerContinent = True

                                                if (bRandomInnerContinent == False and i != 0 and i!= numContinentsX-1 and j != 0 and j!= numContinentsY-1): #only borders allowed
                                                        continue
                                                    
                                                if (skipContinent == i*numContinentsY+j):
                                                        print("skipping continent n.",skipContinent)
                                                        continue

                                                
                                                variationPosY = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2
                                                continentSouthY = 0 + j*continentHeight + continentHeight*variationPosY/10 #-20% to +20%

                                                #print("square", i, j, continentWestX, continentSouthY)
                                                
                                                continentGrain = self.dice.get(4, "Continent Grain") + 1 #1, 2, 3 or 4
                                                if (continentGrain >= 3):
                                                        continentGrain = self.dice.get(4, "Continent Grain") + 1 #roll again 1-4: 37.5, 37.5, 12.5, 12.5 odds
                                                if (continentGrain >= 3):
                                                        continentGrain = self.dice.get(4, "Continent Grain") + 1 #roll again 1-4: 43.75, 43.75, 6.25, 6.25 odds
                                                if (continentGrain == 3):
                                                        if (self.dice.get(100, "% Grain") > 50):
                                                                continentGrain = 1 # 46.875, 43.75, 6.25, 3.125 odds
                                                continentWater = 68 + self.dice.get(9, "Continent Water") + sea + continentGrain #(with little isles, it's better with more water)                                        print("continent", continentWater, continentGrain)
                                                    
                                                variationX = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2
                                                variationY = self.dice.get(maxVariationPos, "variation") -maxVariationPos/2


                                                continentWidth2 = continentWidth
                                                continentWestX2 = continentWestX
                                                continentHeight2 = continentHeight
                                                continentSouthY2 = continentSouthY
                                                if (i == 0):
                                                        continentWidth2 = continentWidth - continentWidth/6
                                                if (i == numContinentsX-1):
                                                        continentWestX2 = continentWestX + continentWidth/6
                                                if (j == 0):
                                                        continentHeight2 = continentHeight - continentHeight/6
                                                if (j == numContinentsY-1):
                                                        continentSouthY2 = continentSouthY + continentHeight/6




                                                if (bArchipelagoWorld):
                                                        continentGrain = 4
                                                        continentWater = 78
                                                


                                                self.generatePlotsInRegionPre(continentWater,
                                                           (continentWidth2 + continentWidth/8 + continentWidth*variationX/12)*2, (continentHeight2 + continentHeight/8 + continentHeight*variationY/12)*2, #-16% to +16%
                                                           continentWestX2 -continentWidth/2 - continentWidth2/16, continentSouthY2 -continentHeight/2 - continentHeight/24,
                                                           continentGrain, archGrain,
                                                           self.iHorzFlags, self.iTerrainFlags,
                                                           -1, -1,
                                                           True, 11,
                                                           -1, False,
                                                           False
                                                           )
                                                self.generatePlotsInRegionPre(continentWater,
                                                           (continentWidth2 + continentWidth/8 + continentWidth*variationX/12)*2, (continentHeight2 + continentHeight/8 + continentHeight*variationY/12)*2, #-16% to +16%
                                                           continentWestX2 -continentWidth/2 - continentWidth2/16, continentSouthY2 -continentHeight/2 - continentHeight/24,
                                                           continentGrain, archGrain,
                                                           self.iHorzFlags, self.iTerrainFlags,
                                                           -1, -1,
                                                           True, 11,
                                                           -1, False,
                                                           False
                                                           )
                                                
##                        for iLoopX in range(40,CyMap().getGridWidth()):
##                                for iLoopY in range(30,CyMap().getGridHeight()):
##                                        pCurrent = CyMap().plot( iLoopX, iLoopY )
##                                        print(iLoopX,iLoopY,"scorrendo")
##                                        #if (pCurrent.isWater()):
##                                        if (pCurrent.getPlotType() == PlotTypes.PLOT_OCEAN):
##                                                print(iLoopX,iLoopY,"acqua")
##                                                pCurrent.setPlotType(PlotTypes.PLOT_PEAK, True, True)
                        


                                        
                        self.setWorldShapeInfo(0,roll1)
                        self.setWorldShapeInfo(1,roll2)
                        self.setWorldShapeInfo(2,roll3)
                        self.setWorldShapeInfo(3,roll4)
                        self.setWorldShapeInfo(4,roll5)
                        self.setWorldShapeInfo(5,roll6)
                        self.setWorldShapeInfo(6,roll7)
                        self.setWorldShapeInfo(7,roll8)
                        self.setWorldShapeInfo(8,roll9)
                        #self.setWorldShapeInfo(9,atlanticLine-0.01)
                        self.setWorldShapeInfo(10,bInnerSea)
                        self.setWorldShapeInfo(11,bForceContinents)
                        
                        # All regions have been processed. Plot Type generation completed.
                        return self.wholeworldPlotTypes




        #Rhye - start
        def generatePlotsInRegionPre(self, iWaterPercent, 
                                          iRegionWidth, iRegionHeight, 
                                          iRegionWestX, iRegionSouthY, 
                                          iRegionGrain, iRegionHillsGrain, 
                                          iRegionPlotFlags, iRegionTerrainFlags, 
                                          iRegionFracXExp, iRegionFracYExp, 
                                          bShift, iStrip, 
                                          rift_grain, has_center_rift, 
                                          invert_heights):
                if (iRegionWestX < 0):
                       iRegionWestX = 0
                if (iRegionSouthY < 0):
                       iRegionSouthY = 0
                if (iRegionWestX + iRegionWidth >= self.iW):
                       iRegionWidth = self.iW - iRegionWestX
                if (iRegionSouthY + iRegionHeight >= self.iH):
                       iRegionHeight = self.iH - iRegionSouthY
                       
                self.generatePlotsInRegion(iWaterPercent, 
                                          iRegionWidth, iRegionHeight, 
                                          iRegionWestX, iRegionSouthY, 
                                          iRegionGrain, iRegionHillsGrain, 
                                          iRegionPlotFlags, iRegionTerrainFlags, 
                                          iRegionFracXExp, iRegionFracYExp, 
                                          bShift, iStrip, 
                                          rift_grain, has_center_rift, 
                                          invert_heights)


        #Rhye - end


        def getWorldShapeInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lWorldShapeInfo'][iParameter]

        def setWorldShapeInfo( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lWorldShapeInfo'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getWrap( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lWrap'][iParameter]

        def setWrap( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lWrap'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getEurasiaInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lEurasiaInfo'][iParameter]

        def setEurasiaInfo( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lEurasiaInfo'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getAfricaInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lAfricaInfo'][iParameter]

        def setAfricaInfo( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lAfricaInfo'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getAmericaInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lAmericaInfo'][iParameter]

        def setAmericaInfo( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lAmericaInfo'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getIsland1Info( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lIsland1Info'][iParameter]

        def setIsland1Info( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lIsland1Info'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getIsland2Info( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lIsland2Info'][iParameter]

        def setIsland2Info( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lIsland2Info'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getBordersCoordinates( self, iBorder, jCoordinate ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lBordersCoordinates'][iBorder][jCoordinate]

        def setBordersCoordinates( self, iBorder, jCoordinate, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lBordersCoordinates'][iBorder][jCoordinate] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getRandomContinents( self, iContinent ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lRandomContinents'][iContinent]

        def setRandomContinents( self, iContinent, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lRandomContinents'][iContinent] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

                
'''
Regional Variables Key:

iWaterPercent,
iRegionWidth, iRegionHeight,
iRegionWestX, iRegionSouthY,
iRegionGrain, iRegionHillsGrain,
iRegionPlotFlags, iRegionTerrainFlags,
iRegionFracXExp, iRegionFracYExp,
bShift, iStrip,
rift_grain, has_center_rift,
invert_heights
'''

def generatePlotTypes():
	print("Setting Plot Types (Python Terra) ...") #Rhye
	NiTextOut("Setting Plot Types (Python Terra) ...")
	# Call generatePlotsByRegion() function, from TerraMultilayeredFractal subclass.
	global plotgen
	plotgen = TerraMultilayeredFractal()
	return plotgen.generatePlotsByRegion()


#Rhye - start
# subclass TerrainGenerator
class RhyesTerraTerrainGenerator(CvMapGeneratorUtil.TerrainGenerator):
    
	iGridW = CyMap().getGridWidth()
	iGridH = CyMap().getGridHeight()

	def getLatitudeAtPlot(self, iX, iY, roll1): #real latitude
		# Latitudes run vertically for a world with a tilted axis.
		#lat = abs((self.iHeight / 2) - iY -10)/float(self.iHeight/2) # 0.0 = equator, 1.0 = pole

                if (CyMap().isWrapX() and not CyMap().isWrapY()):
                        iShift = gc.getGame().getSorenRandNum(30, '')
                        if (CyMap().getSeaLevel() == 0):
                                iShift = 17
                        if (CyMap().getSeaLevel() == 1):
                                iShift = 15
                        
                        iEquator = self.iHeight / 2 - self.iHeight *iShift / 100
                        if (roll1 == 1):
                                iEquator = self.iHeight / 2 + self.iHeight *iShift / 100
                        if (iY > iEquator):
                                lat = abs((iEquator) - iY )/float(self.iHeight - iEquator) 
                        else:
                                lat = abs((iEquator) - iY )/float(iEquator) 

                        # Adjust latitude using self.variation fractal, to mix things up:
                        lat += (128 - self.variation.getHeight(iX, iY))/(255.0 * 5.0)
                        
                elif (CyMap().isWrapY() and not CyMap().isWrapX()):
                        iShift = gc.getGame().getSorenRandNum(30, '')
                        iEquator = self.iWidth / 2 - self.iWidth *iShift / 100
                        if (roll1 == 1):
                                iEquator = self.iWidth / 2 + self.iWidth *iShift / 100
                        #print("LAT", iEquator, self.iWidth, self.iHeight, abs((iEquator) - iX ), float(iEquator))
                        if (iX > iEquator):
                                lat = abs((iEquator) - iX )/float(self.iWidth - iEquator) 
                        else:
                                lat = abs((iEquator) - iX )/float(iEquator) 

                        # Adjust latitude using self.variation fractal, to mix things up:
                        lat += (128 - self.variation.getHeight(iX, iY))/(255.0 * 5.0)
                        
                elif (not CyMap().isWrapY() and not CyMap().isWrapX()):
                        iEquatorX = self.iHeight / 2
                        iEquatorY = self.iWidth / 2
                        #if (iX > iEquatorX and iY > iEquatorY):
                        #        lat = max(abs((iEquatorX) - iY )/float(self.iHeight - iEquatorX),abs((iEquatorY) - iX )/float(self.iWidth - iEquatorY)) 
                        #else:
                        lat = max(abs((iEquatorX) - iY )/float(iEquatorX),abs((iEquatorY) - iX )/float(iEquatorY)) 

                        # Adjust latitude using self.variation fractal, to mix things up:
                        lat += (128 - self.variation.getHeight(iX, iY))/(255.0 * 5.0)
                        
                elif (CyMap().isWrapY() and CyMap().isWrapX()):
                        iEquatorX = self.iHeight / 2
                        iEquatorY = self.iWidth / 2
                        #if (iX > iEquatorX and iY > iEquatorY):
                        #        lat = 1-max(abs((iEquatorX) - iY )/float(self.iHeight - iEquatorX),abs((iEquatorY) - iX )/float(self.iWidth - iEquatorY)) 
                        #else:
                        lat = 1-max(abs((iEquatorX) - iY )/float(iEquatorX),abs((iEquatorY) - iX )/float(iEquatorY)) 

                        # Adjust latitude using self.variation fractal, to mix things up:
                        lat += (128 - self.variation.getHeight(iX, iY))/(255.0 * 5.0)

		# Limit to the range [0, 1]:
		if lat < 0:
			lat = 0.0
		if lat > 1:
			lat = 1.0

		return lat
#Rhye - end
	    
def generateTerrainTypes():
	print("Generating Terrain (Python Terra) ...") #Rhye
	NiTextOut("Generating Terrain (Python Terra) ...")
	#Rhye - start
	#terraingen = TerrainGenerator()
	terraingen = RhyesTerraTerrainGenerator()
	#Rhye - end
	terrainTypes = terraingen.generateTerrain()
	return terrainTypes

#Rhye - start
def getWorldShapeInfo( iParameter ):
        scriptDict = pickle.loads( gc.getGame().getScriptData() )
        return scriptDict['lWorldShapeInfo'][iParameter]
    
# subclass FeatureGenerator
class RhyesTerraFeatureGenerator(CvMapGeneratorUtil.FeatureGenerator):
    
	def getLatitudeAtPlot(self, iX, iY, roll1): #real latitude
		"returns a value in the range of 0.0 (tropical) to 1.0 (polar)"
		#lat = abs((self.iGridH/2) - iY -10)/float(self.iGridH/2) # 0.0 = equator, 1.0 = pole

                if (CyMap().isWrapX() and not CyMap().isWrapY()):
                        iShift = gc.getGame().getSorenRandNum(30, '')
                        if (CyMap().getSeaLevel() == 0):
                                iShift = 18
                        if (CyMap().getSeaLevel() == 1):
                                iShift = 16
                        iEquator = self.iGridH / 2 - self.iGridH *iShift / 100
                        if (roll1 == 1):
                                iEquator = self.iGridH / 2 + self.iGridH *iShift / 100
                        if (iY > iEquator):
                                lat = abs((iEquator) - iY )/float(self.iGridH - iEquator) 
                        else:
                                lat = abs((iEquator) - iY )/float(iEquator) 

                        
                elif (CyMap().isWrapY() and not CyMap().isWrapX()):
                        iShift = gc.getGame().getSorenRandNum(30, '')
                        iEquator = self.iGridW / 2 - self.iGridW *iShift / 100
                        if (roll1 == 1):
                                iEquator = self.iGridW / 2 + self.iGridW *iShift / 100
                        if (iX > iEquator):
                                lat = abs((iEquator) - iX )/float(self.iGridW - iEquator) 
                        else:
                                lat = abs((iEquator) - iX )/float(iEquator) 

                        
                elif (not CyMap().isWrapY() and not CyMap().isWrapX()):
                        iEquatorX = self.iGridH / 2
                        iEquatorY = self.iGridW / 2
                        #if (iX > iEquatorX and iY > iEquatorY):
                        #        lat = max(abs((iEquatorX) - iY )/float(self.iGridH - iEquatorX),abs((iEquatorY) - iX )/float(self.iGridW - iEquatorY)) 
                        #else:
                        lat = max(abs((iEquatorX) - iY )/float(iEquatorX),abs((iEquatorY) - iX )/float(iEquatorY)) 

                        
                elif (CyMap().isWrapY() and CyMap().isWrapX()):
                        iEquatorX = self.iGridH / 2
                        iEquatorY = self.iGridW / 2
                        #if (iX > iEquatorX and iY > iEquatorY):
                        #        lat = 1-max(abs((iEquatorX) - iY )/float(self.iGridH - iEquatorX),abs((iEquatorY) - iX )/float(self.iGridW - iEquatorY)) 
                        #else:
                        lat = 1-max(abs((iEquatorX) - iY )/float(iEquatorX),abs((iEquatorY) - iX )/float(iEquatorY)) 

                                
		# Limit to the range [0, 1]:
		if lat < 0:
			lat = 0.0
		if lat > 1:
			lat = 1.0

		return lat

#Rhye - end
	    
def addFeatures():
	print("Adding Features (Python Terra) ...") #Rhye
	NiTextOut("Adding Features (Python Terra) ...")
	#Rhye - start
	#featuregen = FeatureGenerator()
	featuregen = RhyesTerraFeatureGenerator()
	#Rhye - end
	featuregen.addFeatures()

	
	return 0




