# Rhye's and Fall of Civilization - Barbarian units and cities

from CvPythonExtensions import *
import CvUtil
import PyHelpers        # LOQ
import Popup
import cPickle as pickle
import RFCUtils
import Consts as con

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer	# LOQ
utils = RFCUtils.RFCUtils()


### Constants ###

iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iNative = con.iNative
iCeltia = con.iCeltia
iNumMajorPlayers = con.iNumMajorPlayers
iNumTotalPlayers = con.iNumTotalPlayers

pIndependent = gc.getPlayer(iIndependent)
pIndependent2 = gc.getPlayer(iIndependent2)
pNative = gc.getPlayer(iNative)
pCeltia = gc.getPlayer(iCeltia)
teamIndependent = gc.getTeam(pIndependent.getTeam())
teamIndependent2 = gc.getTeam(pIndependent2.getTeam())
teamNative = gc.getTeam(pNative.getTeam())
teamCeltia = gc.getTeam(pCeltia.getTeam())

iBarbarian = con.iBarbarian
pBarbarian = gc.getPlayer(iBarbarian)
teamBarbarian = gc.getTeam(pBarbarian.getTeam())
      

# city coordinates, spawn 1st turn and retries
#RFCRAND coordinates are replaced by 1st and 2nd favourite civ group, to pick a region where it spawns
#lCivGroups: 0 Euro, 1 Asia, 2 Middle east, 3 Mediterranean, 4 Africa, 5 America
#at the end, the 4 coordinates (BR and TL) of %width and height for the very high
lUr = [2, 3, 0, 0] #3000BC
lJerusalem = [2, 3, 0, 0, 62, 48, 67, 60] #3000BC #should be 3,2, but it's too early for mediterranean civs
lBabylon = [2, 3, 0, 0] #3000BC
lSusa = [2, 3, 0, 0] #3000BC
lTyre = [2, 3, 0, 0, 61, 48, 67, 61] #2700BC #turn10 #should be 3,2, but it's too early for mediterranean civs
lKnossos = [3, 2, 13, 0] #2600BC
lHattusas = [2, 3, 34, 0, 66, 55, 71, 67] #2000BC
lSamarkand = [1, 2, 34, 0, 73, 56, 80, 63] #2000BC
lNineveh = [2, 3, 42, 0] #1800BC
lGadir = [3, 0, 70, 0] #1100BC
lLepcis = [0, 4, 70, 0] #1100BC
lCarthage = [0, 4, 86, 0] #814BC
lGordion = [2, 3, 87, 0] #800BC
lPalermo = [3, 0, 94-5, 0] #700BC
lMilan = [0, 3, 94-5, 0] #700BC
lAugsburg = [0, 3, 94-5, 0] 
lRusadir = [0, 4, 97, 0] #650BC
lLyon = [0, 3, 117, 0] #350BC???
#lAxum = [4, 3, 121, 0] #300BC
lBordeaux = [0, 3, 121, 0] #300BC
lCartagena = [3, 0, 125, 0] #230BC
lArtaxata = [2, 1, 128, 0, 56, 65, 71, 67] #190BC
lLutetia = [0, 3, 137, 0] #50BC
lSeoul = [6, 1, 139, 0, 87, 59, 90, 69] #25BC
lBudapest = [0, -1, 140, 0, 56 ,66, 62, 71]  #0
#lTikal = [5, -1, 145, 0] #60AD
lSanaa = [2, 4, 147, 0, 64, 35, 71, 43] #100AD
lPagan = [1, 6, 148, 0, 85,37,87,43] #107AD
lInverness = [0, 3, 167, 0] #400AD
#lChichenItza = [5, -1, 170, 0] #445AD
lBaku = [2, 1, 180, 0, 70, 60, 73, 70] #600AD ca
lLhasa = [1, 6, 184, 0, 78, 54, 84, 60] #633AD
#lAngkor = [1, -1, 201, 0] #802AD
lHanoi = [6, 1, 209, 0, 87, 46, 90, 50] #866AD
lTucume = [5, -1, 211, 0, 14, 41, 17, 48] #900AD
lJelling = [0, -1, 219, 0] #980AD
lDublin = [0, -1, 220, 0, -1, -1, -1, -1] #990AD
lNidaros = [0, -1, 221, 0] #1000AD
lZimbabwe = [4, -1, 221, 0] #1000AD
lQuelimane = [4, -1, 221, 0, 59, 19, 63, 25] #1000AD
lUppsala = [0, -1, 228, 0] #1070AD
lMombasa = [4, 2, 231, 0, 60, 23, 63, 29] #1100AD
lKazan = [1, 2, 241, 0] #1100AD
lKongo = [4, -1, 278, 0, 52, 28, 56, 36] #1483AD



#handicap level modifier
iHandicapOld = (gc.getGame().getHandicapType() - 1)



class Barbs:

        def makeUnit(self, iUnit, iPlayer, tCoords, iNum, iForceAttack):
            
                #RFCRAND
                #print("MakeUnit1", iUnit, iPlayer, tCoords, iNum, iForceAttack)
                pPlot = gc.getMap().plot(tCoords[0],tCoords[1])
                if (pPlot.area().getNumTiles() < 25):
                        return
                    
                #print("MakeUnit2", iUnit, iPlayer, tCoords, iNum, iForceAttack)
                'Makes iNum units for player iPlayer of the type iUnit at tCoords.'
                for i in range(iNum):
                        player = gc.getPlayer(iPlayer)
                        if (iForceAttack == 0):
                                #print(iUnit, tCoords[0], tCoords[1], UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
                                player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
                        elif (iForceAttack == 1):
                                player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)                                  
                        elif (iForceAttack == 2):
                                player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.UNITAI_ATTACK_SEA, DirectionTypes.DIRECTION_SOUTH)



        	
        def checkTurn(self, iGameTurn):
            
                #handicap level modifier
                iHandicap = (gc.getGame().getHandicapType() - 2) #RFCRAND
                if (iHandicap == 2):
                        iHandicap = 1
                if (iHandicap == -2):
                        iHandicap = -1

                iGridX = gc.getMap().getGridWidth()
                iGridY = gc.getMap().getGridHeight()


                if (CyMap().getSeaLevel() <= 2):

                        #RFCRAND
                        iEurasiaWestX = utils.getEurasiaInfo(0)
                        iEurasiaEastX = utils.getEurasiaInfo(1)
                        iEurasiaSouthY = utils.getEurasiaInfo(2)
                        iEurasiaNorthY = utils.getEurasiaInfo(3)
                        iEurasiaAreaID = utils.getEurasiaInfo(4)
                        iEurasiaCentreY = (iEurasiaNorthY+iEurasiaSouthY)/2
                        iNEurasiaSouthY = iEurasiaCentreY
                        iNEurasiaNorthY = iEurasiaNorthY
                        iSEurasiaSouthY = iEurasiaSouthY
                        iSEurasiaNorthY = iEurasiaCentreY
                        if (utils.getWorldShapeInfo(0) == 1):
                                iNEurasiaSouthY = iEurasiaSouthY
                                iNEurasiaNorthY = iEurasiaCentreY
                                iSEurasiaSouthY = iEurasiaCentreY
                                iSEurasiaNorthY = iEurasiaNorthY
                        iAfricaWestX = utils.getAfricaInfo(0)
                        iAfricaEastX = utils.getAfricaInfo(1)
                        iAfricaSouthY = utils.getAfricaInfo(2)
                        iAfricaNorthY = utils.getAfricaInfo(3)
                        iAfricaAreaID = utils.getAfricaInfo(4)
                        iAmericaWestX = utils.getAmericaInfo(0)
                        iAmericaEastX = utils.getAmericaInfo(1)
                        iAmericaSouthY = utils.getAmericaInfo(2)
                        iAmericaNorthY = utils.getAmericaInfo(3)
                        iNAmericaAreaID = utils.getAmericaInfo(4)
                        iSAmericaAreaID = utils.getAmericaInfo(5)

                        
                                
                        
                        #debug
                        #if (iGameTurn % 50 == 1):
                        #        print ("iHandicap", iHandicap)
                        #        print ("iHandicapOld", iHandicapOld)

                        if (iGameTurn >= con.i2000BC and iGameTurn <= con.i850BC):
                                if (iHandicap >= 0):
                                        self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iWarrior, 1, iGameTurn, 8, 0, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iWolf, 1, iGameTurn, 7, 2, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iBear, 1, iGameTurn, 7, 4, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iAfricaWestX, iAfricaSouthY), (iAfricaEastX, iAfricaNorthY), iAfricaAreaID, con.iLion, 1, iGameTurn, 6, 1, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iAfricaWestX, iAfricaSouthY), (iAfricaEastX, iAfricaNorthY), iAfricaAreaID, con.iPanther, 1, iGameTurn, 6, 3, utils.outerInvasion, 0)


                        #barbarians in europe
                        if (iGameTurn >= con.i210BC and iGameTurn <= con.i690AD):
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iAxeman, 3 + iHandicap, iGameTurn, 8, 3, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iAxeman, 3 + iHandicap, iGameTurn, 8, 0, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iAxeman, 3 + iHandicap, iGameTurn, 8, 5, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iSwordsman, 4 + iHandicap, iGameTurn, 7, 6, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iSwordsman, 4 + iHandicap, iGameTurn, 7, 3, utils.outerInvasion, 0)                       
                        if (iGameTurn >= con.i110BC and iGameTurn <= con.i600AD):
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iHorseArcher, 3 + iHandicap, iGameTurn, 6, 1, utils.outerInvasion, 0)
                                self.spawnUnitsArea( iBarbarian, (iEurasiaWestX, iEurasiaSouthY), (iEurasiaEastX, iEurasiaNorthY), iEurasiaAreaID, con.iHorseArcher, 3 + iHandicap, iGameTurn, 6, 4, utils.outerInvasion, 0)

                        #camels in north africa
                        if (iGameTurn >= con.i300AD and iGameTurn <= con.i900AD):
                                self.spawnUnitsArea( iBarbarian, (iAfricaWestX, iAfricaSouthY), (iAfricaEastX, iAfricaNorthY), iAfricaAreaID, con.iCamelArcher, 2 + iHandicap, iGameTurn, 10, 0, utils.outerInvasion, 0)
                        if (iGameTurn >= con.i190AD and iGameTurn <= con.i1800AD):
                                self.spawnUnitsArea( iBarbarian, (iAfricaWestX, iAfricaSouthY), (iAfricaEastX, iAfricaNorthY), iAfricaAreaID, con.iCamelArcher, 2 + iHandicap, iGameTurn, 13, 4, utils.outerInvasion, 0)

                                
                        #celts
                        if (iGameTurn >= con.i650BC and iGameTurn <= con.i110BC):
                                self.spawnUnitsArea( iCeltia, (iEurasiaWestX, iNEurasiaSouthY), (iEurasiaEastX, iNEurasiaNorthY), iEurasiaAreaID, con.iCelticGallicWarrior, 1, iGameTurn, 8, 0, utils.outerInvasion, 0)
                                if (iHandicap >= 0):
                                        self.spawnUnitsArea( iCeltia, (iEurasiaWestX, iNEurasiaSouthY), (iEurasiaEastX, iNEurasiaNorthY), iEurasiaAreaID, con.iAxeman, 1, iGameTurn, 10, 6, utils.outerInvasion, 0)  

                        #norse
                        if (iGameTurn >= con.i650BC and iGameTurn <= con.i550AD):
                                self.spawnUnits( iCeltia, (iEurasiaWestX, iNEurasiaSouthY), (iEurasiaEastX, iNEurasiaNorthY),  con.iGalley, 1, iGameTurn, 20, 0, utils.outerCoastSpawn, 2)
                                
                                
                        #African natives
                        if (iGameTurn >= con.i140AD and iGameTurn <= con.i1700AD):
                                self.spawnUnitsArea( iNative, (iAfricaWestX, iAfricaSouthY), (iAfricaEastX, iAfricaNorthY), iAfricaAreaID, con.iZuluImpi, 3, iGameTurn, 13, 4, utils.outerInvasion, 1)

                        #American natives
                        if (iGameTurn >= con.i600AD and iGameTurn <= con.i1100AD):
                                self.spawnUnitsArea( iBarbarian, (iAmericaWestX, iAmericaSouthY), (iAmericaEastX, iAmericaNorthY), iNAmericaAreaID, con.iNativeAmericaDogSoldier, 4 + iHandicap, iGameTurn, 9, 0, utils.outerInvasion, 1)
                                self.spawnUnitsArea( iBarbarian, (iAmericaWestX, iAmericaSouthY), (iAmericaEastX, iAmericaNorthY), iSAmericaAreaID, con.iNativeAmericaDogSoldier, 4 + iHandicap, iGameTurn, 9, 0, utils.outerInvasion, 1)
                        if (iGameTurn >= con.i1300AD and iGameTurn <= con.i1600AD):
                                self.spawnUnitsArea( iNative, (iAmericaWestX, iAmericaSouthY), (iAmericaEastX, iAmericaNorthY), iNAmericaAreaID, con.iNativeAmericaDogSoldier, 4 + iHandicap, iGameTurn, 10, 0, utils.outerInvasion, 1)
                                self.spawnUnitsArea( iNative, (iAmericaWestX, iAmericaSouthY), (iAmericaEastX, iAmericaNorthY), iSAmericaAreaID, con.iNativeAmericaDogSoldier, 4 + iHandicap, iGameTurn, 10, 0, utils.outerInvasion, 1)


                        #pirates in Mediterranean
                        if (iGameTurn >= con.i210BC and iGameTurn <= con.i50AD):
                                self.spawnUnits( iBarbarian, (iEurasiaWestX, iSEurasiaSouthY), (iEurasiaEastX, iSEurasiaNorthY),  con.iTrireme, 1, iGameTurn, 8, 0, utils.outerCoastSpawn, 2)
                                

                                
                        #pirates in the Caribbean
                        if (iGameTurn >= con.i1600AD and iGameTurn <= con.i1800AD):
                                self.spawnUnits( iBarbarian, (iAmericaWestX, iAmericaSouthY), (iAmericaEastX, iAmericaNorthY), con.iPrivateer, 1, iGameTurn, 10, 0, utils.outerSeaSpawn, 0)

                else: #low or very low
                        iGridX = CyMap().getGridWidth()
                        iGridY = CyMap().getGridHeight()

                        #animals
                        if (iGameTurn >= con.i2000BC and iGameTurn <= con.i850BC):
                                if (iHandicap >= 0):
                                        self.spawnUnits( iBarbarian, (0, iGridX), (0, iGridY), con.iWarrior, 1, iGameTurn, 8, 0, utils.outerInvasion, 0)
                                self.spawnUnits( iBarbarian, (0, iGridX), (0, iGridY), con.iWolf, 1, iGameTurn, 7, 2, utils.outerInvasion, 0)
                                self.spawnUnits( iBarbarian, (0, iGridX), (0, iGridY), con.iBear, 1, iGameTurn, 7, 4, utils.outerInvasion, 0)
                                self.spawnUnits( iBarbarian, (0, iGridX), (0, iGridY), con.iLion, 1, iGameTurn, 6, 1, utils.outerInvasion, 0)
                                self.spawnUnits( iBarbarian, (0, iGridX), (0, iGridY), con.iPanther, 1, iGameTurn, 6, 3, utils.outerInvasion, 0)


                        #barbarians
                        if (iGameTurn >= con.i110BC and iGameTurn <= con.i690AD):
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 35, 75, con.iAxeman, 3 + iHandicap, iGameTurn, 8, 3, utils.outerInvasion, 0)
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 35, 75, con.iAxeman, 3 + iHandicap, iGameTurn, 8, 0, utils.outerInvasion, 0)
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 35, 75, con.iAxeman, 3 + iHandicap, iGameTurn, 8, 6, utils.outerInvasion, 0)
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 35, 75, con.iSwordsman, 4 + iHandicap*2, iGameTurn, 8, 6, utils.outerInvasion, 0)
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 35, 75, con.iSwordsman, 4 + iHandicap, iGameTurn, 8, 3, utils.outerInvasion, 0)                       
                        if (iGameTurn >= con.i140AD and iGameTurn <= con.i600AD):
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 25, 70, con.iHorseArcher, 3 + iHandicap, iGameTurn, 6, 1, utils.outerInvasion, 0)
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 25, 70, con.iHorseArcher, 3 + iHandicap, iGameTurn, 6, 4, utils.outerInvasion, 0)

                        #camels
                        if (iGameTurn >= con.i300AD and iGameTurn <= con.i600AD):
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 0, 30, con.iCamelArcher, 2 + iHandicap, iGameTurn, 10, 0, utils.outerInvasion, 0)
                        if (iGameTurn >= con.i190AD and iGameTurn <= con.i1800AD):
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 0, 30, con.iCamelArcher, 2 + iHandicap, iGameTurn, 13, 4, utils.outerInvasion, 0)

                                
                        #celts
                        if (iGameTurn >= con.i650BC and iGameTurn <= con.i110BC):
                                self.spawnUnitsLatitude( iCeltia, (0, iGridX), (0, iGridY), 50, 90, con.iCelticGallicWarrior, 1, iGameTurn, 8, 0, utils.outerInvasion, 0)
                                if (iHandicap >= 0):
                                        self.spawnUnitsLatitude( iCeltia, (0, iGridX), (0, iGridY), 50, 90, con.iAxeman, 1, iGameTurn, 10, 6, utils.outerInvasion, 0)  

                        #norse
                        if (iGameTurn >= con.i650BC and iGameTurn <= con.i550AD):
                                self.spawnUnitsLatitude( iCeltia, (0, iGridX), (0, iGridY), 50, 90, con.iGalley, 1, iGameTurn, 20, 0, utils.outerSeaSpawn, 2)

                        #natives
                        if (iGameTurn >= con.i450AD and iGameTurn <= con.i1700AD):
                                self.spawnUnitsLatitude( iNative, (0, iGridX), (0, iGridY), 0, 30, con.iZuluImpi, 3, iGameTurn, 12, 4, utils.outerInvasion, 1)

                        #pirates
                        if (iGameTurn >= con.i210BC and iGameTurn <= con.i50AD):
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 0, 40, con.iTrireme, 1, iGameTurn, 8, 0, utils.outerCoastSpawn, 2)
                        if (iGameTurn >= con.i1600AD and iGameTurn <= con.i1800AD):
                                self.spawnUnitsLatitude( iBarbarian, (0, iGridX), (0, iGridY), 0, 40, con.iPrivateer, 1, iGameTurn, 10, 0, utils.outerSeaSpawn, 0)
                        

                #ad hoc per civ
                iRadius = 9
                if (CyMap().getSeaLevel() <= 4):   #bypass  
                        iCiv = con.iEgypt
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i850BC and iGameTurn <= con.i900AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iChariot, 2, iGameTurn, 6, 3, utils.outerInvasion, 0)
                                if (iGameTurn >= con.i250AD and iGameTurn <= con.i550AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iCamelArcher, 2, iGameTurn, 8, 6, utils.outerInvasion, 0)
                        iCiv = con.iIndia
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i850BC and iGameTurn <= con.i900AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iAxeman, 2, iGameTurn, 7, 3, utils.outerInvasion, 0)
                                if (iGameTurn >= con.i250AD and iGameTurn <= con.i700AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iWarElephant, 2, iGameTurn, 8, 6, utils.outerInvasion, 0)
                        iCiv = con.iChina
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i140AD and iGameTurn <= con.i1000AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iHorseArcher, 2, iGameTurn, 7, 5, utils.outerInvasion, 0)
                        iCiv = con.iBabylonia
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i650BC and iGameTurn <= con.i600AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iChariot, 3, iGameTurn, 7, 4, utils.outerInvasion, 0)
                        iCiv = con.iGreece
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i110BC and iGameTurn <= con.i550AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iAxeman, 2, iGameTurn, 6, 3, utils.outerInvasion, 0)
                                if (iGameTurn >= con.i50AD and iGameTurn <= con.i700AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iHorseArcher, 2, iGameTurn, 6, 6, utils.outerInvasion, 0)
                        iCiv = con.iPersia
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i110BC and iGameTurn <= con.i600AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iHorseArcher, 3, iGameTurn, 6, 4, utils.outerInvasion, 0)
                        iCiv = con.iCarthage
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i10BC and iGameTurn <= con.i700AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iWarElephant, 2, iGameTurn, 12, 6, utils.outerInvasion, 0)
                                if (iGameTurn >= con.i250AD and iGameTurn <= con.i550AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iHorseArcher, 2, iGameTurn, 8, 6, utils.outerInvasion, 0)
                        iCiv = con.iRome
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i10BC and iGameTurn <= con.i550AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iAxeman, 2, iGameTurn, 6, 2, utils.outerInvasion, 0)
                                if (iGameTurn >= con.i140AD and iGameTurn <= con.i700AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iHorseArcher, 2, iGameTurn, 6, 5, utils.outerInvasion, 0)
                        iCiv = con.iEthiopia
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i250AD and iGameTurn <= con.i1000AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iCamelArcher, 2, iGameTurn, 14, 7, utils.outerInvasion, 0)
                        iCiv = con.iMaya
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i300AD and iGameTurn <= con.i1400AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iNativeAmericaDogSoldier, 2, iGameTurn, 9, 3, utils.outerInvasion, 0)
                        iCiv = con.iAztecs
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i1300AD and iGameTurn <= con.i1600AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iNativeAmericaDogSoldier, 3, iGameTurn, 7, 3, utils.outerInvasion, 0)
                        iCiv = con.iInca
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i1300AD and iGameTurn <= con.i1500AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iNativeAmericaDogSoldier, 3, iGameTurn, 7, 3, utils.outerInvasion, 0)
                        iCiv = con.iKhmer
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i1000AD and iGameTurn <= con.i1450AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iWarElephant, 2, iGameTurn, 10, 6, utils.outerInvasion, 0)
                        iCiv = con.iMali
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i1100AD and iGameTurn <= con.i1700AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iWarElephant, 2, iGameTurn, 11, 3, utils.outerInvasion, 0)
                                if (iGameTurn >= con.i1100AD and iGameTurn <= con.i1800AD):
                                        self.spawnUnitsLatitude( iNative, (0, iGridX), (0, iGridY), 0, 30, con.iZuluImpi, 2, iGameTurn, 11, 7, utils.outerInvasion, 1)
                        iCiv = con.iAmerica
                        if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+100 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                if (iGameTurn >= con.i1600AD and iGameTurn <= con.i1850AD):
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, con.iNativeAmericaDogSoldier, 2, iGameTurn, 12, 3, utils.outerInvasion, 0)

                else:  #very low
                        for iCiv in range(iNumMajorPlayers):
                                if (gc.getPlayer(iCiv).isAlive() and iGameTurn >= gc.getPlayer(iCiv).getBirthTurn()+80 and iGameTurn <= gc.getPlayer(iCiv).getBirthTurn()+200):
                                        iWestX = gc.getPlayer(iCiv).getStartingPlot().getX()-iRadius
                                        iEastX = gc.getPlayer(iCiv).getStartingPlot().getX()+iRadius
                                        iSouthY = gc.getPlayer(iCiv).getStartingPlot().getY()-iRadius
                                        iNorthY = gc.getPlayer(iCiv).getStartingPlot().getY()+iRadius
                                        #bestUnit = utils.bestUnitMounted(con.iBarbarian)
                                        #if (bestUnit == -1):
                                        #        bestUnit = utils.bestUnitAttack(con.iBarbarian)
                                        bestUnit = con.iHolyRomanLandsknecht
                                        if (iGameTurn < con.i1300AD):
                                                bestUnit = con.iHorseArcher
                                                if (iGameTurn < con.i300AD):
                                                        bestUnit = con.iSwordsman
                                                        if (iGameTurn < con.i850BC):
                                                                bestUnit = con.iChariot
                                        iPeriod = 7
                                        if (iGameTurn <= con.i110BC):
                                                iPeriod = 8
                                        if (iGameTurn >= con.i1000AD):
                                                iPeriod = 10
                                        if (iGameTurn >= con.i1300AD):
                                                iPeriod = 12
                                        self.spawnUnitsArea( iBarbarian, (iWestX, iSouthY), (iEastX, iNorthY), -1, bestUnit, 3, iGameTurn, iPeriod, (3+iCiv)%iPeriod, utils.outerInvasion, 0)

                    





                #RFCRAND
                #self.foundCity(iIndependent, lUr, "Ur", iGameTurn, 1, con.iWarrior, 1)
                #RFCRAND
                if (int(CyMap().getWorldSize()) >= 1): #standard or huge
                        self.foundCity(iIndependent2, lTyre, "Sur", iGameTurn, 1, con.iArcher, 1)
                self.foundCity(iIndependent, lJerusalem, "Yerushalayim", iGameTurn, 2, con.iArcher, 4) #RFCRAND                        
                #self.foundCity(lBabylon, "Babel", iGameTurn, 1, con.iArcher, 1)
                #self.foundCity(iIndependent2, lSusa, "Shushan", iGameTurn, 1, con.iArcher, 1)
                #self.foundCity(lKnossos, "Knossos", iGameTurn, 1, con.iWarrior, 0)                
                self.foundCity(iBarbarian, lHattusas, "Hattusas", iGameTurn, 1, con.iChariot, 2)
                self.foundCity(iIndependent, lSamarkand, "Samarkand", iGameTurn, 1, con.iArcher, 1) #RFCRAND Afrosiab
                #self.foundCity(iBarbarian, lNineveh, "Nineveh", iGameTurn, 1, -1, -1)
                #self.foundCity(lGadir, "Qart-Gadir", iGameTurn, 1, -1, -1)
                #self.foundCity(lLepcis, "Lpqy", iGameTurn, 2, -1, -1)
                #self.foundCity(lCarthage, "Qart-Hadasht", iGameTurn, 2, -1, -1)
                #self.foundCity(iBarbarian, lGordion, "Gordion", iGameTurn, 1, con.iChariot, 1) #RFCRAND (commented as too many middle eatern)
                #self.foundCity(lPalermo, "Ziz", iGameTurn, 2, con.iArcher, 1)
                #self.foundCity(iCeltia, lMilan, "Melpum", iGameTurn, 2, con.iArcher, 2)
                #self.foundCity(iBarbarian, lAugsburg, "Damasia", iGameTurn, 1, -1, -1)
                #self.foundCity(lRusadir, "Rusadir", iGameTurn, 2, -1, -1)
                #self.foundCity(iCeltia, lLyon, "Lugodunon", iGameTurn, 2, -1, -1)
                #self.foundCity(iIndependent, lAxum, "Axum", iGameTurn, 1, -1, -1)
                #self.foundCity(iCeltia, lBordeaux, "Burdigala", iGameTurn, 2, -1, -1)
                #self.foundCity(lCartagena, "Qart Hadasht", iGameTurn, 1, -1, -1)
                self.foundCity(iIndependent, lSeoul, "Hanseong", iGameTurn, 2, -1, -1)
                #RFCRAND
                if (int(CyMap().getWorldSize()) == 2): #huge
                        self.foundCity(iCeltia, lBudapest, "Ak Ink", iGameTurn, 2, -1, -1)
                if (int(CyMap().getWorldSize()) >= 1): #standard or huge
                        self.foundCity(iIndependent2, lArtaxata, "Artashat", iGameTurn, 1, -1, -1)
                #self.foundCity(iCeltia, lLutetia, "Lutetia", iGameTurn, 2, -1, -1)
                #self.foundCity(iNative, lTikal, "Tikal", iGameTurn, 1, -1, -1)
                #RFCRANDself.foundCity(iIndependent, lSanaa, "Sana'a", iGameTurn, 1, -1, -1)
                if (int(CyMap().getWorldSize()) == 2): #huge
                        self.foundCity(iIndependent2, lPagan, "Pagan", iGameTurn, 2, -1, -1)
                #RFCRAND self.foundCity(iCeltia, lInverness, "Inbhir Nis", iGameTurn, 2, -1, -1)
                #self.foundCity(iNative, lChichenItza, "Chichen Itza", iGameTurn, 1, -1, -1)
                #RFCRAND
                if (int(CyMap().getWorldSize()) == 2): #huge
                        self.foundCity(iBarbarian, lBaku, "Bak&#252;", iGameTurn, 2, con.iArcher, -1)
                self.foundCity(iBarbarian, lLhasa, "Lasa", iGameTurn, 2, -1, -1)
                #if (bLhasaResult == False):
                #        self.foundCity(iBarbarian, (lLhasa[0] - 1, lLhasa[1] - 1, lLhasa[2], lLhasa[3]), "Lhasa", iGameTurn, 2, -1, -1) #try to found it nearby
                #self.foundCity(iIndependent2, lAngkor, "Angkor", iGameTurn, 1, -1, -1)
                #RFCRAND
                if (int(CyMap().getWorldSize()) >= 1): #standard or huge
                        self.foundCity(iBarbarian, lHanoi, "Hanoi", iGameTurn, 2, -1, -1)
                self.foundCity(iNative, lTucume, "Tucume", iGameTurn, 1, -1, -1)
                #RFCRAND
                if (CyMap().getSeaLevel() != 0): #no place on Britain
                        if (int(CyMap().getWorldSize()) >= 1): #standard or huge                
                                self.foundCity(iCeltia, lDublin, "&#193;th Cliath", iGameTurn, 2, -1, -1)
                #self.foundCity(lJelling, "Jelling", iGameTurn, 1, -1, -1)
                #if (gc.getPlayer(0).isPlayable()):  #late start condition
                #        self.foundCity(iCeltia, lDublin, "&#193;th Cliath", iGameTurn, 1, -1, -1)
                #else:
                #        self.foundCity(iIndependent, lDublin, "&#193;th Cliath", iGameTurn, 1, -1, -1)
                #self.foundCity(lNidaros, "Nidaros", iGameTurn, 1, -1, -1)
                #self.foundCity(iNative, lZimbabwe, "Zimbabwe", iGameTurn, 1, con.iZuluImpi, 1)
                self.foundCity(iNative, lQuelimane, "Quelimane", iGameTurn, 1, con.iZuluImpi, 1)
                #self.foundCity(lUppsala, "Upsala", iGameTurn, 1, -1, -1)
                #RFCRAND
                if (int(CyMap().getWorldSize()) == 2): #huge
                        self.foundCity(iNative, lMombasa, "Mombasa", iGameTurn, 1, con.iZuluImpi, 1)
                #self.foundCity(iBarbarian, lKazan, "Kazan", iGameTurn, 2, con.iHorseArcher, 1) #RFCRAND
                self.foundCity(iNative, lKongo, "Mbanza Kongo", iGameTurn, 1, con.iZuluImpi, 1)



        def getCity(self, tCoords): #by LOQ
                'Returns a city at coordinates tCoords.'
                return CyGlobalContext().getMap().plot(tCoords[0], tCoords[1]).getPlotCity()

        def foundCity(self, iCiv, lCity, name, iTurn, iPopulation, iUnitType, iNumUnits):
                #RFCRAND
                if (((iTurn == lCity[2] + lCity[3]) and (lCity[3]<10) and CyMap().getSeaLevel() <= 2) or \
                    (iTurn == (utils.getFakeRandNum(lCity[4]+lCity[5],''))*220/(lCity[4]+lCity[5]) and CyMap().getSeaLevel() >= 3)):
                        #print self.checkRegion(tUr)
                        #bResult, lCity[3] = self.checkRegion((cityX, cityY))
                        #if (bResult == True):
                        (cityX, cityY) = self.findBestCityPlot(lCity[0], lCity[1], lCity[4], lCity[5],lCity[6], lCity[7])
                        #print("barb city",cityX, cityY)
                        if ((cityX, cityY) != (-1,-1)):
                                pCiv = gc.getPlayer(iCiv)
                                pCiv.found(cityX, cityY)
                                print("barb city founded")
                                self.getCity((cityX, cityY)).setName(name, False)
                                if (iPopulation != 1):
                                        self.getCity((cityX, cityY)).setPopulation(iPopulation)
                                if (iNumUnits > 0):
                                        self.makeUnit(iUnitType, iCiv, (cityX, cityY), iNumUnits, 0)
                                if (name == "Yerushalayim"):
                                        utils.setJerusalemLocation(0, cityX)
                                        utils.setJerusalemLocation(1, cityY)
                                return True
                        #if (bResult == False) and (lCity[3] == -1):
                        else:
                                return False
                               
        #RFCRAND
        def findBestCityPlot(self, civGroup1, civGroup2, lX, bY, rX, tY):
                if (CyMap().getSeaLevel() == 0):  #very high
                        iHeight = CyMap().getGridHeight()
                        iWidth = CyMap().getGridWidth()
                        leftX = int((float(lX)/100)*iWidth)
                        rightX = int((float(rX)/100)*iWidth)
                        bottomY = int((float(bY)/100)*iHeight)
                        topY = int((float(tY)/100)*iHeight)
                        plotsList = []
                        for iLoopX in range(leftX, rightX+1):
                                for iLoopY in range(bottomY, topY+1):                                
                                        pCurrent = CyMap().plot( iLoopX, iLoopY )
                                        if (pCurrent.getBonusType(-1) == -1 and not pCurrent.isWater() and not pCurrent.isPeak() and pCurrent.getFeatureType() == -1):
                                                bResult, temp = self.checkRegion((iLoopX, iLoopY, -1, 0))
                                                if (bResult == True):
                                                        plotsList.append((iLoopX, iLoopY))
                        #print(plotsList)
                        if (len(plotsList) > 0):
                                return plotsList[gc.getGame().getSorenRandNum(len(plotsList), 'random plot')]
                        else:
                                return (-1, -1)

                if (CyMap().getSeaLevel() == 4):  #very low
                        civGroup1 = gc.getGame().getSorenRandNum(6, 'randomise')
                        civGroup2 = gc.getGame().getSorenRandNum(6, 'randomise')
                        

                iLoop = gc.getGame().getSorenRandNum(len(con.lCivGroups[civGroup1]), 'random civ')
                for i in range(iLoop, len(con.lCivGroups[civGroup1])+iLoop):
                        iLoopCiv = con.lCivGroups[civGroup1][i%len(con.lCivGroups[civGroup1])]
                        pLoopCiv = gc.getPlayer(iLoopCiv)
                        if (pLoopCiv.isAlive() and utils.getInThisGame(iLoopCiv) == True):
                                #print("civ near", iLoopCiv)
                                plotsList = []
                                for iLoopX in range(pLoopCiv.getStartingPlot().getX()-10, pLoopCiv.getStartingPlot().getX()+10):
                                        for iLoopY in range(pLoopCiv.getStartingPlot().getY()-10, pLoopCiv.getStartingPlot().getY()+10):
                                                x=max(0,min(iLoopX,CyMap().getGridWidth()-1)) #iLoopX%CyMap().getGridWidth()
                                                y=max(0,min(iLoopY,CyMap().getGridHeight()-1))
                                                pCurrent = CyMap().plot( x, y )
                                                if (pCurrent.getBonusType(-1) == -1 and not pCurrent.isWater() and not pCurrent.isPeak() and pCurrent.getFeatureType() == -1):
                                                        bResult, temp = self.checkRegion((x, y, -1, 0))
                                                        if (bResult == True):
                                                                plotsList.append((x, y))
                                #print(plotsList)
                                if (len(plotsList) > 0):
                                        return plotsList[gc.getGame().getSorenRandNum(len(plotsList), 'random plot')]
                                else:
                                        return (-1, -1)
                #same with group2
                for i in range(iLoop, len(con.lCivGroups[civGroup2])+iLoop):
                        iLoopCiv = con.lCivGroups[civGroup2][i%len(con.lCivGroups[civGroup2])]
                        pLoopCiv = gc.getPlayer(iLoopCiv)
                        if (pLoopCiv.isAlive() and utils.getInThisGame(iLoopCiv) == True):
                                plotsList = []
                                for iLoopX in range(pLoopCiv.getStartingPlot().getX()-13, pLoopCiv.getStartingPlot().getX()+13):
                                        for iLoopY in range(pLoopCiv.getStartingPlot().getY()-13, pLoopCiv.getStartingPlot().getY()+13):
                                                x=iLoopX%CyMap().getGridWidth()
                                                y=max(0,min(iLoopY,CyMap().getGridHeight()))
                                                pCurrent = CyMap().plot( x, y )
                                                if (pCurrent.getBonusType(-1) == -1 and not pCurrent.isWater() and not pCurrent.isPeak() and pCurrent.getFeatureType() == -1):
                                                        bResult, temp = self.checkRegion((x, y, -1, 0))
                                                        if (bResult == True):
                                                                plotsList.append((x, y))
                                #print(plotsList)
                                if (len(plotsList) > 0):
                                        return plotsList[gc.getGame().getSorenRandNum(len(plotsList), 'random plot')]
                                else:
                                        return (-1, -1)
                return (-1, -1)


##                            
##        def findBestCityPlot(self, civGroup1, civGroup2):
##                bestPlotsList = []
##                bestValue = 0
##                for iLoopX in range(CyMap().getGridWidth()):
##                        for iLoopY in range(CyMap().getGridHeight()):
##                                pCurrent = CyMap().plot( iLoopX, iLoopY )
##                                if (pCurrent.getBonusType(-1) == -1 and not pCurrent.isWater() and not pCurrent.isPeak() and pCurrent.getFeatureType() == -1):
##                                        cityPlotValue = self.cityPlotValue(iLoopX, iLoopY, civGroup1, civGroup2)
##                                        if (cityPlotValue == bestValue):
##                                                bResult, temp = self.checkRegion((iLoopX, iLoopY, -1, 0))
##                                                if (bResult == True):
##                                                        bestPlotsList.append((iLoopX, iLoopY))
##                                        elif (cityPlotValue > bestValue):
##                                                bResult, temp = self.checkRegion((iLoopX, iLoopY, -1, 0))
##                                                if (bResult == True):
##                                                        bestValue = cityPlotValue
##                                                        bestPlotsList = []
##                                                        bestPlotsList.append((iLoopX, iLoopY))
##                print(bestPlotsList)
##                print(bestValue)
##                if (len(bestPlotsList) > 0):
##                        return bestPlotsList[gc.getGame().getSorenRandNum(len(bestPlotsList), 'random plot')]
##                else:
##                        return (-1, -1)
##
##                        
##        #RFCRAND                        
##        def cityPlotValue(self, x, y, civGroup1, civGroup2):
##                iNumGroup1CivsNear = 0
##                iNumGroup2CivsNear = 0
##                for iLoopCiv in range(con.iNumMajorPlayers):
##                        pLoopCiv = gc.getPlayer(iLoopCiv)
##                        if (pLoopCiv.isAlive() and utils.getInThisGame(iLoopCiv) == True):
##                                if (utils.calculateDistance(x, y, pLoopCiv.getStartingPlot().getX(), pLoopCiv.getStartingPlot().getY()) < 15):
##                                        if (iLoopCiv in con.lCivGroups[civGroup1]):
##                                                iNumGroup1CivsNear += 1
##                                        if (civGroup2 != -1):
##                                                if (iLoopCiv in con.lCivGroups[civGroup2]):
##                                                        iNumGroup2CivsNear += 1
##                iPlotScore = min(iNumGroup1CivsNear,4) + min(iNumGroup2CivsNear,4)/2
##                return iPlotScore
                                
                                


        def checkRegion(self, tCity):
                cityPlot = gc.getMap().plot(tCity[0], tCity[1])
                iNumUnitsInAPlot = cityPlot.getNumUnits()
##                print iNumUnitsInAPlot
                
                #checks if the plot already belongs to someone
                if (cityPlot.isOwned()):
                        if (cityPlot.getOwner() != iBarbarian ):
                                return (False, -1)
                    
##                #checks if there's a unit on the plot
##                if (iNumUnitsInAPlot):
##                        for i in range(iNumUnitsInAPlot):
##                                unit = cityPlot.getUnit(i)
##                                iOwner = unit.getOwner()
##                                pOwner = gc.getPlayer(iOwner)
##                                if (pOwner.isHuman()):
##                                        return (False, tCity[3]+1)                    

                #checks the surroundings and allows only AI units
                for x in range(tCity[0]-1, tCity[0]+2):
                        for y in range(tCity[1]-1, tCity[1]+2):
                                currentPlot=gc.getMap().plot(x,y)
                                if (currentPlot.isCity()):
                                        return (False, -1)                                
                                iNumUnitsInAPlot = currentPlot.getNumUnits()
                                if (iNumUnitsInAPlot):
                                        for i in range(iNumUnitsInAPlot):
                                                unit = currentPlot.getUnit(i)
                                                iOwner = unit.getOwner()
                                                pOwner = gc.getPlayer(iOwner)
                                                if (pOwner.isHuman()):
                                                        return (False, tCity[3]+1)
                return (True, tCity[3])



        def spawnUnits(self, iCiv, tTopLeft, tBottomRight, iUnitType, iNumUnits, iTurn, iPeriod, iRest, function, iForceAttack):
                if (iTurn % iPeriod == iRest):
                        dummy, plotList = utils.squareSearch( tTopLeft, tBottomRight, function, [] )
                        if (len(plotList)):
                                rndNum = gc.getGame().getSorenRandNum(len(plotList), 'Spawn units')
                                result = plotList[rndNum]
                                if (result):
                                        self.makeUnit(iUnitType, iCiv, result, iNumUnits, iForceAttack)             
        #RFCRAND
        def spawnUnitsArea(self, iCiv, tTopLeft, tBottomRight, iContinentID, iUnitType, iNumUnits, iTurn, iPeriod, iRest, function, iForceAttack):
                #print("spawnUnitsArea1",iTurn, iPeriod, iTurn % iPeriod,iRest)
                if (iTurn % iPeriod == iRest):
                        #print("spawnUnitsArea2",iTurn % iPeriod, iRest)
                        dummy, plotList = utils.squareSearch( tTopLeft, tBottomRight, function, [] )
                        #print(plotList)
                        if (len(plotList)):
                                
                                finalPlotList = []
                                for tPlot in plotList:
                                        pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
                                        if (pPlot.area().getID() == iContinentID or (iContinentID == -1 and pPlot.area().getNumTiles() >= 80)):
                                                #print("passable", pPlot.getX(), pPlot.getY(), tPlot[0], tPlot[1], utils.getPassableAreaSize(tPlot[0], tPlot[1], 4), utils.getPassableAreaSize(pPlot.getX(), pPlot.getY(), 4))
                                                if (pPlot.isWater() or (pPlot.area().getNumCities() > 0 and utils.getPassableAreaSize(tPlot[0], tPlot[1], 4)>=13)):
                                                        if (not pPlot.getFeatureType() == con.iSeaIce):
                                                                lat = pPlot.getRealLatitude()
                                                                if (lat <= 80):
                                                                        finalPlotList.append(tPlot)
                                if (len(finalPlotList)):
                                        rndNum = gc.getGame().getSorenRandNum(len(finalPlotList), 'Spawn units')
                                        result = finalPlotList[rndNum]
                                        if (result):
                                                #print("spawnUnitsArea3",result)
                                                self.makeUnit(iUnitType, iCiv, result, iNumUnits, iForceAttack)
        #RFCRAND
        def spawnUnitsLatitude(self, iCiv, tTopLeft, tBottomRight, minLat, maxLat, iUnitType, iNumUnits, iTurn, iPeriod, iRest, function, iForceAttack):
                if (iTurn % iPeriod == iRest):
                        dummy, plotList = utils.squareSearch( tTopLeft, tBottomRight, function, [] )
                        if (len(plotList)):
                                finalPlotList = []
                                for tPlot in plotList:
                                        pPlot = gc.getMap().plot(tPlot[0],tPlot[1])
                                        lat = pPlot.getRealLatitude()
                                        if (lat >= minLat and lat <= maxLat):
                                                if ((pPlot.isWater()) or (pPlot.area().getNumCities() > 0 and utils.getPassableAreaSize(tPlot[0], tPlot[1], 4)>=13 and not pPlot.isPeak() )):
                                                         if (not pPlot.getFeatureType() == con.iSeaIce):
                                                                 finalPlotList.append(tPlot)                                
                                if (len(finalPlotList)):
                                        rndNum = gc.getGame().getSorenRandNum(len(finalPlotList), '')
                                        result = finalPlotList[rndNum]
                                        if (result):
                                                self.makeUnit(iUnitType, iCiv, result, iNumUnits, iForceAttack)     
	    
        def killNeighbours(self, tCoords):
                'Kills all units in the neigbbouring tiles of plot (as well as plot itself) so late starters have some space.'
                for x in range(tCoords[0]-1, tCoords[0]+2):        # from x-1 to x+1
                        for y in range(tCoords[1]-1, tCoords[1]+2):	# from y-1 to y+1
                                killPlot = CyMap().getPlot(x, y)
                                for i in range(killPlot.getNumUnits()):
                                        unit = killPlot.getUnit(0)	# 0 instead of i because killing units changes the indices
                                        unit.kill(False, iBarbarian)

