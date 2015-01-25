# Rhye's and Fall of Civilization - Utilities

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
import cPickle as pickle

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

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


iSettler = con.iSettler

iNumBuildingsPlague = con.iNumBuildingsPlague
iNumBuildingsEmbassy = con.iNumBuildingsEmbassy

tCol = (
'255,255,255',
'200,200,200',
'150,150,150',
'128,128,128')

class RFCUtils:

        #Rise and fall, stability
        def getLastTurnAlive( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lLastTurnAlive'][iCiv]

        def setLastTurnAlive( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lLastTurnAlive'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getCivsWithNationalism( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iCivsWithNationalism']

        #Victory
        def getGoal( self, i, j ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGoals'][i][j]

        def setGoal( self, i, j, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGoals'][i][j] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        #Stability
        
        def getTempFlippingCity( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['tempFlippingCity']

        def setTempFlippingCity( self, tNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['tempFlippingCity'] = tNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) ) 

        def getStability( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lStability'][iCiv]

        def setStability( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lStability'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getBaseStabilityLastTurn( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lBaseStabilityLastTurn'][iCiv]

        def setBaseStabilityLastTurn( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lBaseStabilityLastTurn'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getStabilityParameters( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lStabilityParameters'][iParameter]

        def setStabilityParameters( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lStabilityParameters'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getGreatDepressionCountdown( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGreatDepressionCountdown'][iCiv]

        def setGreatDepressionCountdown( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGreatDepressionCountdown'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                                
        def getLastRecordedStabilityStuff( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lLastRecordedStabilityStuff'][iParameter]

        def setLastRecordedStabilityStuff( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lLastRecordedStabilityStuff'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        #Plague
        def getPlagueCountdown( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lPlagueCountdown'][iCiv]

        def setPlagueCountdown( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lPlagueCountdown'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        #Communications
        def getSeed( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iSeed']

        #RFCRAND
        def getWorldShapeInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lWorldShapeInfo'][iParameter]

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

        def getAfricaInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lAfricaInfo'][iParameter]

        def getAmericaInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lAmericaInfo'][iParameter]

        def getIsland1Info( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lIsland1Info'][iParameter]

        def getIsland2Info( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lIsland2Info'][iParameter]
            

        def getEmptyContinentInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lEmptyContinentInfo'][iParameter]

        def setEmptyContinentInfo( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lEmptyContinentInfo'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getRandomContinents( self, iContinent ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lRandomContinents'][iContinent]

        def setRandomContinents( self, iContinent, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lRandomContinents'][iContinent] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getInThisGame( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lInThisGame'][iCiv]

        def setInThisGame( self, iCiv, bNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lInThisGame'][iCiv] = bNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )       

        def getJerusalemLocation( self, iCoord ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lJerusalemLocation'][iCoord]

        def setJerusalemLocation( self, iCoord, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lJerusalemLocation'][iCoord] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )    

        def getBirthTurnModifier( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lBirthTurnModifier'][iCiv]

        def setBirthTurnModifier( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lBirthTurnModifier'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )   

                
        def getLongSeed( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iLongSeed']

        def setLongSeed( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iLongSeed'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

                
#######################################

        #Stability, RiseNFall, CvFinanceAdvisor
        def setParameter(self, iPlayer, iParameter, bPreviousAmount, iAmount):
            if (gc.getPlayer(iPlayer).isHuman()):
                    if (bPreviousAmount):
                            self.setStabilityParameters(iParameter, self.getStabilityParameters(iParameter) + iAmount)
                    else:
                            self.setStabilityParameters(iParameter, 0 + iAmount)

        def setStartingStabilityParameters(self, iCiv):
                iHandicap = gc.getGame().getHandicapType()

                for i in range(con.iNumStabilityParameters):
                        self.setStabilityParameters(i, 0)

                #RFCRAND
                if (iHandicap == 0):
                        self.setStability(iCiv, 25)
                        self.setParameter(iCiv, con.iParCitiesE, True, 5)
                        self.setParameter(iCiv, con.iParCivicsE, True, 5)
                        self.setParameter(iCiv, con.iParDiplomacyE, True, 5)
                        self.setParameter(iCiv, con.iParEconomyE, True, 5)
                        self.setParameter(iCiv, con.iParExpansionE, True, 5) 
                elif (iHandicap == 1):
                        self.setStability(iCiv, 15)
                        self.setParameter(iCiv, con.iParCitiesE, True, 3)
                        self.setParameter(iCiv, con.iParCivicsE, True, 3)
                        self.setParameter(iCiv, con.iParDiplomacyE, True, 3)
                        self.setParameter(iCiv, con.iParEconomyE, True, 3)
                        self.setParameter(iCiv, con.iParExpansionE, True, 3) 
                elif (iHandicap == 2):
                        self.setStability(iCiv, 5)
                        self.setParameter(iCiv, con.iParCitiesE, True, 1)
                        self.setParameter(iCiv, con.iParCivicsE, True, 1)
                        self.setParameter(iCiv, con.iParDiplomacyE, True, 1)
                        self.setParameter(iCiv, con.iParEconomyE, True, 1)
                        self.setParameter(iCiv, con.iParExpansionE, True, 1) 
                elif (iHandicap == 3):
                        self.setStability(iCiv, -5)
                        self.setParameter(iCiv, con.iParCitiesE, True, -1)
                        self.setParameter(iCiv, con.iParCivicsE, True, -1)
                        self.setParameter(iCiv, con.iParDiplomacyE, True, -1)
                        self.setParameter(iCiv, con.iParEconomyE, True, -1)
                        self.setParameter(iCiv, con.iParExpansionE, True, -1) 
                elif (iHandicap == 4):
                        self.setStability(iCiv, -15)
                        self.setParameter(iCiv, con.iParCitiesE, True, -3)
                        self.setParameter(iCiv, con.iParCivicsE, True, -3)
                        self.setParameter(iCiv, con.iParDiplomacyE, True, -3)
                        self.setParameter(iCiv, con.iParEconomyE, True, -3)
                        self.setParameter(iCiv, con.iParExpansionE, True, -3) 




        #CvFinanceAdvisor
        def getParCities(self):
            if (self.getStabilityParameters(con.iParCitiesE) > 7):
                    return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParCitiesE) < -7):
                    return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE)

        def getParCivics(self):
            if (self.getStabilityParameters(con.iParCivicsE) > 7):
                    return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParCivicsE) < -7):
                    return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE)

        def getParDiplomacy(self):
            if (self.getStabilityParameters(con.iParDiplomacyE) > 7):
                    return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParDiplomacyE) < -7):
                    return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE)

                
        def getParEconomy(self):
            #print ("ECO", self.getStabilityParameters(con.iParEconomy3), self.getStabilityParameters(con.iParEconomy1), self.getStabilityParameters(con.iParEconomyE))
            if (self.getStabilityParameters(con.iParEconomyE) > 7):
                    return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParEconomyE) < -7):
                    return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE)
                
        def getParExpansion(self):
            if (self.getStabilityParameters(con.iParExpansionE) > 7):
                    return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParExpansionE) < -7):
                    return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE)

        def getArrow(self, iParameter):
            if (iParameter == 0):
                    if (self.getStability(self.getHumanID()) >= self.getLastRecordedStabilityStuff(iParameter) + 6):
                            return 1
                    elif (self.getStability(self.getHumanID()) <= self.getLastRecordedStabilityStuff(iParameter) - 6):
                            return -1
                    else:
                            return 0
            else:
                    if (iParameter == 1):
                            iNewValue = self.getParCities()
                    elif (iParameter == 2):
                            iNewValue = self.getParCivics()
                    elif (iParameter == 3):
                            iNewValue = self.getParEconomy()
                    elif (iParameter == 4):
                            iNewValue = self.getParExpansion()
                    elif (iParameter == 5):
                            iNewValue = self.getParDiplomacy()
                    if (iNewValue >= self.getLastRecordedStabilityStuff(iParameter) + 4):
                            return 1
                    elif (iNewValue <= self.getLastRecordedStabilityStuff(iParameter) - 4):
                            return -1
                    else:
                            return 0

        #Victory
        def countAchievedGoals(self, iPlayer):
                iResult = 0
                for j in range(3):                        
                        #iTemp = self.getGoal(iPlayer, j)
                        #if (iTemp < 0):
                        #        iTemp = 0
                        #iResult += iTemp
                        if (self.getGoal(iPlayer, j) == 1):
                                iResult += 1
                return iResult
                
        def getGoalsColor(self, iPlayer): #by CyberChrist
                iCol = 0
                for j in range(3):
                        if (self.getGoal(iPlayer, j) == 0):
                                iCol += 1
                return tCol[iCol]

            
        #Plague
        def getRandomCity(self, iPlayer):
                cityList = []
                apCityList = PyPlayer(iPlayer).getCityList()
                for pCity in apCityList:
                        cityList.append(pCity.GetCy())
                if (len(cityList)):           
                        return cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
                else:
                        return -1                   
                                            

        def isMortalUnit(self, unit):
                if (unit.isHasPromotion(42)): #leader
                        if (not gc.getPlayer(unit.getOwner()).isHuman()):
                                return False
                        else:
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 50):
                                        return False              
                iUnitType = unit.getUnitType()
                if (iUnitType <= con.iKhmerBallistaElephant \
                     and iUnitType != con.iSettler and iUnitType != con.iMechanizedInfantry):
                        return True
                if (iUnitType >= con.iCatapult and iUnitType <= con.iMobileArtillery ):
                        if (gc.getPlayer(unit.getOwner()).isHuman()):
                                return True
                        else:
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 30):
                                        return True
                if (iUnitType == con.iSettler ):
                        if (gc.getPlayer(unit.getOwner()).isHuman()):
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 50):
                                        return True
                        else:
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 20):
                                        return True
                return False

        def isDefenderUnit(self, unit):
                iUnitType = unit.getUnitType()
                if (iUnitType >= con.iSpearman and iUnitType <= con.iChinaChokonu):
                        return True
                return False

        #AIWars
        def checkUnitsInEnemyTerritory(self, iCiv1, iCiv2): 
                unitList = PyPlayer(iCiv1).getUnitList()
                if(len(unitList)):
                        for unit in unitList:
                                iX = unit.getX()
                                iY = unit.getY()
                                if (gc.getMap().plot( iX, iY ).getOwner() == iCiv2):
                                        return True
                return False

        #AIWars
        def restorePeaceAI(self, iMinorCiv, bOpenBorders):
                teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
                for iActiveCiv in range( iNumActivePlayers ):
                        if (gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman()):
                                if (teamMinor.isAtWar(iActiveCiv)):
                                        bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
                                        bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)                                                                  
                                        if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):            
                                                teamMinor.makePeace(iActiveCiv)
                                                if (bOpenBorders):
                                                        teamMinor.signOpenBorders(iActiveCiv)
        #AIWars
        def restorePeaceHuman(self, iMinorCiv, bOpenBorders): 
                teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
                for iActiveCiv in range( iNumActivePlayers ):
                        if (gc.getPlayer(iActiveCiv).isHuman()):
                                if (gc.getPlayer(iActiveCiv).isAlive()):
                                        if (teamMinor.isAtWar(iActiveCiv)):
                                                bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
                                                bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)                                                                  
                                                if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):            
                                                        teamMinor.makePeace(iActiveCiv)
                                return
        #AIWars
        def minorWars(self, iMinorCiv):
                teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
                if (gc.getPlayer(iMinorCiv).isAlive()):
                        apCityList = PyPlayer(iMinorCiv).getCityList() #RFCRAND
                        for pCity in apCityList:
                                city = pCity.GetCy()
                                x = city.getX()
                                y = city.getY()
                                for iActiveCiv in range( iNumActivePlayers ):
                                        if (gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman()):
                                                #RFCRAND
                                                #if (gc.getPlayer(iActiveCiv).getSettlersMaps( CyMap().getGridHeight()-1-y, x ) >= 90):
                                                if (self.blindSettlersMap(iActiveCiv, x, y) >= 120):
                                                        if (not teamMinor.isAtWar(iActiveCiv)):
                                                                print ("Minor war", city.getName(), gc.getPlayer(iActiveCiv).getCivilizationAdjective(0))
                                                                teamMinor.declareWar(iActiveCiv, False, WarPlanTypes.WARPLAN_LIMITED)
                                                                



            
        #RiseAndFall, Stability
        def calculateDistance(self, x1, y1, x2, y2):
                dx = abs(x2-x1)
                dy = abs(y2-y1)
                return max(dx, dy)


            
        #RiseAndFall
        def debugTextPopup(self, strText):
                popup = Popup.PyPopup()
                popup.setBodyString( strText )
                popup.launch()		

        #RiseAndFall
        def updateMinorTechs( self, iMinorCiv, iMajorCiv):                
                for t in range(con.iNumTechs):
                        if (gc.getTeam(gc.getPlayer(iMajorCiv).getTeam()).isHasTech(t)):
                                    gc.getTeam(gc.getPlayer(iMinorCiv).getTeam()).setHasTech(t, True, iMinorCiv, False, False)


        #RiseAndFall, Religions, Congresses, UniquePowers
        def makeUnit(self, iUnit, iPlayer, tCoords, iNum): #by LOQ
                'Makes iNum units for player iPlayer of the type iUnit at tCoords.'
                #print(gc.getGame().getGameTurn(),"MAKEUNIT",iUnit, iPlayer, tCoords, iNum)
                #RFCRAND
                if (iUnit != None):
                        for i in range(iNum):
                                player = gc.getPlayer(iPlayer)
                                player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

        #RiseAndFall, Religions, Congresses
        def getHumanID(self):
##                for iCiv in range(iNumPlayers):
##                        if (gc.getPlayer(iCiv).isHuman()):
##                                return iCiv     
                return gc.getGame().getActivePlayer()



        #RiseAndFall
        def flipUnitsInCityBefore(self, tCityPlot, iNewOwner, iOldOwner):
                #print ("tCityPlot Before", tCityPlot)
                plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                city = plotCity.getPlotCity()    
                iNumUnitsInAPlot = plotCity.getNumUnits()
                j = 0
                for i in range(iNumUnitsInAPlot):                        
                        unit = plotCity.getUnit(j)
                        unitType = unit.getUnitType()
                        if (unit.getOwner() == iOldOwner):
                                unit.kill(False, con.iBarbarian)
                                if (iNewOwner < con.iNumActivePlayers or unitType > con.iSettler):
                                        self.makeUnit(unitType, iNewOwner, [2, 2], 1) #RFCRAND
                        else:
                                j += 1
        #RiseAndFall
        def flipUnitsInCityAfter(self, tCityPlot, iCiv):
                #moves new units back in their place
                print ("tCityPlot After", tCityPlot)
                tempPlot = gc.getMap().plot(2, 2)
                if (tempPlot.getNumUnits() != 0):
                        iNumUnitsInAPlot = tempPlot.getNumUnits()
                        #print ("iNumUnitsInAPlot", iNumUnitsInAPlot)                        
                        for i in range(iNumUnitsInAPlot):
                                unit = tempPlot.getUnit(0)
                                unit.setXYOld(tCityPlot[0],tCityPlot[1])
                #cover plots revealed
                gc.getMap().plot(1, 1).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(1, 2).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(1, 3).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(2, 1).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(2, 2).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(2, 3).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(3, 1).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(3, 2).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(3, 3).setRevealed(iCiv, False, True, -1);


        def killUnitsInArea(self, tTopLeft, tBottomRight, iCiv):
                for x in range(tTopLeft[0], tBottomRight[0]+1):
                        for y in range(tTopLeft[1], tBottomRight[1]+1):
                                killPlot = gc.getMap().plot(x,y)
                                iNumUnitsInAPlot = killPlot.getNumUnits()
                                if (iNumUnitsInAPlot):
                                        for i in range(iNumUnitsInAPlot):                                                        
                                                unit = killPlot.getUnit(0)
                                                if (unit.getOwner() == iCiv):
                                                        unit.kill(False, con.iBarbarian)

                                                        
        #RiseAndFall
        def flipUnitsInArea(self, tTopLeft, tBottomRight, iNewOwner, iOldOwner, bSkipPlotCity, bKillSettlers):
                """Deletes, recreates units in 0,67 and moves them to the previous tile.
                If there are units belonging to others in that plot and the new owner is barbarian, the units aren't recreated.
                Settlers aren't created.
                If bSkipPlotCity is True, units in a city won't flip. This is to avoid converting barbarian units that would capture a city before the flip delay"""
                for x in range(tTopLeft[0], tBottomRight[0]+1):
                        for y in range(tTopLeft[1], tBottomRight[1]+1):
                                killPlot = gc.getMap().plot(x,y)
                                iNumUnitsInAPlot = killPlot.getNumUnits()
                                if (iNumUnitsInAPlot):
                                        bRevealedZero = False
                                        if (gc.getMap().plot(2,2).isRevealed(iNewOwner, False)):
                                                bRevealedZero = True
                                        #print ("killplot", x, y)
                                        if (bSkipPlotCity == True) and (killPlot.isCity()):
                                                #print (killPlot.isCity())
                                                #print 'do nothing'
                                                pass
                                        else:
                                                j = 0
                                                for i in range(iNumUnitsInAPlot):                                                        
                                                        unit = killPlot.getUnit(j)
                                                        #print ("killplot", x, y, unit.getUnitType(), unit.getOwner(), "j", j)
                                                        if (unit.getOwner() == iOldOwner):
                                                                unit.kill(False, con.iBarbarian)
                                                                if (bKillSettlers):
                                                                        if ((unit.getUnitType() > iSettler)):
                                                                                self.makeUnit(unit.getUnitType(), iNewOwner, [2, 2], 1)
                                                                else:
                                                                        if ((unit.getUnitType() >= iSettler)): #skip animals
                                                                                self.makeUnit(unit.getUnitType(), iNewOwner, [2, 2], 1)
                                                        else:
                                                                j += 1
                                                tempPlot = gc.getMap().plot(2,2) #RFCRAND
                                                #moves new units back in their place
                                                if (tempPlot.getNumUnits() != 0):
                                                        iNumUnitsInAPlot = tempPlot.getNumUnits()
                                                        for i in range(iNumUnitsInAPlot):
                                                                unit = tempPlot.getUnit(0)
                                                                unit.setXYOld(x,y)
                                                        iCiv = iNewOwner
                                                        if (bRevealedZero == False):
                                                                gc.getMap().plot(1, 1).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(1, 2).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(1, 3).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(2, 1).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(2, 2).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(2, 3).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(3, 1).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(3, 2).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(3, 3).setRevealed(iCiv, False, True, -1);



        #Congresses, RiseAndFall
        def flipCity(self, tCityPlot, bFlipType, bKillUnits, iNewOwner, iOldOwners):
                """Changes owner of city specified by tCityPlot.
                bFlipType specifies if it's conquered or traded.
                If bKillUnits != 0 all the units in the city will be killed.
                iRetainCulture will determine the split of the current culture between old and new owner. -1 will skip
                iOldOwners is a list. Flip happens only if the old owner is in the list.
                An empty list will cause the flip to always happen."""
                pNewOwner = gc.getPlayer(iNewOwner)
                city = gc.getMap().plot(tCityPlot[0], tCityPlot[1]).getPlotCity()
                if (gc.getMap().plot(tCityPlot[0], tCityPlot[1]).isCity()):
                        if not city.isNone():
                                iOldOwner = city.getOwner()
                                if (iOldOwner in iOldOwners or not iOldOwners):

                                        if (bKillUnits):
                                                killPlot = gc.getMap().plot( tCityPlot[0], tCityPlot[1] )
                                                for i in range(killPlot.getNumUnits()):
                                                        unit = killPlot.getUnit(0)
                                                        unit.kill(False, iNewOwner)
                                                        
                                        if (bFlipType): #conquest
                                                if (city.getPopulation() == 2):
                                                        city.setPopulation(3)
                                                if (city.getPopulation() == 1):
                                                        city.setPopulation(2)
                                                pNewOwner.acquireCity(city, True, False)
                                        else: #trade
                                                pNewOwner.acquireCity(city, False, True)
                                                
                                        return True
                return False


        #Congresses, RiseAndFall
        def cultureManager(self, tCityPlot, iCulturePercent, iNewOwner, iOldOwner, bBarbarian2x2Decay, bBarbarian2x2Conversion, bAlwaysOwnPlots):
                """Converts the culture of the city and of the surrounding plots to the new owner of a city.
                iCulturePercent determine the percentage that goes to the new owner.
                If old owner is barbarian, all the culture is converted"""

                pCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                city = pCity.getPlotCity()                

                #city
                if (pCity.isCity()):
                        iCurrentCityCulture = city.getCulture(iOldOwner)
                        city.setCulture(iOldOwner, iCurrentCityCulture*(100-iCulturePercent)/100, False)
                        if (iNewOwner != con.iBarbarian):
                                city.setCulture(con.iBarbarian, 0, True)
                        city.setCulture(iNewOwner, iCurrentCityCulture*iCulturePercent/100, False)
                        if (city.getCulture(iNewOwner) <= 10):
                                city.setCulture(iNewOwner, 20, False)

                #halve barbarian culture in a broader area
                if (bBarbarian2x2Decay or bBarbarian2x2Conversion):
                        if (iNewOwner != con.iBarbarian and iNewOwner != con.iIndependent and iNewOwner != con.iIndependent2):
                                for x in range(tCityPlot[0]-2, tCityPlot[0]+3):        # from x-2 to x+2
                                        for y in range(tCityPlot[1]-2, tCityPlot[1]+3):	# from y-2 to y+2                                
                                                iPlotBarbCulture = gc.getMap().plot(x, y).getCulture(con.iBarbarian)
                                                if (iPlotBarbCulture > 0):
                                                        if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
                                                                if (bBarbarian2x2Decay):
                                                                        gc.getMap().plot(x, y).setCulture(con.iBarbarian, iPlotBarbCulture/4, True)
                                                                if (bBarbarian2x2Conversion):
                                                                        gc.getMap().plot(x, y).setCulture(con.iBarbarian, 0, True)
                                                                        gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotBarbCulture, True)
                                                iPlotIndependentCulture = gc.getMap().plot(x, y).getCulture(con.iIndependent)
                                                if (iPlotIndependentCulture > 0):
                                                        if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
                                                                if (bBarbarian2x2Decay):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent, iPlotIndependentCulture/4, True)
                                                                if (bBarbarian2x2Conversion):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent, 0, True)
                                                                        gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotIndependentCulture, True)
                                                iPlotIndependent2Culture = gc.getMap().plot(x, y).getCulture(con.iIndependent2)
                                                if (iPlotIndependent2Culture > 0):
                                                        if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
                                                                if (bBarbarian2x2Decay):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent2, iPlotIndependent2Culture/4, True)
                                                                if (bBarbarian2x2Conversion):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent2, 0, True)
                                                                        gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotIndependent2Culture, True)
                                                                        
                #plot                               
                for x in range(tCityPlot[0]-1, tCityPlot[0]+2):        # from x-1 to x+1
                        for y in range(tCityPlot[1]-1, tCityPlot[1]+2):	# from y-1 to y+1
                                pCurrent = gc.getMap().plot(x, y)
                                
                                iCurrentPlotCulture = pCurrent.getCulture(iOldOwner)

                                if (pCurrent.isCity()):                                
                                        pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/100, True)
                                        pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent)/100, True)
                                else:
                                        pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/3/100, True)
                                        pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent/3)/100, True)

                                #cut other players culture
##                                for iCiv in range(iNumPlayers):
##                                        if (iCiv != iNewOwner and iCiv != iOldOwner):
##                                                iPlotCulture = gc.getMap().plot(x, y).getCulture(iCiv)
##                                                if (iPlotCulture > 0):
##                                                        gc.getMap().plot(x, y).setCulture(iCiv, iPlotCulture/3, True)
                                                        
                                #print (x, y, pCurrent.getCulture(iNewOwner), ">", pCurrent.getCulture(iOldOwner))

                                if (not pCurrent.isCity()):
                                        if (bAlwaysOwnPlots):
                                                pCurrent.setOwner(iNewOwner)
                                        else:
                                                if (pCurrent.getCulture(iNewOwner)*4 > pCurrent.getCulture(iOldOwner)):
                                                        pCurrent.setOwner(iNewOwner)                                        
                                        #print ("NewOwner", pCurrent.getOwner())



        #handler
        def spreadMajorCulture(self, iMajorCiv, iX, iY):                
                for x in range(iX-4, iX+5):        # from x-4 to x+4
                        for y in range(iY-4, iY+5):	# from y-4 to y+4
                                pCurrent = gc.getMap().plot(x, y)
                                if (pCurrent.isCity()):
                                        city = pCurrent.getPlotCity()
                                        if (city.getOwner() >= iNumMajorPlayers):
                                                iMinor = city.getOwner()
                                                iDen = 25
                                                #RFCRAND
                                                #if (gc.getPlayer(iMajorCiv).getSettlersMaps( CyMap().getGridHeight()-1-y, x ) >= 400):
                                                if (self.blindSettlersMap(iMajorCiv, x, y) >= 130):
                                                        iDen = 10
                                                #elif (gc.getPlayer(iMajorCiv).getSettlersMaps( CyMap().getGridHeight()-1-y, x ) >= 150):
                                                elif (self.blindSettlersMap(iMajorCiv, x, y) >= 90):
                                                        iDen = 15
                                                        
                                                iMinorCityCulture = city.getCulture(iMinor)
                                                city.setCulture(iMajorCiv, iMinorCityCulture/iDen, True)
                                                
                                                iMinorPlotCulture = pCurrent.getCulture(iMinor)
                                                pCurrent.setCulture(iMajorCiv, iMinorPlotCulture/iDen, True)                                

        #UniquePowers
        def convertPlotCulture(self, pCurrent, iCiv, iPercent, bOwner):
                
                if (pCurrent.isCity()):
                        city = pCurrent.getPlotCity()
                        iCivCulture = city.getCulture(iCiv)
                        iLoopCivCulture = 0
                        for iLoopCiv in range(iNumTotalPlayers):
                                if (iLoopCiv != iCiv):
                                        iLoopCivCulture += city.getCulture(iLoopCiv)                                
                                        city.setCulture(iLoopCiv, city.getCulture(iLoopCiv)*(100-iPercent)/100, True)
                        city.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)  
        
##                for iLoopCiv in range(iNumTotalPlayers):
##                        if (iLoopCiv != iCiv):
##                                iLoopCivCulture = pCurrent.getCulture(iLoopCiv)
##                                iCivCulture = pCurrent.getCulture(iCiv)
##                                pCurrent.setCulture(iLoopCiv, iLoopCivCulture*(100-iPercent)/100, True)
##                                pCurrent.setCulture(iCiv, iCivCulture + iLoopCivCulture*iPercent/100, True)
                iCivCulture = pCurrent.getCulture(iCiv)
                iLoopCivCulture = 0
                for iLoopCiv in range(iNumTotalPlayers):
                        if (iLoopCiv != iCiv):
                                iLoopCivCulture += pCurrent.getCulture(iLoopCiv)                                
                                pCurrent.setCulture(iLoopCiv, pCurrent.getCulture(iLoopCiv)*(100-iPercent)/100, True)
                pCurrent.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)                                
                if (bOwner == True):
                        pCurrent.setOwner(iCiv)



                                




        #Congresses, RiseAndFall
        def pushOutGarrisons(self, tCityPlot, iOldOwner):
                tDestination = (-1, -1)
                for x in range(tCityPlot[0]-2, tCityPlot[0]+3):
                        for y in range(tCityPlot[1]-2, tCityPlot[1]+3):
                                pDestination = gc.getMap().plot(x, y)
                                if (pDestination.getOwner() == iOldOwner and (not pDestination.isWater()) and (not pDestination.isImpassable())):
                                        tDestination = (x, y)
                                        break
                                        break
                if (tDestination != (-1, -1)):
                        plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                        iNumUnitsInAPlot = plotCity.getNumUnits()
                        j = 0
                        for i in range(iNumUnitsInAPlot):                        
                                unit = plotCity.getUnit(j)
                                if (unit.getDomainType() == 2): #land unit
                                        unit.setXYOld(tDestination[0], tDestination[1])
                                else:
                                        j = j + 1
                                
        #Congresses, RiseAndFall
        def relocateSeaGarrisons(self, tCityPlot, iOldOwner):
                tDestination = (-1, -1)
                cityList = PyPlayer(iOldOwner).getCityList()
                for pyCity in cityList:
                        if (pyCity.GetCy().isCoastalOld()):
                                tDestination = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
                if (tDestination == (-1, -1)):                    
                        for x in range(tCityPlot[0]-12, tCityPlot[0]+12):
                                for y in range(tCityPlot[1]-12, tCityPlot[1]+12):
                                        pDestination = gc.getMap().plot(x, y)
                                        if (pDestination.isWater()):
                                                tDestination = (x, y)
                                                break
                                                break
                if (tDestination != (-1, -1)):
                        plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                        iNumUnitsInAPlot = plotCity.getNumUnits()
                        j = 0
                        for i in range(iNumUnitsInAPlot):
                                unit = plotCity.getUnit(j)
                                if (unit.getDomainType() == 0): #sea unit
                                        unit.setXYOld(tDestination[0], tDestination[1])
                                else:
                                        j = j + 1


        #Congresses, RiseAndFall
        def createGarrisons(self, tCityPlot, iNewOwner, iNumUnits):
                plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                city = plotCity.getPlotCity()    
                iNumUnitsInAPlot = plotCity.getNumUnits()
                pCiv = gc.getPlayer(iNewOwner)

                if (gc.getTeam(pCiv.getTeam()).isHasTech(con.iAssemblyLine) and gc.getTeam(pCiv.getTeam()).isHasTech(con.iRifling)):
                        iUnitType = con.iInfantry
                elif (gc.getTeam(pCiv.getTeam()).isHasTech(con.iRifling)):
                        if (iNewOwner != con.iEngland):
                                iUnitType = con.iRifleman
                        else:
                                iUnitType = con.iEnglishRedcoat
                elif (gc.getTeam(pCiv.getTeam()).isHasTech(con.iGunpowder)):
                        if (iNewOwner != con.iFrance):
                                iUnitType = con.iMusketman
                        else:
                                iUnitType = con.iFrenchMusketeer
                else:
                        iUnitType = con.iLongbowman

                self.makeUnit(iUnitType, iNewOwner, [tCityPlot[0], tCityPlot[1]], iNumUnits)



        #RiseAndFall, Stability

        def killCiv(self, iCiv, iNewCiv):
                self.clearPlague(iCiv)
                for pyCity in PyPlayer(iCiv).getCityList():
                        tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
                        self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
                        self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv]) #by trade because by conquest may raze the city
                        #pyCity.GetCy().setHasRealBuilding(con.iPlague, False)  #buggy
                self.flipUnitsInArea([0,0], [CyMap().getGridWidth(),CyMap().getGridHeight()], iNewCiv, iCiv, False, True)
                #self.killUnitsInArea([0,0], [CyMap().getGridWidth(),CyMap().getGridHeight()], iNewCiv, iCiv) ?
                if (iCiv < iNumMajorPlayers):
                        self.clearEmbassies(iCiv)
                self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())
                self.resetUHV(iCiv)

        def killAndFragmentCiv(self, iCiv, iNewCiv1, iNewCiv2, iNewCiv3, bAssignOneCity):
                print("Fragmentation into:", iNewCiv1, iNewCiv2, iNewCiv3)
                self.clearPlague(iCiv)
                iNumLoyalCities = 0
                iCounter = gc.getGame().getSorenRandNum(6, 'random start')
                iNumPlayerCities = len(PyPlayer(iCiv).getCityList()) #needs to be assigned cause it changes dinamically
                for pyCity in PyPlayer(iCiv).getCityList():
                        #print("iCounter",iCounter)
                        tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
                        pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
                        #loyal cities for the human player
                        #print(bAssignOneCity,iNumLoyalCities,1+(iNumPlayerCities-1)/6,pyCity.GetCy().isCapital(),iCounter%6 == 0)
                        if (bAssignOneCity and iNumLoyalCities <= 1+(iNumPlayerCities-1)/6 and (pyCity.GetCy().isCapital() or iCounter%6 == 0)):
                                iNumLoyalCities += 1
                                if (iNumLoyalCities == 1):
                                        gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(iNewCiv1, False, -1) #too dangerous?
                                        gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(iNewCiv2, False, -1)
                                iCounter += 1
                                #print(pyCity.GetCy().getName(), "loyal")
                                continue
                        #assign to neighbours first
                        bNeighbour = False
                        iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
                        for j in range(iRndnum, iRndnum + iNumPlayers): #only major players
                                iLoopCiv = j % iNumPlayers
                                if (gc.getPlayer(iLoopCiv).isAlive() and iLoopCiv != iCiv and not gc.getPlayer(iLoopCiv).isHuman()):
                                        if (pCurrent.getCulture(iLoopCiv) > 0):
                                                if (pCurrent.getCulture(iLoopCiv)*100 / (pCurrent.getCulture(iLoopCiv) + pCurrent.getCulture(iCiv) + pCurrent.getCulture(iBarbarian) + pCurrent.getCulture(iIndependent) + pCurrent.getCulture(iIndependent2)) >= 5): #change in vanilla
                                                        self.flipUnitsInCityBefore((tCoords[0],tCoords[1]), iLoopCiv, iCiv)                            
                                                        self.setTempFlippingCity((tCoords[0],tCoords[1]))
                                                        self.flipCity(tCoords, 0, 0, iLoopCiv, [iCiv])
                                                        #pyCity.GetCy().setHasRealBuilding(con.iPlague, False)  #buggy
                                                        self.flipUnitsInCityAfter(self.getTempFlippingCity(), iLoopCiv)
                                                        self.flipUnitsInArea([tCoords[0]-2,tCoords[1]-2], [tCoords[0]+2,tCoords[1]+2], iLoopCiv, iCiv, True, True)
                                                        bNeighbour = True
                                                        break
                        if (bNeighbour):
                                iCounter += 1
                                continue
                        #fragmentation in 2
                        if (iNewCiv3 == -1):
                                #iNewCiv = -1 #debug
                                if (iCounter % 2 == 0):
                                        iNewCiv = iNewCiv1
                                elif (iCounter % 2 == 1):
                                        iNewCiv = iNewCiv2
                                self.flipUnitsInCityBefore((tCoords[0],tCoords[1]), iNewCiv, iCiv)                            
                                self.setTempFlippingCity((tCoords[0],tCoords[1]))                                                        
                                self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
                                self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv])
                                #pyCity.GetCy().setHasRealBuilding(con.iPlague, False)  #buggy
                                self.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
                                #print(pyCity.GetCy().getName(), iNewCiv)
                                iCounter += 1
                                self.flipUnitsInArea([tCoords[0]-1,tCoords[1]-1], [tCoords[0]+1,tCoords[1]+1], iNewCiv, iCiv, False, True)
                        #fragmentation with barbs
                        else:
                                if (iCounter % 3 == 0):
                                        iNewCiv = iNewCiv1
                                elif (iCounter % 3 == 1):
                                        iNewCiv = iNewCiv2
                                elif (iCounter % 3 == 2):
                                        iNewCiv = iNewCiv3
                                self.flipUnitsInCityBefore((tCoords[0],tCoords[1]), iNewCiv, iCiv)                            
                                self.setTempFlippingCity((tCoords[0],tCoords[1]))         
                                self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
                                self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv])
                                #pyCity.GetCy().setHasRealBuilding(con.iPlague, False) #buggy
                                self.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
                                iCounter += 1                                      
                                self.flipUnitsInArea([tCoords[0]-1,tCoords[1]-1], [tCoords[0]+1,tCoords[1]+1], iNewCiv, iCiv, False, True)
                if (bAssignOneCity == False):
                        #self.flipUnitsInArea([0,0], [CyMap().getGridWidth(),CyMap().getGridHeight()], iNewCiv1, iCiv, False, True) #causes a bug: if a unit was inside another city's civ, when it becomes independent or barbarian, may raze it
                        self.killUnitsInArea([0,0], [CyMap().getGridWidth(),CyMap().getGridHeight()], iCiv)
                        self.resetUHV(iCiv)
                if (iCiv < iNumMajorPlayers):
                        self.clearEmbassies(iCiv)
                self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())



        def pickFragmentation(self, iPlayer, iNewCiv1, iNewCiv2, iNewCiv3, bAssignCities):
                if (iPlayer == con.iAztecs or \
                    iPlayer == con.iInca or \
                    iPlayer == con.iMaya or \
                    iPlayer == con.iEthiopia or \
                    iPlayer == con.iMali):
                        if (self.getCivsWithNationalism() <= 0):
                                self.killAndFragmentCiv(iPlayer, con.iNative, iBarbarian, iNewCiv3, bAssignCities)
                        else:
                                self.killAndFragmentCiv(iPlayer, iNewCiv1, iNewCiv2, iNewCiv3, bAssignCities)
                else:
                        self.killAndFragmentCiv(iPlayer, iNewCiv1, iNewCiv2, iNewCiv3, bAssignCities)


                
        def resetUHV(self, iPlayer):
                if (iPlayer < iNumMajorPlayers):
                        if (self.getGoal(iPlayer, 0) == -1):
                                self.setGoal(iPlayer, 0, 0)
                        if (self.getGoal(iPlayer, 1) == -1):
                                self.setGoal(iPlayer, 1, 0)
                        if (self.getGoal(iPlayer, 2) == -1):
                                self.setGoal(iPlayer, 2, 0)
                                                
        def clearEmbassies(self, iDeadCiv):
                for i in range (iNumTotalPlayers):
                        for pyCity in PyPlayer(i).getCityList():
                                if (pyCity.GetCy().hasBuilding(iNumBuildingsPlague + iDeadCiv)):
                                        pyCity.GetCy().setHasRealBuilding(iNumBuildingsPlague + iDeadCiv, False)
                                        continue


        def clearPlague(self, iCiv):
                for pyCity in PyPlayer(iCiv).getCityList():
                        if (pyCity.GetCy().hasBuilding(con.iPlague)):
                                pyCity.GetCy().setHasRealBuilding(con.iPlague, False)




        #AIWars, by CyberChrist

        def isNoVassal(self, iCiv):
                iMaster = 0
                for iMaster in range (iNumTotalPlayers):
                        if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster)):
                                return False
                return True

        def isAVassal(self, iCiv):
                iMaster = 0
                for iMaster in range (iNumTotalPlayers):
                        if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster)):
                                return True
                return False

        #Barbs, RiseAndFall
        def squareSearch( self, tTopLeft, tBottomRight, function, argsList ): #by LOQ
                """Searches all tile in the square from tTopLeft to tBottomRight and calls function for
                every tile, passing argsList. The function called must return a tuple: (1) a result, (2) if
                a plot should be painted and (3) if the search should continue."""
                tPaintedList = []
                result = None
                #RFCRAND
                lBounds = self.checkBounds(tTopLeft[0], tTopLeft[1], tBottomRight[0], tBottomRight[1])
                for x in range(lBounds[0], lBounds[2]+1):
                        for y in range(lBounds[1], lBounds[3]+1):
                                result, bPaintPlot, bContinueSearch = function((x, y), result, argsList)
                                if bPaintPlot:			# paint plot
                                        tPaintedList.append((x, y))
                                if not bContinueSearch:		# goal reached, so stop
                                        return result, tPaintedList
                return result, tPaintedList

        #Barbs, RiseAndFall
        def outerInvasion( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh and pCurrent.getTerrainType() != con.iSnow) and (pCurrent.getFeatureType() != con.iJungle and pCurrent.getFeatureType() != con.iSeaIce): #RFCRAND
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        if (pCurrent.countTotalCulture() == 0 ):
                                                # this is a good plot, so paint it and continue search
                                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #Barbs
        def innerSeaSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's water and it isn't occupied by any unit. Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isWater() and pCurrent.getFeatureType() != con.iSeaIce):
                        if ( not pCurrent.isCity() and not pCurrent.isUnit() and pCurrent.area().getNumTiles() > 10 ):
                                iClean = 0
                                for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                        for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                if (pCurrent.getNumUnits() != 0):
                                                        iClean += 1
                                if ( iClean == 0 ):   
                                        # this is a good plot, so paint it and continue search
                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #Barbs
        def outerSeaSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's water and it isn't occupied by any unit and if it isn't a civ's territory. Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isWater() and pCurrent.getFeatureType() != con.iSeaIce): #RFCRAND
                        if ( not pCurrent.isCity() and not pCurrent.isUnit() and pCurrent.area().getNumTiles() > 10):
                                if (pCurrent.countTotalCulture() == 0 ):
                                        iClean = 0
                                        for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                                for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                        if (pCurrent.getNumUnits() != 0):
                                                                iClean += 1
                                        if ( iClean == 0 ):   
                                                # this is a good plot, so paint it and continue search
                                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        def outerCoastSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's water and it isn't occupied by any unit and if it isn't a civ's territory. Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.getTerrainType() == con.iCoast and pCurrent.getFeatureType() != con.iSeaIce): #RFCRAND
                        if ( not pCurrent.isCity() and not pCurrent.isUnit() and pCurrent.area().getNumTiles() > 10 ):
                                if (pCurrent.countTotalCulture() == 0 ):
                                        iClean = 0
                                        for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                                for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                        if (pCurrent.getNumUnits() != 0):
                                                                iClean += 1
                                        if ( iClean == 0 ):   
                                                # this is a good plot, so paint it and continue search
                                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)
            
        #Barbs
        def outerSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory.
                Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle and pCurrent.getFeatureType() != con.iSeaIce):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        iClean = 0
                                        for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                                for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                        if (pCurrent.getNumUnits() != 0):
                                                                iClean += 1
                                        if ( iClean == 0 ):
                                                if (pCurrent.countTotalCulture() == 0 ):
                                                        # this is a good plot, so paint it and continue search
                                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)                                        

        #RiseAndFall
        def innerInvasion( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh and pCurrent.getTerrainType() != con.iSnow) and (pCurrent.getFeatureType() != con.iJungle and pCurrent.getFeatureType() != con.iSeaIce): #RFCRAND
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        if (pCurrent.getOwner() in argsList ):
                                                # this is a good plot, so paint it and continue search
                                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)
            
        def innerSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle and pCurrent.getFeatureType() != con.iSeaIce):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        iClean = 0
                                        for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                                for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                        if (pCurrent.getNumUnits() != 0):
                                                                iClean += 1
                                        if ( iClean == 0 ):  
                                                if (pCurrent.getOwner() in argsList ):
                                                        # this is a good plot, so paint it and continue search
                                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #RiseAndFall
        def goodPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't desert, tundra, marsh or jungle; it isn't occupied by a unit or city and if it isn't a civ's territory.
                Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if ( not pCurrent.isImpassable()):
                                if ( not pCurrent.isUnit() ):
                                        if (pCurrent.getTerrainType() != con.iDesert) and (pCurrent.getTerrainType() != con.iTundra) and (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                                if (pCurrent.countTotalCulture() == 0 ):
                                                        # this is a good plot, so paint it and continue search
                                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #RiseAndFall
        def ownedCityPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it contains a city belonging to the civ"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if (pCurrent.getOwner() == argsList ):
                        if (pCurrent.isCity()):
                                # this is a good plot, so paint it and continue search
                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue) 

        def ownedPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it is in civ's territory."""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if (pCurrent.getOwner() == argsList ):
                        # this is a good plot, so paint it and continue search
                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        def goodOwnedPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands; it isn't marsh or jungle, it isn't occupied by a unit and if it is in civ's territory."""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                            if (pCurrent.getOwner() == argsList ):
                                                    # this is a good plot, so paint it and continue search
                                                    return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #RFCMP
        #RFCRAND
        def getFakeRandNum( self, iMax, logString ): 
                """Returns a number from 0 to iMax-1 that's not really a random number. Because of MP problems"""
                #print (logString);
                if (iMax != 0):
                        #return (gc.getGame().getSorenRand().getSeed() % (gc.getGame().getGameTurn() + 100)) % iMax
                        return (self.getLongSeed() % (1000)) % iMax #RFCRAND (different purpose: here we need it to stay the same value every turn, and has to be higher)
                else:
                        return 0

        #RFCRAND
        def countMajorCivsAlive(self):
                iResult = 0
                for i in range(iNumMajorPlayers):
                        if (gc.getPlayer(i).isAlive()):
                                iResult += 1
                return iResult

            
        def checkBounds(self, leftX, bottomY, rightX, topY):
                iGridX = CyMap().getGridWidth()
                iGridY = CyMap().getGridHeight()
                if (leftX <= 0):
                    leftX = 1
                if (bottomY <= 0):
                    bottomY = 1
                if (rightX >= iGridX-1):
                    rightX = iGridX-2
                if (topY >= iGridY-1):
                    topY = iGridY-2
                return [leftX, bottomY, rightX, topY]

        def getAreas(self):
                "Returns a list of CyArea objects representing all the areas in the map (land and water)"
                map = CyMap()
                
                areas = []
                for i in range(map.getIndexAfterLastArea()):
                        area = map.getArea(i)
                        if not area.isNone():
                                areas.append(area)
                                
                return areas
            
        def blindSettlersMap(self, iPlayer, iX, iY):
                "Same as in AI_foundValue"
                iValue = 100
                pPlot = gc.getMap().plot(iX, iY)
                player = gc.getPlayer(iPlayer)
                pStartingPlot = player.getStartingPlot()


                if (iPlayer >= con.iNumMajorPlayers):
                        return 100

                if (pPlot.getRealLatitude() <= player.getSettlersCoords(2)):
                        iValue *= max(30,(100 - 2*(player.getSettlersCoords(2)-pPlot.getRealLatitude())))
                        iValue /= 100
                elif (pPlot.getRealLatitude() >= player.getSettlersCoords(3)):
                        iValue *= max(30,(100 - 2*(pPlot.getRealLatitude()-player.getSettlersCoords(3))))
                        iValue /= 100
                else:
                        iValue *= 120
                        iValue /= 100      

                iMaxExtension = player.getSettlersCoords(4)*CyMap().getGridWidth()/100
                
                if not (pStartingPlot.isNone()):
                        if ((iX + CyMap().getGridWidth() >= pStartingPlot.getX() + iMaxExtension + CyMap().getGridWidth())):
                                iValue *= max(60, 100 - (iX - (pStartingPlot.getX() + iMaxExtension)))
                                iValue /= 100
                        elif ((iX + CyMap().getGridWidth() <= pStartingPlot.getX() - iMaxExtension + CyMap().getGridWidth()) ):
                                iValue *= max(60, 100 - ((pStartingPlot.getX() + iMaxExtension) - iX))
                                iValue /= 100

                if not (pStartingPlot.isNone()):
                        if (pPlot.area().getID() == pStartingPlot.area().getID()): 
                                iValue *= player.getSettlersModifiers(0)
                                iValue /= 100
                        else:
                                iValue *= 200-player.getSettlersModifiers(0)
                                iValue /= 100
                        if (player.getSettlersModifiers(0) < 100 and player.getNumCities() >= player.getSettlersCoords(6)-1):
                                if (pPlot.area().getID() == pStartingPlot.area().getID()): 
                                        iValue *= player.getSettlersModifiers(0)
                                        iValue /= 100
                                #else:
                                #        iValue *= 200-player.getSettlersModifiers(0)
                                #        iValue /= 100

##                        if (player.getSettlersModifiers(0) <= 60): 
##                                IDSAmerica = -1
##                                IDNAmerica = -1
##                                IDCAmerica = -1
##                                if (gc.getPlayer(con.iInca).isAlive()):
##                                        IDSAmerica = gc.getPlayer(con.iInca).getStartingPlot().area().getID()
##                                if (gc.getPlayer(con.iAztecs).isAlive()):
##                                        IDNAmerica = gc.getPlayer(con.iAztecs).getStartingPlot().area().getID()
##                                if (gc.getPlayer(con.iMaya).isAlive()):
##                                        IDCAmerica = gc.getPlayer(con.iMaya).getStartingPlot().area().getID()
##                                currentArea = pPlot.area().getID()
##				#if (pPlot.area().getID() == self.getAmericaInfo(4) or pPlot.area().getID() == self.getAmericaInfo(5)):
##                                if ((currentArea == IDNAmerica or currentArea == IDCAmerica or currentArea == IDSAmerica) and currentArea != pStartingPlot.area().getID()):
##                                        iValue *= 400
##                                        iValue /= 100

                        if (((CyMap().getSeaLevel() <= 4) and (self.isNewWorld(pPlot.getX(), pPlot.getY()) and not self.isNewWorldCiv(iPlayer))) or \
                            ((CyMap().getSeaLevel() == 4) and (self.isOtherWorld(pPlot.getX(), pPlot.getY(), iPlayer)))):
                                if (player.getSettlersModifiers(0) <= 60):
                                        iValue *= 360
                                        iValue /= 100
                                else:
                                        iValue *= 130
                                        iValue /= 100
                        else:
                                if (player.getSettlersModifiers(0) <= 60):
                                        iValue *= 80
                                        iValue /= 100



                if (pPlot.isCoastalLand()):
                        iValue *= player.getSettlersModifiers(1)
                        iValue /= 100

                if (pPlot.getTerrainType() == 2): #desert
                        iValue *= player.getSettlersModifiers(5)
                        iValue /= 100
                else:
                        iValue *= 200-player.getSettlersModifiers(5)
                        iValue /= 100

                if (pPlot.isRiverSide()):
                        iValue *= player.getSettlersModifiers(2)
                        iValue /= 100

                numJungles = 0
                numPeaks = 0
                
                for iLoopX in range(iX-2, iX+3):
                        for iLoopY in range(iY-2, iY+3):
                                if (not (abs(iLoopX-iX) == 2 and abs(iLoopY-iY) == 2)):
                                        pLoopPlot = gc.getMap().plot(iLoopX, iLoopY)                
                                        if (not pLoopPlot.isNone()):
                                                if (pLoopPlot.getFeatureType() == 1): #jungle
                                                        numJungles += 1
                                                if (pLoopPlot.isPeak()):
                                                        numPeaks += 1
                                                
                if (numJungles >= 2):
                        iValue *= player.getSettlersModifiers(4)
                        iValue /= 100
                        if (numJungles >= 4):
                                iValue *= player.getSettlersModifiers(4)
                                iValue /= 100

                if (numPeaks >= 2):
                        iValue *= player.getSettlersModifiers(3)
                        iValue /= 100
                        if (numPeaks >= 4):
                                iValue *= player.getSettlersModifiers(3)
                                iValue /= 100
                                if (numPeaks >= 6):
                                        iValue *= player.getSettlersModifiers(3)
                                        iValue /= 100


                #here's a part specific only of this function, for stability. Not present in the dll
                distFromStartPlot = self.calculateDistance(iX, iY, pStartingPlot.getX(), pStartingPlot.getY())
                if (distFromStartPlot > 15):
                        iValue *= 50
                        iValue /= 100
                elif (distFromStartPlot > 5):
                        iValue *= 400 - (distFromStartPlot-5)*35
                        iValue /= 100
                else:
                        iValue *= 400
                        iValue /= 100
                        

                
                iValue /= 2 #normalization for stability

                return iValue


        def printBlindSettlersMap(self, iPlayer):
                settmap = []                        
                for j in range(CyMap().getGridHeight()):
                        iY = CyMap().getGridHeight()-1-j
                        tempRow = []
                        for i in range(CyMap().getGridWidth()):
                                iX = i
                                modifier = self.blindSettlersMap(iPlayer, iX, iY)
                                if (CyMap().plot( iX, iY ).isWater()):
                                        modifier = 0
                                tempRow.append(modifier)
                        settmap.append(tempRow)
                print(settmap)
                


##        def blindSettlersStartingMap(self, iPlayer, iX, iY):
##
##                iValue = 100
##                Map = gc.getMap()
##                pPlot = Map.plot(iX, iY)
##                player = gc.getPlayer(iPlayer)
##
##                if (iPlayer >= con.iNumMajorPlayers):
##                        return 100
##
##                if (pPlot.getLatitude() <= player.getSettlersCoords(0)):
##                        iValue *= max(20, (100 - 3*(player.getSettlersCoords(0)-pPlot.getLatitude())))
##                        iValue /= 100
##                elif (pPlot.getLatitude() >= player.getSettlersCoords(1)):
##                        iValue *= max(20, (100 - 3*(pPlot.getLatitude()-player.getSettlersCoords(1))))
##                        iValue /= 100
##                else:
##                        iValue *= 130
##                        iValue /= 100        
##
##                #print(iPlayer, iX, iY, "A:", iValue)  
##
##                bNextToCoastal = False
##                if (not pPlot.isCoastalLand()):                    
##                        for iLoopX in range(iX-2, iX+3):
##                                for iLoopY in range(iY-2, iY+3):
##                                        pLoopPlot = Map.plot(iLoopX, iLoopY)                
##                                        if (pLoopPlot.isCoastalLand()):
##                                                bNextToCoastal = True
##                                                break
##                                                break
##                bCloseToOcean = False
##                for iLoopX in range(iX-2, iX+3):
##                        for iLoopY in range(iY-2, iY+3):
##                                pLoopPlot = Map.plot(iLoopX, iLoopY)                
##                                if (pLoopPlot.isWater()):
##                                        if (pLoopPlot.area().getID() == Map.plot(0, 0).area().getID()):
##                                                bCloseToOcean = True
##                                                break
##                                                break
##
##                iCoords5 = player.getSettlersCoords(5)
##                if (iCoords5 == 3 or iCoords5 == 5):
##                        if (pPlot.isCoastalLand()):
##                                iValue *= 150
##                                iValue /= 100
##                        else:
##                                iValue *= 50
##                                iValue /= 100                          
##                elif (iCoords5 == 2 or iCoords5 == 4):                  
##                        if (bNextToCoastal):
##                                iValue *= 150
##                                iValue /= 100
##                        else:
##                                iValue *= 50
##                                iValue /= 100
##                elif (iCoords5 <= 1):
##                        if (pPlot.isCoastalLand()):
##                                iValue *= 50
##                                iValue /= 100
##                        else:
##                                iValue *= 150
##                                iValue /= 100
##                        if (iCoords5 == 0):
##                                if (bNextToCoastal):
##                                        iValue *= 50
##                                        iValue /= 100
##                                else:
##                                        iValue *= 150
##                                        iValue /= 100
##                if (iCoords5 == 4 or iCoords5 == 5):
##                        if (bCloseToOcean):
##                                iValue *= 150
##                                iValue /= 100
##                        else:
##                                iValue *= 50
##                                iValue /= 100           
##
##                #print(iPlayer, iX, iY, "B:", iValue)  
##
##                if (pPlot.getTerrainType() == 2): #desert
##                        iValue *= player.getSettlersModifiers(5)
##                        iValue /= 100
##                else:
##                        iValue *= 200-player.getSettlersModifiers(5)
##                        iValue /= 100
##
##                if (pPlot.isRiverSide()):
##                        iValue *= player.getSettlersModifiers(2)
##                        iValue /= 100
##                else:
##                        iValue *= 200-player.getSettlersModifiers(2)
##                        iValue /= 100
##
##
##                #print(iPlayer, iX, iY, "C:", iValue)  
##                        
##                numJungles = 0
##                numPeaks = 0
##                numSettleable = 0
##                
##                for iLoopX in range(iX-2, iX+3):
##                        for iLoopY in range(iY-2, iY+3):
##                                pLoopPlot = Map.plot(iLoopX, iLoopY)                
##                                if (not pLoopPlot.isNone()):
##                                        if (pLoopPlot.getFeatureType() == 1): #jungle
##                                                numJungles += 1
##                                        if (pLoopPlot.isPeak()):
##                                                numPeaks += 1
##                                        if (player.canFound(iLoopX, iLoopY)):
##                                                numSettleable += 1
##
##                if (numSettleable >= 3):                       
##                        if (numJungles >= 3):
##                                iValue *= player.getSettlersModifiers(4)
##                                iValue /= 100
##                                if (numJungles + numPeaks <= 7):
##                                        iValue *= player.getSettlersModifiers(4)
##                                        iValue /= 100
##
##                        if (numPeaks >= 3):
##                                iValue *= player.getSettlersModifiers(3)
##                                iValue /= 100
##                                if (numJungles + numPeaks <= 7):
##                                        iValue *= player.getSettlersModifiers(3)
##                                        iValue /= 100
##
##                #print(iPlayer, iX, iY, "D:", iValue)  
##
##                return iValue


        def blindSpecificStartingModifiers(self, iPlayer, iX, iY, lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents):

                iValue = 100
                Map = gc.getMap()
                pPlot = Map.plot(iX, iY)
                player = gc.getPlayer(iPlayer)

                if (CyMap().getSeaLevel() <= 2):
                    
                        iCentrality = player.getSettlersCoords(7)
                        #print ("iCentrality", iCentrality)
                        if (iCentrality == 2):
                                if (iX >= (lEurasia[1]-lEurasia[0])*2/5 + lEurasia[0] and iX <= (lEurasia[1]-lEurasia[0])*3/5 + lEurasia[0]):
                                        iValue *= 200
                                        iValue /= 100
                                elif (iX >= (lEurasia[1]-lEurasia[0])/3 + lEurasia[0] and iX <= (lEurasia[1]-lEurasia[0])*2/3 + lEurasia[0]):
                                        iValue *= 150
                                        iValue /= 100
                                else:
                                        iValue *= 20
                                        iValue /= 100  
                        elif (iCentrality == 1):
                                if (iX >= (lEurasia[1]-lEurasia[0])/3 + lEurasia[0] and iX <= (lEurasia[1]-lEurasia[0])*2/3 + lEurasia[0]):
                                        iValue *= 160
                                        iValue /= 100
                                else:
                                        iValue *= 40
                                        iValue /= 100                                 
                        elif (iCentrality == -1):
                                if (iX >= (lEurasia[1]-lEurasia[0])*1/7 + lEurasia[0] and iX <= (lEurasia[1]-lEurasia[0])/3 + lEurasia[0] \
                                    or iX >= (lEurasia[1]-lEurasia[0])*2/3 + lEurasia[0] and iX <= (lEurasia[1]-lEurasia[0])*6/7 + lEurasia[0]):
                                        iValue *= 170
                                        iValue /= 100
                                else:
                                        iValue *= 30
                                        iValue /= 100  
                        elif (iCentrality == -2):
                                if (iX <= (lEurasia[1]-lEurasia[0])*1/5 + lEurasia[0] or iX >= (lEurasia[1]-lEurasia[0])*4/5 + lEurasia[0]):
                                        iValue *= 200
                                        iValue /= 100
                                elif (iX <= (lEurasia[1]-lEurasia[0])/3 + lEurasia[0] or iX >= (lEurasia[1]-lEurasia[0])*2/3 + lEurasia[0]):
                                        iValue *= 150
                                        iValue /= 100
                                else:
                                        iValue *= 20
                                        iValue /= 100   

                                                
                        iFirstTerm = 90
                        iSecondTerm = 110
                        if (iPlayer == con.iEngland):
                                iFirstTerm = 150
                                iSecondTerm = 50
                        elif (iPlayer == con.iJapan):
                                if (lRolls[7] == 4):
                                        iFirstTerm = 150
                                        iSecondTerm = 50
                                else:
                                        iFirstTerm = 110
                                        iSecondTerm = 90
                        elif (iPlayer < con.iJapan):
                                iFirstTerm = 50
                                iSecondTerm = 150
                        elif (iPlayer < con.iEngland):
                                iFirstTerm = 75
                                iSecondTerm = 125
                        elif (iPlayer in con.lCivBioOldWorld):
                                iFirstTerm = 85
                                iSecondTerm = 115                        



                        iFirstTerm2 = iFirstTerm
                        if (CyMap().getSeaLevel() == 1):
                                if (iPlayer == con.iJapan):
                                        iFirstTerm = 50
                                if (iPlayer == con.iEngland):
                                        iFirstTerm2 = 50
                        elif (CyMap().getSeaLevel() == 2):
                                if (iPlayer == con.iJapan and lRolls[7] == 4):
                                        xChina = gc.getPlayer(con.iChina).getStartingPlot().getX()
                                        dist1 = abs(lIsland1[1]-xChina)
                                        dist2 = abs(xChina-lIsland2[0])
                                        if (dist1 > dist2):
                                                iFirstTerm = iSecondTerm
                                        else:
                                                iFirstTerm2 = iSecondTerm       

                                                        

                        if (lRolls[7] >= 2):            
                                if (pPlot.area().getID() != lEurasia[4] and pPlot.area().getID() == lIsland1[4]):
                                        iValue *= iFirstTerm
                                        iValue /= 100
                                elif (pPlot.area().getID() != lEurasia[4] and pPlot.area().getID() == lIsland2[4]):
                                        iValue *= iFirstTerm2
                                        iValue /= 100
                                else:
                                        iValue *= iSecondTerm
                                        iValue /= 100

                                if (iX >= lIsland1[0] and iX <= lIsland1[1] and iY >= lIsland1[2] and iY <= lIsland1[3]):
                                        iValue *= iFirstTerm       
                                        iValue /= 100
                                elif (iX >= lIsland2[0] and iX <= lIsland2[1] and iY >= lIsland2[2] and iY <= lIsland2[3]):
                                        iValue *= iFirstTerm2
                                        iValue /= 100
                                else:
                                        iValue *= iSecondTerm
                                        iValue /= 100

                elif (CyMap().getSeaLevel() == 3): #low likelihood
                        #not hardcoded in isValid()
                        iContinent = 0
                        continentWidth = int(CyMap().getGridWidth()/3)
                        continentHeight = int(CyMap().getGridHeight()/2)
                        for i in range(3):
                                for j in range(2):
                                        continentWestX = i*continentWidth
                                        continentEastX = (i+1)*continentWidth
                                        continentBottomY = j*continentHeight
                                        continentTopY = (j+1)*continentHeight
                                        if (iX >= continentWestX and iX <= continentEastX and iY >= continentBottomY and iY <= continentTopY):
                                                if (iPlayer == con.iAmerica):
                                                        if (lRandomContinents[iContinent] == 1): #new world
                                                                iValue *= 150
                                                                iValue /= 100
                                                        else:
                                                                iValue *= 75
                                                                iValue /= 100
                                                else:
                                                        if (lRandomContinents[iContinent] == 1 and (iPlayer in con.lCivBioOldWorld)): #new world
                                                                iValue *= 75
                                                                iValue /= 100
                                                                if (iPlayer >= con.iPersia and iPlayer <= con.iJapan):  #cos otherwise ancient civs all spawn in the old world and one classical one ends up in the new world
                                                                        iValue *= 85 #70 before semi-random spawn dates
                                                                        iValue /= 100
                                                                if (iPlayer < con.iGreece): #added after semi-random spawn dates
                                                                        iValue *= 95
                                                                        iValue /= 100   
                                                        if (lRandomContinents[iContinent] == 0 and (iPlayer in con.lCivBioNewWorld)): #old world
                                                                iValue *= 88
                                                                iValue /= 100
                                                        if (lRandomContinents[iContinent] == 1 and (iPlayer in con.lCivGroups[0])): #new world
                                                                iValue *= 75
                                                                iValue /= 100
                                                        if (lRandomContinents[iContinent] == 0 and (iPlayer in con.lCivGroups[0])): #old world
                                                                iValue *= 130
                                                                iValue /= 100
                                                        if (lRandomContinents[iContinent] == 1): #lower because the new world shouldn't be very crowded
                                                                iValue *= 90
                                                                iValue /= 100
                                                        
                                        iContinent = iContinent + 1

                elif (CyMap().getSeaLevel() == 4): #very low likelihood
                        if (self.isNewWorld(iX,iY)):
                                if (iPlayer == con.iAmerica or iPlayer in con.lCivBioOldWorld):
                                        iValue *= 80
                                        iValue /= 100
                                else:
                                        iValue *= 120
                                        iValue /= 100
                        else:
                                if (iPlayer == con.iAmerica or iPlayer in con.lCivBioOldWorld):
                                        iValue *= 120
                                        iValue /= 100
                                else:
                                        iValue *= 80
                                        iValue /= 100
                                        
                iIslandModifier = 130
                if (CyMap().getSeaLevel() >= 3): #very low likelihood
                        iIslandModifier = 120
                if (iPlayer == con.iEngland or iPlayer == con.iJapan):
                        if (pPlot.area().getNumTiles() <= 100):
                                iValue *= iIslandModifier
                                iValue /= 100


                                
                if (iPlayer == con.iAmerica):
                        iModifier = 70
                        if (CyMap().getSeaLevel() == 4): #very low likelihood
                                iModifier = 40
                        iNumOwnedPlots = 0                      
                        for iLoopX in range(iX-3, iX+4):
                                for iLoopY in range(iY-3, iY+4):
                                        pLoopPlot = Map.plot(iLoopX, iLoopY)
                                        if (pLoopPlot.isOwned()):
                                                iNumOwnedPlots += 1
                                                if (pLoopPlot.isCity()):
                                                        iOwner = pLoopPlot.getOwner()
                                                        if (iOwner<iNumMajorPlayers):
                                                                if ((CyMap().getSeaLevel() == 4) or (iOwner in con.lCivBioOldWorld)):        #on very low, no Euro civs condition
                                                                        #print("america", iLoopX, iLoopY, pLoopPlot.area().getID(), iOwner)
                                                                        areaID = pLoopPlot.area().getID()
                                                                        ownerArea = gc.getPlayer(iOwner).getStartingPlot().area().getID()
                                                                        if (areaID != ownerArea):
                                                                                iValue *= 100+iModifier
                                                                                iValue /= 100
                        if (iNumOwnedPlots == 0):
                                iValue *= 100-iModifier
                                iValue /= 100
                                        
                return iValue


        def isValid(self, playerID, x, y, lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents, bSecondPass, bThirdPass):

                ##map = CyMap()
                Map = gc.getMap()
                pPlot = Map.plot(x, y)
                areaID = pPlot.area().getID()
                iHeight = Map.getGridHeight()
                iWidth = Map.getGridWidth()

                if (y <= 3 or y >= iHeight-4 or x <= 3 or y >= iWidth-4):
                        return False #save the borders

                #forbid any plot has less than x passable plots around
                impassablePlots = 0
                impassablePlotsCap = 5
                if (CyMap().getSeaLevel() == 4): #very low likelihood
                        impassablePlotsCap = 7
                for iLoopX in range(x-1, x+2):
                        for iLoopY in range(y-1, y+2):
                                pCurrent = CyMap().plot( iLoopX%CyMap().getGridWidth(), iLoopY%CyMap().getGridHeight() )
                                if (pCurrent.isImpassable() or pCurrent.isWater() or pCurrent.isPeak() or pCurrent.getTerrainType() == con.iMarsh or pCurrent.getFeatureType() == con.iJungle):
                                        impassablePlots = impassablePlots + 1
                if (impassablePlots > impassablePlotsCap): #less than x passable plots around
                        return False

                
                #may slow down, but it's necessary to prevent locked starts
                passableAreaSizeCap1 = 10
                passableAreaSizeCap2 = 20
                if (CyMap().getSeaLevel() == 4): #very low likelihood
                        passableAreaSizeCap1 = 8
                        passableAreaSizeCap2 = 16                   
                passableAreaSize = self.getPassableAreaSize(x, y, 6)
                if (passableAreaSize < passableAreaSizeCap1):
                        return False
                if (not bSecondPass):
                        if (passableAreaSize < passableAreaSizeCap2):
                                return False

                if (CyMap().getSeaLevel() >= 3): #low and very low likelihood
                        if (not bSecondPass):
                                if (playerID != con.iAmerica):
                                        if (x >= self.getEmptyContinentInfo(0) and \
                                            x <= self.getEmptyContinentInfo(1) and \
                                            y >= self.getEmptyContinentInfo(2) and \
                                            y <= self.getEmptyContinentInfo(3)):
                                                return False
                                                        
                        
                        
                if (CyMap().getSeaLevel() == 4): #very low likelihood
                        if (not bSecondPass):
                                if (pPlot.area().getNumTiles() <= 50):
                                        return False
                                return True
                        if (bSecondPass):
                                return True

                if (CyMap().getSeaLevel() == 3): #low likelihood
                        if (pPlot.area().getNumTiles() >= 50):
                                #this constraint is necessary for the "new world" uhvs: 
                                if (gc.getPlayer(playerID).isHuman() and (self.isNewWorld(x, y) == True) and (playerID == con.iFrance or playerID == con.iSpain)):
                                        return False
                                if (gc.getPlayer(con.iSpain).isHuman() and (self.isNewWorld(x, y) == True) and (playerID == con.iFrance or playerID == con.iEngland or playerID == con.iNetherlands)):
                                        return False
                                return True
                        else:
                                return False
                else:
                        if (pPlot.area().getNumTiles() <= 15):
                                return False

                if (CyMap().getSeaLevel() == 0): #very high likelihood
                        leftX = (float(con.tCoreAreasTL[playerID][0])/100)*iWidth
                        rightX = (float(con.tCoreAreasBR[playerID][0])/100)*iWidth
                        bottomY = (float(con.tCoreAreasTL[playerID][1])/100)*iHeight
                        topY = (float(con.tCoreAreasBR[playerID][1])/100)*iHeight
                        if (not bSecondPass):
                                if (x < leftX or x >= rightX or y < bottomY or y >= topY):
                                        return False
                        if (not bThirdPass):
                                if (x < leftX-3 or x >= rightX+3 or y < bottomY-3 or y >= topY+3):
                                        return False


                    

                #high and medium
                #print("XY",x,y)
                if (playerID in con.lCivBioOldWorld and playerID != con.iAmerica):
                        if (areaID != lEurasia[4] and areaID != lAfrica[4] and areaID != lIsland1[4] and areaID != lIsland2[4]):
                                #print ("case0", areaID, lEurasia[4])
                                #print("False1")
                                return False
                        if (not bSecondPass):
                                if (lRolls[8] == 1):   #equator N/S division
                                        iEquator = iHeight/2 - iHeight*7/100 -1; #7 instead of 15 because India must be below
                                        if (lRolls[0] == 1):
                                                iEquator = iHeight/2 + iHeight*7/100 -1; #necessary, because rolls[8] can be 1 with medium likelihood as well.  
                                        if (playerID in con.lEquatorDivisionN):
                                                if (lRolls[0] == 0):
                                                        if (pPlot.getY() < iEquator - 5): #5 of tolerance
                                                                #print("False2")
                                                                return False
                                                else:
                                                        if (pPlot.getY() > iEquator + 5): #5 of tolerance
                                                                #print("False3")
                                                                return False
                                        elif (playerID in con.lEquatorDivisionS):
                                                if (lRolls[0] == 0):
                                                        if (pPlot.getY() > iEquator + 12): #12 of tolerance
                                                                #print("False4")
                                                                return False
                                                else:
                                                        if (pPlot.getY() < iEquator - 10): #10 of tolerance
                                                                #print("False5")
                                                                return False
                                        #east/west eurasia division
                                        if (playerID in con.lCivGroups[1]): #asian
                                                if (x < (lEurasia[1]-lEurasia[0])*65/100+lEurasia[0]):
                                                        #print("False7")
                                                        return False                                        
                                        if (playerID in con.lCivGroups[2]): #middle eastern
                                                if (x > (lEurasia[1]-lEurasia[0])*70/100+lEurasia[0] or x < (lEurasia[1]-lEurasia[0])*20/100+lEurasia[0]):
                                                        #print("False6")
                                                        return False
                                        if (playerID in con.lCivGroups[4]): #african
                                                if (x > (lEurasia[1]-lEurasia[0])*40/100+lEurasia[0]):
                                                        #print("False7")
                                                        return False                                        
                                        if (playerID in con.lCivGroups[3]): #mediterranean
                                                if (x > (lEurasia[1]-lEurasia[0])*70/100+lEurasia[0]):
                                                        #print("False6")
                                                        return False
                                        if (playerID in con.lCivGroups[0]): #euro
                                                if (x > (lEurasia[1]-lEurasia[0])*70/100+lEurasia[0]):
                                                        #print("False6")
                                                        return False
                                                    
                                                    
                                if (lRolls[8] == 2):   #N/S division
                                        if (playerID in con.lHorizontalDivisionN):
                                                if (lRolls[0] == 0):
                                                        if (y < iHeight*3/7):
                                                                return False
                                                else:
                                                        if (y > iHeight*4/7):
                                                                return False
                                        elif (playerID in con.lHorizontalDivisionS):
                                                if (lRolls[0] == 0):
                                                        if (y > iHeight*4/7):
                                                                return False
                                                else:
                                                        if (y < iHeight*3/7):
                                                                return False
                                elif (lRolls[8] == 3): 
                                        if (playerID in con.lVerticalDivisionW):
                                                if (lRolls[0] == 0):
                                                        if (y < iHeight*3/7):
                                                                return False
                                                else:
                                                        if (y > iHeight*4/7):
                                                                return False
                                        elif (playerID in con.lVerticalDivisionE):
                                                if (lRolls[0] == 0):
                                                        if (y > iHeight*4/7):
                                                                return False
                                                else:
                                                        if (y < iHeight*3/7):
                                                                return False                                        

                                    
                else:
                        if (areaID != lAmerica[4] and areaID != lAmerica[5]):
                                return False
                        if (x < lAmerica[0] or x > lAmerica[1] or y < lAmerica[2] or y > lAmerica[3]):
                                return False
                        if (not bSecondPass):
                                if (lRolls[8] == 1):   #equator N/S division
                                        iEquator = iHeight/2 - iHeight*13/100 -1;
                                        if (lRolls[0] == 1):
                                                iEquator = iHeight/2 + iHeight*13/100 -1; #necessary, because rolls[8] can be 1 with medium likelihood as well
                                        if (playerID in con.lEquatorDivisionN):
                                                if (lRolls[0] == 0):
                                                        if (pPlot.getY() < iEquator):
                                                                #print("False2")
                                                                return False
                                                else:
                                                        if (pPlot.getY() > iEquator):
                                                                #print("False3")
                                                                return False
                                        elif (playerID in con.lEquatorDivisionS):
                                                if (lRolls[0] == 0):
                                                        if (pPlot.getY() > iEquator):
                                                                #print("False4")
                                                                return False
                                                else:
                                                        if (pPlot.getY() < iEquator):
                                                                #print("False5")
                                                                return False
                                                            
                                if (playerID == con.iAmerica):
                                        if (CyMap().getSeaLevel() == 1): #high likelihood
                                                if (y < iHeight/2):
                                                        return False

                return True



        def resetStartingPlots(self, Map, iGridX, iGridY):
                for i in range(iNumMajorPlayers):
                        print(i, gc.getPlayer(i).getStartingPlot().getX(), gc.getPlayer(i).getStartingPlot().getY())
                for iX in range(iGridX):
                        for iY in range(iGridY):
                                if (Map.plot(iX,iY).isStartingPlot()):
                                        print(iX,iY)
                                        #Map.plot(iX,iY).setStartingPlot(False)
                for i in range(iNumMajorPlayers):
                        gc.getPlayer(i).setStartingPlot(None, True)
                        print(i, gc.getPlayer(i).getStartingPlot().getX(), gc.getPlayer(i).getStartingPlot().getY())

    

        def improveStartingLocation(self, iCiv, startX, startY):
            
                #print("iCiv, startX, startY", iCiv, startX, startY)
            
                for x in range(startX-1, startX+2):
                        for y in range(startY-1, startY+2):
                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                if (pCurrent.getBonusType(-1) == con.iSwamp or pCurrent.getTerrainType() == con.iTundra):
                                        pCurrent.setTerrainType(con.iGrass, True, True)                                        
                                        if (pCurrent.getBonusType(-1) == con.iSwamp):
                                                pCurrent.setFeatureType(con.iForest, 0)
                                                pCurrent.setBonusType(-1)

                for x in range(startX-3, startX+4):
                        for y in range(startY-3, startY+4):
                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                if (pCurrent.getTerrainType() == con.iTundra):
                                        if (gc.getGame().getSorenRandNum(2, '50%') == 1):
                                                pCurrent.setTerrainType(con.iGrass, True, True)
                                if (pCurrent.getTerrainType() == con.iSnow):
                                        pCurrent.setTerrainType(con.iTundra, True, True)

                pJungleList = []
                for x in range(startX-3, startX+4):
                        for y in range(startY-3, startY+4):
                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                if (pCurrent.getFeatureType() == con.iJungle):
                                        #if (pCurrent.getBonusType(-1) == -1):
                                        pJungleList.append(pCurrent)
                iListCounter = 0
                for pCurrent in pJungleList:
                        if iListCounter % 4 == 1:
                                pCurrent.setFeatureType(-1, 0)
                        iListCounter += 1
                pJungleList = []
                for x in range(startX-2, startX+3):
                        for y in range(startY-2, startY+3):
                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                if (pCurrent.getFeatureType() == con.iJungle):
                                        #if (pCurrent.getBonusType(-1) == -1):
                                        pJungleList.append(pCurrent)
                iListCounter = 0
                for pCurrent in pJungleList:
                        if iListCounter % 2 == 1:
                                pCurrent.setFeatureType(-1, 0)
                        iListCounter += 1

                bSilverAlreadyAdded = False
                for iPass in range(3):
                        iRadius = 2
                        iMinFood = 12
                        iMinShields = 7
                        iMinCommerce = 4
                        if (iPass == 2):
                                iRadius = 1
                                iMinFood = 6
                                iMinShields = 5
                                iMinCommerce = 2
                        iTotalFood = 0
                        iTotalShields = 0
                        iTotalCommerce = 0

                        bDoubleFood = False
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        if (self.isPlotInFatCross(startX, startY, x, y)):
                                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                iTotalFood += pCurrent.getYield(YieldTypes.YIELD_FOOD)
                                                iTotalShields += pCurrent.getYield(YieldTypes.YIELD_PRODUCTION)
                                                iTotalCommerce += pCurrent.getYield(YieldTypes.YIELD_COMMERCE)
                                                if (pCurrent.getYield(YieldTypes.YIELD_FOOD) >= 2):
                                                        bDoubleFood = True

                        if (bDoubleFood == False):
                                pSingleFoodPlotList = []
                                for x in range(startX-1, startX+2):
                                        for y in range(startY-1, startY+2):
                                                if (x != startX and y != startY):
                                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                        if (pCurrent.getYield(YieldTypes.YIELD_FOOD) == 1):
                                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                                        pSingleFoodPlotList.append(pCurrent)
                                if (len(pSingleFoodPlotList) > 0):
                                        chosenPlotIndex = gc.getGame().getSorenRandNum(len(pSingleFoodPlotList), 'random plot')
                                        if (pSingleFoodPlotList[chosenPlotIndex].isWater()):
                                                pSingleFoodPlotList[chosenPlotIndex].setBonusType(con.iFish)
                                        elif (pSingleFoodPlotList[chosenPlotIndex].isFlatlands()):
                                                pSingleFoodPlotList[chosenPlotIndex].setBonusType(con.iPig)

                                                
                        #print("iTotalFood", iTotalFood)
                        if (iTotalFood < iMinFood):
                                pFloodPlotList = []
                                pFreePlotList = []
                                for x in range(startX-1, startX+2):
                                        for y in range(startY-1, startY+2):
                                                if (x != startX and y != startY):
                                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                        if (pCurrent.getTerrainType() == con.iDesert and pCurrent.isFlatlands() and self.isRiverAdjacent(x,y)):
                                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                                        pFloodPlotList.append(pCurrent)
                                                        if ((pCurrent.getTerrainType() == con.iTundra or pCurrent.getTerrainType() == con.iGrass or pCurrent.getTerrainType() == con.iPlains or pCurrent.getTerrainType() == con.iDesert) and not pCurrent.isPeak()):
                                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                                        pFreePlotList.append(pCurrent)
                                #print("pFloodPlotList",pFloodPlotList)
                                #print("pFreePlotList",pFreePlotList)
                                if (len(pFloodPlotList) > 0):
                                        rndnum = gc.getGame().getSorenRandNum(len(pFloodPlotList), 'random plot')
                                        pFloodPlotList[rndnum].setFeatureType(con.iFloodPlains, 0)
                                        #pFloodPlotList[rndnum].setPlotType(PlotTypes.PLOT_LAND, True, True) #causes a weird shadow and it's too late to regenerate
                                elif (len(pFreePlotList) > 0):
                                        chosenPlotIndex = gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')
                                        if (pFreePlotList[chosenPlotIndex].getTerrainType() == con.iDesert):
                                                pFreePlotList[chosenPlotIndex].setTerrainType(con.iPlains, True, True)
                                        elif (pFreePlotList[chosenPlotIndex].getTerrainType() == con.iPlains):
                                                pFreePlotList[chosenPlotIndex].setTerrainType(con.iGrass, True, True)
                                        elif (pFreePlotList[chosenPlotIndex].getTerrainType() == con.iTundra):
                                                pFreePlotList[chosenPlotIndex].setTerrainType(con.iGrass, True, True)
                                        if (iPass > 0):
                                                if (self.isNewWorldCiv(iCiv)): 
                                                        pFreePlotList[chosenPlotIndex].setBonusType(con.iCorn)
                                                else:
                                                        pFreePlotList[chosenPlotIndex].setBonusType(con.iWheat)
                        if (iTotalShields < iMinShields):
                                pDesertPlotList = []
                                pJunglePlotList = []
                                pTundraPlotList = []
                                for x in range(startX-1, startX+2):
                                        for y in range(startY-1, startY+2):
                                                if (x != startX and y != startY):
                                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                        if (pCurrent.getTerrainType() == con.iDesert):
                                                                if (pCurrent.getFeatureType() == -1):
                                                                        pDesertPlotList.append(pCurrent)
                                                        if (pCurrent.getTerrainType() == con.iGrass and pCurrent.getFeatureType() == con.iJungle):
                                                                if (pCurrent.getBonusType(-1) == -1):
                                                                        pJunglePlotList.append(pCurrent)
                                                        if (pCurrent.getTerrainType() == con.iTundra):
                                                                if (pCurrent.getBonusType(-1) == -1):
                                                                        pTundraPlotList.append(pCurrent)
                                if (len(pDesertPlotList) > 0):
                                        rndnum = gc.getGame().getSorenRandNum(len(pDesertPlotList), 'random plot')
                                        pDesertPlotList[rndnum].setTerrainType(con.iPlains, True, True)
                                elif (len(pJunglePlotList) > 0):
                                        rndnum = gc.getGame().getSorenRandNum(len(pJunglePlotList), 'random plot')
                                        pJunglePlotList[rndnum].setFeatureType(con.iForest, 0)
                                elif (len(pTundraPlotList) > 0):
                                        rndnum = gc.getGame().getSorenRandNum(len(pTundraPlotList), 'random plot')
                                        pTundraPlotList[rndnum].setFeatureType(con.iForest, 2)
                                        #pTundraPlotList[rndnum].setPlotType(PlotTypes.PLOT_HILL, True, True) #causes no shadow and it's too late to regenerate

                        if (iTotalCommerce < iMinCommerce and bSilverAlreadyAdded == False):
                                pFreePlotList = []
                                for x in range(startX-1, startX+2):
                                        for y in range(startY-1, startY+2):
                                                if (x != startX and y != startY):
                                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                        if (not pCurrent.isPeak() and not pCurrent.isWater()):
                                                                if (pCurrent.getFeatureType() == -1 and pCurrent.getBonusType(-1) == -1):
                                                                        pFreePlotList.append(pCurrent)
                                if (len(pFreePlotList) > 0):
                                        rndnum = gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')
                                        if (gc.getGame().getSorenRandNum(3, 'roll') >= 1):
                                                pFreePlotList[rndnum].setBonusType(con.iSilver)
                                        else:
                                                pFreePlotList[rndnum].setBonusType(con.iGold)
                                        bSilverAlreadyAdded = True


                #up to classical
                pFreePlotList = []
                if (gc.getPlayer(iCiv).getBirthTurn() < con.i600BC): #RFCRAND
                        bNeedsResource = True
                        for x in range(startX-2, startX+3):
                                for y in range(startY-2, startY+3):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if (pCurrent.getBonusType(-1) == con.iMarble or pCurrent.getBonusType(-1) == con.iStone):
                                                bNeedsResource = False
                        if (bNeedsResource):      
                                for x in range(startX-4, startX+5):
                                        for y in range(startY-4, startY+5):
                                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                if ((pCurrent.getTerrainType() == con.iDesert or pCurrent.getTerrainType() == con.iPlains) and not pCurrent.isPeak() and not pCurrent.isWater()):
                                                        if (pCurrent.getBonusType(-1) == -1):
                                                                pFreePlotList.append(pCurrent)
                                iResource = -1
                                resourceRoll = gc.getGame().getSorenRandNum(3, 'stone/marble/nothing')
                                if (resourceRoll == 1):
                                        iResource = con.iMarble
                                elif (resourceRoll == 2):
                                        iResource = con.iStone
                                #print(pFreePlotList)
                                if (iResource != -1):
                                        if (len(pFreePlotList) > 0):
                                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(iResource)

                #stone
                if (iCiv == con.iEgypt or iCiv == con.iChina or iCiv == con.iBabylonia or iCiv == con.iMaya or iCiv == con.iMali or iCiv == con.iAztecs):
                        pFreePlotList = []
                        iRadius = 3
                        if (CyMap().getSeaLevel() >= 2):
                                iRadius = 3
                        if (CyMap().getSeaLevel() >= 4):
                                iRadius = 4                        
                        bAlreadyAround = False
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if ((pCurrent.getTerrainType() == con.iDesert or pCurrent.getTerrainType() == con.iPlains) and not pCurrent.isPeak() and not pCurrent.isWater()):
                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iStone):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iStone)
    
                #marble
                if (iCiv == con.iIndia or iCiv == con.iGreece or iCiv == con.iRome):
                        pFreePlotList = []
                        iRadius = 3
                        if (CyMap().getSeaLevel() >= 2):
                                iRadius = 3
                        if (CyMap().getSeaLevel() >= 4):
                                iRadius = 4                        
                        bAlreadyAround = False
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if ((pCurrent.getTerrainType() == con.iDesert or pCurrent.getTerrainType() == con.iPlains) and not pCurrent.isPeak() and not pCurrent.isWater()):
                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iMarble):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iMarble)

                #copper
                if (iCiv == con.iGreece or iCiv == con.iAmerica):
                        pFreePlotList = []
                        iRadius = 5
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 6
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 7                        
                        bAlreadyAround = False
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if (not pCurrent.isPeak() and not pCurrent.isWater()):
                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iCopper):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iCopper)
    
                #dye
                if (iCiv == con.iCarthage):
                        pFreePlotList = []
                        iRadius = 3
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 4
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 5                        
                        bAlreadyAround = False
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                    pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                    if (not pCurrent.isPeak() and not pCurrent.isWater()):
                                            if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == con.iForest):
                                                    if (not pCurrent.isOwned()):
                                                            pFreePlotList.append(pCurrent)
                                    if (pCurrent.getBonusType(-1) == con.iDye):
                                            bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iDye)
    
                #spices
                if (iCiv == con.iNetherlands):
                        pFreePlotList = []
                        iRadius = 4
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 4
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 5                        
                        bAlreadyAround = False
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if (not pCurrent.isPeak() and not pCurrent.isWater()):
                                                if (pCurrent.getBonusType(-1) == -1 and (pCurrent.getFeatureType() == con.iForest or pCurrent.getFeatureType() == con.iJungle)):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iSpices):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iSpices)

                #gold
                if (iCiv == con.iKhmer or iCiv == con.iInca):
                        pFreePlotList = []
                        iRadius = 4
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 5
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 6
                        bAlreadyAround = False
                        if (gc.getGame().getSorenRandNum(10-iRadius, 'roll') == 1):
                                bAlreadyAround = True #that is, skip
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if (not pCurrent.isPeak() and not pCurrent.isWater() and not pCurrent.isFlatlands()):
                                                if (pCurrent.getBonusType(-1) == -1):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iGold):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iGold)


                #Horse
                if (iCiv == con.iEgypt or iCiv == con.iPersia or iCiv == con.iCarthage or iCiv == con.iEthiopia or iCiv == con.iSpain or iCiv == con.iRussia or iCiv == con.iMongolia):
                        pFreePlotList = []
                        iRadius = 4
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 5
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 5                        
                        bAlreadyAround = False
                        if (gc.getGame().getSorenRandNum(10-iRadius, 'roll') == 1):
                                bAlreadyAround = True #that is, skip
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if ((pCurrent.getTerrainType() == con.iDesert or pCurrent.getTerrainType() == con.iPlains or pCurrent.getTerrainType() == con.iGrass) and not pCurrent.isPeak() and not pCurrent.isWater() and not pCurrent.isHills()):
                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iHorse):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iHorse)

                #Iron
                if (iCiv == con.iChina or iCiv == con.iRome or iCiv == con.iJapan or iCiv == con.iVikings or iCiv == con.iSpain or iCiv == con.iFrance or iCiv == con.iGermany):
                        pFreePlotList = []
                        iRadius = 3
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 4
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 5                        
                        bAlreadyAround = False
                        if (gc.getGame().getSorenRandNum(10-iRadius, 'roll') == 1):
                                bAlreadyAround = True #that is, skip
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if (not pCurrent.isPeak() and not pCurrent.isWater() and not pCurrent.isFlatlands()):
                                                if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iIron):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iIron)

                #oil
                if (iCiv == con.iArabia):
                        pFreePlotList = []
                        iRadius = 3
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 4
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 5                        
                        bAlreadyAround = False
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        #if (self.isPlotInFatCross(startX, startY, x, y)):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if ((pCurrent.getTerrainType() == con.iDesert) and not pCurrent.isPeak() and not pCurrent.isWater() and not pCurrent.isHills()):
                                                if (pCurrent.getBonusType(-1) == -1 and (pCurrent.getFeatureType() == con.iForest or pCurrent.getFeatureType() == con.iJungle)):
                                                        if (not pCurrent.isOwned()):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iOil):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iOil)

    
                #rice
                if (iCiv == con.iJapan):
                        pFreePlotList = []
                        iRadius = 2
                        if (CyMap().getSeaLevel() == 2):
                                iRadius = 3
                        elif (CyMap().getSeaLevel() >= 3):
                                iRadius = 4
                        bAlreadyAround = False
                        if (gc.getGame().getSorenRandNum(10-iRadius, 'roll') == 1):
                                bAlreadyAround = True #that is, skip
                        for x in range(startX-iRadius, startX+iRadius+1):
                                for y in range(startY-iRadius, startY+iRadius+1):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if ((pCurrent.getTerrainType() == con.iPlains or pCurrent.getTerrainType() == con.iGrass) and not pCurrent.isPeak() and not pCurrent.isWater() and not pCurrent.isHills()):
                                                if (pCurrent.getBonusType(-1) == -1):
                                                        if (not pCurrent.isOwned()):
                                                                #if (self.isPlotInFatCross(startX, startY, x, y)):
                                                                pFreePlotList.append(pCurrent)
                                        if (pCurrent.getBonusType(-1) == con.iGold):
                                                bAlreadyAround = True
                        if (len(pFreePlotList) > 0 and bAlreadyAround == False):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iRice)


                #medieval euros
                pFreePlotList = []
                if (iCiv in con.lCivGroups[0] and gc.getPlayer(iCiv).getBirthTurn() > con.i450AD): #RFCRAND 
                        for x in range(startX-2, startX+3):
                                for y in range(startY-2, startY+3):
                                        if (self.isPlotInFatCross(startX, startY, x, y)):
                                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                if ((pCurrent.getTerrainType() == con.iTundra or pCurrent.getTerrainType() == con.iGrass or pCurrent.getTerrainType() == con.iPlains) and not pCurrent.isPeak()):
                                                        if (pCurrent.getBonusType(-1) == -1):
                                                                pFreePlotList.append(pCurrent)
                        if (len(pFreePlotList) > 0):
                                chosenPlotIndex = gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')
                                if (pFreePlotList[chosenPlotIndex].getTerrainType() == con.iTundra):
                                                pFreePlotList[chosenPlotIndex].setTerrainType(con.iGrass, True, True)
                                pFreePlotList[chosenPlotIndex].setBonusType(con.iCow)



                        

                #late medieval euros
                pFreePlotList = []
                if (iCiv in con.lCivGroups[0] and gc.getPlayer(iCiv).getBirthTurn() > con.i900AD):  #RFCRAND
                        for x in range(startX-2, startX+3):
                                for y in range(startY-2, startY+3):
                                        if (self.isPlotInFatCross(startX, startY, x, y)):
                                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                if ((pCurrent.getTerrainType() == con.iGrass or pCurrent.getTerrainType() == con.iPlains) and not pCurrent.isPeak()):
                                                        if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                                pFreePlotList.append(pCurrent)
                        if (len(pFreePlotList) > 0):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iWheat)


                if (iCiv == con.iEngland or iCiv == con.iJapan or iCiv == con.iPortugal or iCiv == con.iNetherlands):
                        pFreePlotList = []
                        #if (( CyMap().plot( startX, startY ).area().getID() != self.getEurasiaInfo(4) and CyMap().getSeaLevel() <= 2) or (CyMap().plot( startX, startY ).area().getNumTiles() <= 120 and CyMap().getSeaLevel() == 2)):  #on island
                        for x in range(startX-2, startX+3):
                                for y in range(startY-2, startY+3):
                                        if (self.isPlotInFatCross(startX, startY, x, y)):
                                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                if (pCurrent.getTerrainType() == con.iCoast):
                                                        if (pCurrent.getBonusType(-1) == -1):
                                                                pFreePlotList.append(pCurrent)
                        if (len(pFreePlotList) > 0):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iFish)

                if (iCiv == con.iAmerica):
                        pFreePlotList = []
                        for x in range(startX-1, startX+2):
                                for y in range(startY-2, startY+2):
                                        if (self.isPlotInFatCross(startX, startY, x, y)):
                                                pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                                if ((pCurrent.getTerrainType() == con.iGrass or pCurrent.getTerrainType() == con.iPlains) and not pCurrent.isPeak()):
                                                        if (pCurrent.getBonusType(-1) == -1 and pCurrent.getFeatureType() == -1):
                                                                pFreePlotList.append(pCurrent)
                        if (len(pFreePlotList) > 0):
                                pFreePlotList[gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')].setBonusType(con.iWheat)
                        pFreePlotList = []
                        for x in range(startX-6, startX+6):
                                for y in range(startY-5, startY+6):
                                        pCurrent = CyMap().plot( x%CyMap().getGridWidth(), y%CyMap().getGridHeight() )
                                        if ((pCurrent.getTerrainType() == con.iGrass or pCurrent.getTerrainType() == con.iPlains) and not pCurrent.isPeak()):
                                                if (pCurrent.getBonusType(-1) == -1):
                                                        pFreePlotList.append(pCurrent)
                        if (len(pFreePlotList) > 0):
                                rndnum = gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')
                                pFreePlotList[rndnum].setBonusType(con.iCotton)
                                pFreePlotList.remove(pFreePlotList[rndnum])
                        if (len(pFreePlotList) > 0):
                                rndnum = gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')
                                pFreePlotList[rndnum].setBonusType(con.iCow)
                                pFreePlotList.remove(pFreePlotList[rndnum])
                        if (len(pFreePlotList) > 0):
                                rndnum = gc.getGame().getSorenRandNum(len(pFreePlotList), 'random plot')
                                pFreePlotList[rndnum].setBonusType(con.iPig)
                                pFreePlotList.remove(pFreePlotList[rndnum])


            

        def loadRandomWorldInfo(self):

                lEurasia = []
                lIsland1 = []
                lIsland2 = []
                lAfrica = []
                lAmerica = []
                lRolls = []
                lContinents = []        

                for i in range (5):
                    lEurasia.append(self.getEurasiaInfo(i))
                    lIsland1.append(self.getIsland1Info(i))
                    lIsland2.append(self.getIsland2Info(i))
                    lAfrica.append(self.getAfricaInfo(i))

                for i in range (6):  
                    lAmerica.append(self.getAmericaInfo(i))

                for i in range (12):                    
                    lRolls.append(self.getWorldShapeInfo(i))

                for i in range (6):  
                    lContinents.append(self.getRandomContinents(i))

                return (lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lContinents)
            

        def isEofRiver(self, x, y):

                pLeft = CyMap().plot( (x-1)%CyMap().getGridWidth(), y )
                return pLeft.isWOfRiver()


        def isSofRiver(self, x, y):

                pTop = CyMap().plot( x, (y+1)%CyMap().getGridHeight() )
                return pTop.isNOfRiver()

        def isRiverAdjacent(self, x, y):
                
                return (CyMap().plot(x,y).isWOfRiver() or CyMap().plot(x,y).isNOfRiver() or self.isEofRiver(x,y) or self.isSofRiver(x,y))

        def getPassableAreaSize(self, x, y, iMaxRadius):
                
                plotList = []
                plotList.append((x,y))
                for iRadius in range(iMaxRadius):
                        if iRadius == 0:
                                continue
                        #xList = [x-iRadius, x+iRadius+1]
                        #yList = [y-iRadius, y+iRadius+1]
                        for iLoopX in range(x-iRadius, x+iRadius+1):
                                for iLoopY in range(y-iRadius, y+iRadius+1):
                                        iLoopX = min(max(iLoopX,0),CyMap().getGridWidth()-1)
                                        iLoopY = min(max(iLoopY,0),CyMap().getGridHeight()-1)
                                        #print("prova", iLoopX, iLoopY)
                                        if ((iLoopX, iLoopY) not in plotList):
                                                pCurrent = CyMap().plot( iLoopX, iLoopY )
                                                if (pCurrent.getBonusType(-1) == con.iSwamp or pCurrent.isWater() or pCurrent.isPeak() or pCurrent.getFeatureType() == con.iJungle or pCurrent.getTerrainType() == con.iSnow): #snow is passable but useless (dangerous in icy climate)
                                                        pass
                                                else:
                                                        #print("dentro")
                                                        for iLoopListPlot in plotList:
                                                                #print(iLoopX, iLoopY, iLoopListPlot[0], iLoopListPlot[1])
                                                                if (self.isPlotAdjacent(iLoopX, iLoopY, iLoopListPlot[0], iLoopListPlot[1])):
                                                                        plotList.append((iLoopX, iLoopY))
                                                                        #print("append")
                                                                        if (len(plotList) == 50):
                                                                                return len(plotList)
                                                                        break
                #for iLoopListPlot in plotList:
                #        print(iLoopListPlot)
                return(len(plotList))
                         

        def isPlotAdjacent(self, x1, y1, x2, y2):
                if (x2 == x1 or x2 == x1+1 or x2 == x1-1):
                        if (y2 == y1 or y2 == y1+1 or y2 == y1-1):
                                return True
                return False

        def isPlotInFatCross(self, cityX, cityY, x, y):
                if (x == cityX+2 or x == cityX-2):
                        if (y == cityY+2 or y == cityY-2):
                                return False
                if (x == cityX and y == cityY):
                        return False
                return True

        def isNewWorldCiv(self, iCiv):
                SL = gc.getPlayer(iCiv).getStartingPlot()
                if (self.isNewWorld(SL.getX(), SL.getY())):
                        return True
                return False
                
        def isNewWorld(self, x, y):

                area = CyMap().plot(x, y).area()
                if (area == None):
                        #print("no area")
                        return False

##                if (area.getID() == self.getAmericaInfo(4) or area.getID() == self.getAmericaInfo(5)):
##                        #print("matching ID")
##                        return True

                if (CyMap().getSeaLevel() <= 2):      
                        if (x >= self.getAmericaInfo(0) and x <= self.getAmericaInfo(1) and y >= self.getAmericaInfo(2) and y <= self.getAmericaInfo(3)):
                                #print("in the box")
                                return True
                elif (CyMap().getSeaLevel() == 3):                                               
                        continentWidth = int(CyMap().getGridWidth()/3)
                        continentHeight = int(CyMap().getGridHeight()/2)

                        continentCounter = 0
                        for i in range(3):
                                continentWestX = 0 + i*continentWidth
                                for j in range(2):
                                        continentSouthY = 0 + j*continentHeight
                                        if (not CyMap().plot(15+continentCounter, 0).isWater()):
                                                if (x >= continentWestX and x <= continentWestX+continentWidth and y >= continentSouthY and y <= continentSouthY+continentHeight):
                                                        #print("in the box")
                                                        return True
                                        continentCounter = continentCounter + 1

                elif (CyMap().getSeaLevel() == 4):                        
                        if (area.getID() != CyMap().findBiggestArea(False).getID()):
                                if (area.getNumTiles() > 60):
                                        return True

                                        
                #print("nothing")
                return False

        def isOtherWorld(self, x, y, iPlayer):

                area = CyMap().plot(x, y).area()
                if (area == None):
                        return False

                startingPlot = gc.getPlayer(iPlayer).getStartingPlot()

                if (startingPlot.area().getID() == area.getID()):
                        return False

                startingPlotWorld = self.isNewWorld(startingPlot.getX(), startingPlot.getY())
                currentWorld = self.isNewWorld(x, y)

                if (startingPlotWorld == self.isNewWorld):
                        return False

                return True

                




##                        if (area.getNumCities() == 0):
##                                return True
##                        else:                                        
##                                for iLoopCiv in range(iNumMajorPlayers):
##                                        if (iLoopCiv in con.lCivBioOldWorld):
##                                                if (gc.getPlayer(iLoopCiv).getStartingPlot().area() != None):
##                                                        if (gc.getPlayer(iLoopCiv).getStartingPlot().area().getID() == area.getID()):
##                                                                return False
##                                return True


        def bestUnitAttack(self, iCiv):

                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())

                if (tCiv.isHasTech(con.iChemistry)):
                        return con.iGrenadier
                elif (tCiv.isHasTech(con.iCivilService) and tCiv.isHasTech(con.iMachinery)):
                        if (iCiv == iJapan):
                                return con.iJapanSamurai
                        elif (iCiv == iVikings):
                                return con.iVikingBeserker
                        else:
                                return con.iMaceman
                elif (tCiv.isHasTech(con.iHunting) and iCiv == iPersia):
                        return con.iPersiaImmortal
                elif (tCiv.isHasTech(con.iIronWorking)):
                        if (iCiv == iRome):
                                return con.iRomePraetorian
                        elif (iCiv == iAztecs):
                                return con.iAztecJaguar
                        else:
                                return con.iSwordsman                
                return con.iWarrior

        def bestUnitDefence(self, iCiv):

                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())

                if (tCiv.isHasTech(con.iRifling)):
                        if (iCiv == iEngland):
                                return con.iEnglishRedcoat
                        else:
                                return con.iRifleman
                elif (tCiv.isHasTech(con.iGunpowder)):
                        if (iCiv == iFrance):
                                return con.iFrenchMusketeer
                        elif (iCiv == iTurkey):
                                return con.iOttomanJanissary
                        elif (iCiv == iEthiopia):
                                return con.iEthiopianOromoWarrior
                        else:
                                return con.iMusketman
                elif (tCiv.isHasTech(con.iFeudalism) and tCiv.isHasTech(con.iArchery)):
                        return con.iLongbowman
                elif (tCiv.isHasTech(con.iArchery)):
                        if (iCiv == iBabylonia):
                                return con.iBabylonBowman
                        elif (iCiv == iMali):
                                return con.iMaliSkirmisher
                        else:
                                return con.iArcher
                return con.iWarrior

        def bestUnitCounter(self, iCiv):

                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())

                if (tCiv.isHasTech(con.iRifling)):
                        if (iCiv == iEngland):
                                return con.iEnglishRedcoat
                        else:
                                return con.iRifleman
                elif (tCiv.isHasTech(con.iEngineering)):
                        return con.iPikeman
                elif (tCiv.isHasTech(con.iMachinery) and tCiv.isHasTech(con.iArchery)):
                        if (iCiv == iChina):
                                return con.iChinaChokonu
                        else:
                                return con.iCrossbowman
                elif (tCiv.isHasTech(con.iBronzeWorking)):
                        if (iCiv == iMaya):
                                return con.iMayaHolkan
                        elif (iCiv == iGreece):
                                return con.iGreekPhalanx
                        elif (iCiv == iInca):
                                return con.iIncanQuechua
                        else:
                                return con.iAxeman
                elif (tCiv.isHasTech(con.iHunting)):
                        return con.iSpearman
                return None


        def bestUnitMounted(self, iCiv):

                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())

                if (tCiv.isHasTech(con.iRifling) and tCiv.isHasTech(con.iMilitaryTradition) and tCiv.isHasTech(con.iHorsebackRiding)):
                        if (iCiv == iRussia):
                                return con.iRussiaCossack
                        else:
                                return con.iCavalry
                elif (tCiv.isHasTech(con.iGunpowder) and tCiv.isHasTech(con.iMilitaryTradition) and tCiv.isHasTech(con.iHorsebackRiding)):
                        if (iCiv == iSpain):
                                return con.iSpanishConquistador
                        else:
                                return con.iCuirassier
                elif (tCiv.isHasTech(con.iGuilds) and tCiv.isHasTech(con.iHorsebackRiding)):
                        if (iCiv == iMongolia):
                                return con.iMongolKeshik
                        elif (iCiv == iArabia):
                                return con.iArabiaCamelarcher
                        else:
                                return con.iKnight
                elif (tCiv.isHasTech(con.iConstruction) and self.getIvoryAround(iCiv, 4) == True):
                        if (iCiv == iKhmer):
                                return con.iKhmerBallistaElephant
                        else:
                                return con.iWarElephant
                elif (tCiv.isHasTech(con.iHorsebackRiding)):
                        if (iCiv == iCarthage):
                                return con.iCarthageNumidianCavalry
                        elif (iCiv == iEgypt):
                                return con.iEgyptWarchariot
                        else:
                                return con.iHorseArcher
                elif (tCiv.isHasTech(con.iTheWheel)):
                        if (iCiv == iEgypt):
                                return con.iEgyptWarchariot
                        else:
                                return con.iChariot
                return None 

        def getIvoryAround(self, iCiv, iRadius):
                pStartingPlot = gc.getPlayer(iCiv).getStartingPlot()
                for x in range (pStartingPlot.getX() - iRadius, pStartingPlot.getX() + iRadius +1):
                        for y in range (pStartingPlot.getY() - iRadius, pStartingPlot.getY() + iRadius +1):
                                pCurrent = gc.getMap().plot(x,y)
                                if (pCurrent.getBonusType(-1) == con.iIvory):
                                        return True
                return False

        def bestUnitSiege(self, iCiv):

                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())
                
                if (tCiv.isHasTech(con.iGunpowder)):
                        return con.iCannon
                elif (tCiv.isHasTech(con.iMathematics)):
                        return con.iCatapult
                return None 
                            
        def bestUnitSeaTransport(self, iCiv):

                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())
                
                if (tCiv.isHasTech(con.iAstronomy) and tCiv.isHasTech(con.iSailing)):
                        if (iCiv == iNetherlands):
                                return con.iNetherlandsOostindievaarder
                        else:
                                return con.iGalleon
                elif (tCiv.isHasTech(con.iCompass) and tCiv.isHasTech(con.iSailing)):
                        if (iCiv == iPortugal):
                                return con.iPortugalCarrack
                elif (tCiv.isHasTech(con.iSailing)):
                        return con.iGalley
                return None 

        def bestUnitSeaCombat(self, iCiv):

                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())
                
                if (tCiv.isHasTech(con.iMilitaryScience) and tCiv.isHasTech(con.iAstronomy) and tCiv.isHasTech(con.iSailing)):
                        return con.iFrigate
                elif (tCiv.isHasTech(con.iMetalCasting) and tCiv.isHasTech(con.iSailing)):
                        return con.iTrireme
                elif (tCiv.isHasTech(con.iSailing)):
                        return con.iGalley
                return None




            
                
