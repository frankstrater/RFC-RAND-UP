# Rhye's and Fall of Civilization RAND- Pots

from CvPythonExtensions import *
import CvUtil
import PyHelpers  
import Consts as con
import RFCUtils
utils = RFCUtils.RFCUtils()

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

### Constants ###

iEgypt = con.iEgypt
iIndia = con.iIndia
iChina = con.iChina
iBabylonia = con.iBabylonia
iGreece = con.iGreece
iPersia = con.iPersia
iCarthage = con.iCarthage
iRome = con.iRome
iJapan = con.iJapan
iEthiopia = con.iEthiopia
iMaya = con.iMaya
iVikings = con.iVikings
iArabia = con.iArabia
iKhmer = con.iKhmer
iSpain = con.iSpain
iFrance = con.iFrance
iEngland = con.iEngland
iGermany = con.iGermany
iRussia = con.iRussia
iNetherlands = con.iNetherlands
iHolland = con.iHolland
iMali = con.iMali
iTurkey = con.iTurkey
iPortugal = con.iPortugal
iInca = con.iInca
iMongolia = con.iMongolia
iAztecs = con.iAztecs
iAmerica = con.iAmerica
iNumPlayers = con.iNumPlayers
iNumMajorPlayers = con.iNumMajorPlayers
iNumActivePlayers = con.iNumActivePlayers
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iNative = con.iNative
iCeltia = con.iCeltia
iBarbarian = con.iBarbarian
iNumTotalPlayers = con.iNumTotalPlayers

tProb = (
1, #Egypt
1, #India
1, #China 
0, #Babylonia
1, #Greece
0, #Persia
0, #Carthage
1, #Rome
1, #Japan
1, #Ethiopia
0, #Maya
0, #Vikings
1, #Arabia
0, #Khmer
1, #Spain
1, #France
1, #England
1, #Germany
1, #Russia
0, #Holland
0, #Mali
0, #Portugal
1, #Inca
1, #Mongolia
0, #Aztecs
0, #Turkey
1 #America
) 

#scrambled pools
tPots = ((iEgypt, iIndia, iChina, iBabylonia), #1
        (iGreece, iPersia, iCarthage, iRome), #2
        (iJapan, iKhmer, iMongolia), #3
        (iEthiopia, iMali), #4
        (iArabia, iTurkey), #5
        (iVikings, iSpain, iFrance, iEngland, iGermany, iRussia, iNetherlands, iPortugal), #6
        (iMaya, iInca, iAztecs, iAmerica)) #7

#27 is huge
tNumCivsMedium = (3,3,2,1,2,6,3) #20 (+1 randomly picked)
tNumCivsSmall  = (3,2,1,1,1,4,2) #14 (+1 randomly picked)






class Pots:


       	
        def setup(self):
            
                if (CyMap().getWorldSize() == 2): #huge
                        for i in range(iNumPlayers):
                                utils.setInThisGame(i, True)
                        return
                            
                for i in range(iNumPlayers):
                        if (gc.getPlayer(i).isHuman()):
                                utils.setInThisGame(i, True)
                                
                for iPot in range(7):
                        iCounter = 0
                        lTempResults = []
                        lNumCivs = []
                        lPots = []
                        
                        lCurrentPot = tPots[iPot]
                        if (int(CyMap().getWorldSize()) == 0): #standard
                                lNumCivs = tNumCivsSmall
                        elif (int(CyMap().getWorldSize()) == 1): #large
                                lNumCivs = tNumCivsMedium
                                
                        if (utils.getHumanID() in lCurrentPot):
                                lTempResults.append(utils.getHumanID())
                                iCounter = 1
                                #print("Added human civ", utils.getHumanID())
                        
                        while (iCounter < lNumCivs[iPot]):
                                roll = gc.getGame().getSorenRandNum(len(lCurrentPot), '')
                                currentCiv = lCurrentPot[roll]
                                
                                if (tProb[currentCiv] == 0): #less important civ
                                        rollProb = gc.getGame().getSorenRandNum(100, '')
                                        if (rollProb > 50):
                                                roll = gc.getGame().getSorenRandNum(len(lCurrentPot), '') #roll again
                                                currentCiv = lCurrentPot[roll]

                                if (currentCiv not in lTempResults):
                                        lTempResults.append(currentCiv)
                                        iCounter = iCounter + 1
                                        #print("Added civ", currentCiv)

                        for iCiv in (lTempResults):
                                utils.setInThisGame(iCiv, True)

                rollLastPick = gc.getGame().getSorenRandNum(iNumMajorPlayers, '')
                for i in range(rollLastPick, rollLastPick+iNumMajorPlayers):
                        iLoopCiv = i%iNumMajorPlayers
                        if (utils.getInThisGame(iLoopCiv) == False):
                                utils.setInThisGame(iLoopCiv, True)
                                print("Added one last civ", iLoopCiv)
                                break
                                


