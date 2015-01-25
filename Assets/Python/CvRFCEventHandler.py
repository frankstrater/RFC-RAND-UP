from CvPythonExtensions import *
import CvUtil
import CvEventManager #Mercenaries
import sys #Mercenaries
import PyHelpers 
import CvMainInterface #Mercenaries
import CvMercenaryManager #Mercenaries
import MercenaryUtils #Mercenaries
import CvScreenEnums  #Mercenaries
#import CvConfigParser #Mercenaries #Rhye
import Popup as PyPopup 

import StoredData
import RiseAndFall        
import Barbs                
import Religions        
# import Resources        # Tweaked - not used
import CityNameManager  
import UniquePowers     
import AIWars           
import Congresses
import Consts as con 
import RFCUtils
utils = RFCUtils.RFCUtils()
import CvScreenEnums #Mercenaries, Rhye
import Victory
import Stability
import Plague
import Communications
import RandomRFC
import CvMapGeneratorUtil #debug

import CvMainInterface #Rhye RFCRAND
        
gc = CyGlobalContext()        
#iBetrayalCheaters = 15


#Rhye - start
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
iPortugal = con.iPortugal
iInca = con.iInca
iMongolia = con.iMongolia
iAztecs = con.iAztecs
iTurkey = con.iTurkey
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
#Rhye - end



#Mercenaries - start
objMercenaryUtils = MercenaryUtils.MercenaryUtils()

PyPlayer = PyHelpers.PyPlayer
PyGame = PyHelpers.PyGame()
PyInfo = PyHelpers.PyInfo

# Set g_bGameTurnMercenaryCreation to true if mercenary creation should happen during the 
# onBeginGameTurn method, false if it should happen during the onBeginPlayerTurn method
# Default value is true
g_bGameTurnMercenaryCreation = true

# Set g_bDisplayMercenaryManagerOnBeginPlayerTurn to true if the "Mercenary Manager" 
# screen should be displayed at the beginning of every player turn. 
# Default value is false
g_bDisplayMercenaryManagerOnBeginPlayerTurn = false

# This value also controls the "Mercenary Manager" button and when it should be displayed.
# Default value is "ERA_ANCIENT"
#Rhye - start (was causing an assert)
#g_iStartingEra = gc.getInfoTypeForString("ERA_ANCIENT")
g_iStartingEra = 0
#Rhye - end

# Change this to false if mercenaries should be removed from the global mercenary pool 
# at the beginning of the game turn. When set to true a number of mercenaries will 
# wander away from the global mercenary pool. This is another variable used to control 
# the load time for the "Mercenary Manager" screen.
# Default valus is true
g_bWanderlustMercenaries = true

# Change this to increase the max number of mercenaries that may wander away from the
# global mercenary pool.
# Default valus is 3
g_iWanderlustMercenariesMaximum = 7 #Rhye

# Default valus is 0 
g_iWanderlustMercenariesMinimum = 2 #Rhye

# Change this to false to supress the mercenary messages.
# Default value is true
g_bDisplayMercenaryMessages = false #Rhye

# Set to true to print out debug messages in the logs
g_bDebug = false

# Default valus is 1 
g_bUpdatePeriod = 5 #Rhye

# Default valus is 1 
g_bAIThinkPeriod = 6 #Rhye (5 in Warlords, 4 in vanilla)

# globals

#Mercenaries - end


###################################################
class CvRFCEventHandler:



        mercenaryManager = None #Mercenaries


        def __init__(self, eventManager):

                self.EventKeyDown=6 #Mercenaries

                # initialize base class
                eventManager.addEventHandler("GameStart", self.onGameStart) #Stability
                eventManager.addEventHandler("BeginGameTurn", self.onBeginGameTurn) #Stability
                eventManager.addEventHandler("cityAcquired", self.onCityAcquired) #Stability
                eventManager.addEventHandler("cityRazed", self.onCityRazed) #Stability
                eventManager.addEventHandler("cityBuilt", self.onCityBuilt) #Stability
                eventManager.addEventHandler("combatResult", self.onCombatResult) #Stability
                #eventManager.addEventHandler("changeWar", self.onChangeWar)
                eventManager.addEventHandler("religionFounded",self.onReligionFounded) #Victory
                eventManager.addEventHandler("buildingBuilt",self.onBuildingBuilt) #Victory
                eventManager.addEventHandler("projectBuilt",self.onProjectBuilt) #Victory
                eventManager.addEventHandler("BeginPlayerTurn", self.onBeginPlayerTurn) #Mercenaries
                #eventManager.addEventHandler("EndPlayerTurn", self.onEndPlayerTurn)
                eventManager.addEventHandler("EndGameTurn", self.onEndGameTurn) #Stability
                eventManager.addEventHandler("kbdEvent",self.onKbdEvent) #Mercenaries
                eventManager.addEventHandler("unitLost",self.onUnitLost) #Mercenaries
                eventManager.addEventHandler("unitKilled",self.onUnitKilled) #Mercenaries
                eventManager.addEventHandler("OnLoad",self.onLoadGame) #Mercenaries
                eventManager.addEventHandler("unitPromoted",self.onUnitPromoted) #Mercenaries
                eventManager.addEventHandler("techAcquired",self.onTechAcquired) #Mercenaries, Rhye #Stability
                #eventManager.addEventHandler("improvementDestroyed",self.onImprovementDestroyed) #Stability
                eventManager.addEventHandler("religionSpread",self.onReligionSpread) #Stability
                eventManager.addEventHandler("firstContact",self.onFirstContact)
                eventManager.addEventHandler("corporationFounded",self.onCorporationFounded) #Stability
                


               
                self.eventManager = eventManager

                self.data = StoredData.StoredData()
                self.rnf = RiseAndFall.RiseAndFall()
                self.barb = Barbs.Barbs()
                self.rel = Religions.Religions()
                # self.res = Resources.Resources()	# Tweaked - not used
                self.cnm = CityNameManager.CityNameManager()
                self.up = UniquePowers.UniquePowers()
                self.aiw = AIWars.AIWars()
                self.cong = Congresses.Congresses()
                self.vic = Victory.Victory()
                self.sta = Stability.Stability()
                self.pla = Plague.Plague()
                self.com = Communications.Communications()
                self.rnd = RandomRFC.RandomRFC()
                
                
                #Mercenaries - start
                
                self.mercenaryManager = CvMercenaryManager.CvMercenaryManager(CvScreenEnums.MERCENARY_MANAGER)        

                global g_bGameTurnMercenaryCreation
                global g_bDisplayMercenaryManagerOnBeginPlayerTurn
                global g_iStartingEra
                global g_bWanderlustMercenaries
                global g_iWanderlustMercenariesMaximum
                global g_bDisplayMercenaryMessages 

		#Rhye - start comment
##		# Load the Mercenaries Mod Config INI file containing all of the configuration information		
##		config = CvConfigParser.CvConfigParser("Mercenaries Mod Config.ini")
##
##		# If we actually were able to open the "Mercenaries Mod Config.ini" file then read in the values.
##		# otherwise we'll keep the default values that were set at the top of this file.
##		if(config != None):
##			g_bGameTurnMercenaryCreation = config.getboolean("Mercenaries Mod", "Game Turn Mercenary Creation", true)
##			g_bDisplayMercenaryManagerOnBeginPlayerTurn = config.getboolean("Mercenaries Mod", "Display Mercenary Manager On Begin Player Turn", false)
##			g_iStartingEra = gc.getInfoTypeForString(config.get("Mercenaries Mod","Starting Era","ERA_ANCIENT"))
##			g_bWanderlustMercenaries = config.getboolean("Mercenaries Mod", "Wanderlust Mercenaries", true)
##			g_iWanderlustMercenariesMaximum = config.getint("Mercenaries Mod","Wanderlust Mercenaries Maximum", 5)
##			g_bDisplayMercenaryMessages = config.getboolean("Mercenaries Mod", "Display Mercenary Messages", true)
		#Rhye - end comment

                objMercenaryUtils = MercenaryUtils.MercenaryUtils()
                #Mercenaries - end


        def onGameStart(self, argsList):
                'Called at the start of the game'
                self.rnd.setup()
                #self.data.setupScriptData() #RFCRAND
                self.rnf.setup()
                self.rel.setup()
                self.pla.setup()
                self.sta.setup()
                self.aiw.setup()
                #self.rnf.warOnSpawn() #RFCRAND

                

                #Mercenaries - start
                global objMercenaryUtils        
                objMercenaryUtils = MercenaryUtils.MercenaryUtils()
		#Mercenaries - end

                #RFCRAND - bugfix
                gc.getPlayer(con.iIndependent).setMinorCiv(True)
                gc.getPlayer(con.iIndependent2).setMinorCiv(True)
                gc.getPlayer(con.iNative).setMinorCiv(True)
                gc.getPlayer(con.iCeltia).setMinorCiv(True)
                CvMainInterface.CvMainInterface().updateScoreStrings()
                
                return 0


        def onCityAcquired(self, argsList):
                #'City Acquired'
                owner,playerType,city,bConquest,bTrade = argsList
                #CvUtil.pyPrint('City Acquired Event: %s' %(city.getName()))
                self.cnm.renameCities(city, playerType)
                
                if (playerType == con.iArabia):
                        self.up.arabianUP(city)
                elif (playerType == con.iTurkey):
                        self.up.turkishUP(city)

                if (playerType < iNumMajorPlayers):
                         utils.spreadMajorCulture(playerType, city.getX(), city.getY())

                self.sta.onCityAcquired(owner,playerType,city,bConquest,bTrade)

                #kill byzantium
                if (not gc.getPlayer(0).isPlayable()):  #late start condition
                        if (owner == iCeltia and gc.getPlayer(iCeltia).isAlive()):
                                if ((city.getX() == 68 and city.getY() == 45) or gc.getPlayer(iCeltia).getNumCities() <= 2): #constantinopolis captured or empire size <=2
                                        print ("killed Byzantium")
                                        utils.killAndFragmentCiv(iCeltia, iIndependent, iIndependent2, -1, False)

                
                if (bConquest):
                        #self.rnf.collapseCapitals(owner, city, playerType)
                        if (owner == utils.getHumanID() and playerType != con.iBarbarian):
                                self.rnf.collapseHuman(owner, city, playerType)
                        #print ("exile data:", self.rnf.getExileData(0), city.getX(), self.rnf.getExileData(1), city.getY(), self.rnf.getExileData(2))
                        if (self.rnf.getExileData(0) == city.getX() and self.rnf.getExileData(1) == city.getY()):
                                if (playerType == utils.getHumanID() and self.rnf.getExileData(2) != -1):
                                        self.rnf.escape(city)
                if (bTrade):
                        for i in range (con.iScotlandYard +1 - con.iHeroicEpic):
                                iNationalWonder = i + con.iHeroicEpic
                                if (city.hasBuilding(iNationalWonder)):
                                        city.setHasRealBuilding((iNationalWonder), False)

                self.pla.onCityAcquired(owner,playerType,city) #Plague

                self.com.onCityAcquired(city) #Communications

                self.vic.onCityAcquired(owner, playerType, bConquest) #Victory
                
                return 0

        def onCityRazed(self, argsList):
                #'City Razed'
                city, iPlayer = argsList

                self.sta.onCityRazed(city.getOwner(),iPlayer,city)
		
                if (iPlayer == con.iMongolia):
                        self.up.setLatestRazeData(0, gc.getGame().getGameTurn())
                        owner = city.getOwner()
                        if (city.getOwner() == iPlayer):
                                if (city.getPreviousOwner() != -1):
                                        owner = city.getPreviousOwner()                        
                        self.up.setLatestRazeData(1, owner)
                        self.up.setLatestRazeData(2, city.getPopulation())
                        self.up.setLatestRazeData(3, city.getX())
                        self.up.setLatestRazeData(4, city.getY())
                        print ("city.getPopulation()", city.getPopulation())
                        print ("prev", city.getPreviousOwner(), "curr", city.getOwner())
                        self.up.setMongolAI()

                self.pla.onCityRazed(city,iPlayer) #Plague
                        
                if (iPlayer == con.iMongolia):
                        self.vic.onCityRazed(iPlayer) #Victory



        def onCityBuilt(self, argsList):
                'City Built'
                city = argsList[0]
                
                iOwner = city.getOwner()
                
                if (iOwner < con.iNumActivePlayers): 
                        self.cnm.assignName(city)


                #Rhye - delete culture of barbs and minor civs to prevent weird unhappiness
                pCurrent = gc.getMap().plot( city.getX(), city.getY() )
                for i in range(con.iNumTotalPlayers - con.iNumActivePlayers):
                        iMinorCiv = i + con.iNumActivePlayers
                        pCurrent.setCulture(iMinorCiv, 0, True)
                pCurrent.setCulture(con.iBarbarian, 0, True)

                if (iOwner < iNumMajorPlayers):
                        utils.spreadMajorCulture(iOwner, city.getX(), city.getY())


                if (iOwner == con.iTurkey):
                        self.up.turkishUP(city)


                if (self.vic.getNewWorld(0) == -1):
                        #RFCRAND
                        if (iOwner in con.lCivGroups[0] and iOwner < iNumActivePlayers):
                                area = city.area()
                                if (area.getNumTiles() >= 100 and utils.isNewWorld(city.getX(), city.getY())):  #we should count only the main land
                                #if (area.getNumTiles() >= 100 and area.getID() == self.rnd.getAmericaInfo(4) or area.getID() == self.rnd.getAmericaInfo(5)):
                                        bFirstInTheNewWorld = True
                                        if (area.getNumCities() == 0):
                                                bFirstInTheNewWorld = True
                                        for iLoopCiv in range(iNumMajorPlayers):
                                                if (iLoopCiv in con.lCivBioOldWorld):                                                
                                                        if (area.getCitiesPerPlayer(iLoopCiv) > 0):
                                                                bFirstInTheNewWorld = False
                                                                break
                                        
                                        if (bFirstInTheNewWorld == True):
                                                self.vic.setNewWorld(0, iOwner)
                                                if (iOwner != iVikings):
                                                        self.vic.setGoal(iVikings, 2, 0)
                                                if (iOwner != iSpain):
                                                        self.vic.setGoal(iSpain, 0, 0) 

                if (iOwner == con.iRussia or \
                    iOwner == con.iFrance or \
                    iOwner == con.iEngland or \
                    iOwner == con.iSpain or \
                    #iOwner == con.iCarthage or \
                    iOwner == con.iVikings or \
                    iOwner == con.iPortugal or \
                    iOwner == con.iNetherlands):    
                        self.vic.onCityBuilt(city, iOwner) #Victory

                if (iOwner < con.iNumPlayers):
                        self.sta.onCityBuilt(iOwner, city.getX(), city.getY() )

        def onCombatResult(self, argsList):
                self.up.aztecUP(argsList)
                self.vic.onCombatResult(argsList)
                self.sta.onCombatResult(argsList)
                self.rnf.immuneMode(argsList)



##        def onChangeWar(self, argsList):
##                print ("No cheaters1")
##                if (bIsWar):
##                        print ("No cheaters2")
##                        if (argsList[1] == utils.getHumanID() and gc.getGame().getGameTurn() <= con.tBirth[argsList[1]] + iBetrayalCheaters):
##                                print ("No cheaters3")
##                                self.rnf.setNewCivFlip(argsList[1])
##                                self.rnf.setTempTopLeft(rnf.tCoreAreasTL[argsList[1]])
##                                self.rnf.setTempBottomRight(rnf.tCoreAreasBR[argsList[1]])
##                                self.rnf.setBetrayalTurns(rnf.iBetrayalPeriod)
##                                self.rnf.initBetrayal()



        def onReligionFounded(self, argsList):
                'Religion Founded'
                iReligion, iFounder = argsList

                if (not gc.getPlayer(0).isPlayable() and gc.getGame().getGameTurn() == 151): #late start condition
                        return
        
                self.vic.onReligionFounded(iReligion, iFounder)
        
                if (iFounder < con.iNumPlayers):
                        self.sta.onReligionFounded(iFounder)


	def onCorporationFounded(self, argsList):
		'Corporation Founded'
		iCorporation, iFounder = argsList
		#player = PyPlayer(iFounder)
		
                if (iFounder < con.iNumPlayers):
                        self.sta.onCorporationFounded(iFounder)


                        

        def onBuildingBuilt(self, argsList):
                city, iBuildingType = argsList
                iOwner = city.getOwner()
                self.vic.onBuildingBuilt(city.getOwner(), iBuildingType)
                if (city.getOwner() < con.iNumPlayers):
                        self.sta.onBuildingBuilt(iOwner, iBuildingType, city)
                        self.com.onBuildingBuilt(iOwner, iBuildingType, city)
                self.cong.onBuildingBuilt(iOwner, iBuildingType, city)

        def onProjectBuilt(self, argsList):
                city, iProjectType = argsList
                self.vic.onProjectBuilt(city.getOwner(), iProjectType)
                if (city.getOwner() < con.iNumPlayers):
                        self.sta.onProjectBuilt(city.getOwner(), iProjectType)

        def onImprovementDestroyed(self, argsList):
                pass
                #iImprovement, iOwner, iX, iY = argsList
                #if (iOwner < con.iNumPlayers):
                #        self.sta.onImprovementDestroyed(iOwner)           
                
        def onBeginGameTurn(self, argsList):
                iGameTurn = argsList[0]

                print ("iGameTurn", iGameTurn)
                self.printDebug(iGameTurn)
                #print("minor ind", gc.getPlayer(con.iIndependent).isMinorCiv())
                #print("minor cel", gc.getPlayer(con.iCeltia).isMinorCiv())

                #debug - stop autoplay
                #gc.getActivePlayer().setStartingPlot(gc.getMap().plot(2, 2),False) #to prevent C++ exception
                #utils.makeUnit(con.iAxeman, utils.getHumanID(), (0,0), 1)
                #if (iGameTurn >= 86): #jap
                #        utils.makeUnit(con.iAxeman, utils.getHumanID(), (0,0), 1)
                #if (iGameTurn >= 82): #rome
                #        utils.makeUnit(con.iAxeman, utils.getHumanID(), (0,0), 1)
                #if (iGameTurn >= 48): #greece
                #        utils.makeUnit(con.iAxeman, utils.getHumanID(), (0,0), 1)
                
                self.rnf.checkTurn(iGameTurn)
                self.barb.checkTurn(iGameTurn)
                self.rel.checkTurn(iGameTurn)
                #self.res.checkTurn(iGameTurn)
                self.up.checkTurn(iGameTurn)
                self.aiw.checkTurn(iGameTurn)
                self.cong.checkTurn(iGameTurn)
                self.pla.checkTurn(iGameTurn)
                #self.vic.checkTurn(iGameTurn)
                self.sta.checkTurn(iGameTurn)
                self.com.checkTurn(iGameTurn)

                #Mercenaries - start

                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= gc.getActivePlayer().getBirthTurn()): #RFCRAND
                        
                        # Get the list of active players in the game
                        playerList = PyGame.getCivPlayerList()
                        
                        # Go through each of the players and deduct their mercenary maintenance amount from their gold
                        for i in range(len(playerList)):
                                playerList[i].setGold(playerList[i].getGold()-objMercenaryUtils.getPlayerMercenaryMaintenanceCost(playerList[i].getID()))
                                playerList[i].setGold(playerList[i].getGold()+objMercenaryUtils.getPlayerMercenaryContractIncome(playerList[i].getID()))
                
                        # Have some mercenaries wander away from the global mercenary pool if 
                        # g_bWanderlustMercenaries is set to true.        
                        if(g_bWanderlustMercenaries):

                                #Rhye - start (less frequent updates)
                                #wanderingMercenaryCount = gc.getGame().getMapRand().get(g_iWanderlustMercenariesMaximum, "Random Num")
                                #objMercenaryUtils.removeMercenariesFromPool(wanderingMercenaryCount)
                                teamPlayer = gc.getTeam(gc.getActivePlayer().getTeam())
                                if (not teamPlayer.isHasTech(con.iNationalism)):                     
                                        if (iGameTurn % g_bUpdatePeriod == (g_bUpdatePeriod-1)):
                                                wanderingMercenaryCount = gc.getGame().getMapRand().get(g_iWanderlustMercenariesMaximum, "Random Num") + g_iWanderlustMercenariesMinimum
                                                objMercenaryUtils.removeMercenariesFromPool(wanderingMercenaryCount)
                                #Rhye - end
                            
                                
                        # Add the mercenaries to the global mercenary pool if the g_bGameTurnMercenaryCreation 
                        # is set to true
                        if(g_bGameTurnMercenaryCreation):
                            
                                #Rhye - start (less frequent updates)
                                #objMercenaryUtils.addMercenariesToPool()                  
                                if (iGameTurn % g_bUpdatePeriod == (g_bUpdatePeriod-1)):
                                        objMercenaryUtils.addMercenariesToPool()
                                #Rhye - end                
                return 0



        def onBeginPlayerTurn(self, argsList):        
                iGameTurn, iPlayer = argsList

                #print ("PLAYER", iPlayer)
                #if (iPlayer == con.iMongolia):
                #        if (iGameTurn == self.up.getLatestRazeData(0) +1):
                #                self.up.setMongolAI()
                
                #debug - stop autoplay
                #utils.makeUnit(con.iAxeman, iAmerica, (0,0), 1)

                if (self.rnf.getDeleteMode(0) != -1):
                        self.rnf.deleteMode(iPlayer)
                        
                self.pla.checkPlayerTurn(iGameTurn, iPlayer)

                if (gc.getPlayer(iPlayer).isAlive()):
                        self.vic.checkPlayerTurn(iGameTurn, iPlayer)


                if (gc.getPlayer(iPlayer).isAlive() and iPlayer < con.iNumPlayers and gc.getPlayer(iPlayer).getNumCities() > 0):
                        self.sta.updateBaseStability(iGameTurn, iPlayer)

                if (gc.getPlayer(iPlayer).isAlive() and iPlayer < con.iNumPlayers and not gc.getPlayer(iPlayer).isHuman()):
                        self.rnf.checkPlayerTurn(iGameTurn, iPlayer) #for leaders switch

                #Mercenaries - start
        
                # This method will add mercenaries to the global mercenary pool, display the mercenary manager screen
                # and provide the logic to make the computer players think.
                player = gc.getPlayer(iPlayer)

                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= gc.getActivePlayer().getBirthTurn()): #Rhye #RFCRAND

                        # Debug code - start
                        if(g_bDebug):
                                CvUtil.pyPrint(player.getName() + " Gold: " + str(player.getGold()) + " is human: " + str(player.isHuman()))
                        # Debug code - end        
                        
                        # Add the mercenaries to the global mercenary pool if the 
                        # g_bGameTurnMercenaryCreation is set to false
                        if(not g_bGameTurnMercenaryCreation):
                                objMercenaryUtils.addMercenariesToPool()

                        # if g_bDisplayMercenaryManagerOnBeginPlayerTurn is true the the player is human
                        # then display the mercenary manager screen
                        if(g_bDisplayMercenaryManagerOnBeginPlayerTurn and player.isHuman()):
                                self.mercenaryManager.interfaceScreen()

                        # if the player is not human then run the think method
                        if(not player.isHuman()):
                            
                                #Rhye - start
                                #objMercenaryUtils.computerPlayerThink(iPlayer)                                        
                                if (player.isAlive()):
                                        if (iPlayer % (g_bAIThinkPeriod) == iGameTurn % (g_bAIThinkPeriod) and not gc.getTeam(player.getTeam()).isHasTech(con.iNationalism)):
                                                print ("AI thinking (Mercenaries)", iPlayer) #Rhye
                                                objMercenaryUtils.computerPlayerThink(iPlayer)                                                                
                                #Rhye - end
                
                        # Place any mercenaries that might be ready to be placed.
                        objMercenaryUtils.placeMercenaries(iPlayer)
                #print ("PLAYER FINE", iPlayer)
        
        
        def onEndPlayerTurn(self, argsList):

                iGameTurn, iPlayer = argsList
                #print ("END PLAYER", iPlayer)
                
                'Called at the end of a players turn'

##                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= con.tBirth[utils.getHumanID()]): #Rhye
##                
##                        iGameTurn, iPlayer = argsList
##                        
##                        player = gc.getPlayer(iPlayer)
##
##                        CyInterface().addImmediateMessage(player.getName(),"")
##                #print ("END PLAYER FINE", iPlayer)



        def onEndGameTurn(self, argsList):
            
                iGameTurn = argsList[0]
                self.sta.checkImplosion(iGameTurn)


        def onReligionSpread(self, argsList):
            
                iReligion, iOwner, pSpreadCity = argsList
                self.sta.onReligionSpread(iReligion, iOwner)             

        def onFirstContact(self, argsList):
            
                iTeamX,iHasMetTeamY = argsList
                self.rnf.onFirstContact(iTeamX, iHasMetTeamY)
                self.pla.onFirstContact(iTeamX, iHasMetTeamY)

        #Rhye - start
        def onTechAcquired(self, argsList):

                #print ("onTechAcquired", argsList)
                iPlayer = argsList[2]

                iHuman = utils.getHumanID()
                
                if (not gc.getPlayer(0).isPlayable() and gc.getGame().getGameTurn() == 151): #late start condition
                        return
                
                if (gc.getGame().getGameTurn() > gc.getPlayer(iPlayer).getBirthTurn()):  #RFCRAND                   
                        if (iPlayer == con.iGreece or \
                            iPlayer == con.iJapan or \
                            iPlayer == con.iMaya or \
                            iPlayer == con.iEngland or \
                            iPlayer == con.iGermany or \
                            iPlayer == con.iAztecs or \
                            iPlayer == con.iBabylonia):                            
                                self.vic.onTechAcquired(argsList[0], argsList[2])
                        self.cnm.onTechAcquired(argsList[2])
                
                if (gc.getPlayer(iPlayer).isAlive() and gc.getGame().getGameTurn() > gc.getPlayer(iPlayer).getBirthTurn() and iPlayer < con.iNumPlayers): #RFCRAND
                        self.sta.onTechAcquired(argsList[0], argsList[2])

                        if (gc.getGame().getGameTurn() > con.i1700AD):
                                self.aiw.forgetMemory(argsList[0], argsList[2])

                if (gc.getGame().getGameTurn() > con.i1000AD):
                        self.cong.onTechAcquired(argsList[0], argsList[2])

                if (argsList[0] == con.iAstronomy):
                        if (iPlayer == con.iSpain or \
                            iPlayer == con.iFrance or \
                            iPlayer == con.iEngland or \
                            iPlayer == con.iGermany or \
                            iPlayer == con.iVikings or \
                            iPlayer == con.iNetherlands or \
                            iPlayer == con.iPortugal):  
                                self.rnf.setAstronomyTurn(iPlayer, gc.getGame().getGameTurn())
                if (argsList[0] == con.iCompass):
                        if (iPlayer == con.iVikings):
                                gc.getMap().plot(49, 62).setTerrainType(con.iCoast, True, True)
                if (argsList[0] == con.iMedicine):
                        self.pla.onTechAcquired(argsList[0], argsList[2])
                    
                if (gc.getGame().getGameTurn() >= gc.getPlayer(iHuman).getBirthTurn()): #RFCRAND

                        if (argsList[0] == con.iNationalism):
                                if (argsList[2] == iHuman):
                                        for iLoopCiv in range (con.iNumPlayers):
                                    
                                                mercenaryDict = objMercenaryUtils.getPlayerMercenaries(iLoopCiv)
                                                mercenary = objMercenaryUtils.getHighestMaintenanceMercenary(mercenaryDict)

                                                while(mercenary != None):
                                                        # Get the mercenary with the highest maintenance cost
                                                        mercenaryDict = objMercenaryUtils.getPlayerMercenaries(iLoopCiv)
                                                        mercenary = objMercenaryUtils.getHighestMaintenanceMercenary(mercenaryDict)
                                                        # Have the computer fire the mercenary
                                                        if(mercenary != None):
                                                                objMercenaryUtils.fireMercenary(mercenary.getName(), iLoopCiv)
                                        screen = CyGInterfaceScreen( "MainInterface", CvScreenEnums.MAIN_INTERFACE )
                                        screen.hide("MercenaryManagerButton")
                                        CyInterface().addMessage(iHuman, False, con.iDuration, CyTranslator().getText("TXT_KEY_MERCENARIES_DISABLED", ()), "", 0, "", ColorTypes(con.iWhite), -1, -1, True, True)
                                
        #Rhye - end
                
                



        # This method creates a new instance of the MercenaryUtils class to be used later
        def onLoadGame(self, argsList):

                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= gc.getActivePlayer().getBirthTurn()): #Rhye #RFCRAND

                        global objMercenaryUtils

                        objMercenaryUtils = MercenaryUtils.MercenaryUtils()



        # This method will redraw the main interface once a unit is promoted. This way the 
        # gold/turn information will be updated.        
        def onUnitPromoted(self, argsList):
                'Unit Promoted'

                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= gc.getActivePlayer().getBirthTurn()): #Rhye  #RFCRAND       
                        pUnit, iPromotion = argsList
                        player = PyPlayer(pUnit.getOwner())

                        if(objMercenaryUtils.isMercenary(pUnit)):
                                CyInterface().setDirty(InterfaceDirtyBits.GameData_DIRTY_BIT, True)




        # This method will remove a mercenary unit from the game if it is killed
        def onUnitKilled(self, argsList):
                'Unit Killed'

                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= gc.getActivePlayer().getBirthTurn()): #Rhye #RFCRAND
                    
                        unit, iAttacker = argsList
                        
                        mercenary = objMercenaryUtils.getMercenary(unit.getNameNoDesc())

                        if(mercenary != None and g_bDisplayMercenaryMessages and mercenary.getBuilder() != -1 and unit.isDead()):
                                strMessage = mercenary.getName() + " has died under " + gc.getPlayer(mercenary.getOwner()).getName() + "'s service."
                                # Inform the player that the mercenary has died.
                                CyInterface().addMessage(mercenary.getBuilder(), True, 20, strMessage, "", 0, "", ColorTypes(0), -1, -1, True, True) 

                        objMercenaryUtils.removePlayerMercenary(unit)


        # This method will remove a mercenary unit from the game if it is lost
        def onUnitLost(self, argsList):
                'Unit Lost'

                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= gc.getActivePlayer().getBirthTurn()): #Rhye #RFCRAND
        
                        unit = argsList[0]
                        
                        # Debug code - start
                        if(g_bDebug):
                                CvUtil.pyPrint("lost: " + unit.getName())
                        # Debug code - end
                        
                        # If the unit being lost is a mercenary, check to see if they have been
                        # replaced by an upgraded version of themselves. If they are then save
                        # the new upgraded version of themselves and return immediately.
                        if(objMercenaryUtils.isMercenary(unit)):

                                # Debug code - start
                                if(g_bDebug):        
                                        CvUtil.pyPrint("mercenary unit lost: " + unit.getName())
                                # Debug code - end
                                        
                                # Get the active player ID
                                iPlayer = gc.getGame().getActivePlayer()
                                
                                # Get the reference of the actual player
                                pyPlayer = PyPlayer(iPlayer)

                                # Get the list of units for the player
                                unitList = pyPlayer.getUnitList()
                                        
                                # Go through the list of units to see if an upgraded version of 
                                # the unit has been added. If it exists then save it and return
                                # immediately.
                                for unit in unitList:

                                        if(unit.getUnitType() != argsList[0].getUnitType() and unit.getNameNoDesc() == argsList[0].getNameNoDesc()):

                                                # Debug code - start
                                                if(g_bDebug):        
                                                        CvUtil.pyPrint("mercenary unit upgraded: " + unit.getName())
                                                # Debug code - end
                                                
                                                tmpMerc = objMercenaryUtils.createBlankMercenary()
                                                tmpMerc.loadUnitData(unit)
                                                tmpMerc.iBuilder = -1
                                                objMercenaryUtils.saveMercenary(tmpMerc)
                                                return
                                                
                        mercenary = objMercenaryUtils.getMercenary(unit.getNameNoDesc())

                        if(mercenary != None and g_bDisplayMercenaryMessages and mercenary.getBuilder() != -1 and unit.isDead()):
                                strMessage = mercenary.getName() + " was lost under " + gc.getPlayer(mercenary.getOwner()).getName() + "'s service."
                                # Inform the player that the mercenary has died.
                                CyInterface().addMessage(mercenary.getBuilder(), True, 20, strMessage, "", 0, "", ColorTypes(0), -1, -1, True, True) 
                        unit = argsList[0]
                        
                        # Debug code - start
                        if(g_bDebug):        
                                CvUtil.pyPrint("lost??: " + unit.getNameNoDesc())        
                        # Debug code - end

                        objMercenaryUtils.removePlayerMercenary(unit)


        # This method handles the key input and will bring up the mercenary manager screen if the 
        # player has at least one city and presses the 'M' key.
        def onKbdEvent(self, argsList):
                'keypress handler - return 1 if the event was consumed'

                if ((not gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iNationalism)) and gc.getGame().getGameTurn() >= gc.getActivePlayer().getBirthTurn()): #Rhye #RFCRAND
                
                        # TO DO: REMOVE THE FOLLOWING LINE BEFORE RELEASE.
                        #gc.getPlayer(0).setGold(20000)
                        eventType,key,mx,my,px,py = argsList
                                
                        theKey=int(key)

                        if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_M) and self.eventManager.bAlt and gc.getActivePlayer().getNumCities() > 0 and gc.getActivePlayer().getCurrentEra() >= g_iStartingEra):

                                self.mercenaryManager.interfaceScreen()

                #Rhye - start debug
                eventType,key,mx,my,px,py = argsList
                        
                theKey=int(key)

                if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_B) and self.eventManager.bAlt):


                        iHuman = utils.getHumanID()
                        iGameTurn = gc.getGame().getGameTurn()
                        
                        Map = gc.getMap()
                        iGridX = Map.getGridWidth()
                        iGridY = Map.getGridHeight()
                        lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents = utils.loadRandomWorldInfo()

                        print(CyMap().getWorldSize())
                        print("lRolls", lRolls)
                        print("sealevel", CyMap().getSeaLevel())
                        print("lEurasia", lEurasia)
                        print("lIsland1", lIsland1)
                        print("lIsland2", lIsland2)
                        print("lAmerica", lAmerica)
                        

                        print("BORDER")
                        for iBorder in range (7):
                                print(iBorder,self.rnd.getBordersCoordinates(iBorder, 0))

                        lBonuses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        for iX in range(iGridX):
                                for iY in range(iGridY):
                                        if (Map.plot(iX,iY).getBonusType(-1) != -1):
                                                lBonuses[Map.plot(iX,iY).getBonusType(-1)] += 1
                                                if (Map.plot(iX,iY).getBonusType(-1) == 35):
                                                        print(iX,iY,Map.plot(iX,iY).getBonusType(-1))
                        print("BONUS")
                        # for iBonus in range(36):
                        for iBonus in range(35):
                                print(iBonus, lBonuses[iBonus])

                        #print(gc.getPlayer(con.iRome).getCurrentEra())

##                        bAmericas = True
##                        for iPlayerLoop in range(gc.getMAX_PLAYERS()):
##                                if (iPlayerLoop == iFrance or iPlayerLoop == iEngland or iPlayerLoop == iNetherlands):
##                                        apCityList = PyPlayer(iPlayerLoop).getCityList()
##
##                                        for pCity in apCityList:			
##                                                if (utils.isNewWorld(pCity.GetCy().getX(), pCity.GetCy().getY())):
##                                                #if (pCity.GetCy().area().getID() == utils.getAmericaInfo(4) or pCity.GetCy().area().getID() == utils.getAmericaInfo(5)):
##                                                        bAmericas = False
##                                                        print(iPlayerLoop, pCity.GetCy().getX(), pCity.GetCy().getY())
##                                                        break
##                                                        break
##                        print(bAmericas,iPlayerLoop)



                                
##                        print(lAmerica)
##                        print(CyMap().plot( 13, 55 ).area().getID())
##                        print(CyMap().plot( 5, 57 ).area().getID())
                        #CityNameManager.CityNameManager().sovietNames()
                        #utils.improveStartingLocation(con.iEgypt, 52, 20)
                        #self.rnd.processResourcesClusters(Map, iGridX, iGridY)

                        #self.rnd.searchAtlantis(Map, iGridX, iGridY)

                        #self.barb.foundCity(con.iIndependent, [1, -1, 120, 0], "Seoulla", iGameTurn, 2, con.iChariot, 1)


##                        for iCiv in range(iNumMajorPlayers):
##                                print(iCiv, utils.getBirthTurnModifier(iCiv), con.tBirth[iCiv]+utils.getBirthTurnModifier(iCiv))

##                        pCurrent = CyMap().plot( 27, 40 )
##                        if (pCurrent.getBonusType(-1) == -1 and not pCurrent.isWater() and not pCurrent.isPeak() and pCurrent.getFeatureType() == -1):
##                                cityPlotValue = self.barb.cityPlotValue(27, 40, 1, -1)
##                                print(cityPlotValue)
##                                bResult, temp = self.barb.checkRegion((27, 40, -1, 0))
##                                print(bResult)

                
##                        iAmericaWestX = utils.getAmericaInfo(0)
##                        iAmericaEastX = utils.getAmericaInfo(1)
##                        iAmericaSouthY = utils.getAmericaInfo(2)
##                        iAmericaNorthY = utils.getAmericaInfo(3)
##                        iNAmericaAreaID = utils.getAmericaInfo(4)
##                        iSAmericaAreaID = utils.getAmericaInfo(5)
##
                        #print(utils.getPassableAreaSize(14, 12))
##                        self.rnd.processResources(Map, iGridX, iGridY)
##                        for jj in range(37):
##                                gc.getMap().plot( 40+jj, 40 ).setBonusType(jj-1)

                        #self.rnd.addIce(Map, iGridX, iGridY)
                        


                        #gc.getPlayer(30).initUnit(28, 0, 57, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)        
##                        print(gc.getPlayer(con.iIndependent).isMinorCiv())
##                        gc.getPlayer(con.iIndependent).setMinorCiv(True)
##                        print(gc.getPlayer(con.iIndependent).isMinorCiv())
##                        print(gc.getPlayer(con.iIndependent2).isMinorCiv())
##                        gc.getPlayer(con.iIndependent2).setMinorCiv(True)
##                        print(gc.getPlayer(con.iIndependent2).isMinorCiv())
##                        #CyInterface().setDirty(InterfaceDirtyBits.InfoPane_DIRTY_BIT, True)
##                        #CyInterface().setDirty(InterfaceDirtyBits.Score_DIRTY_BIT, True)
##                        #CvMainInterface.CvMainInterface().redraw()
##                        CvMainInterface.CvMainInterface().updateScoreStrings()


                        #self.rnd.checkContinentsDistance(Map, iGridX, iGridY)

                        
##                        print("lat", CyMap().plot( 49, 50 ).getLatitude())
##                        print("real lat", CyMap().plot( 95, 67 ).getRealLatitude())
##                        print("lat", CyMap().plot( 95, 30 ).getLatitude())
##                        print("real lat", CyMap().plot( 95, 30 ).getRealLatitude())
##                        print("lat", CyMap().plot( 95, 0 ).getLatitude())
##                        print("real lat", CyMap().plot( 95, 0 ).getRealLatitude())
##                        print("lat", CyMap().plot( 58, 67 ).getLatitude())
##                        print("real lat", CyMap().plot( 58, 67 ).getRealLatitude())
##                        print("lat", CyMap().plot( 58, 30 ).getLatitude())
##                        print("real lat", CyMap().plot( 58, 30 ).getRealLatitude())
##                        print("lat", CyMap().plot( 58, 0 ).getLatitude())
##                        print("real lat", CyMap().plot( 58, 0 ).getRealLatitude())


                        #print(gc.getTeam(gc.getPlayer(con.iIndia).getTeam()).isDefensivePact(iChina))
                        
                        #gc.getMap().rebuildLandscape()
                        #self.rnd.setup()
                        #self.rnd.printBlindSettlersMap(iSpain)
                        #utils.printBlindSettlersMap(iEgypt)
                        #utils.printBlindSettlersMap(iFrance)
                        #gc.getGame().setActivePlayer(con.iFrance, False)
                        
                        #gc.getPlayer(iChina).setHandicapType(gc.getPlayer(iEgypt).getHandicapType())
                        #gc.getPlayer(iEgypt).setHandicapType(1)
                        #print("hand",gc.getPlayer(iEgypt).getHandicapType(),gc.getPlayer(iIndia).getHandicapType(),gc.getPlayer(iChina).getHandicapType(),gc.getPlayer(iGreece).getHandicapType(),gc.getGame().getHandicapType())
##                        print("hu",gc.getPlayer(iChina).isHuman(),gc.getPlayer(iEgypt).isHuman(),gc.getGame().getActivePlayer(),gc.getActivePlayer().getID())
##                        for i in range(iNumMajorPlayers):
##                                print(i,gc.getPlayer(i).getTeam())
                        #gc.getPlayer(iGermany).setLeader(con.tLeaders[iGermany][0])
                        #self.rnf.setEarlyLeaders()
                        #utils.killAndFragmentCiv(iEgypt, iIndependent, iIndependent2, iBarbarian, True)
                        
                        #print("atlantic line", int(CyMap().getGridWidth()*utils.getWorldShapeInfo(9)-1))
                        #self.rnd.checkContinentsDistance(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())
                        #print(78,21+1,Map.plot( 78, (21+1)%iGridY).isWater())
                        #for i in range(7):
                        #        print(self.rnd.getBordersCoordinates(i,0),self.rnd.getBordersCoordinates(i,1),self.rnd.getBordersCoordinates(i,2),self.rnd.getBordersCoordinates(i,3))
                        #atl=self.rnd.getWorldShapeInfo(9)*CyMap().getGridWidth()
                        
                        #pResult=Map.plotByIndex(CvMapGeneratorUtil.findStartingPlot(iEgypt, lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents, utils.isValid))
                        #print(pResult.getX(), pResult.getY())
                        #print(utils.isValid(iEgypt, 75, 32, lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls))
                        
                        #self.rnd.recordAreaIDs(Map, iGridX, iGridY)

                        #utils.resetStartingPlots(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())


                        #lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents = utils.loadRandomWorldInfo()
                        #pResult=Map.plotByIndex(CvMapGeneratorUtil.findStartingPlot(con.iChina, lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents, utils.isValid))                                       
                        #print("pResult",pResult.getX(),pResult.getY())

                        
                                                
                        #self.rnd.improveWarmRegions(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())
                        #self.rnd.openJunglePassage(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())
                        #self.rnd.smoothShapes(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())
                        #self.rnd.correctRivers(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())

                        #self.rnd.openBlockedPlots(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())
                        #self.rnd.processResources(gc.getMap(), CyMap().getGridWidth(), CyMap().getGridHeight())

                        
##                        print(gc.getMap().plot(36,11).getLatitude())
##                        print(gc.getMap().plot(22,28).getLatitude())
##                        print(gc.getMap().plot(63,23).area().getID())
##                        print(utils.getIsland2Info(4))
##                        print(gc.getMap().plot(75,27).area().getID())
##                        print(gc.getMap().plot(72,5).area().getID())
##                        print(gc.getMap().plot(0,0).area().getID())
                        
##                        iPlayer = 10
##                        for x in range(CyMap().getGridWidth()):
##                                for y in range(CyMap().getGridHeight()):
##                                        #pCurrent = CyMap().plot( x, y )                                        
##                                        player = gc.getPlayer(iPlayer)
##                                        #print(iPlayer, x, y, player.AI_blindSettlersMap(x,y,False))
##                                        print(iPlayer, x, y, player.AI_foundValue(x,y,-1,False))
##                                        print(iPlayer, x, y, utils.blindSettlersMap(iPlayer, x, y))
##                        for i in range(6):
##                                print(iPlayer, gc.getPlayer(iPlayer).getSettlersCoords(i))
##                                print(iPlayer, gc.getPlayer(iPlayer).getSettlersModifiers(i))
                        
##                        print(gc.getPlayer(10).getSettlersCoords(5))
##                        print(gc.getPlayer(10).getSettlersModifiers(5))
##                        print(utils.blindSettlersMap(1, 68, 10))
##                        print(utils.blindSettlersStartingMap(1, 36, 11))
##                        print(utils.blindSettlersStartingMap(1, 34, 29))
                        
                        
##                        iTotSettleable = 0
##                        for x in range(CyMap().getGridWidth()):
##                                for y in range(CyMap().getGridHeight()):
##                                        #pCurrent = Map.plot( x, y )
##                                        player = gc.getPlayer(0)
##                                        if (player.canFound(x,y)):
##                                                iTotSettleable += 1
##                        print ("Settleable:", iTotSettleable)
##                        print ("Land:", gc.getMap().getLandPlots())

##                        gc.getMap().plot(27, 30).setFeatureType(-1, 0)
##                        gc.getMap().plot(28, 31).setFeatureType(-1, 0)
##                        gc.getMap().plot(31, 13).setPlotType(PlotTypes.PLOT_HILLS, True, True)

                        #self.com.decay(con.iGermany)

                        #print("fake20",utils.getFakeRandNum(20,''))
                        #print("fake21",utils.getFakeRandNum(21,''))      
                        
                        #self.data.setupScriptData()
                        #gc.getGame().setWinner(con.iEgypt, 0)
                        #if (len(lLeaders[iDeadCiv]) > 1):
                        #gc.getTeam(gc.getPlayer(con.iIndia).getTeam()).signOpenBorders(con.iChina)
                        #print ("CC1", gc.getTeam(gc.getPlayer(con.iIndia).getTeam()).canContact(con.iEgypt))
                        #print ("ME1", gc.getTeam(gc.getPlayer(con.iIndia).getTeam()).isHasMet(con.iEgypt))
                        #gc.getTeam(gc.getPlayer(con.iJapan).getTeam()).cutContact(con.iChina)
                        #gc.getTeam(gc.getPlayer(con.iChina).getTeam()).cutContact(con.iJapan)
                        #print ("CC2", gc.getTeam(gc.getPlayer(con.iIndia).getTeam()).canContact(con.iEgypt))
                        #print ("ME2", gc.getTeam(gc.getPlayer(con.iIndia).getTeam()).isHasMet(con.iEgypt))
                        #for i in range (con.iNumPlayers):
                        #        gc.getTeam(gc.getPlayer(con.iInca).getTeam()).cutContact(i)
                        #gc.getTeam(gc.getPlayer(con.iChina).getTeam()).setVassal(con.iJapan, True, True)
                        #gc.getGame().changePlayer(con.iChina, 0, 22, con.iChina, False, True)
                        #gc.getPlayer(con.iBabylonia).setLeader(24)
                        #gc.getPlayer(con.iEgypt).changeGold(3000)
                        #gc.getMap().plot(72, 32).getPlotCity().changeBuildingProduction(con.iBroadway,639)
                        #print ("CC2", gc.getTeam(gc.getPlayer(con.iEgypt).getTeam()).canContact(con.iNative))
                        #newCivDesc = CyTranslator().getText("TXT_KEY_NAM_CHI1", ())
##                        newCivDesc = "TXT_KEY_NAM_CHI1"
##                        newDesc = newCivDesc.encode('latin-1')
##                        gc.getPlayer(con.iChina).setCivDescription(newDesc)
##                        print (gc.getPlayer(con.iChina).getCivilizationDescription(0), gc.getPlayer(con.iChina).getCivilizationDescriptionKey(), gc.getPlayer(con.iChina).getCivilizationAdjective(0), gc.getPlayer(con.iChina).getCivilizationAdjectiveKey())
##                        print (gc.getPlayer(con.iIndia).getCivilizationDescription(0), gc.getPlayer(con.iIndia).getCivilizationDescriptionKey(), gc.getPlayer(con.iIndia).getCivilizationAdjective(0), gc.getPlayer(con.iIndia).getCivilizationAdjectiveKey())
##                        self.rnf.showPopup(7614, CyTranslator().getText("TXT_KEY_NEWCIV_TITLE", ()), CyTranslator().getText("TXT_KEY_NEWCIV_MESSAGE", (gc.getPlayer(con.iChina).getCivilizationDescriptionKey(),)), (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), CyTranslator().getText("TXT_KEY_POPUP_NO", ())))

                        #gc.getTeam(gc.getPlayer(con.iChina).getTeam()).setVassal(con.iArabia, True, True)

                        #invasion attempt
                        #if (iGameTurn == 100):
                        #        utils.makeUnit(con.iAxeman, iGermany, con.tCapitals[iGermany], 3)
                        #        utils.makeUnit(con.iSwordsman, iGermany, con.tCapitals[iGermany], 3)
                        
                        #for iCiv in range(iNumPlayers):
                        #        for pyCity in PyPlayer(iCiv).getCityList():
                        #                print (pyCity.GetCy().getName())
                        #print(gc.getGame().getCircumnavigated())

##                        print(utils.isNewWorld(67,7),CyMap().plot(67,7).area().getID(),CyMap().plot(67,7).area().getNumTiles())
##                        print(utils.isNewWorld(47,9),CyMap().plot(47,9).area().getID(),CyMap().plot(47,9).area().getNumTiles())
##                        print(utils.isNewWorld(9,8),CyMap().plot(9,8).area().getID(),CyMap().plot(9,8).area().getNumTiles())
##                        print(CyMap().findBiggestArea(False).getID())
##                        print(utils.isNewWorld(gc.getPlayer(iEngland).getStartingPlot().getX(), gc.getPlayer(iEngland).getStartingPlot().getY()))
##                        for i in range(iNumMajorPlayers):
##                                print(i,gc.getPlayer(i).getSettlersCoords(0),gc.getPlayer(i).getSettlersCoords(1),gc.getPlayer(i).getSettlersCoords(2),gc.getPlayer(i).getSettlersCoords(3),gc.getPlayer(i).getSettlersCoords(4),gc.getPlayer(i).getSettlersCoords(5),gc.getPlayer(i).getSettlersCoords(6))
##                        for i in range(iNumMajorPlayers):
##                                print(i,gc.getPlayer(i).getSettlersModifiers(0),gc.getPlayer(i).getSettlersModifiers(1),gc.getPlayer(i).getSettlersModifiers(2),gc.getPlayer(i).getSettlersModifiers(3),gc.getPlayer(i).getSettlersModifiers(4),gc.getPlayer(i).getSettlersModifiers(5),gc.getPlayer(i).getSettlersModifiers(6))
                        #pPlot = gc.getMap().plot( 9, 56 )
                        #print(utils.getPassableAreaSize(97, 44, 4))
                        #self.rnd.processEarthResources(Map, iGridX, iGridY)

                        
                        #debug - kills every unit
                        #for x in range(40, 123):
                        #        for y in range(0, 67):
                        #                pCurrent = gc.getMap().plot( x, y )
                        #                if (pCurrent.getNumUnits() > 0):
                        #                        for i in range (pCurrent.getNumUnits()):
                        #                                unit = pCurrent.getUnit(0)
                        #                                unit.kill(False, con.iBarbarian)


##                        if (gc.getPlayer(utils.getHumanID()).getNumCities() > 1):
##                                CyInterface().addImmediateMessage(CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR_HUMAN", ()), "")
##                                utils.killAndFragmentCiv(utils.getHumanID(), True)
##                                utils.setStability(utils.getHumanID(), -15)


                        #self.pla.setGenericPlagueDates(0, 96)
                        #self.pla.spreadPlague(con.iJapan)
                        #self.pla.stopPlague(con.iJapan)
                        #self.pla.infectCity(utils.getRandomCity(con.iJapan))
                        #print ("Countdown", self.pla.getPlagueCountdown( con.iJapan ))
                    
                        
                        #utils.killAndFragmentCiv(con.iEngland, iIndependent, iIndependent2, -1, False)
                        #self.rnf.resurrection(302)
                        
                        #utils.killAndFragmentCiv(con.iRome, iIndependent, iIndependent2, -1, True)
                        #gc.getGame().setActivePlayer(con.iSpain, False)
                        #teamEgypt.changeResearchProgress(con.iNationalism, 3299, iEgypt)
                        #teamAztecs.changeResearchProgress(con.iSteel, 3399, iAztecs)
                        
                        #self.sta.normalization(200)
                        #gc.getGame().setActivePlayer(con.iNetherlands, False)
                        #gc.getPlayer(con.iPortugal).changeGold(200)
                        
                        #CyInterface().addImmediateMessage(CyTranslator().getText("TXT_KEY_PLAGUE_SPREAD_CITY", ()), "")
                        #CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, CyTranslator().getText("TXT_KEY_EMBASSY_ESTABLISHED", (gc.getPlayer(con.iRussia).getCivilizationAdjectiveKey(),)) + " " + "Citta di prova", "", 0, "", ColorTypes(con.iWhite), -1, -1, True, True)

                        #CyInterface().addMessage(utils.getHumanID(), True, 5, CyTranslator().getText("TXT_KEY_CONGRESS_NOTIFY_YES2", ()), "", 0, "", ColorTypes(100), -1, -1, True, True)
##                        for i in range(128):
##                                CyInterface().addMessage(utils.getHumanID(), True, 1, "i", "", 0, "", ColorTypes(i), -1, -1, False, True)
##                                if (i % 10 == 0):
##                                         CyInterface().addMessage(utils.getHumanID(), True, 1, "10", "", 0, "", ColorTypes(0), -1, -1, False, True)
                        #print ("vic", self.vic.getNumSinks())

                        #dummy, plotList = utils.squareSearch( (29,28), (31,31), utils.outerInvasion, [])
                        #print (plotList)
                        #utils.setStability(con.iChina, -25)
                        
                        #city = gc.getMap().plot( 79, 40 ).getPlotCity() 
                        #self.pla.infectCity(city)
                        #self.pla.spreadPlague(con.iPersia)
                        #self.pla.processPlague(con.iPersia)

                        #city = gc.getMap().plot( 90, 40 ).getPlotCity()
                        #print ("9040", city.getCulture(con.iIndia), 4000 + 2000*gc.getPlayer(con.iIndia).getCurrentEra())

                        
                        #CyInterface().DoSoundtrack("AS2D_R_F_C")
                        #if (gc.getPlayer(con.iNetherlands).countOwnedBonuses(con.iSpices) + gc.getPlayer(con.iNetherlands).getBonusImport(con.iSpices) >= 5):
                        #        self.vic.setGoal(iNetherlands, 2, 0)

##                        for iCiv in range(iNumMajorPlayers):
##                                print(gc.getPlayer(iCiv).getBirthTurn(),con.tBirth[iCiv],con.tCapitals[iCiv],con.tNormalAreasTL[iCiv])

                        #utils.setLastRecordedStabilityStuff(2, 0)
                        #utils.setLastRecordedStabilityStuff(1, 40)

##                        #print (CyGame().getCurrentLanguage())
##                        popup = PyPopup.PyPopup()
##                        popup.setHeaderString(CyTranslator().getText("TXT_KEY_EXILE_TITLE", ()))          
##                        popup.setBodyString( CyTranslator().getText("TXT_KEY_EXILE_TEXT", (gc.getPlayer(con.iGermany).getCivilizationAdjectiveKey(), gc.getPlayer(con.iSpain).getCivilizationShortDescription(0))))
####                        popup.setHeaderString(CyTranslator().getText("TXT_KEY_ESCAPE_TITLE", ()))          
####                        popup.setBodyString( CyTranslator().getText("TXT_KEY_ESCAPE_TEXT", (gc.getPlayer(con.iGermany).getCivilizationAdjectiveKey(),)))
##                        popup.launch()
##
##                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration/2, ("XXX" + " " + \
##                                                                                   CyTranslator().getText("TXT_KEY_CONGRESS_NOTIFY_YES", (gc.getPlayer(con.iSpain).getCivilizationAdjectiveKey(),))), \
##                                                                                   "", 0, "", ColorTypes(con.iCyan), -1, -1, True, True)
##                        self.rnf.newCivPopup(con.iSpain)
##
##                        self.rnf.showPopup(7622, CyTranslator().getText("TXT_KEY_REBELLION_TITLE", ()), \
##                               CyTranslator().getText("TXT_KEY_REBELLION_TEXT", (gc.getPlayer(con.iGermany).getCivilizationAdjectiveKey(),)), \
##                               (CyTranslator().getText("TXT_KEY_POPUP_YES", ()), \
##                                CyTranslator().getText("TXT_KEY_POPUP_NO", ())))
##
##                        CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, \
##                                                                                 CyTranslator().getText("TXT_KEY_STABILITY_GREAT_DEPRESSION_INFLUENCE", (gc.getPlayer(con.iSpain).getCivilizationDescription(0),)), \
##                                                                                 "", 0, "", ColorTypes(con.iOrange), -1, -1, True, True)
##
####                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, \
####                                                        (CyTranslator().getText("TXT_KEY_INDEPENDENCE_TEXT", (gc.getPlayer(con.iGermany).getCivilizationAdjectiveKey(),))), "", 0, "", ColorTypes(con.iGreen), -1, -1, True, True)
##
                        #print ("ERA", gc.getInfoTypeForString("ERA_CLASSICAL"))
##                        for iEuroCiv in range(iNumPlayers):
##                                if (iEuroCiv in con.lCivGroups[0]):
##                                        if (not self.vic.checkNotOwnedArea_Skip(iEuroCiv, (24, 3), (43, 32), (32,14), (43,30))):
##                                                CyInterface().addImmediateMessage(CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR_HUMAN", ()), "")


                        
                        pass


                if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_N) and self.eventManager.bAlt):

                        print("ALT-N")
                        
                        self.printEmbassyDebug()
                        self.printPlotsDebug()
                        self.printStabilityDebug()
                        self.printBirthDebug()


                if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_C) and self.eventManager.bAlt and self.eventManager.bShift):
                        print("SHIFT-ALT-C") #picks a dead civ so that autoplay can be started with game.AIplay xx
                        iDebugDeadCiv = iCarthage #default iCarthage: often dead in 3000BC
                        gc.getTeam(gc.getPlayer(iDebugDeadCiv).getTeam()).setHasTech(con.iCalendar, True, iDebugDeadCiv, False, False)
                        utils.makeUnit(con.iAxeman, iDebugDeadCiv, (0,0), 1)
                        gc.getGame().setActivePlayer(iDebugDeadCiv, False)
                        gc.getPlayer(iDebugDeadCiv).setPlayable(True)

                if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_E) and self.eventManager.bAlt and self.eventManager.bShift):
                        print("SHIFT-ALT-E") #picks a dead civ so that autoplay can be started with game.AIplay xx
                        iDebugDeadCiv = iEthiopia #default iEthiopia: always dead in 600AD
                        gc.getTeam(gc.getPlayer(iDebugDeadCiv).getTeam()).setHasTech(con.iCalendar, True, iDebugDeadCiv, False, False)
                        utils.makeUnit(con.iAxeman, iDebugDeadCiv, (0,0), 1)
                        gc.getGame().setActivePlayer(iDebugDeadCiv, False)
                        gc.getPlayer(iDebugDeadCiv).setPlayable(True)
                        
                if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_Q) and self.eventManager.bAlt and self.eventManager.bShift):
                        print("SHIFT-ALT-Q") #enables squatting
                        self.rnf.setCheatMode(True);
                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "EXPLOITER!!! ;)", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)

                #Stability Cheat
                if self.rnf.getCheatMode() and theKey == int(InputTypes.KB_S) and self.eventManager.bAlt and self.eventManager.bShift:
                        print("SHIFT-ALT-S") #boosts stability by +10 for the human player
                        utils.setStability(utils.getHumanID(), utils.getStability(utils.getHumanID())+10)
                        
                #RFCRAND
                if ( eventType == self.EventKeyDown and theKey == int(InputTypes.KB_W) and self.eventManager.bAlt and self.eventManager.bShift):
                        print("SHIFT-ALT-W") #hints for the new world
                        if (gc.getTeam(gc.getActivePlayer().getTeam()).isHasTech(con.iCompass)):
                                if (CyMap().plot(15, 0).getPlotType() == PlotTypes.PLOT_LAND):
                                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "New World is bottom left", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
                                if (CyMap().plot(16, 0).getPlotType() == PlotTypes.PLOT_LAND):
                                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "New World is top left", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
                                if (CyMap().plot(17, 0).getPlotType() == PlotTypes.PLOT_LAND):
                                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "New World is bottom centre", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
                                if (CyMap().plot(18, 0).getPlotType() == PlotTypes.PLOT_LAND):
                                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "New World is top centre", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
                                if (CyMap().plot(19, 0).getPlotType() == PlotTypes.PLOT_LAND):
                                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "New World is bottom right", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
                                if (CyMap().plot(20, 0).getPlotType() == PlotTypes.PLOT_LAND):
                                        CyInterface().addMessage(utils.getHumanID(), True, con.iDuration, "New World is top right", "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)

                #Rhye - end debug
        
        #Mercenaries - end



        #Rhye - start
        def printDebug(self, iGameTurn):

                
                if (iGameTurn %50 == 1):
                        self.printEmbassyDebug()

                if (iGameTurn %20 == 0):
                        self.printPlotsDebug()

                if (iGameTurn %10 == 0): 
                        self.printStabilityDebug()



        def printBirthDebug(self):

                print("Birth turn:")
                for i in range(con.iNumPlayers):
                        print (gc.getPlayer(i).getCivilizationShortDescription(0), gc.getPlayer(i).getBirthTurn())


                        
        def printPlotsDebug(self):

            
                #countTotalUnits
                iTotal = 0
                iTotalCities = 0
##                lType = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##                lOwner = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                
                #lOwnerLongbow = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #         0, 0, 0, 0, 0, 0, 0]
                #lOwnerCannon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #         0, 0, 0, 0, 0, 0, 0]
##                lPlotOwner = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                              0, 0]
                #lPlotOwner2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #              0, 0]
##                lCityOwner2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
##                              0, 0]
                #lCityOwner_sb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                #              0, 0]
                for x in range(0, CyMap().getGridWidth()):
                        for y in range(0, CyMap().getGridHeight()):
                                pCurrent = gc.getMap().plot( x, y )
                                iTotal += pCurrent.getNumUnits()
##                                if (pCurrent.getNumUnits() > 0):
##                                        for i in range (pCurrent.getNumUnits()):
##                                                unit = pCurrent.getUnit(i)
##                                                lType[unit.getUnitType()] += 1
##                                                lOwner[unit.getOwner()] += 1
                                                #if (unit.getUnitType() == con.iLongbowman):
                                                #       lOwnerLongbow[unit.getOwner()] += 1
                                                #if (unit.getUnitType() == con.iCannon):
                                                #       lOwnerCannon[unit.getOwner()] += 1

                                if ( pCurrent.isCity()):
                                        iTotalCities += 1
                                        
                print ("TOTAL UNITS", iTotal)  
                print ("TOTAL CITIES", iTotalCities)

##                print ("Unit types")
##                for i in range (len(lType)):
##                        print (i, lType[i])
##                print ("Unit owners")
##                for i in range (len(lOwner)):
##                        print (i, lOwner[i])
                #print ("LB owners")
                #for j in range (len(lOwnerLongbow)):
                #        print (j, lOwnerLongbow[j])               
                #print ("Cannon owners")
                #for j in range (len(lOwnerCannon)):
                #        print (j, lOwnerCannon[j])               
        
                pass

        def printEmbassyDebug(self):
                for i in range(con.iNumPlayers):
                        if (gc.getPlayer(i).isAlive()):
                                apCityList = PyPlayer(i).getCityList()
                                print (gc.getPlayer(i).getCivilizationShortDescription(0), gc.getTeam(gc.getPlayer(i).getTeam()).isHasTech(con.iCivilService), gc.getTeam(gc.getPlayer(i).getTeam()).isHasTech(con.iPaper))                                                                                     
                                for j in range(con.iNumPlayers):
                                        if (gc.getTeam(gc.getPlayer(i).getTeam()).canContact(j)):   
                                                bEmb = False
                                                for pCity in apCityList:
                                                        city = pCity.GetCy()
                                                        if (city.hasBuilding(con.iNumBuildingsPlague+j)):
                                                                print (city.getName(), "HAS EMBASSY", gc.getPlayer(j).getCivilizationAdjective(0))
                                                                bEmb = True
                                                                break
                                                if (bEmb == False):
                                                        print ("NO EMBASSY", gc.getPlayer(j).getCivilizationAdjective(0))


        def printStabilityDebug(self):
                print ("Stability")
                for iCiv in range(con.iNumPlayers):
                        if (gc.getPlayer(iCiv).isAlive()):
                                print ("Base:", utils.getBaseStabilityLastTurn(iCiv), "Modifier:", utils.getStability(iCiv)-utils.getBaseStabilityLastTurn(iCiv), "Total:", utils.getStability(iCiv), "civic", gc.getPlayer(iCiv).getCivics(5), gc.getPlayer(iCiv).getCivilizationDescription(0))
                        else:
                                print ("dead", iCiv)
                for i in range(con.iNumStabilityParameters):
                        print("Parameter", i, utils.getStabilityParameters(i))
                #for i in range (len(lPlotOwner)):
                for i in range(con.iNumPlayers):
                        print (gc.getPlayer(i).getCivilizationShortDescription(0), "PLOT OWNERSHIP ABROAD:", self.sta.getOwnedPlotsLastTurn(i), "CITY OWNERSHIP LOST:", self.sta.getOwnedCitiesLastTurn(i) )
