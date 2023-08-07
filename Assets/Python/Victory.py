# Rhye's and Fall of Civilization - Historical Victory Goals


from CvPythonExtensions import *
import CvUtil
import PyHelpers   
import Popup
import cPickle as pickle
import Consts as con
import RFCUtils
utils = RFCUtils.RFCUtils()

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer





### Constants ###

i850BC = con.i850BC #new timeline
i700BC = con.i700BC
i250BC = con.i250BC #new timeline
i100BC = con.i100BC #new timeline
i50AD = con.i50AD
i140AD = con.i140AD #new timeline
i170AD = con.i170AD
i200AD = con.i200AD #new timeline
i250AD = con.i250AD
i350AD = con.i350AD
i450AD = con.i450AD
i470AD = con.i470AD #new timeline
i500AD = con.i500AD #new timeline
i600AD = con.i600AD
i700AD = con.i700AD
i900AD = con.i900AD
i1000AD = con.i1000AD
i1200AD = con.i1200AD
i1300AD = con.i1300AD
i1400AD = con.i1400AD
i1450AD = con.i1450AD
i1500AD = con.i1500AD
i1600AD = con.i1600AD
i1650AD = con.i1650AD
i1700AD = con.i1700AD
i1715AD = con.i1715AD
i1730AD = con.i1730AD
i1745AD = con.i1745AD
i1760AD = con.i1760AD
i1775AD = con.i1775AD
i1800AD = con.i1800AD
i1820AD = con.i1820AD
i1850AD = con.i1850AD
i1860AD = con.i1860AD
i1870AD = con.i1870AD
i1880AD = con.i1880AD
i1900AD = con.i1900AD
i1910AD = con.i1910AD
i1930AD = con.i1930AD
i1940AD = con.i1940AD
i1950AD = con.i1950AD
i2000AD = con.i2000AD


iAncient = con.iAncient
iClassical = con.iClassical
iMedieval = con.iMedieval
iRenaissance = con.iRenaissance
iIndustrial = con.iIndustrial
iModern = con.iModern
iFuture = con.iFuture

tCoreAreasTL = con.tCoreAreasTL
tCoreAreasBR = con.tCoreAreasBR
tNormalAreasTL = con.tNormalAreasTL
tNormalAreasBR = con.tNormalAreasBR
tAmericasTL = con.tAmericasTL
tAmericasBR = con.tAmericasBR
tSAmericaTL = (24, 3)
tSAmericaBR = (43, 32)
tNCAmericaTL = (3, 33)
tNCAmericaBR = (37, 63)
tCAmericaTL = (12, 33)
tCAmericaBR = (33, 43)
tSiberiaTL = (82, 50)
tSiberiaBR = (112, 64)
tNECanadaTL = (22, 50)
tNECanadaBR = (37, 60)
tLouisianaTL = (19, 42)
tLouisianaBR = (24, 50)
tEastCoastTL = (25, 42)
tEastCoastBR = (35, 52)
tSouthAfricaTL = (61, 10)
tSouthAfricaBR = (72, 18)
tAustraliaTL = (103, 10)
tAustraliaBR = (118, 22)
tScandinaviaTL = (57, 55)
tScandinaviaBR = (65, 65)
tNearEastTL = (70, 37)
tNearEastBR = (78, 45)
tCarthageTL = (50, 36)
tCarthageBR = (61, 39)
tAfricaTL = (45, 10)
tAfricaBR = (76, 39)
tAsiaTL = (73, 29)
tAsiaBR = (121, 64)
tOceaniaTL = (99, 5)
tOceaniaBR = (123, 28)
tMediterraneanTL = (51, 36)
tMediterraneanBR = (73, 46)
tHokkaidoTL = (115, 50)
tHokkaidoBR = (116, 52)
tHonshuTL = (112, 44)
tHonshuBR = (116, 49)
tBalkansTL = (64, 40)
tBalkansBR = (68, 47)
tBlackSeaTL = (67, 44)
tBlackSeaBR = (76, 50)
tMesopotamiaTL = (73, 37)
tMesopotamiaBR = (78, 42)
tFranceTL = (51, 47)
tEuropeTL = (44, 40)
tEuropeBR = (68, 65)
##tNubiaTL = (67, 29)
##tNubiaBR = (74, 32)
##tEastAfricaTL = (67, 20)
##tEastAfricaBR = (77, 28)
tSomaliaTL = (73, 24)
tSomaliaBR = (77, 29)
tSubeqAfricaTL = (60, 10)
tSubeqAfricaBR = (72, 29)
tBrazilTL = (32, 14)
tBrazilBR = (43, 30)

# initialise player variables
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


pEgypt = gc.getPlayer(iEgypt)
pIndia = gc.getPlayer(iIndia)
pChina = gc.getPlayer(iChina)
pBabylonia = gc.getPlayer(iBabylonia)
pGreece = gc.getPlayer(iGreece)
pPersia = gc.getPlayer(iPersia)
pCarthage = gc.getPlayer(iCarthage)
pRome = gc.getPlayer(iRome)
pJapan = gc.getPlayer(iJapan)
pEthiopia = gc.getPlayer(iEthiopia)
pMaya = gc.getPlayer(iMaya)
pVikings = gc.getPlayer(iVikings)
pArabia = gc.getPlayer(iArabia)
pKhmer = gc.getPlayer(iKhmer)
pSpain = gc.getPlayer(iSpain)
pFrance = gc.getPlayer(iFrance)
pEngland = gc.getPlayer(iEngland)
pGermany = gc.getPlayer(iGermany)
pRussia = gc.getPlayer(iRussia)
pNetherlands = gc.getPlayer(iNetherlands)
pHolland = gc.getPlayer(iHolland)
pMali = gc.getPlayer(iMali)
pTurkey = gc.getPlayer(iTurkey)
pPortugal = gc.getPlayer(iPortugal)
pInca = gc.getPlayer(iInca)
pMongolia = gc.getPlayer(iMongolia)
pAztecs = gc.getPlayer(iAztecs)
pAmerica = gc.getPlayer(iAmerica)
pIndependent = gc.getPlayer(iIndependent)
pIndependent2 = gc.getPlayer(iIndependent2)
pNative = gc.getPlayer(iNative)
pCeltia = gc.getPlayer(iCeltia)
pBarbarian = gc.getPlayer(iBarbarian)

teamEgypt = gc.getTeam(pEgypt.getTeam())
teamIndia = gc.getTeam(pIndia.getTeam())
teamChina = gc.getTeam(pChina.getTeam())
teamBabylonia = gc.getTeam(pBabylonia.getTeam())
teamGreece = gc.getTeam(pGreece.getTeam())
teamPersia = gc.getTeam(pPersia.getTeam())
teamCarthage = gc.getTeam(pCarthage.getTeam())
teamRome = gc.getTeam(pRome.getTeam())
teamJapan = gc.getTeam(pJapan.getTeam())
teamEthiopia = gc.getTeam(pEthiopia.getTeam())
teamMaya = gc.getTeam(pMaya.getTeam())
teamVikings = gc.getTeam(pVikings.getTeam())
teamArabia = gc.getTeam(pArabia.getTeam())
teamKhmer = gc.getTeam(pKhmer.getTeam())
teamSpain = gc.getTeam(pSpain.getTeam())
teamFrance = gc.getTeam(pFrance.getTeam())
teamEngland = gc.getTeam(pEngland.getTeam())
teamGermany = gc.getTeam(pGermany.getTeam())
teamRussia = gc.getTeam(pRussia.getTeam())
teamNetherlands = gc.getTeam(pNetherlands.getTeam())
teamHolland = gc.getTeam(pHolland.getTeam())
teamMali = gc.getTeam(pMali.getTeam())
teamTurkey = gc.getTeam(pTurkey.getTeam())
teamPortugal = gc.getTeam(pPortugal.getTeam())
teamInca = gc.getTeam(pInca.getTeam())
teamMongolia = gc.getTeam(pMongolia.getTeam())
teamAztecs = gc.getTeam(pAztecs.getTeam())
teamAmerica = gc.getTeam(pAmerica.getTeam())
teamIndependent = gc.getTeam(pIndependent.getTeam())
teamIndependent2 = gc.getTeam(pIndependent2.getTeam())
teamNative = gc.getTeam(pNative.getTeam())
teamCeltia = gc.getTeam(pCeltia.getTeam())
teamBarbarian = gc.getTeam(pBarbarian.getTeam())

#RFCRAND
tRadius = con.tRadius

class Victory:

     
##################################################
### Secure storage & retrieval of script data ###
################################################   
		           

        def getGoal( self, i, j ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGoals'][i][j]

        def setGoal( self, i, j, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGoals'][i][j] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getReligionFounded( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lReligionFounded'][iCiv]

        def setReligionFounded( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lReligionFounded'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getEnslavedUnits( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iEnslavedUnits']

        def getRazedByMongols( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iRazedByMongols']
            
        def setRazedByMongols( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iRazedByMongols'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getEnglishEras( self, i ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lEnglishEras'][i]

        def setEnglishEras( self, i, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lEnglishEras'][i] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getGreekTechs( self, i ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGreekTechs'][i]

        def setGreekTechs( self, i, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGreekTechs'][i] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        def getWondersBuilt( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lWondersBuilt'][iCiv]

        def setWondersBuilt( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lWondersBuilt'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        def get2OutOf3( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['l2OutOf3'][iCiv]

        def set2OutOf3( self, iCiv, bNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['l2OutOf3'][iCiv] = bNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getNumSinks( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iNumSinks']
            
        def setNumSinks( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iNumSinks'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getBabylonianTechs( self, i ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lBabylonianTechs'][i]

        def setBabylonianTechs( self, i, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lBabylonianTechs'][i] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getMediterraneanColonies( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iMediterraneanColonies']
            
        def setMediterraneanColonies( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iMediterraneanColonies'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        #RFCRAND
        def getEnglishColonies( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iEnglishColonies']
            
        def setEnglishColonies( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iEnglishColonies'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getRussianColonies( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iRussianColonies']
            
        def setRussianColonies( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iRussianColonies'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        def getPortugueseColonies( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iPortugueseColonies']
            
        def setPortugueseColonies( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iPortugueseColonies'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getFrenchColonies( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iFrenchColonies']
            
        def setFrenchColonies( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iFrenchColonies'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getNewWorld( self, i ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lNewWorld'][i]

        def setNewWorld( self, i, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lNewWorld'][i] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
#######################################
### Main methods (Event-Triggered) ###
#####################################  


        def checkOwnedCiv(self, iActiveCiv, iOwnedCiv):
                #RFCRAND
                SL = gc.getPlayer(iOwnedCiv).getStartingPlot()
                tTL = ((SL.getX() - 5)%CyMap().getGridWidth(), (SL.getY() - 5)%CyMap().getGridHeight())
                tBR = ((SL.getX() + 5)%CyMap().getGridWidth(), (SL.getY() + 5)%CyMap().getGridHeight())
                dummy1, plotList1 = utils.squareSearch( tTL, tBR, utils.ownedCityPlots, iActiveCiv )
                dummy2, plotList2 = utils.squareSearch( tTL, tBR, utils.ownedCityPlots, iOwnedCiv )
                if ((len(plotList1) >= 2 and len(plotList1) > len(plotList2)) or (len(plotList1) >= 1 and not gc.getPlayer(iOwnedCiv).isAlive())):
                        return True
                else:
                        return False


        def checkOwnedArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
                dummy1, plotList = utils.squareSearch( tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv )
                if (len(plotList) >= iThreshold):
                        return True
                else:
                        return False

        def checkFoundedArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
                dummy1, plotList = utils.squareSearch( tTopLeft, tBottomRight, utils.foundedCityPlots, iActiveCiv )
                if (len(plotList) >= iThreshold):
                        return True
                else:
                        return False

        def checkNotOwnedArea(self, iActiveCiv, tTopLeft, tBottomRight):
                dummy1, plotList = utils.squareSearch( tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv )
                if (len(plotList)):
                        return False
                else:
                        return True

        def checkNotOwnedArea_Skip(self, iActiveCiv, tTopLeft, tBottomRight, tSkipTopLeft, tSkipBottomRight):
                dummy1, plotList = utils.squareSearch( tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv )
                if (not len(plotList)):
                        return True
                else:
                        for loopPlot in plotList:
                                if not (loopPlot[0] >= tSkipTopLeft[0] and loopPlot[0] <= tSkipBottomRight[0] and \
                                    loopPlot[1] >= tSkipTopLeft[1] and loopPlot[1] <= tSkipBottomRight[1]):
                                        return False
                return True
                                        

        def checkOwnedCoastalArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
                dummy1, plotList = utils.squareSearch( tTopLeft, tBottomRight, utils.ownedCityPlots, iActiveCiv )
                iCounter = 0
                for i in range(len(plotList)):
                        x = plotList[i][0]
                        y = plotList[i][1]
                        plot = gc.getMap().plot(x, y)
                        if (plot.isCity()):
                               if (plot.getPlotCity().isCoastalOld()):
                                       iCounter += 1
                if (iCounter >= iThreshold):
                        return True
                else:
                        return False

        def checkFoundedCoastalArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
                dummy1, plotList = utils.squareSearch( tTopLeft, tBottomRight, utils.foundedCityPlots, iActiveCiv )
                iCounter = 0
                for i in range(len(plotList)):
                        x = plotList[i][0]
                        y = plotList[i][1]
                        plot = gc.getMap().plot(x, y)
                        if (plot.isCity()):
                               if (plot.getPlotCity().isCoastalOld()):
                                       iCounter += 1
                if (iCounter >= iThreshold):
                        return True
                else:
                        return False

        def checkFoundedNotCoastalArea(self, iActiveCiv, tTopLeft, tBottomRight, iThreshold):
                dummy1, plotList = utils.squareSearch( tTopLeft, tBottomRight, utils.foundedCityPlots, iActiveCiv )
                iCounter = 0
                for i in range(len(plotList)):
                        x = plotList[i][0]
                        y = plotList[i][1]
                        plot = gc.getMap().plot(x, y)
                        if (plot.isCity()):
                               if (not plot.getPlotCity().isCoastalOld()):
                                       iCounter += 1
                if (iCounter >= iThreshold):
                        return True
                else:
                        return False

        def checkTurn(self, iGameTurn):

                #debug
                #self.setGoal(iEgypt, 0, 1)
                #self.setGoal(iEgypt, 1, 1)
                #self.setGoal(iEgypt, 2, 1)

                pass
                #for iCiv in range(iNumPlayers):
                #    print (iCiv, self.getGoal(iCiv, 0), self.getGoal(iCiv, 1), self.getGoal(iCiv, 2))


                    
       	
        def checkPlayerTurn(self, iGameTurn, iPlayer):


                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return
                
                if (iPlayer == iEgypt):
                        if (pEgypt.isAlive()):
                            
                                if (iGameTurn == i850BC):
                                        if (pEgypt.countTotalCulture() >= 500):
                                                self.setGoal(iEgypt, 0, 1)
                                        else:
                                                self.setGoal(iEgypt, 0, 0)
                                                
                                if (iGameTurn == i170AD):
                                        if (pEgypt.countTotalCulture() >= 5000):
                                                self.setGoal(iEgypt, 2, 1)
                                        else:
                                                self.setGoal(iEgypt, 2, 0)
                                                
                                if (iGameTurn == i100BC+1):
                                        if (self.getGoal(iEgypt, 1) == -1):                                  
                                                self.setGoal(iEgypt, 1, 0)                      

                                                
                elif (iPlayer == iIndia):
                        if (pIndia.isAlive()):                                                            
                                                                
                                if (iGameTurn == i1200AD):
                                        iPop = pIndia.getRealPopulation()
                                        #iPop = pIndia.getTotalPopulation()
                                        #print ("india pop", pIndia.getTotalPopulation(), pIndia.getRealPopulation())
                                        bFirst = True
                                        for iCiv in range(iNumPlayers):
                                                #print ("other pop", iCiv, gc.getPlayer(iCiv).getTotalPopulation(), gc.getPlayer(iCiv).getRealPopulation())
                                                if (iPop < gc.getPlayer(iCiv).getRealPopulation()):
                                                        bFirst = False
                                                        break
                                        if (bFirst):                                                
                                                self.setGoal(iIndia, 2, 1)
                                        else:
                                                self.setGoal(iIndia, 2, 0)

                            
                        
                elif (iPlayer == iChina):
                        if (pChina.isAlive()):

                                if (self.getGoal(iChina, 0) == -1):
                                        if (iGameTurn > i1000AD):
                                                self.setGoal(iChina, 0, 0)


                                if (iGameTurn == i1400AD):      
                                        if (self.getGoal(iChina, 1) == -1): #see onCityAcquired()
                                                self.setGoal(iChina, 1, 1)

                                if (iGameTurn == i1600AD):
                                        if (pChina.getNumUnits() >= 120):
                                                self.setGoal(iChina, 2, 1)
                                        else:
                                                self.setGoal(iChina, 2, 0)


                elif (iPlayer == iBabylonia):
                        if (pBabylonia.isAlive()):
                                if (iGameTurn == i850BC):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()                                
                                        bestCity = self.calculateTopCityPopulation(capitalX, capitalY)                                        
                                        if (bestCity != -1):
                                                print ("bestCity.getOwner()", bestCity.getOwner())
                                                if (bestCity.getOwner() == iBabylonia and bestCity.getX() == capitalX and bestCity.getY() == capitalY):
                                                        self.setGoal(iBabylonia, 1, 1)
                                                else:
                                                        self.setGoal(iBabylonia, 1, 0)
                                        else:
                                                self.setGoal(iBabylonia, 1, 0)
                                if (iGameTurn == i700BC):           
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()                                
                                        bestCity = self.calculateTopCityCulture(capitalX, capitalY)                                        
                                        if (bestCity != -1):
                                                print ("bestCity.getOwner()", bestCity.getOwner())
                                                if (bestCity.getOwner() == iBabylonia and bestCity.getX() == capitalX and bestCity.getY() == capitalY):
                                                        self.setGoal(iBabylonia, 2, 1)
                                                else:
                                                        self.setGoal(iBabylonia, 2, 0)
                                        else:
                                                self.setGoal(iBabylonia, 2, 0)


                                                
                elif (iPlayer == iGreece):
                        if (pGreece.isAlive()):

                                if (self.getGoal(iGreece, 2) == -1):
                                        if (gc.getGame().getCircumnavigated() != -1):
                                                if (gc.getGame().getCircumnavigated() == iGreece):
                                                        self.setGoal(iGreece, 2, 1)
                                                else:
                                                        self.setGoal(iGreece, 2, 0)



                        
                elif (iPlayer == iPersia):
                        if (pPersia.isAlive()):

                                if (self.getGoal(iPersia, 0) == -1):
                                        if (iGameTurn <= i140AD):
                                                totalLand = gc.getMap().getLandPlots()
                                                persianLand = pPersia.getTotalLand()
                                                if (totalLand > 0):
                                                        landPercent = (persianLand * 100.0) / totalLand
                                                else:
                                                        landPercent = 0.0
                                                        
                                                if (landPercent >= 6.995): #it's shown as 7.00 in the victory screen) #RFCRAND
                                                        self.setGoal(iPersia, 0, 1)
                                        else:
                                                self.setGoal(iPersia, 0, 0)

                                if (self.getGoal(iPersia, 1) == -1):
                                        if (iGameTurn <= i350AD):
                                                iCounter = 0
                                                apCityList = PyPlayer(iPersia).getCityList()
                                                for i in range(con.iSpaceElevator+1 - con.iPyramid):
                                                        iWonder = i + con.iPyramid
                                                        iWonderFlag = 0                                                        
                                                        for pCity in apCityList:
                                                                if (pCity.hasBuilding(iWonder)):
                                                                        iWonderFlag = 1
                                                                        break
                                                        #print ("Persian UHV", iWonder, pPersia.getBuildingClassCount(iWonder), iWonderFlag)
                                                        #iCounter += pPersia.getBuildingClassCount(iWonder) #BUGGY!
                                                        iCounter += iWonderFlag
                                                for i in range(con.iMoaiStatues+1 - con.iArtemis):
                                                        iWonder = i + con.iArtemis
                                                        iWonderFlag = 0
                                                        for pCity in apCityList:
                                                                if (pCity.hasBuilding(iWonder)):
                                                                        iWonderFlag = 1
                                                                        break
                                                        iCounter += iWonderFlag
                                                for i in range(con.iOlympicPark+1 - con.iApostolicPalace):
                                                        iWonder = i + con.iApostolicPalace
                                                        iWonderFlag = 0
                                                        for pCity in apCityList:
                                                                if (pCity.hasBuilding(iWonder)):
                                                                        iWonderFlag = 1
                                                                        break
                                                        iCounter += iWonderFlag
                                                for pCity in apCityList:
                                                        if (pCity.hasBuilding(con.iFlavianAmphitheatre)):
                                                                iCounter += 1
                                                                break
                                                if (iCounter >= 7):
                                                        self.setGoal(iPersia, 1, 1)
                                        else:
                                                self.setGoal(iPersia, 1, 0)
                            
                                if (iGameTurn == i350AD):
                                        iCounter = 0
                                        for iReligion in range(con.iNumReligions):
                                                iCurrentShrine = con.iShrine + iReligion*4
                                                apCityList = PyPlayer(iPersia).getCityList()
                                                for pCity in apCityList:
                                                        if (pCity.hasBuilding(iCurrentShrine)):
                                                                iCounter += 1
                                                                break
                                                #iCounter += pPersia.getBuildingClassCount(con.iShrine + iReligion*4) #BUGGY!
                                        if (iCounter >= 2):
                                                self.setGoal(iPersia, 2, 1)
                                        else:
                                                self.setGoal(iPersia, 2, 0)



                                                
                elif (iPlayer == iCarthage):
                        if (pCarthage.isAlive()):


                                if (self.getGoal(iCarthage, 1) == -1):
                                        if (iGameTurn <= i200AD):
                                                #if (pCarthage.countOwnedBonuses(con.iDye) + pCarthage.getBonusImport(con.iDye) >= 3):
                                                if (pCarthage.getNumAvailableBonuses(con.iDye) >= 3):
                                                        self.setGoal(iCarthage, 1, 1)
                                        else:
                                                self.setGoal(iCarthage, 1, 0)
                                                
                                if (iGameTurn == i100BC):                                              
                                        #RFCRAND
                                        if (self.checkOwnedCoastalArea(iCarthage, (0,0), (CyMap().getGridWidth(), CyMap().getGridHeight()), 5)):
                                                self.setGoal(iCarthage, 0, 1)
                                        else:
                                                self.setGoal(iCarthage, 0, 0)   
                                #if (self.getGoal(iCarthage, 1) == -1):
                                #        if (iGameTurn == i350AD+1):
                                #                self.setGoal(iCarthage, 1, 0)

                                    

                                if (self.getGoal(iCarthage, 2) == -1):
                                        if (gc.getGame().getCircumnavigated() != -1):
                                                if (gc.getGame().getCircumnavigated() == iCarthage):
                                                        self.setGoal(iCarthage, 2, 1)
                                                else:
                                                        self.setGoal(iCarthage, 2, 0)

                elif (iPlayer == iRome):
                        if (pRome.isAlive()):

                                if (iGameTurn <= i200AD):
                                        if (self.getGoal(iRome, 0) == -1):
                                                iCounterBarracks = 0
                                                iCounterAqueduct = 0
                                                iCounterColosseum = 0
                                                cityList = PyPlayer(iRome).getCityList()                                        
                                                for city in cityList:
                                                        if (city.hasBuilding(con.iBarracks)):
                                                                iCounterBarracks += 1
                                                        if (city.hasBuilding(con.iAqueduct)):
                                                                iCounterAqueduct += 1
                                                        if (city.hasBuilding(con.iColosseum)):
                                                                iCounterColosseum += 1
        ##                                                if (not city.isConnectedToCapital(iRome)):
        ##                                                        bConditions = False
                                                if (iCounterBarracks >= 5 and iCounterAqueduct >= 5 and iCounterColosseum >= 5):
                                                        self.setGoal(iRome, 0, 1)
                                                        
                                if (iGameTurn == i200AD+1):
                                        if (self.getGoal(iRome, 0) == -1):
                                                self.setGoal(iRome, 0, 0)  
                                    
                                if (iGameTurn == i470AD):                                              
                                        #RFCRAND
                                        bLargest = True
                                        romanLand = pRome.getTotalLand()
                                        for iLoopCiv in range(iNumMajorPlayers):
                                                if (gc.getPlayer(iLoopCiv).getTotalLand() > romanLand):
                                                        bLargest = False
                                                        
                                        if (bLargest == True):
                                                self.setGoal(iRome, 1, 1)  
                                        else:
                                                self.setGoal(iRome, 1, 0)

                                                
                                if (iGameTurn == i1000AD):      
                                        if (self.getGoal(iRome, 2) == -1): #see onCityAcquired()
                                                self.setGoal(iRome, 2, 1)

                        
                elif (iPlayer == iJapan):
                        if (pJapan.isAlive()):

                            
                                if (iGameTurn == i1650AD):
                                        bForeignPresence = False
                                        #Honshu
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()
                                        iRadius = 5
                                        for x in range(capitalX-iRadius, capitalX+iRadius+1):
                                                for y in range(capitalY-iRadius, capitalY+iRadius+1):
                                                        pCurrent = gc.getMap().plot(x,y)
                                                        if (not pCurrent.isWater()):
                                                                for iLoop in range(iNumMajorPlayers): #no minor civs
                                                                        if (iLoop != iJapan):
                                                                                if (pCurrent.getCulture(iLoop) > 0):
                                                                                        bForeignPresence = True
                                                                                        print (iPlayer, "presence in Japan")

                                        print ("bForeignPresence ", bForeignPresence)
                                        if (bForeignPresence == False):
                                                self.setGoal(iJapan, 0, 1)
                                        else:
                                                self.setGoal(iJapan, 0, 0)

                                if (iGameTurn == i1930AD):
                                        if (gc.getGame().getTeamRank(iJapan) == 0):
                                                self.setGoal(iJapan, 1, 1)
                                        else:
                                                self.setGoal(iJapan, 1, 0)

                                                
##                                if (iGameTurn == i1850AD):      
##                                        if (self.getGoal(iJapan, 2) == -1): #see onCityAcquired()
##                                                self.setGoal(iJapan, 2, 1)
                                        


                elif (iPlayer == iEthiopia):
                        if (pEthiopia.isAlive()):
                                
                                if (iGameTurn == i1500AD):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()
                                        iRadius = 10                                
                                        
                                        bAfrica = True                                        
                                        for iEuroCiv in range(iNumPlayers):
                                                if (iEuroCiv in con.lCivGroups[0]):
                                                        #RFCRAND        
                                                        if (self.checkNotOwnedArea(iEuroCiv, (capitalX - iRadius, capitalY - iRadius), (capitalX + iRadius, capitalY + iRadius)) == False):
                                                                bAfrica = False
                                                                break
                                        if (bAfrica):
                                                self.setGoal(iEthiopia, 1, 1)
                                        else:
                                                self.setGoal(iEthiopia, 1, 0)

                                if (iGameTurn == i1910AD):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()
                                        iRadius = 10                                

                                        bAfrica = True
                                        for iEuroCiv in range(iNumPlayers):
                                                if (iEuroCiv in con.lCivGroups[0]):
                                                        #RFCRAND  
                                                        if (self.checkNotOwnedArea(iEuroCiv, (capitalX - iRadius, capitalY - iRadius), (capitalX + iRadius, capitalY + iRadius)) == False):
                                                                bAfrica = False
                                                                break
                                        if (bAfrica):
                                                self.setGoal(iEthiopia, 2, 1)
                                        else:
                                                self.setGoal(iEthiopia, 2, 0)

                elif (iPlayer == iMaya):
                        if (pMaya.isAlive()):

                                if (iGameTurn == i600AD+1):
                                        if (self.getGoal(iMaya, 0) == -1): #see onTechAcquired()                                        
                                                self.setGoal(iMaya, 0, 0)

                                if (iGameTurn == i900AD+1):
                                        if (self.getGoal(iMaya, 1) == -1): #see onBuildingBuilt()
                                                self.setGoal(iMaya, 1, 0)

                                if (iGameTurn == i1745AD):      
                                        if (self.getGoal(iMaya, 2) == -1): #see onCityAcquired()
                                                self.setGoal(iMaya, 2, 1)


                                                

                elif (iPlayer == iVikings):
                        if (pVikings.isAlive()):

                                if (iGameTurn == i1500AD):
                                        if (pVikings.getGold() >= 5000):
                                                self.setGoal(iVikings, 0, 1)
                                        else:
                                                self.setGoal(iVikings, 0, 0)


                        
                elif (iPlayer == iArabia):
                        if (pArabia.isAlive()):


                                if (self.getGoal(iArabia, 2) == -1):
                                        religionPercent = gc.getGame().calculateReligionPercent(con.iIslam)
                                        #print ("religionPercent", religionPercent)
                                        if (religionPercent >= 40.0):
                                                self.setGoal(iArabia, 2, 1)

                                                

                                if (iGameTurn == i1300AD):
                                        iCounter = 0
                                        for iReligion in range(con.iNumReligions):
                                                iCurrentShrine = con.iShrine + iReligion*4
                                                apCityList = PyPlayer(iArabia).getCityList()
                                                for pCity in apCityList:
                                                        if (pCity.hasBuilding(iCurrentShrine)):
                                                                iCounter += 1
                                                                break
                                                #iCounter += pArabia.getBuildingClassCount(con.iShrine + iReligion*4) #BUGGY!                                                
                                                #print (iReligion, con.iShrine + iReligion*4, pArabia.getBuildingClassCount(con.iShrine + iReligion*4))
                                        if (iCounter >= 3):
                                                self.setGoal(iArabia, 0, 1)
                                        else:
                                                self.setGoal(iArabia, 0, 0)



                            
                                if (iGameTurn >= gc.getPlayer(iSpain).getBirthTurn()+1 and iGameTurn <= i1300AD): #RFCRAND
                                        if (self.getGoal(iArabia, 1) == -1):
                                                #RFCRAND
                                                iOwnedCivs = 0
                                                for iLoopCiv in range(iNumMajorPlayers):
                                                        if (iLoopCiv != iArabia):
                                                                if (utils.getInThisGame(iLoopCiv)):
                                                                        if (self.checkOwnedCiv(iArabia, iLoopCiv) or gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isVassal(iArabia)):                                                                
                                                                                iOwnedCivs += 1
                                                                                if (iOwnedCivs == 3):
                                                                                        break                                     
                                                if (iOwnedCivs >= 3):
                                                        self.setGoal(iArabia, 1, 1)
                                elif (iGameTurn > i1300AD):
                                        if (self.getGoal(iArabia, 1) == -1):
                                                        self.setGoal(iArabia, 1, 0)



                elif (iPlayer == iKhmer):
                        if (pKhmer.isAlive()):

                                if (iGameTurn == i1450AD):
                                        print ("khmer culture", pKhmer.countTotalCulture())
                                        if (pKhmer.countTotalCulture() >= 12000):
                                                self.setGoal(iKhmer, 0, 1)
                                        else:
                                                self.setGoal(iKhmer, 0, 0)

                                                
                                if (iGameTurn == i1450AD):
                                        apCityList = PyPlayer(iKhmer).getCityList()
                                        iTotalPopulation = 0
                                        for pCity in apCityList:			
                                                iTotalPopulation += pCity.getPopulation()
                                        if (iTotalPopulation / len(apCityList) >= 10):
                                                self.setGoal(iKhmer, 1, 1)
                                        else:
                                                self.setGoal(iKhmer, 1, 0)                                        
                                        #bestCity = self.calculateTopCityPopulation(102, 34)                                        #if (bestCity != -1):
                                        #        if (bestCity.getOwner() == iKhmer and bestCity.getX() == 102 and bestCity.getY() == 34):
                                        #                self.setGoal(iKhmer, 1, 1)
                                        #        else:
                                        #                self.setGoal(iKhmer, 1, 0)


                                if (self.getGoal(iKhmer, 2) == -1):
                                        religionPercent = gc.getGame().calculateReligionPercent(con.iBuddhism)
                                        #print ("religionPercent", religionPercent)
                                        if (religionPercent >= 30.0):
                                                self.setGoal(iKhmer, 2, 1)
                                                


                        
                elif (iPlayer == iSpain):
                        if (pSpain.isAlive()):

##                                if (self.getGoal(iSpain, 0) == -1):
##                                        if (gc.getGame().getCircumnavigated() != -1):
##                                                if (gc.getGame().getCircumnavigated() == iSpain):
##                                                        self.setGoal(iSpain, 0, 1)
##                                                else:
##                                                        self.setGoal(iSpain, 0, 0)

                                                    

                                if (iGameTurn == i1700AD):
                                        bAmericas = True
                                        #RFCRAND
                                        for iPlayerLoop in range(iNumMajorPlayers):#gc.getMAX_PLAYERS()):
                                                if (iPlayerLoop == iFrance or iPlayerLoop == iEngland or iPlayerLoop == iNetherlands):
                                                        apCityList = PyPlayer(iPlayerLoop).getCityList()

                                                        for pCity in apCityList:			
                                                                if (utils.isNewWorld(pCity.GetCy().getX(), pCity.GetCy().getY())):
                                                                #if (pCity.GetCy().area().getID() == utils.getAmericaInfo(4) or pCity.GetCy().area().getID() == utils.getAmericaInfo(5)):
                                                                        bAmericas = False
                                                                        break
                                                                        break
                                        if (bAmericas):
                                                self.setGoal(iSpain, 1, 1)
                                        else:
                                                self.setGoal(iSpain, 1, 0)

                                if (iGameTurn == i1760AD):
                                        #RFCRAND
                                        bAmer = False
                                        for iLoopCiv in range(iNumMajorPlayers):
                                                if (iLoopCiv != iSpain):
                                                        if (utils.getInThisGame(iLoopCiv)):
                                                                if ((CyMap().getSeaLevel() <= 1 and (iLoopCiv in con.lCivBioNewWorld)) or (CyMap().getSeaLevel() == 2 and utils.isNewWorldCiv(iLoopCiv))):
                                                                        if (self.checkOwnedCiv(iSpain, iLoopCiv)):                                                                
                                                                                bAmer = True
                                                                                break                                                                             
                                        if (bAmer):
                                                self.setGoal(iSpain, 2, 1)
                                        else:
                                                self.setGoal(iSpain, 2, 0)
                            
                        
                elif (iPlayer == iFrance):
                        if (pFrance.isAlive()):
                            
                                if (iGameTurn == i1700AD):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()                                
                                        bestCity = self.calculateTopCityCulture(capitalX, capitalY)
                                        if (bestCity != -1):
                                                if (bestCity.getOwner() == iFrance and bestCity.getX() == capitalX and bestCity.getY() == capitalY):
                                                        self.setGoal(iFrance, 0, 1)
                                                else:
                                                        self.setGoal(iFrance, 0, 0)
                                        else:
                                                self.setGoal(iFrance, 0, 0)
                                                        
                                if (iGameTurn == i1760AD):
                                        if (self.getGoal(iFrance, 1) == -1):
                                                self.setGoal(iFrance, 1, 0)

                                            
                        
                elif (iPlayer == iEngland):
                        if (pEngland.isAlive()):


                                if (self.getGoal(iEngland, 0) == -1):
                                        if (gc.getGame().getCircumnavigated() != -1):
                                                if (gc.getGame().getCircumnavigated() == iEngland):
                                                        self.setGoal(iEngland, 0, 1)
                                                else:
                                                        self.setGoal(iEngland, 0, 0)


                                if (iGameTurn == i1730AD):
                                        if (self.getGoal(iEngland, 1) == -1):
                                                self.setGoal(iEngland, 1, 0)

                elif (iPlayer == iGermany):
                        if (pGermany.isAlive()):

                                #RFCRAND
                                if (iGameTurn == i1870AD):
                                        iOwnedCivs = 0
                                        for iLoopCiv in range(iNumMajorPlayers):
                                                if (iLoopCiv != iGermany and utils.isNewWorldCiv(iLoopCiv) == False):
                                                        if (utils.getInThisGame(iLoopCiv)):
                                                                if (iLoopCiv in con.lCivGroups[0]):
                                                                        if (self.checkOwnedCiv(iGermany, iLoopCiv)):                                                                
                                                                                iOwnedCivs += 1
                                                                                if (iOwnedCivs == 3):
                                                                                        break                                     
                                        if (iOwnedCivs >= 3):
                                                self.setGoal(iGermany, 0, 1)
                                        else:
                                                self.setGoal(iGermany, 0, 0)
                                                        
                                #RFCRAND
                                if (iGameTurn == i1940AD):
                                        iOwnedCivs = 0
                                        for iLoopCiv in range(iNumMajorPlayers):
                                                if (iLoopCiv != iGermany):
                                                        if (utils.getInThisGame(iLoopCiv)):
                                                                if (self.checkOwnedCiv(iGermany, iLoopCiv)):                                                                
                                                                        iOwnedCivs += 1
                                                                        if (iOwnedCivs == 6):
                                                                                break                                     
                                        if (iOwnedCivs >= 6):
                                                self.setGoal(iGermany, 1, 1)
                                        else:
                                                self.setGoal(iGermany, 1, 0)
                        
                elif (iPlayer == iRussia):
                        if (pRussia.isAlive()):

                                if (iGameTurn == i1700AD):  
                                        if (self.getGoal(iRussia, 0) == -1):
                                                self.setGoal(iRussia, 0, 0)

                                if (iGameTurn == i1950AD+1):      
                                        if (self.getGoal(iRussia, 1) == -1): 
                                                self.setGoal(iRussia, 1, 0)

                                if (iGameTurn == i1950AD):                                                  
                                        if (self.getGoal(iRussia, 2) == -1): 
                                                self.setGoal(iRussia, 2, 1)



                elif (iPlayer == iNetherlands):
                        if (pNetherlands.isAlive()):

                                if (iGameTurn == i1600AD):
                                        lRevealedMap = con.l0Array
                                        for iCiv in range(iNumPlayers):
                                                for x in range(124):
                                                        for y in range(68):
                                                                if (gc.getMap().plot(x, y).isRevealed(iCiv, False)):
                                                                      lRevealedMap[iCiv] += 1
                                        bBestMap = True
                                        for iCiv in range(iNumPlayers):
                                                if (lRevealedMap[iNetherlands] < lRevealedMap[iCiv]):                                                        
                                                        bBestMap = False
                                                        break

                                        if (bBestMap == True):
                                                self.setGoal(iNetherlands, 0, 1)
                                        else:
                                                self.setGoal(iNetherlands, 0, 0)
                                                


                                if (self.getGoal(iNetherlands, 2) == -1):
                                        if (iGameTurn <= i1775AD):
                                                #print ("Dutch goal", pNetherlands.countOwnedBonuses(con.iSpices), pNetherlands.getBonusImport(con.iSpices))
                                                #RFCRAND
                                                #if (pNetherlands.countOwnedBonuses(con.iSpices) + pNetherlands.getBonusImport(con.iSpices) >= 7):
                                                if (pNetherlands.getNumAvailableBonuses(con.iSpices) >= 5):
                                                        self.setGoal(iNetherlands, 2, 1)
                                        else:
                                                self.setGoal(iNetherlands, 2, 0)
                        
                elif (iPlayer == iMali):
                        if (pMali.isAlive()):

                                if (iGameTurn == i1300AD-10): #temporary fix, they use too many specialist and make Mali UHV very hard
                                        if (not pFrance.isHuman()):
                                                if (pFrance.getGold() > 2000):
                                                        pFrance.setGold(pFrance.getGold()*50/100)
                                                elif (pFrance.getGold() > 1000):
                                                        pFrance.setGold(pFrance.getGold()*70/100)
                                                        

                                if (iGameTurn == i1300AD):
                                        iGold = pMali.getGold()
                                        for iCiv in range(iNumPlayers):
                                                if (iCiv != iMali and gc.getPlayer(iCiv).isAlive()):
                                                        if (gc.getPlayer(iCiv).getGold() > iGold):
                                                               self.setGoal(iMali, 0, 0)
                                                               return
                                        self.setGoal(iMali, 0, 1)
                                 
                                if (iGameTurn == i1500AD):
                                        if (pMali.getGold() >= 4000):
                                                self.setGoal(iMali, 1, 1)
                                        else:
                                                self.setGoal(iMali, 1, 0)
                                                
                                if (iGameTurn == i1700AD):
                                        if (pMali.getGold() >= 16000):
                                                self.setGoal(iMali, 2, 1)
                                        else:
                                                self.setGoal(iMali, 2, 0)

                elif (iPlayer == iTurkey):
                        if (pTurkey.isAlive()):

                                if (self.getGoal(iTurkey, 0) == -1):
                                        if (iGameTurn <= i1500AD):
                                                #RFCRAND
                                                for iLoopCiv in range(iNumMajorPlayers):
                                                        if (iLoopCiv != iTurkey):
                                                                SL = gc.getPlayer(iLoopCiv).getStartingPlot()                                                     
                                                                if (gc.getMap().plot(SL.getX(), SL.getY()).getOwner() == iTurkey):
                                                                        self.setGoal(iTurkey, 0, 1)
                                                                        break
                                        else:
                                                self.setGoal(iTurkey, 0, 0)


                                if (iGameTurn == i1700AD):

                                        #RFCRAND
                                        iLandMasses = 0

                                        for i in range(gc.getMap().getIndexAfterLastArea()):
                                                area = gc.getMap().getArea(i)
                                                if (area.getCitiesPerPlayer(iPlayer) >= 3):
                                                        iLandMasses = iLandMasses + 1

                                        if (iLandMasses >= 4):
                                                self.setGoal(iTurkey, 1, 1)
                                        else:
                                                self.setGoal(iTurkey, 1, 0)

                                if (iGameTurn == i1870AD):
                                        iCounter = 0
                                        for iCiv in range(iNumPlayers):
                                                if (iCiv != iTurkey):
                                                        if (gc.getPlayer(iCiv).isAlive()):
                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iTurkey)):
                                                                        iCounter += 1
                                        if (iCounter >= 3):
                                                self.setGoal(iTurkey, 2, 1)
                                        else:
                                                self.setGoal(iTurkey, 2, 0)



                elif (iPlayer == iPortugal):
                        if (pPortugal.isAlive()):

                                if (iGameTurn == i1500AD):
                                        lRevealedMap = con.l0Array
                                        for iCiv in range(iNumPlayers):
                                                for x in range(124):
                                                        for y in range(68):
                                                                if (gc.getMap().plot(x, y).isRevealed(iCiv, False)):
                                                                      lRevealedMap[iCiv] += 1
                                        bBestMap = True
                                        for iCiv in range(iNumPlayers):
                                                if (lRevealedMap[iPortugal] < lRevealedMap[iCiv]):                                                        
                                                        bBestMap = False
                                                        break

                                        if (bBestMap == True):
                                                self.setGoal(iPortugal, 0, 1)
                                        else:
                                                self.setGoal(iPortugal, 0, 0)

                                if (self.getGoal(iPortugal, 1) == -1):
                                        if (iGameTurn == i1650AD):
                                                #RFCRAND (used to be 12)
                                                iTarget = utils.countMajorCivsAlive()*2/3 #gc.getGame().countCivPlayersAlive() would count minors too
                                                iCount = 0
                                                for iLoopCiv in range(iNumMajorPlayers):
                                                        if (iLoopCiv != iPortugal):
                                                                if (teamPortugal.isOpenBorders(iLoopCiv)):
                                                                       iCount += 1
                                                if (iCount >= iTarget):                                                                    
                                                        self.setGoal(iPortugal, 1, 1)
                                                else:
                                                        self.setGoal(iPortugal, 1, 0)

                                    


                            
                        
                elif (iPlayer == iInca):
                        if (pInca.isAlive()):

                                if (iGameTurn == i1600AD):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()
                                        iRadius = 10                                

                                        bSAmerica = True
                                        for iEuroCiv in range(iNumPlayers): #not really a euro civ, just an old world's one
                                                #if (iEuroCiv in con.lCivGroups[0]):
                                                if (not utils.isNewWorldCiv(iEuroCiv)):
                                                        #RFCRAND        
                                                        if (self.checkNotOwnedArea(iEuroCiv, (capitalX - iRadius, capitalY - iRadius), (capitalX + iRadius, capitalY + iRadius)) == False):
                                                                bSAmerica = False
                                                                break
                                        if (bSAmerica):
                                                self.setGoal(iInca, 0, 1)
                                        else:
                                                self.setGoal(iInca, 0, 0)                                                

                                if (iGameTurn == i1700AD):
                                        if (pInca.getGold() >= 3000):
                                                self.setGoal(iInca, 1, 1)
                                        else:
                                                self.setGoal(iInca, 1, 0)
                                                
                                if (iGameTurn == i1800AD):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()
                                        iRadius = 10                                

                                        bSAmerica = True
                                        for iEuroCiv in range(iNumPlayers):
                                                if (iEuroCiv in con.lCivGroups[0]):
                                                        #RFCRAND        
                                                        if (self.checkNotOwnedArea(iEuroCiv, (capitalX - iRadius, capitalY - iRadius), (capitalX + iRadius, capitalY + iRadius)) == False):
                                                                bSAmerica = False
                                                                break
                                        if (bSAmerica):
                                                self.setGoal(iInca, 2, 1)
                                        else:
                                                self.setGoal(iInca, 2, 0)            

                        
                elif (iPlayer == iMongolia):
                        if (pMongolia.isAlive()):

                                if (iGameTurn <= i1300AD):
                                        #RFCRAND
                                        bChina = False
                                        bIndia = False
                                        bJapan = False
                                        if (self.getGoal(iMongolia, 0) == -1):
                                                if (utils.getInThisGame(iChina)):
                                                        bChina = self.checkOwnedCiv(iMongolia, iChina)
                                                if (utils.getInThisGame(iIndia)):
                                                        bIndia = self.checkOwnedCiv(iMongolia, iIndia)
                                                if (utils.getInThisGame(iJapan)):
                                                        bJapan = self.checkOwnedCiv(iMongolia, iJapan)
                                                if (bChina or bIndia or bJapan):
                                                        self.setGoal(iMongolia, 0, 1)
                                else:
                                        if (self.getGoal(iMongolia, 0) == -1):
                                                        self.setGoal(iMongolia, 0, 0)


                                if (self.getGoal(iMongolia, 2) == -1):
                                        if (iGameTurn <= i1500AD):
                                                totalLand = gc.getMap().getLandPlots()
                                                mongolLand = pMongolia.getTotalLand()
                                                if (totalLand > 0):
                                                        landPercent = (mongolLand * 100.0) / totalLand
                                                else:
                                                        landPercent = 0.0
                                                        
                                                if (landPercent >= 9.995): #it's shown as 10.00 in the victory screen) #RFCRAND
                                                        self.setGoal(iMongolia, 2, 1)
                                        else:
                                                self.setGoal(iMongolia, 2, 0)

                            
                        
                elif (iPlayer == iAztecs):
                        if (pAztecs.isAlive()):
                            
                                if (self.getGoal(iAztecs, 0) == -1):
                                        if (self.getEnslavedUnits() >= 5):
                                                self.setGoal(iAztecs, 0, 1)   
                                            
                                if (iGameTurn == i1700AD):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()
                                        iRadius = 10
                                        
                                        bCAmerica = True
                                        for iEuroCiv in range(iNumPlayers): #not really a euro civ, just an old world's one
                                                #if (iEuroCiv in con.lCivGroups[0]):
                                                if (not utils.isNewWorldCiv(iEuroCiv)):
                                                        #RFCRAND        
                                                        if (self.checkNotOwnedArea(iEuroCiv, (capitalX - iRadius, capitalY - iRadius), (capitalX + iRadius, capitalY + iRadius)) == False):
                                                                bCAmerica = False
                                                                break
                                        if (bCAmerica):
                                                self.setGoal(iAztecs, 1, 1)
                                        else:
                                                self.setGoal(iAztecs, 1, 0)          


##                                if (iGameTurn == i1820AD):
##                                        bestCity = self.calculateTopCityPopulation(18, 37)
##                                        if (bestCity != -1):
##                                                if (bestCity.getOwner() == iAztecs and bestCity.getX() == 18 and bestCity.getY() == 37):
##                                                        self.setGoal(iAztecs, 2, 1)
##                                                else:
##                                                        self.setGoal(iAztecs, 2, 0)

                        
                elif (iPlayer == iAmerica):
                        if (pAmerica.isAlive()):

                                if (iGameTurn == i1930AD):
                                        #RFCRAND        
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        capitalX = capital.getX()                                
                                        capitalY = capital.getY()
                                        iRadius = 12
                                
                                        bAmericas = True
                                        for iEuroCiv in range(iNumPlayers): #not really a euro civ, just an old world's one
                                                #if (iEuroCiv in con.lCivGroups[0]):
                                                if (not utils.isNewWorldCiv(iEuroCiv)):
                                                        #RFCRAND        
                                                        if (self.checkNotOwnedArea(iEuroCiv, (capitalX - iRadius, capitalY - iRadius), (capitalX + iRadius, capitalY + iRadius)) == False):
                                                                bAmericas = False
                                                                break
                                        if (bAmericas):
                                                self.setGoal(iAmerica, 0, 1)
                                        else:
                                                self.setGoal(iAmerica, 0, 0)

                                if (iGameTurn == i2000AD+1):
                                        if (self.getGoal(iAmerica, 1) == -1):
                                                if (self.getWondersBuilt(iAmerica) != 3):                                    
                                                        self.setGoal(iAmerica, 1, 0)

##                                if (iGameTurn == i2000AD):
##                                        iCounter = 0
##                                        for iCiv in range(iNumPlayers):
##                                                if (iCiv != iAmerica):
##                                                        if (gc.getPlayer(iCiv).isAlive()):
##                                                                if (self.checkOwnedCiv(iAmerica, iCiv)):
##                                                                        iCounter += 1
##                                        if (iCounter >= 4):
##                                                self.setGoal(iAmerica, 2, 1)
##                                        else:
##                                                self.setGoal(iAmerica, 2, 0)


                                if (self.getGoal(iAmerica, 2) == -1):
                                        if (iGameTurn <= i2000AD):
                                                #iCounter = pAmerica.countOwnedBonuses(con.iOil)
                                                iCounter = pAmerica.getNumAvailableBonuses(con.iOil) - pAmerica.getBonusImport(con.iOil)
                                                for iCiv in range(iNumPlayers):
                                                        if (iCiv != iAmerica):
                                                                if (gc.getPlayer(iCiv).isAlive()):
                                                                        if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iAmerica)):
                                                                                #iCounter += gc.getPlayer(iCiv).countOwnedBonuses(con.iOil)
                                                                                iCounter += gc.getPlayer(iCiv).getNumAvailableBonuses(con.iOil) - gc.getPlayer(iCiv).getBonusImport(con.iOil)
                                                if (iCounter >= 10):
                                                        self.setGoal(iAmerica, 2, 1)
                                        else:
                                                self.setGoal(iAmerica, 2, 0)                                                


                #generic checks
                pPlayer = gc.getPlayer(iPlayer)
                if (pPlayer.isAlive() and iPlayer < iNumMajorPlayers):
                    
                        if (self.get2OutOf3(iPlayer) == False):                              
                                if (utils.countAchievedGoals(iPlayer) == 2):
                                        #intermediate bonus
                                        self.set2OutOf3(iPlayer, True)
                                        if (gc.getPlayer(iPlayer).getNumCities() > 0): #this check is needed, otherwise game crashes
                                                capital = gc.getPlayer(iPlayer).getCapitalCity()
                                                capital.setHasRealBuilding(con.iTriumphalArch, True)
                                                if (pPlayer.isHuman()):
                                                        CyInterface().addMessage(iPlayer, False, con.iDuration, CyTranslator().getText("TXT_KEY_VICTORY_INTERMEDIATE", ()), "", 0, "", ColorTypes(con.iPurple), -1, -1, True, True)
                                                        
                                                        for iCiv in range(iNumPlayers):
                                                                if (iCiv != iPlayer):
                                                                        pCiv = gc.getPlayer(iCiv)
                                                                        if (pCiv.isAlive()):
                                                                                iAttitude = pCiv.AI_getAttitude(iPlayer)
                                                                                if (iAttitude != 0):
                                                                                        pCiv.AI_setAttitudeExtra(iPlayer, iAttitude-1) #da controllare

                                                        iWarCounter = 0
                                                        iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'civs')
                                                        for i in range( iRndnum, iNumPlayers + iRndnum ):
                                                                iCiv = i % iNumPlayers
                                                                pCiv = gc.getPlayer(iCiv)
                                                                if (pCiv.isAlive() and pCiv.canContact(iPlayer)):                                                                
                                                                        if (pCiv.AI_getAttitude(iPlayer) == 0):
                                                                                teamCiv = gc.getTeam(pCiv.getTeam())
                                                                                if (not teamCiv.isAtWar(iPlayer) and not teamCiv.isDefensivePact(iPlayer) and not utils.isAVassal(iCiv)):
                                                                                        teamCiv.declareWar(iPlayer, True, -1)
                                                                                        iWarCounter += 1
                                                                                        if (iWarCounter == 2):
                                                                                                break
                                

                        if (gc.getGame().getWinner() == -1):                              
                                if (self.getGoal(iPlayer, 0) == 1 and self.getGoal(iPlayer, 1) == 1 and self.getGoal(iPlayer, 2) == 1):
                                        gc.getGame().setWinner(iPlayer, 7) #Historical Victory




        def onCityBuilt(self, city, iPlayer): #see onCityBuilt in CvRFCEventHandler

                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return
                    
                iGameTurn = gc.getGame().getGameTurn()

##                if (iPlayer == iCarthage):
##                        if (self.getGoal(iCarthage, 0) == -1):
##                                if (iGameTurn <= i350AD):
##                                        if (city.getX() >= tMediterraneanTL[0] and city.getX() <= tMediterraneanBR[0] and city.getY() >= tMediterraneanTL[1] and city.getY() <= tMediterraneanBR[1]):
##                                                if (city.isCoastalOld()):
##                                                        self.setMediterraneanColonies(self.getMediterraneanColonies() + 1)
##                                                if (self.getMediterraneanColonies() >= 7):
##                                                        self.setGoal(iCarthage, 0, 1)


                if (iPlayer == iVikings):
                        if (self.getGoal(iVikings, 2) == -1):
                                #RFCRAND
                                #if (city.getX() >= tAmericasTL[0] and city.getX() <= tAmericasBR[0] and city.getY() >= tAmericasTL[1] and city.getY() <= tAmericasBR[1]):
                                area = city.area()
                                if (area.getNumTiles() >= 100 and utils.isNewWorld(city.getX(),city.getY())): #we should count only the main land
##                                        bFirst = True
##                                        for iCiv in range(iNumPlayers):
##                                                if ((iCiv != iVikings) and (iCiv not in con.lCivGroups[5])):
##                                                        if (self.checkNotOwnedArea(iCiv, tAmericasTL, tAmericasBR) == False):
##                                                                bFirst = False
##                                                                break
##                                        if (bFirst):
                                        if (self.getNewWorld(0) == -1 or self.getNewWorld(0) == iPlayer):
                                                self.setGoal(iVikings, 2, 1)
                                                #failure moved to EventHandler

                
                elif (iPlayer == iSpain):
                        if (self.getGoal(iSpain, 0) == -1):
                                area = city.area()
                                if (area.getNumTiles() >= 100 and utils.isNewWorld(city.getX(),city.getY())): #we should count only the main land
                                #if (city.area().getID() == utils.getAmericaInfo(4) or city.area().getID() == utils.getAmericaInfo(5)):

                                        if (self.getNewWorld(0) == -1 or self.getNewWorld(0) == iPlayer):
                                                self.setGoal(iSpain, 0, 1)
                                                #failure moved to EventHandler


                              
                elif (iPlayer == iFrance):
                        if (iGameTurn <= i1760AD):
                                if (self.getGoal(iFrance, 1) == -1):
                                        #RFCRAND
                                        if (utils.isNewWorld(city.getX(),city.getY())):
                                        #if (city.area().getID() == utils.getAmericaInfo(4) or city.area().getID() == utils.getAmericaInfo(5)):
                                                self.setFrenchColonies(self.getFrenchColonies() + 1)

                                                if (self.getFrenchColonies() >= 7):
                                                        self.setGoal(iFrance, 1, 1)
                                                

                elif (iPlayer == iEngland):
                        if (iGameTurn <= i1730AD):
                                if (self.getGoal(iEngland, 1) == -1):
                                        #RFCRAND
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        if (utils.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY()) >= 12):
                                                self.setEnglishColonies(self.getEnglishColonies() + 1)
                                                if (self.getEnglishColonies() >= 15):
                                                        self.setGoal(iEngland, 1, 1)                                            


                elif (iPlayer == iRussia):
                        if (iGameTurn <= i1700AD):
                                if (self.getGoal(iRussia, 0) == -1):
                                        #RFCRAND
                                        #if (not city.isCoastalOld()):
                                        capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                        if (utils.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY()) >= 8):
                                                if (city.area().getID() == capital.area().getID()):
                                                        self.setRussianColonies(self.getRussianColonies() + 1)
                                                        if (self.getRussianColonies() >= 5):
                                                                self.setGoal(iRussia, 0, 1)



                elif (iPlayer == iNetherlands):
                        if (self.getGoal(iNetherlands, 1) == -1):
                                #RFCRAND
                                if (iGameTurn <= i1760AD):
                                        pPlot = gc.getMap().plot(city.getX(), city.getY())
                                        if (pPlot.area().getNumCities() == 1 and pPlot.area().getNumTiles() >= 25):
                                                self.setGoal(iNetherlands, 1, 1)
                                else:
                                        self.setGoal(iNetherlands, 1, 0)

                elif (iPlayer == iPortugal):
                        if (self.getGoal(iPortugal, 2) == -1):
                                #RFCRAND        
                                capital = gc.getPlayer(iPlayer).getCapitalCity()                                  
                                if (utils.calculateDistance(city.getX(), city.getY(), capital.getX(), capital.getY()) >= 12):
                                        self.setPortugueseColonies(self.getPortugueseColonies() + 1)
                                        if (self.getPortugueseColonies() >= 15):
                                                self.setGoal(iPortugal, 2, 1)

                                                
                        
        def onReligionFounded(self, iReligion, iFounder):

                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return

                iPlayer = iFounder

                if (iFounder == iIndia):
                        self.setReligionFounded(iReligion, 1)

                if (self.getGoal(iIndia, 0) == -1):
                        if (iReligion == con.iHinduism):
                                if (iFounder != iIndia):
                                        self.setGoal(iIndia, 0, 0) 
                        elif (iReligion == con.iBuddhism):
                                if (iFounder != iIndia):
                                        self.setGoal(iIndia, 0, 0)
                        if (self.getReligionFounded(con.iHinduism) == 1 and self.getReligionFounded(con.iBuddhism) == 1):
                                self.setGoal(iIndia, 0, 1)     

                if (self.getGoal(iIndia, 1) == -1):
                        iCounter = 0
                        for i in range(con.iNumReligions):
                                if (self.getReligionFounded(i) == 1):
                                        iCounter += 1
                        if (iCounter >= 5):
                                self.setGoal(iIndia, 1, 1)

                        if (self.getGoal(iIndia, 1) == -1):
                                iFounded = 0
                                for iLoopReligion in range(con.iNumReligions):
                                        if (gc.getGame().isReligionFounded(iLoopReligion)):
                                                iFounded += 1
                                if (iFounded == con.iNumReligions):
                                        self.setGoal(iIndia, 1, 0)


                if (iPlayer == iEthiopia):
                        if (pEthiopia.isAlive()):
                                if (self.getGoal(iEthiopia, 0) == -1):
                                        self.setGoal(iEthiopia, 0, 1)

                elif (iReligion == con.iIslam):
                        if (self.getGoal(iEthiopia, 0) == -1):
                                self.setGoal(iEthiopia, 0, 0)


        def onCityAcquired(self, owner, playerType, bConquest):

                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return

                iPlayer = owner
                iGameTurn = gc.getGame().getGameTurn()
                
                if (iPlayer == iChina):
                        if (pChina.isAlive()):
                                if (bConquest):
                                        if (self.getGoal(iChina, 1) == -1):
                                                if (iGameTurn <= i1400AD):
                                                        if (playerType == iBarbarian or playerType == iMongolia):
                                                                self.setGoal(iChina, 1, 0)   

                elif (iPlayer == iRome):
                        if (pRome.isAlive()):
                                if (bConquest):
                                        if (self.getGoal(iRome, 2) == -1):
                                                if (iGameTurn <= i1000AD):
                                                        if (playerType == iBarbarian):
                                                                self.setGoal(iRome, 2, 0)

##                elif (iPlayer == iJapan):
##                        if (pJapan.isAlive()):
##                                if (bConquest):
##                                        if (self.getGoal(iJapan, 2) == -1):
##                                                if (iGameTurn <= i1850AD):
##                                                        self.setGoal(iJapan, 2, 0)


                elif (iPlayer == iMaya):
                        if (pMaya.isAlive()):
                                if (bConquest):
                                        if (self.getGoal(iMaya, 2) == -1):
                                                if (iGameTurn <= i1745AD):
                                                        self.setGoal(iMaya, 2, 0)
                                        
                elif (iPlayer == iRussia):
                        if (pRussia.isAlive()):
                                if (bConquest):
                                        if (self.getGoal(iRussia, 2) == -1):
                                                if (iGameTurn <= i1950AD):
                                                        self.setGoal(iRussia, 2, 0)          


        def onCityRazed(self, iPlayer):

                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return

                if (iPlayer == iMongolia):
                        if (pMongolia.isAlive()):
                                self.setRazedByMongols(self.getRazedByMongols() + 1)
                                if (self.getGoal(iMongolia, 1) == -1):
                                        if (self.getRazedByMongols() >= 7):
                                                self.setGoal(iMongolia, 1, 1)

                                                


        def onTechAcquired(self, iTech, iPlayer):

                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return

                iGameTurn = gc.getGame().getGameTurn()

                if (iPlayer == iBabylonia):
                        if (pBabylonia.isAlive()):
                                if (self.getGoal(iBabylonia, 0) == -1): #eof error???
                                        if (iTech == con.iWriting):
                                                self.setBabylonianTechs(0, 1)
                                                for iCiv in range(iNumPlayers):
                                                        if (iCiv != iBabylonia):
                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
                                                                        self.setBabylonianTechs(0, 0)
                                        elif (iTech == con.iCodeOfLaws):
                                                self.setBabylonianTechs(1, 1)
                                                for iCiv in range(iNumPlayers):
                                                        if (iCiv != iBabylonia):
                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
                                                                        self.setBabylonianTechs(1, 0)
                                        elif (iTech == con.iMonarchy):
                                                self.setBabylonianTechs(2, 1)
                                                for iCiv in range(iNumPlayers):
                                                        if (iCiv != iBabylonia):
                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
                                                                        self.setBabylonianTechs(2, 0)
                                        print ("self.getBabylonianTechs", self.getBabylonianTechs(0), self.getBabylonianTechs(1), self.getBabylonianTechs(2))
                                        if (self.getBabylonianTechs(0) == 1 and self.getBabylonianTechs(1) == 1 and self.getBabylonianTechs(2) == 1):
                                                self.setGoal(iBabylonia, 0, 1)
                                        elif (self.getBabylonianTechs(0) == 0 or self.getBabylonianTechs(1) == 0 or self.getBabylonianTechs(2) == 0):
                                                self.setGoal(iBabylonia, 0, 0)

                elif (iPlayer == iGreece):
                        if (pGreece.isAlive()):
                                if (self.getGoal(iGreece, 0) == -1): #eof error???
                                        if (iTech == con.iLiterature):
                                                self.setGreekTechs(0, 1)
                                                for iCiv in range(iNumPlayers):
                                                        if (iCiv != iGreece):
                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
                                                                        self.setGreekTechs(0, 0)
                                        elif (iTech == con.iDrama):
                                                self.setGreekTechs(1, 1)
                                                for iCiv in range(iNumPlayers):
                                                        if (iCiv != iGreece):
                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
                                                                        self.setGreekTechs(1, 0)
                                        elif (iTech == con.iPhilosophy):
                                                self.setGreekTechs(2, 1)
                                                for iCiv in range(iNumPlayers):
                                                        if (iCiv != iGreece):
                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == True):
                                                                        self.setGreekTechs(2, 0)
                                        print ("self.getGreekTechs", self.getGreekTechs(0), self.getGreekTechs(1), self.getGreekTechs(2))
                                        if (self.getGreekTechs(0) == 1 and self.getGreekTechs(1) == 1 and self.getGreekTechs(2) == 1):
                                                self.setGoal(iGreece, 0, 1)
                                        elif (self.getGreekTechs(0) == 0 or self.getGreekTechs(1) == 0 or self.getGreekTechs(2) == 0):
                                                self.setGoal(iGreece, 0, 0)


                elif (iPlayer == iJapan):
                        if (pJapan.isAlive()):
                                if (iGameTurn >= i1700AD and pJapan.getCurrentEra() >= iModern):
                                        if (self.getGoal(iJapan, 2) == -1):
                                                bCompleted = True
                                                for iTech in range(con.iNumTechs):
                                                        if (teamJapan.isHasTech(iTech) == False):
                                                                bCompleted = False
                                                                return
                                                if (bCompleted):
                                                        for iCiv in range(iNumPlayers):
                                                                if (iCiv != iJapan):
                                                                        bOtherCompleted = True
                                                                        for iTech in range(con.iNumTechs):
                                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == False):
                                                                                        bOtherCompleted = False
                                                                                        break
                                                                        if (bOtherCompleted):
                                                                                break
                                                        if (not bOtherCompleted):
                                                                self.setGoal(iJapan, 2, 1)
                                                        else:
                                                                self.setGoal(iJapan, 2, 0) 
                                                

                elif (iPlayer == iMaya):
                        if (pMaya.isAlive()):
                                if (self.getGoal(iMaya, 0) == -1): #eof error???
                                        if (iTech == con.iCalendar):
                                                if (iGameTurn <= i600AD):
                                                        self.setGoal(iMaya, 0, 1)



                elif (iPlayer == iEngland):
                        if (pEngland.isAlive()):
                                if (iGameTurn >= i1300AD):
                                        if (self.getGoal(iEngland, 2) == -1):
                                                englishEra = pEngland.getCurrentEra()
                                                if (englishEra == iIndustrial):
                                                        if (self.getEnglishEras(0) == -1): #just entered
                                                                bFirst = True
                                                                for iCiv in range(iNumPlayers):
                                                                        if (iCiv != iEngland):
                                                                                if (gc.getPlayer(iCiv).getCurrentEra() == iIndustrial):
                                                                                        bFirst = False
                                                                                        break
                                                                if (bFirst):
                                                                        self.setEnglishEras(0, 1)
                                                                else:
                                                                        self.setEnglishEras(0, 0)
                                                if (englishEra == iModern):
                                                        if (self.getEnglishEras(1) == -1): #just entered
                                                                bFirst = True
                                                                for iCiv in range(iNumPlayers):
                                                                        if (iCiv != iEngland):
                                                                                if (gc.getPlayer(iCiv).getCurrentEra() == iModern):
                                                                                        bFirst = False
                                                                                        break
                                                                if (bFirst):
                                                                        self.setEnglishEras(1, 1)
                                                                        if (self.getEnglishEras(0) == 1):
                                                                                self.setGoal(iEngland, 2, 1)
                                                                        else:
                                                                                self.setGoal(iEngland, 2, 0)
                                                                else:
                                                                        self.setEnglishEras(1, 0)
                                                                        self.setGoal(iEngland, 2, 0)

                                                                        


                
                elif (iPlayer == iGermany):
                        if (pGermany.isAlive()):
                                if (iGameTurn >= i1700AD and pGermany.getCurrentEra() >= iModern):
                                        if (self.getGoal(iGermany, 2) == -1):
                                                bCompleted = True
                                                for iTech in range(con.iNumTechs):
                                                        if (teamGermany.isHasTech(iTech) == False):
                                                                bCompleted = False
                                                                return
                                                if (bCompleted):
                                                        for iCiv in range(iNumPlayers):
                                                                if (iCiv != iGermany):
                                                                        bOtherCompleted = True
                                                                        for iTech in range(con.iNumTechs):
                                                                                if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isHasTech(iTech) == False):
                                                                                        bOtherCompleted = False
                                                                                        break
                                                                        if (bOtherCompleted):
                                                                                break
                                                        if (not bOtherCompleted):
                                                                self.setGoal(iGermany, 2, 1)
                                                        else:
                                                                self.setGoal(iGermany, 2, 0) 
                                                        

                elif (iPlayer == iAztecs):
                        if (self.getGoal(iAztecs, 2) == -1):
                                if (iGameTurn <= i1860AD):                            
                                        aztecEra = pAztecs.getCurrentEra()
                                        if (aztecEra == iIndustrial):
                                                self.setGoal(iAztecs, 2, 1)                                        
                                else:
                                        self.setGoal(iAztecs, 2, 0)
                                                



        def onBuildingBuilt(self, iPlayer, iBuilding):

                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return

                iGameTurn = gc.getGame().getGameTurn()

                if (iPlayer == iEgypt):
                        if (pEgypt.isAlive()):
                                if (self.getGoal(iEgypt, 1) == -1):
                                        if (iGameTurn <= i100BC):
                                                if (iBuilding == con.iPyramid or iBuilding == con.iGreatLibrary or iBuilding == con.iGreatLighthouse):
                                                        self.setWondersBuilt(iEgypt, self.getWondersBuilt(iEgypt) + 1)
                                                if (self.getWondersBuilt(iEgypt) == 3):                                    
                                                        self.setGoal(iEgypt, 1, 1)
                                        if (iGameTurn >= i100BC):
                                                if (self.getWondersBuilt(iEgypt) != 3):                                    
                                                        self.setGoal(iEgypt, 1, 0)      


                elif (iPlayer == iChina):
                        if (pChina.isAlive()):
                                if (self.getGoal(iChina, 0) == -1):
                                        if (iGameTurn <= i1000AD):
                                                if (iBuilding == con.iConfucianCathedral or iBuilding == con.iTaoistCathedral):
                                                        #iConfucianCounter = pChina.getBuildingClassCount(con.iConfucianCathedral)
                                                        #iTaoistCounter = pChina.getBuildingClassCount(con.iTaoistCathedral)
                                                        iConfucianCounter = 0
                                                        iTaoistCounter = 0
                                                        for iCity in range(pChina.getNumCities()):
                                                                pCity = pChina.getCity(iCity)
                                                                if (pCity.hasBuilding(con.iConfucianCathedral)):
                                                                        iConfucianCounter += 1
                                                                if (pCity.hasBuilding(con.iTaoistCathedral)):
                                                                        iTaoistCounter += 1
                                                        if (iConfucianCounter >= 2 and iTaoistCounter >= 2):
                                                                self.setGoal(iChina, 0, 1)
                                        else:
                                                self.setGoal(iChina, 0, 0)



                elif (iPlayer == iGreece):
                        if (pGreece.isAlive()):
                                if (self.getGoal(iGreece, 1) == -1):
                                        if (iGameTurn <= i250BC):
                                                if (iBuilding == con.iOracle or iBuilding == con.iColossus or iBuilding == con.iParthenon or iBuilding == con.iArtemis):
                                                        self.setWondersBuilt(iGreece, self.getWondersBuilt(iGreece) + 1)
                                                if (self.getWondersBuilt(iGreece) == 4):                                    
                                                        self.setGoal(iGreece, 1, 1)
                                        if (iGameTurn > i250BC):                                   
                                                self.setGoal(iGreece, 1, 0)     

                                                

                elif (iPlayer == iFrance):
                        if (pFrance.isAlive()):
                                if (self.getGoal(iFrance, 2) == -1):
                                        if (iGameTurn <= i1900AD):
                                                if (iBuilding == con.iNotreDame or iBuilding == con.iStatueOfLiberty or iBuilding == con.iEiffelTower):
                                                        self.setWondersBuilt(iFrance, self.getWondersBuilt(iFrance) + 1)
                                                if (self.getWondersBuilt(iFrance) == 3):                                    
                                                        self.setGoal(iFrance, 2, 1)
                                        if (iGameTurn > i1900AD):
                                                if (self.getWondersBuilt(iFrance) != 3):                                    
                                                        self.setGoal(iFrance, 2, 0) 

                elif (iPlayer == iAmerica):
                        if (pAmerica.isAlive()):
                                if (self.getGoal(iAmerica, 1) == -1):
                                        if (iGameTurn <= i2000AD):
                                                if (iBuilding == con.iStatueOfLiberty or iBuilding == con.iPentagon or iBuilding == con.iUnitedNations):
                                                        self.setWondersBuilt(iAmerica, self.getWondersBuilt(iAmerica) + 1)
                                                if (self.getWondersBuilt(iAmerica) == 3):                                    
                                                        self.setGoal(iAmerica, 1, 1)
                                        if (iGameTurn > i2000AD):
                                                if (self.getWondersBuilt(iAmerica) != 3):                                    
                                                        self.setGoal(iAmerica, 1, 0)






                if (iBuilding == con.iTempleOfKukulkan):      
                        if (iPlayer == iMaya):
                                if (pMaya.isAlive()):
                                        if (self.getGoal(iMaya, 1) == -1):
                                                if (iGameTurn <= i900AD):                                                                            
                                                        self.setGoal(iMaya, 1, 1)
                        else:
                                self.setGoal(iMaya, 1, 0)


                            
        def onProjectBuilt(self, iPlayer, iProject):

                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return

                iGameTurn = gc.getGame().getGameTurn()

                if (iProject == con.iApolloProgram):
                        if (iPlayer == iRussia):
                                if (iGameTurn <= i1950AD):                                
                                        self.setGoal(iRussia, 1, 1)
                        else:
                                if (self.getGoal(iRussia, 1) == -1):
                                        self.setGoal(iRussia, 1, 0)



        def onCombatResult(self, argsList):
            
                if (not gc.getGame().isVictoryValid(7)): #7 == historical
                        return

                pWinningUnit,pLosingUnit = argsList
                pWinningPlayer = gc.getPlayer(pWinningUnit.getOwner())
                pLosingPlayer = gc.getPlayer(pLosingUnit.getOwner())
                cLosingUnit = PyHelpers.PyInfo.UnitInfo(pLosingUnit.getUnitType())
                iPlayer = pWinningPlayer.getID()

                if (iPlayer == iVikings):
                        if (self.getGoal(iVikings, 1) == -1):
                                if (cLosingUnit.getDomainType() == gc.getInfoTypeForString("DOMAIN_SEA")):
                                        self.setNumSinks(self.getNumSinks() + 1)
                                        if (self.getNumSinks() == 25):
                                                self.setGoal(iVikings, 1, 1)
                                        


        def calculateTopCityCulture(self, x, y):
                iBestCityValue = 0
                pCurrent = gc.getMap().plot( x, y )
                if (pCurrent.isCity()):
                        bestCity = pCurrent.getPlotCity()
                        for iPlayerLoop in range(gc.getMAX_PLAYERS()):
                                apCityList = PyPlayer(iPlayerLoop).getCityList()

                                for pCity in apCityList:
                                        iTotalCityValue = pCity.GetCy().countTotalCultureTimes100()
                                        #iTotalCityValue = (pCity.getCulture() / 5) + (pCity.getFoodRate() + pCity.getProductionRate() \
                                        #	+ pCity.calculateGoldRate())) * pCity.getPopulation()
                                        if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
                                                bestCity = pCity
                                                iBestCityValue = iTotalCityValue
                        return bestCity
                return -1


        def calculateTopCityPopulation(self, x, y):
                iBestCityValue = 0
                pCurrent = gc.getMap().plot( x, y )
                if (pCurrent.isCity()):
                        bestCity = pCurrent.getPlotCity()
                        for iPlayerLoop in range(gc.getMAX_PLAYERS()):
                                apCityList = PyPlayer(iPlayerLoop).getCityList()

                                for pCity in apCityList:			
                                        iTotalCityValue = pCity.getPopulation()
                                        if (iTotalCityValue > iBestCityValue and not pCity.isBarbarian()):
                                                bestCity = pCity
                                                iBestCityValue = iTotalCityValue
                        return bestCity
                return -1




