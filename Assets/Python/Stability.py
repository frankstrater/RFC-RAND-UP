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

iNumPlayers = con.iNumPlayers
iNumMajorPlayers = con.iNumMajorPlayers
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iNumTotalPlayers = con.iNumTotalPlayers
iBarbarian = con.iBarbarian
tCapitals = con.tCapitals

iParCities3 = con.iParCities3
iParCitiesE = con.iParCitiesE
iParCivics3 = con.iParCivics3
iParCivics1 = con.iParCivics1
iParCivicsE = con.iParCivicsE
iParDiplomacy3 = con.iParDiplomacy3
iParDiplomacyE = con.iParDiplomacyE
iParEconomy3 = con.iParEconomy3
iParEconomy1 = con.iParEconomy1
iParEconomyE = con.iParEconomyE
iParExpansion3 = con.iParExpansion3
iParExpansion1 = con.iParExpansion1
iParExpansionE = con.iParExpansionE



class Stability:



     
##################################################
### Secure storage & retrieval of script data ###
################################################   
		           


        def getBaseStabilityLastTurn( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lBaseStabilityLastTurn'][iCiv]

        def setBaseStabilityLastTurn( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lBaseStabilityLastTurn'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
            
        def getStability( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lStability'][iCiv]

        def setStability( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lStability'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getStatePropertyCountdown( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lStatePropertyCountdown'][iCiv]

        def setStatePropertyCountdown( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lStatePropertyCountdown'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getDemocracyCountdown( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lDemocracyCountdown'][iCiv]

        def setDemocracyCountdown( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lDemocracyCountdown'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        def getGreatDepressionCountdown( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGreatDepressionCountdown'][iCiv]

        def setGreatDepressionCountdown( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGreatDepressionCountdown'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getCombatResultTempModifier( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lCombatResultTempModifier'][iCiv]

        def setCombatResultTempModifier( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lCombatResultTempModifier'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getGNPold( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGNPold'][iCiv]

        def setGNPold( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGNPold'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getGNPnew( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGNPnew'][iCiv]

        def setGNPnew( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGNPnew'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getRebelCiv( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iRebelCiv']

        def getLatestRebellionTurn( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lLatestRebellionTurn'][iCiv]

        def getPartialBaseStability( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lPartialBaseStability'][iCiv]

        def setPartialBaseStability( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lPartialBaseStability'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getOwnedPlotsLastTurn( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lOwnedPlotsLastTurn'][iCiv]

        def setOwnedPlotsLastTurn( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lOwnedPlotsLastTurn'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getOwnedCitiesLastTurn( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lOwnedCitiesLastTurn'][iCiv]

        def setOwnedCitiesLastTurn( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lOwnedCitiesLastTurn'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        def getStabilityParameters( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lStabilityParameters'][iParameter]

        def setStabilityParameters( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lStabilityParameters'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        def getLastRecordedStabilityStuff( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lLastRecordedStabilityStuff'][iParameter]

        def setLastRecordedStabilityStuff( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lLastRecordedStabilityStuff'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
#######################################
### Main methods (Event-Triggered) ###
#####################################  

        def setParameter(self, iPlayer, iParameter, bPreviousAmount, iAmount):
            if (gc.getPlayer(iPlayer).isHuman()):
            #if (iPlayer == con.iChina): #debug
                    if (bPreviousAmount):
                            self.setStabilityParameters(iParameter, self.getStabilityParameters(iParameter) + iAmount)
                    else:
                            self.setStabilityParameters(iParameter, 0 + iAmount)

        def setup(self):

                utils.setStartingStabilityParameters(utils.getHumanID())





        def checkTurn(self, iGameTurn):


                #moved here with its own stored value to save loading time (scrolls the map only once instead of every player)
                if (iGameTurn % 6 == 0): #3 is too short to detect any change; must be a multiple of 3 anyway
                        lOwnedPlots = []
                        lOwnedCities = []
                        for i in range(len(con.l0Array)):
                                lOwnedPlots.append(0)
                                lOwnedCities.append(0)
                        for x in range(0, CyMap().getGridWidth()):
                                for y in range(0, CyMap().getGridHeight()):
                                        pCurrent = gc.getMap().plot( x, y )
                                        iOwner = pCurrent.getOwner()
                                        if (iOwner >= 0 and iOwner < iNumPlayers and (pCurrent.isHills() or pCurrent.isFlatlands())):
                                                #if (gc.getPlayer(iOwner).getSettlersMaps( 67-y, x ) < 90): #RFCRAND
                                                #if (gc.getPlayer(iOwner).AI_blindSettlersMap( x, y, False ) <= 70):
                                                if (utils.blindSettlersMap( iOwner, x, y ) <= 70):
                                                        lOwnedPlots[iOwner] += 1
                                                if (pCurrent.isCity()):
                                                        cityOwner = pCurrent.getPlotCity().getOwner()
                                                        for iLoop in range(con.iNumPlayers): #RFCRAND
                                                                if (iLoop != cityOwner and gc.getPlayer(iLoop).isAlive() and iGameTurn >= gc.getPlayer(iLoop).getBirthTurn()+30 and iGameTurn >= self.getLatestRebellionTurn(iLoop) + 15):
                                                                        #if (gc.getPlayer(iLoop).getSettlersMaps( 67-y, x ) >= 400):  #RFCRAND
                                                                         #if (gc.getPlayer(iLoop).AI_blindSettlersMap( x, y, False ) >= 120):
                                                                        iRadius = 5
                                                                        if (x >= gc.getPlayer(iLoop).getStartingPlot().getX()-iRadius and x <= gc.getPlayer(iLoop).getStartingPlot().getX()+iRadius and \
                                                                            y >= gc.getPlayer(iLoop).getStartingPlot().getY()-iRadius and y <= gc.getPlayer(iLoop).getStartingPlot().getY()+iRadius):
                                                                                    if ((x,y) not in con.tNormalAreasSubtract[iLoop]):
                                                                                            lOwnedCities[iLoop] += 1
                                                                #RFCRAND - comment
##                                                                if (iLoop == con.iAmerica):
##                                                                        if (lOwnedCities[iLoop] >= 2):
##                                                                                lOwnedCities[iLoop] -= 2 #their normal area is too large
                        for iLoopCiv in range(iNumPlayers):
                                self.setOwnedPlotsLastTurn(iLoopCiv, lOwnedPlots[iLoopCiv])
                                self.setOwnedCitiesLastTurn(iLoopCiv, lOwnedCities[iLoopCiv])

                        #for up/down arrows
                        if (iGameTurn % 3 == 0 and gc.getActivePlayer().getNumCities() > 0):  #numcities required to test autoplay with minor civs
                                self.setLastRecordedStabilityStuff(0, self.getStability(utils.getHumanID()))
                                self.setLastRecordedStabilityStuff(1, utils.getParCities())
                                self.setLastRecordedStabilityStuff(2, utils.getParCivics())
                                self.setLastRecordedStabilityStuff(3, utils.getParEconomy())
                                self.setLastRecordedStabilityStuff(4, utils.getParExpansion())
                                self.setLastRecordedStabilityStuff(5, utils.getParDiplomacy())
                            

                
                for iPlayer in range(iNumPlayers):
                        
                        if (gc.getPlayer(iPlayer).isAlive()):
                                iTempNormalizationThreshold = self.getStability(iPlayer)
                                
                                if (iGameTurn > con.i1760AD and iGameTurn % 12 == 7):
                                        if (self.getStability(iPlayer) < 40):
                                                self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                                elif (iGameTurn > con.i1000BC and iGameTurn % 22 == 7):
                                        if (self.getStability(iPlayer) < 20 and self.getStability(iPlayer) >= -50):
                                                self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                                if (iGameTurn % 10 == 8):
                                        if (self.getStability(iPlayer) < -50):
                                                self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                                if (iGameTurn % 10 == 9):
                                        if (self.getStability(iPlayer) > 50):
                                                self.setStability(iPlayer, self.getStability(iPlayer) - 1 )
                                if (iGameTurn > con.i1000BC and iGameTurn % 12 == 5):
                                        iPermanentModifier = self.getStability(iPlayer) - self.getBaseStabilityLastTurn(iPlayer)
                                        if (iPermanentModifier > 15):
                                                self.setStability(iPlayer, self.getStability(iPlayer) - 1 )
                                        elif (iPermanentModifier < -40):
                                                self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                                if (iGameTurn % 20 == 1):
                                        if (gc.getPlayer(iPlayer).isHuman()):
                                                iHandicap = (gc.getGame().getHandicapType() - 1)
                                                self.setStability(iPlayer, self.getStability(iPlayer) + iHandicap )
                                
                                #print("stability wave", self.getStability(iPlayer) - iTempNormalizationThreshold)
                                self.setParameter(iPlayer, iParDiplomacyE, True, self.getStability(iPlayer) - iTempNormalizationThreshold)


                if (((iGameTurn > con.i600BC and gc.getPlayer(0).isPlayable()) or (iGameTurn > 181+20 and not gc.getPlayer(0).isPlayable())) and iGameTurn % 20 == 15): #late start condition
                #if (iGameTurn > 0): #debug
                        self.continentsNormalization(iGameTurn)
                        self.normalization(iGameTurn)
                        #debug
                        print ("Stability after normalization")
                        for iCiv in range(iNumPlayers):
                                if (gc.getPlayer(iCiv).isAlive()):
                                        print ("Base:", self.getBaseStabilityLastTurn(iCiv), "Modifier:", self.getStability(iCiv)-self.getBaseStabilityLastTurn(iCiv), "Total:", self.getStability(iCiv), "civic", gc.getPlayer(iCiv).getCivics(5), gc.getPlayer(iCiv).getCivilizationShortDescription(0))
                                else:
                                        print ("dead", iCiv)


        def continentsNormalization(self, iGameTurn):
                lContinentModifier = [0, 2, 0, -2, 0] #Eur, Far east, M. East, Med/Afr, Ame
                for iPlayer in range(iNumPlayers):
                        if (gc.getPlayer(iPlayer).isAlive()):
                                iTempNormalizationThreshold = self.getStability(iPlayer)
                                for j in range(len(con.lCivStabilityGroups)):
                                        if (iPlayer in con.lCivStabilityGroups[j]):
                                                self.setStability(iPlayer, (self.getStability(iPlayer) + lContinentModifier[j]))
                                self.setParameter(iPlayer, iParDiplomacyE, True, self.getStability(iPlayer) - iTempNormalizationThreshold)


        def normalization(self, iGameTurn):
                iMean = 0
                iTotal = 0
                iStandardMean = 3
                iSigma = 0
                iMinSigma = 7 + (iGameTurn - 100)/50
                iMaxSigma = 15 + (iGameTurn - 100)/50
                iStandardSigma = 11 + (iGameTurn - 100)/50
                iNumAlive = 0
                for iPlayer in range(iNumPlayers):
                        if (gc.getPlayer(iPlayer).isAlive()):
                                iNumAlive += 1
                                iTotal += self.getStability(iPlayer)
                iMean = iTotal/iNumAlive
                iDifferences = 0
                for iPlayer in range(iNumPlayers):
                        if (gc.getPlayer(iPlayer).isAlive()):
                               iDifferences += abs(self.getStability(iPlayer) - iMean)
                iSigma = iDifferences/iNumAlive

                #print ("mean=", iMean, "sigma=", iSigma)
                
                #division by zero fix
                if (iSigma == 0):
                        iSigma = 1
                        iStandardSigma = 8
                        iMinSigma = 5

                iMonitorPlayer = utils.getHumanID() #debug con.iRome
                iTempNormalizationThreshold = self.getStability(iMonitorPlayer)
                        
                if (iSigma > iMaxSigma+3):
                        #print ("Normalized sigma1")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, (self.getStability(iPlayer) - iMean)*iMaxSigma/iSigma + iMean )
                elif (iSigma > iMaxSigma):
                        #print ("Normalized sigma2")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, (self.getStability(iPlayer) - iMean)*iStandardSigma/iSigma + iMean )
                elif (iSigma < iMinSigma-3):
                        #print ("Normalized sigma3")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, (self.getStability(iPlayer) - iMean)*iMinSigma/iSigma + iMean )
                elif (iSigma < iMinSigma):
                        #print ("Normalized sigma4")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, (self.getStability(iPlayer) - iMean)*iStandardSigma/iSigma + iMean )
                #calculate mean again cos it might have changed for values close to 0
                for iPlayer in range(iNumPlayers):
                        if (gc.getPlayer(iPlayer).isAlive()):
                                iNumAlive += 1
                                iTotal += self.getStability(iPlayer)
                iMean = iTotal/iNumAlive
                #print ("mean=", iMean)
                
                if (iMean > iStandardMean+6):
                        #print ("Normalized mean1")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, self.getStability(iPlayer) - iMean + iStandardMean+3)
                elif (iMean > iStandardMean+3):
                        #print ("Normalized mean2")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, self.getStability(iPlayer) - iMean + iStandardMean)
                elif (iMean < iStandardMean-6):
                        #print ("Normalized mean3")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, self.getStability(iPlayer) - iMean + iStandardMean-3)
                elif (iMean < iStandardMean-3):
                        #print ("Normalized mean4")
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive()):
                                        self.setStability(iPlayer, self.getStability(iPlayer) - iMean + iStandardMean)

                #print("parametersE before", self.getStabilityParameters(iParDiplomacyE), self.getStabilityParameters(iParEconomyE), self.getStabilityParameters(iParCitiesE), self.getStabilityParameters(iParCivicsE), self.getStabilityParameters(iParExpansionE))
                #print("prestab", self.getStability(iMonitorPlayer))
                iVariation = self.getStability(iMonitorPlayer) - iTempNormalizationThreshold
                if (iVariation != 0):
                        for iLoopPoint in range (abs(iVariation)): #points are distributed in various categories
                                if (iLoopPoint % 5 == 0 or iLoopPoint % 5 == 1):
                                        if (iVariation > 0):
                                                self.setParameter(iMonitorPlayer, iParDiplomacyE, True, 1)
                                        else: 
                                                self.setParameter(iMonitorPlayer, iParDiplomacyE, True, -1)
                                elif (iLoopPoint % 5 == 2):
                                        if (iVariation > 0):
                                                self.setParameter(iMonitorPlayer, iParEconomyE, True, 1)
                                        else: 
                                                self.setParameter(iMonitorPlayer, iParEconomyE, True, -1)
                                elif (iLoopPoint % 5 == 3):
                                        if (iVariation > 0):
                                                self.setParameter(iMonitorPlayer, iParCitiesE, True, 1)
                                        else: 
                                                self.setParameter(iMonitorPlayer, iParCitiesE, True, -1)
                                elif (iLoopPoint % 5 == 4):
                                        if (iVariation > 0):
                                                self.setParameter(iMonitorPlayer, iParCivicsE, True, 1)
                                        else: 
                                                self.setParameter(iMonitorPlayer, iParCivicsE, True, -1)
                                
                #print("parametersE after ", self.getStabilityParameters(iParDiplomacyE), self.getStabilityParameters(iParEconomyE), self.getStabilityParameters(iParCitiesE), self.getStabilityParameters(iParCivicsE), self.getStabilityParameters(iParExpansionE))
                #self.setParameter(iPlayer, iParDiplomacyE, True, self.getStability(iMonitorPlayer) - iTempNormalizationThreshold)
                print ("Stability normalization:", self.getStability(iMonitorPlayer) - iTempNormalizationThreshold)


        def updateBaseStability(self, iGameTurn, iPlayer):

                pPlayer = gc.getPlayer(iPlayer)
                teamPlayer = gc.getTeam(pPlayer.getTeam())

                iCivic0 = pPlayer.getCivics(0)
                iCivic1 = pPlayer.getCivics(1)
                iCivic2 = pPlayer.getCivics(2)
                iCivic3 = pPlayer.getCivics(3)
                iCivic4 = pPlayer.getCivics(4)
                iCivic5 = pPlayer.getCivics(5)
                
                if (iGameTurn % 3 != 0):
                        iNewBaseStability = self.getPartialBaseStability(iPlayer)
                        iEconomy = pPlayer.calculateTotalYield(YieldTypes.YIELD_COMMERCE) - pPlayer.calculateInflatedCosts() #used later
                        iIndustry = pPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION) #used later
                        iAgriculture = pPlayer.calculateTotalYield(YieldTypes.YIELD_FOOD) #used later
                        iPopulation = pPlayer.getRealPopulation() #used later                        
                        iDifference = (iIndustry*1000000/iPopulation) - (iEconomy*1000000/iPopulation) #used later
                        iEraModifier = pPlayer.getCurrentEra() #used later

                        if (iPlayer == con.iMali): #counterbalance its UP
                                #iEconomy *= 4
                                #iEconomy /= 7
                                iEconomy /= 2

                        if (iPlayer == con.iEgypt or iPlayer == con.iMali or iPlayer == con.iEthiopia): #counterbalance the flood plains
                                iAgriculture *= 7 #3
                                iAgriculture /= 10 #5

                else:   #every 3 turns
                        iNewBaseStability = 0
               
                        iNewBaseStability += 10*teamPlayer.getDefensivePactTradingCount()
                        if (teamPlayer.getDefensivePactTradingCount() > 0):
                                #print("iNewBaseStability defensive pact",iNewBaseStability, iPlayer)
                                pass
                        
                        #if (teamPlayer.isPermanentAllianceTrading()):
                        #        iNewBaseStability += 10
                        #        #print("iNewBaseStability permanent alliance",iNewBaseStability, iPlayer)
                        
                        iNewBaseStability += 2*teamPlayer.getOpenBordersTradingCount()
                        #print("iNewBaseStability open borders",iNewBaseStability, iPlayer)

                        for iLoopCiv in range (iNumPlayers):
                                if (iLoopCiv in con.lNeighbours[iPlayer]):
                                        if (gc.getPlayer(iLoopCiv).isAlive()):
                                                if (self.getStability(iLoopCiv) < -20):
                                                        if (self.getStability(iPlayer) >= 0):
                                                                iNewBaseStability -= 5
                                                                #print("iNewBaseStability neighbours", iNewBaseStability, iPlayer)
                                                                break
                                
                        for iLoopCiv in range( iNumPlayers ):                                
                                if (teamPlayer.isVassal(iLoopCiv)):
                                        iNewBaseStability += 10                                
                                        #print("iNewBaseStability vassal",iNewBaseStability, iPlayer)
                                        iNewBaseStability += min(5,max(-6,self.getStability(iLoopCiv)/4))
                                        break

                        for iLoopCiv2 in range( iNumPlayers ):                                
                                if (gc.getTeam(gc.getPlayer(iLoopCiv2).getTeam()).isVassal(iPlayer)):
                                        iNewBaseStability += min(3,max(-3,self.getStability(iLoopCiv2)/4))                             
                                        #print("iNewBaseStability master",iNewBaseStability, iPlayer)
                                        if (iCivic5 == 26):
                                                iNewBaseStability += 4
                                                #print("iNewBaseStability civic 6th column viceroyalty",iNewBaseStability, iPlayer)

                        iNumContacts = 0
                        for iLoopCiv3 in range( iNumPlayers ):     
                                if (pPlayer.canContact(iLoopCiv3) and iLoopCiv3 != iPlayer):
                                        iNumContacts += 1
                        iNewBaseStability -= (iNumContacts/3 - 4)
                        #print("iNewBaseStability contacts",iNewBaseStability, iPlayer)
                        
                        self.setParameter(iPlayer, iParDiplomacy3, False, iNewBaseStability) 


                        iTempExpansionThreshold = iNewBaseStability

                        iMaxPlotsAbroad = 36
                        iHandicap = gc.getGame().getHandicapType()
                        if (iHandicap == 0):
                                iMaxPlotsAbroad = 44
                        elif (iHandicap == 1):
                                iMaxPlotsAbroad = 40
                        elif (iHandicap == 3):
                                iMaxPlotsAbroad = 32
                        elif (iHandicap == 4):
                                iMaxPlotsAbroad = 28

                        if (CyMap().getWorldSize() == 0): #huge
                                iMaxPlotsAbroad += 4
                        elif (CyMap().getWorldSize() == 0): #small
                                iMaxPlotsAbroad -= 4
                                
                        
                        iNumPlotsAbroad = max(0,self.getOwnedPlotsLastTurn(iPlayer)-iMaxPlotsAbroad)                        
                        iNewBaseStability -= iNumPlotsAbroad*2/7
                        #if (not gc.getPlayer(iPlayer).isHuman()):
                        #        iNewBaseStability += iNumPlotsAbroad*1/14
                        #print("iNewBaseStability number of owned plots abroad",iNewBaseStability, iPlayer)
                        if (self.getOwnedCitiesLastTurn(iPlayer) <= 20):
                                iNewBaseStability -= self.getOwnedCitiesLastTurn(iPlayer)*7
                        else:
                                iNewBaseStability -= (self.getOwnedCitiesLastTurn(iPlayer)-6)*10
                        #print("iNewBaseStability number of cities in homeland not owned", self.getOwnedCitiesLastTurn(iPlayer), iNewBaseStability, iPlayer)
                        self.setParameter(iPlayer, iParExpansion3, False, iNewBaseStability - iTempExpansionThreshold)

                                        
                        iTempCivicThreshold = iNewBaseStability
                        if (iCivic0 == 3 and iCivic1 == 9): #police and free speech
                                iNewBaseStability -= 10
                                #print("iNewBaseStability civic combination1",iNewBaseStability, iPlayer)
                        
                        if (iCivic4 == 22 and iCivic2 == 14): #theo and emanc
                                iNewBaseStability -= 3
                                #print("iNewBaseStability civic combination2",iNewBaseStability, iPlayer)

                        if (iCivic0 == 4 and iCivic1 == 5): #univ and barbar
                                iNewBaseStability -= 3
                                #print("iNewBaseStability civic combination3",iNewBaseStability, iPlayer)
                        
                        if (iCivic2 == 13 and iCivic3 == 18): #caste and state prop
                                iNewBaseStability -= 7
                                #print("iNewBaseStability civic combination4",iNewBaseStability, iPlayer)

                        if (iCivic0 == 0 and iCivic1 == 7): #despo and bureo
                                iNewBaseStability -= 2
                                #print("iNewBaseStability civic combination5",iNewBaseStability, iPlayer)
                                   
                        if (iCivic1 == 6 and iCivic3 == 18): #vassal and state prop
                                iNewBaseStability -= 7
                                #print("iNewBaseStability civic combination6",iNewBaseStability, iPlayer)

                        if (iCivic1 == 8 and iCivic4 == 23): #nation and pacifism
                                iNewBaseStability -= 10
                                #print("iNewBaseStability civic combination7",iNewBaseStability, iPlayer)
                                
                        if (iCivic0 == 3 and iCivic1 == 8): #police and nation
                                iNewBaseStability += 10
                                #print("iNewBaseStability civic combination8",iNewBaseStability, iPlayer)

                        if (iCivic0 == 3 and iCivic3 == 18): #police and state prop
                                iNewBaseStability += 5
                                #print("iNewBaseStability civic combination9",iNewBaseStability, iPlayer)

                        if (iCivic1 == 8 and iCivic3 == 16): #nation and mercant
                                iNewBaseStability += 6
                                #print("iNewBaseStability civic combination10",iNewBaseStability, iPlayer)
                                
                        if (iCivic0 == 1 and iCivic1 == 6): #heredit and vassal
                                iNewBaseStability += 3
                                #print("iNewBaseStability civic combination11",iNewBaseStability, iPlayer)
                                
                        if (iCivic0 == 2 and iCivic1 == 7): #repres and bureo
                                iNewBaseStability += 4
                                #print("iNewBaseStability civic combination12",iNewBaseStability, iPlayer)

                        if (iCivic2 == 14 and iCivic4 == 24): #emancip and free rel
                                iNewBaseStability += 2
                                #print("iNewBaseStability civic combination13",iNewBaseStability, iPlayer)

                        if (iCivic1 == 6): #vassallage
                                if (pPlayer.getCurrentEra() == 2):
                                        iNewBaseStability += 3
                                else:
                                        iNewBaseStability -= 3
                                #print("iNewBaseStability civic single 1",iNewBaseStability, iPlayer)

                        if (iCivic1 == 7): #burocr
                                if (pPlayer.getNumCities() <= 5):
                                        iNewBaseStability += 5
                                else:
                                        iNewBaseStability += max(-7,(5 - pPlayer.getNumCities()))
                                #print("iNewBaseStability civic single 2",iNewBaseStability, iPlayer)

                        if (iCivic0 == 2): #represent
                                iNewBaseStability += max(-7,2*(3 - pPlayer.getNumCities()))
                                #print("iNewBaseStability civic single 3",iNewBaseStability, iPlayer)

                        if (iCivic0 == 3): #police
                                iNewBaseStability += min(10, pPlayer.getNumCities()/5) #slightly counterbalances the effect of number of cities (below)

                                #print("iNewBaseStability civic single 4",iNewBaseStability, iPlayer)
                                
                        if (iCivic1 == 8): #nationhood
                                iNewBaseStability += 3*teamPlayer.getAtWarCount(True)
                                #print("iNewBaseStability civic single 5",iNewBaseStability, iPlayer)

                        if (iCivic0 == 0): #despotism
                                if (self.getStability(iPlayer) < -60):
                                        self.setStability(iPlayer, self.getStability(iPlayer)+20)
                                        #print("iNewBaseStability civic first column 1",iNewBaseStability, iPlayer)
                        if (iCivic0 == 1): #hereditary rule
                                if (self.getStability(iPlayer) < -50):
                                        self.setStability(iPlayer, -50)
                                        #print("iNewBaseStability civic first column 2",iNewBaseStability, iPlayer)
                        if (iCivic0 == 2): #representation
                                if (self.getStability(iPlayer) > 30):
                                        iNewBaseStability += 5
                                        #print("iNewBaseStability civic first column 3",iNewBaseStability, iPlayer)
                        if (iCivic0 == 3): #police state
                                if (self.getStability(iPlayer) < -60):
                                        self.setStability(iPlayer, self.getStability(iPlayer)+30)
                                        #print("iNewBaseStability civic first column 4",iNewBaseStability, iPlayer)
                        if (iCivic0 == 4): #universal suffrage
                                if (self.getStability(iPlayer) > 50):
                                        iNewBaseStability += 10
                                        #print("iNewBaseStability civic first column 5",iNewBaseStability, iPlayer)
                                        
                        if (teamPlayer.isHasTech(con.iDemocracy)):
                                if (iCivic0 != 4): #universal suffrage
                                        iNewBaseStability -= 3
                                        #print("iNewBaseStability universal suffrage",iNewBaseStability, iPlayer)
                                if (iCivic2 != 14): #emancipation
                                        iNewBaseStability -= 3
                                        #print("iNewBaseStability emancipation",iNewBaseStability, iPlayer)
                        if (teamPlayer.isHasTech(con.iLiberalism)):
                                if (iCivic1 != 9): #free speech
                                        iNewBaseStability -= 3
                                        #print("iNewBaseStability free speech",iNewBaseStability, iPlayer)

                        if (teamPlayer.isHasTech(con.iBronzeWorking) and not teamPlayer.isHasTech(con.iConstitution)):
                                if (iCivic2 == 11): #slavery
                                        iNewBaseStability += 3
                                        #print("iNewBaseStability slavery",iNewBaseStability, iPlayer)
                                
                        if (iCivic3 == 15): #decentralization
                                if (teamPlayer.isHasTech(con.iEconomics)):
                                        iNewBaseStability -= 5
                                        #print("iNewBaseStability decentralization",iNewBaseStability, iPlayer)    
                                        
                        self.setParameter(iPlayer, iParCivics3, False, iNewBaseStability - iTempCivicThreshold)


                        iTotalTempCityStability = 0
                        apCityList = PyPlayer(iPlayer).getCityList()

                        for pLoopCity in apCityList:
                                #RFCRAND
                                iX = pLoopCity.GetCy().getX()
                                iY = pLoopCity.GetCy().getY()
                                #if (gc.getPlayer(iPlayer).getSettlersMaps( 67-iY, iX ) < 150):
                                #if (gc.getPlayer(iPlayer).AI_blindSettlersMap( iX, iY, False ) < 150):
                                for iLoop in range(iNumMajorPlayers):
                                        if (iGameTurn > gc.getPlayer(iLoop).getBirthTurn() and iLoop != iPlayer): #RFCRAND
                                                tCapital = (gc.getPlayer(iPlayer).getStartingPlot().getX(), gc.getPlayer(iPlayer).getStartingPlot().getY())
                                                if (iX >= tCapital[0]-4 and iX <= tCapital[0]+4 and \
                                                    iY >= tCapital[1]-4 and iY <= tCapital[1]+4):
                                                        if (utils.blindSettlersMap( iPlayer, iX, iY ) < 150):
                                                                iNewBaseStability -= 3
                                                                self.setParameter(iPlayer, iParExpansion3, True, -3)                                                                
                                                                #print("city owned in unstable area: -3", pLoopCity.GetCy().getName(), iPlayer)
                                                                break
                                                        else:
                                                                iNewBaseStability -= 1
                                                                self.setParameter(iPlayer, iParExpansion3, True, -1)
                                                                #print("city owned in unstable area: -1", pLoopCity.GetCy().getName(), iPlayer)
                                                                break
                            
                        
                        for pCity in apCityList:
                                city = pCity.GetCy()
                                pCurrent = gc.getMap().plot(city.getX(), city.getY())
                                iTempCityStability = 0

                                if (iCivic5 == 28 and city.isOccupation()):                  
                                        #print("iTotalTempCityStability civic 6th column occupation", iTotalTempCityStability, city.getName(), iPlayer)
                                        pass
                                else:
                                        if (city.angryPopulation(0) > 0):
                                                iTempCityStability -= 2
                                        #if (city.healthRate(False, 0) < 0):
                                        #        iTempCityStability -= 2
                                        if (city.getReligionBadHappiness() > 0):
                                                iTempCityStability -= 2
                                        if (city.getLargestCityHappiness() < 0):
                                                iTempCityStability -= 2
                                        if (city.getHurryAngerModifier() > 0):
                                                iTempCityStability -= 2
                                        if (city.getNoMilitaryPercentAnger() > 0):
                                                iTempCityStability -= 1
                                        if (city.getWarWearinessPercentAnger() > 0):
                                                iTempCityStability -= 1

                                        if (iTempCityStability <= -5): #middle check, for optimization
                                                iTotalTempCityStability += max(-5,iTempCityStability)
                                                #print("iTotalTempCityStability", iTotalTempCityStability, city.getName(), iPlayer)
                                                if (iTotalTempCityStability <= -10): #middle check, for optimization
                                                        break
                                                else:
                                                        continue
                                                    
                                        if (iCivic4 == 21 or iCivic4 == 22): #org rel / theo
                                                iCounter = 0
                                                for iLoop in range(con.iNumReligions):                                    
                                                        if (city.isHasReligion(iLoop) and pPlayer.getStateReligion() != iLoop):
                                                                iTempCityStability -= 1
                                                                
                                        for iLoop in range(iNumTotalPlayers+1):
                                                if (iLoop != iPlayer):
                                                        if (pCurrent.getCulture(iLoop) > 0):
                                                                if (pCurrent.getCulture(iPlayer) == 0): #division by zero may happen
                                                                        iTempCityStability -= 2
                                                                elif (iCivic1 == 8): #nationhood
                                                                        if (pCurrent.getCulture(iLoop)*100/pCurrent.getCulture(iPlayer) >= 5):
                                                                                iTempCityStability -= 2
                                                                                break
                                                                else:
                                                                        if (pCurrent.getCulture(iLoop)*100/pCurrent.getCulture(iPlayer) >= 15):
                                                                                if (iPlayer == con.iTurkey or iPlayer == con.iAmerica or iPlayer == con.iPortugal or iPlayer == con.iNetherlands): #they have too much foreign culture
                                                                                        iTempCityStability -= 1
                                                                                else:
                                                                                        iTempCityStability -= 2
                                                                                break

                                        
                                        if (iTempCityStability < 0):
                                                iTotalTempCityStability += max(-5,iTempCityStability)
                                                #print("iTotalTempCityStability", iTotalTempCityStability, city.getName(), iPlayer)
                                        
                                        if (iTotalTempCityStability <= -12): #middle check, for optimization
                                                break

                        if (iTotalTempCityStability < 0):
                                iNewBaseStability += max(-12, iTotalTempCityStability)
                                #print("iNewBaseStability city check", iNewBaseStability, iPlayer)
                        self.setParameter(iPlayer, iParCities3, False, iTotalTempCityStability)

                        iTempEconomyThreshold = iNewBaseStability
                        iImports = pPlayer.calculateTotalImports(YieldTypes.YIELD_COMMERCE)
                        iExports = pPlayer.calculateTotalExports(YieldTypes.YIELD_COMMERCE)
                        iEraModifier = pPlayer.getCurrentEra()
                        iImportExportOffset = 5
                        
                        if (iPlayer == con.iChina or iPlayer == con.iJapan): #counterbalance their isolation
                                iImportExportOffset = 3
                                
                        if (iEraModifier >= 3):
                                iEraModifier += 1
                        if (iCivic5 != 29):
                                iNewBaseStability += min(10,(iImports+iExports)/(2*iEraModifier+1) -iImportExportOffset)
                                #print("iNewBaseStability import/export check", iNewBaseStability, iPlayer)
                        else:
                                iNewBaseStability += max(0, min(10,(iImports+iExports)/(2*iEraModifier+1) -iImportExportOffset))
                                #print("iNewBaseStability import/export check + civic 6th column commonwealth", iNewBaseStability, iPlayer)

                        iEconomy = pPlayer.calculateTotalYield(YieldTypes.YIELD_COMMERCE) - pPlayer.calculateInflatedCosts()
                        iIndustry = pPlayer.calculateTotalYield(YieldTypes.YIELD_PRODUCTION)
                        iAgriculture = pPlayer.calculateTotalYield(YieldTypes.YIELD_FOOD)
                        iPopulation = pPlayer.getRealPopulation()

                        if (iPlayer == con.iIndia or iPlayer == con.iChina or iPlayer == con.iJapan): #counterbalance the low growth threshold of ancient civs
                                iPopulation *= 3
                                iPopulation /= 4
                        if (iPlayer == con.iEgypt or iPlayer == con.iMaya or iPlayer == con.iMali or iPlayer == con.iKhmer): #counterbalance the high growth threshold
                                iPopulation *= 4
                                iPopulation /= 3

                        if (iPlayer == con.iMali): #counterbalance its UP
                                #iEconomy *= 4
                                #iEconomy /= 7
                                iEconomy /= 2

                        if (iPlayer == con.iEgypt or iPlayer == con.iMali or (iPlayer == con.iEthiopia and not gc.getPlayer(con.iEgypt).isAlive())): #counterbalance the flood plains
                                iAgriculture *= 75 #3
                                iAgriculture /= 100 #5
                        
                        iNewBaseStability += min(8,max(-8,(iAgriculture*100000/iPopulation - 8 + (iEraModifier - 3)*2)))
                        #print("iNewBaseStability Agriculture/Population check", iNewBaseStability, iPlayer)
                        iMaxEconomyGain = 3
                        iMaxEconomyLoss = -3
                        if (iCivic5 != 29):
                                iNewBaseStability += min(iMaxEconomyGain,max(iMaxEconomyLoss,(iEconomy*100000/iPopulation - 5 + (iEraModifier - 3)*2))) #less important cos it's already counted in other parameters
                                #print("iNewBaseStability Economy/Population check", iNewBaseStability, iPlayer)
                        else:
                                iNewBaseStability += min(iMaxEconomyGain,max(0,(iEconomy*100000/iPopulation - 5 + (iEraModifier - 3)*2)))
                                #print("iNewBaseStability Economy/Population check + civic 6th column commonwealth", iNewBaseStability, iPlayer)

                        self.setParameter(iPlayer, iParEconomy3, False, iNewBaseStability - iTempEconomyThreshold)

                        iDifference = (iIndustry*1000000/iPopulation) - (iEconomy*1000000/iPopulation)



                        iHappiness = -10
                        if (pPlayer.calculateTotalCityHappiness() > 0):
                                iHappiness = int((1.0 * pPlayer.calculateTotalCityHappiness()) / (pPlayer.calculateTotalCityHappiness() + \
                                                pPlayer.calculateTotalCityUnhappiness()) * 100) - 60			
                        iNewBaseStability += iHappiness/10
                        self.setParameter(iPlayer, iParCities3, True, iHappiness/10)                        
                        #print("iNewBaseStability happiness check", iNewBaseStability, iPlayer)

                        #iHealth = -30
                        #if (pPlayer.calculateTotalCityHealthiness() > 0):
                        #        iHealth = int((1.0 * pPlayer.calculateTotalCityHealthiness()) / (pPlayer.calculateTotalCityHealthiness() + \
                        #                        pPlayer.calculateTotalCityUnhealthiness()) * 100) - 60
                        #iNewBaseStability += iHealth/10
                        ##print("iNewBaseStability health check", iNewBaseStability, iPlayer)
                        
                        self.setPartialBaseStability(iPlayer, iNewBaseStability)


                #every turn

                if (iGameTurn >= gc.getPlayer(iPlayer).getBirthTurn()+utils.getBirthTurnModifier(iPlayer)+15): #RFCRAND
                        self.setGNPnew(iPlayer, self.getGNPnew(iPlayer) + (iEconomy + 4*iIndustry + 2*iAgriculture)/7)
                        if (iGameTurn % 3 == 2):
                                iTempEconomyThreshold = self.getStability(iPlayer)
                                iMaxShrink = 7
                                iMaxGrowth = 3
                                iNegativeFasterGrowth = (self.getGNPnew(iPlayer)-4)/3 - self.getGNPold(iPlayer)/3   #-1:-1 -2:-2 -3:-2 -4:-2 -5:-3 -6:-3 -7:-3 -8:-4 
                                iNegativeNormalGrowth = (self.getGNPnew(iPlayer)-3)/3 - self.getGNPold(iPlayer)/3   #-1:-1 -2:-1 -3:-2 -4:-2 -5:-2 -6:-3 -7:-3 -8:-3 
                                iNegativeSlowerGrowth = (self.getGNPnew(iPlayer)-1)/3 - self.getGNPold(iPlayer)/3   #-1: 0 -2:-1 -3:-1 -4:-1 -5:-2 -6:-2 -7:-2 -8:-3 
                                
                                iPositiveFasterGrowth = self.getGNPnew(iPlayer)/3 - self.getGNPold(iPlayer)/3   # 0: 0 +1: 0 +2: 0 +3:+1 +4:+1 +5:+1 +6:+2 +7:+2 +8:+2 +9:+3   
                                iPositiveNormalGrowth = self.getGNPnew(iPlayer)/4 - self.getGNPold(iPlayer)/4       # 0: 0 +1: 0 +2: 0 +3: 0 +4:+1 +5:+1 +6:+1 +7:+1 +8:+2 +9:+2 
                                iPositiveSlowerGrowth = self.getGNPnew(iPlayer)/5 - self.getGNPold(iPlayer)/5       # 0: 0 +1: 0 +2: 0 +3: 0 +4: 0 +5:+1 +6:+1 +7:+1 +8:+1 +9:+1 

                                iNegativeGrowth = iNegativeNormalGrowth
                                iPositiveGrowth = iPositiveNormalGrowth
                                if (iPlayer == con.iEgypt or iPlayer == con.iIndia or iPlayer == con.iChina or iPlayer == con.iBabylonia): #counterbalance their stagnation due to the very early start
                                        iNegativeGrowth = iNegativeSlowerGrowth
                                if (iPlayer == con.iNetherlands or iPlayer == con.iMali or iPlayer == con.iPortugal or iPlayer == con.iMongolia or iPlayer == con.iTurkey): #counterbalance their late start
                                        iNegativeGrowth = iPositiveSlowerGrowth
                                if (iPlayer == con.iMali or iPlayer == con.iPortugal or iPlayer == con.iMongolia or iPlayer == con.iTurkey or iPlayer == con.iAmerica): #counterbalance their late start
                                        iNegativeGrowth = iNegativeFasterGrowth
                                if (iPlayer == con.iJapan or iPlayer == con.iInca): #counterbalance their stagnation due to isolation
                                        iNegativeGrowth = iNegativeSlowerGrowth
                                if (iPlayer == con.iIndia or iPlayer == con.iChina or iPlayer == con.iJapan or iPlayer == con.iKhmer or iPlayer == con.iMaya or iPlayer == con.iAztecs or iPlayer == con.iInca): #counterbalance their stagnation due to isolation
                                        iPositiveGrowth = iPositiveFasterGrowth
                                                          
                                if (self.getGNPnew(iPlayer) < self.getGNPold(iPlayer)):
                                        self.setStability(iPlayer, self.getStability(iPlayer) + max(-iMaxShrink, iNegativeGrowth))
                                        #print("Stability - GNP check", iNegativeGrowth, iPlayer)
                                elif (self.getGNPnew(iPlayer) >= self.getGNPold(iPlayer)):
                                        self.setStability(iPlayer, self.getStability(iPlayer) + min(iMaxGrowth, iPositiveGrowth))
                                        #print("Stability - GNP check", iPositiveGrowth, iPlayer)
                                
                                self.setParameter(iPlayer, iParEconomyE, True, self.getStability(iPlayer) - iTempEconomyThreshold)


                                if (self.getGreatDepressionCountdown(iPlayer) == 0):   #great depression checked when GNP can be compared
                                        if (iCivic3 == 17 and teamPlayer.isHasTech(con.iCorporation)): #free market
                                                if (not pPlayer.isGoldenAge()):
                                                        if ((iDifference > 11 and self.getGNPnew(iPlayer) > self.getGNPold(iPlayer)) or \
                                                            (iDifference > 6 and self.getGNPnew(iPlayer) > self.getGNPold(iPlayer) + 4)): #low wages and big growth
                                                                self.setGreatDepressionCountdown(iPlayer, 8) #8 turns
                                                                print ("Start Great Depression Player", iPlayer)
                                                                
                if (self.getGreatDepressionCountdown(iPlayer) < 0):
                        self.setGreatDepressionCountdown(iPlayer, self.getGreatDepressionCountdown(iPlayer)+1)
                                                                
                iTempEconomyThreshold = iNewBaseStability
                if (self.getGreatDepressionCountdown(iPlayer) > 0):
                        iNewBaseStability -= (15 + min(15, iDifference))
                        if (iPlayer == utils.getHumanID()):
                                CyInterface().addMessage(iPlayer, False, con.iDuration, CyTranslator().getText("TXT_KEY_STABILITY_PERIOD", ()) + " " + CyTranslator().getText("TXT_KEY_STABILITY_GREAT_DEPRESSION", ()), "", 0, "", ColorTypes(con.iOrange), -1, -1, True, True)
                        #print("iNewBaseStability civic single 5: great depression",iNewBaseStability, iPlayer)
                        self.setGreatDepressionCountdown(iPlayer, self.getGreatDepressionCountdown(iPlayer)-1)
                        bQuit = False
                        if (self.getGreatDepressionCountdown(iPlayer) == 0): #just quit
                                bQuit = True
                        if (self.getGreatDepressionCountdown(iPlayer) > 0 and self.getGreatDepressionCountdown(iPlayer) <= 7): #should last at least 3 turns 
                                if ((iDifference < 5 and self.getGNPnew(iPlayer) <= self.getGNPold(iPlayer)) or iCivic3 != 17): #better wages and natural deflation, or no free market anymore
                                        bQuit = True
                                        
                        if (bQuit == True):
                                self.setGreatDepressionCountdown(iPlayer, -30) ##quit from the spiral immediately and set turns of immunity
                                bOtherDepressionAround = False
                                for iLoopCiv in range(iNumPlayers):
                                        if (self.getGreatDepressionCountdown(iLoopCiv) > 0):
                                                bOtherDepressionAround = True
                                if (bOtherDepressionAround == False):
                                        for iLoopCiv in range(iNumPlayers):
                                                if (iLoopCiv != iPlayer):
                                                        self.setGreatDepressionCountdown(iPlayer, -20) ##set turns of immunity for the other civs

                if (iGameTurn % 3 == 2):
                        self.setGNPold(iPlayer, self.getGNPnew(iPlayer))
                        self.setGNPnew(iPlayer, 0)

                if (self.getGreatDepressionCountdown(iPlayer) == 0 and iCivic3 != 18 and not pPlayer.isGoldenAge()):   #acquire only if there's no depression already and if it's not immune, no state property and no golden age
                        for iLoopCiv in range(iNumPlayers):
                                if (teamPlayer.isOpenBorders(iLoopCiv)):
                                        if (self.getGreatDepressionCountdown(iLoopCiv) > 0):
                                                if (iCivic3 == 16): #mercantilism
                                                        iNewBaseStability -= 4
                                                else:
                                                        iNewBaseStability -= 10
                                                #print("acquired great depression", iPlayer, "from", iLoopCiv)                        
                                                #print("iNewBaseStability: acquired great depression",iNewBaseStability, iPlayer)                        
                                                if (iPlayer == utils.getHumanID()):
                                                        CyInterface().addMessage(iPlayer, False, con.iDuration, \
                                                                                 CyTranslator().getText("TXT_KEY_STABILITY_GREAT_DEPRESSION_INFLUENCE", (gc.getPlayer(iLoopCiv).getCivilizationDescription(0),)), \
                                                                                 "", 0, "", ColorTypes(con.iOrange), -1, -1, True, True)
                                                break #just once is enough
         
                
                if (teamPlayer.isHasTech(con.iCommunism)): #post communism
                        if (iCivic3 == 18): #state prop
                                self.setStatePropertyCountdown(iPlayer, -1) #has state property
                        if (self.getStatePropertyCountdown(iPlayer) == -1 and iCivic3 != 18): #switched
                                self.setStatePropertyCountdown(iPlayer, 8) #8 turns
                        if (self.getStatePropertyCountdown(iPlayer) > 0):
                                iNewBaseStability -= 25
                                self.setStatePropertyCountdown(iPlayer, self.getStatePropertyCountdown(iPlayer)-1)
                                if (iPlayer == utils.getHumanID()):
                                        CyInterface().addMessage(iPlayer, False, con.iDuration, CyTranslator().getText("TXT_KEY_STABILITY_PERIOD", ()) + " " + CyTranslator().getText("TXT_KEY_STABILITY_POST_COMMUNISM", ()), "", 0, "", ColorTypes(con.iOrange), -1, -1, True, True)
                                #print("iNewBaseStability civic single 6: post communism",iNewBaseStability, iPlayer)
                self.setParameter(iPlayer, iParEconomy1, False, iNewBaseStability - iTempEconomyThreshold)

                iTempCivicThreshold = iNewBaseStability
                if (teamPlayer.isHasTech(con.iDemocracy)): #transition to democracy
                        if (iCivic0 == 0 or iCivic0 == 1 or iCivic0 == 3): #despotic governments
                                self.setDemocracyCountdown(iPlayer, -1) #has a desp. gov.
                        if (self.getDemocracyCountdown(iPlayer) == -1 and iCivic0 == 4): #switched to universal suffrage
                                self.setDemocracyCountdown(iPlayer, 7) #7 turns
                        if (self.getDemocracyCountdown(iPlayer) > 0):
                                iNewBaseStability -= 20
                                self.setDemocracyCountdown(iPlayer, self.getDemocracyCountdown(iPlayer)-1)
                                if (iPlayer == utils.getHumanID()):
                                        CyInterface().addMessage(iPlayer, False, con.iDuration, CyTranslator().getText("TXT_KEY_STABILITY_PERIOD", ()) + " " + CyTranslator().getText("TXT_KEY_STABILITY_DEMOCRACY", ()), "", 0, "", ColorTypes(con.iOrange), -1, -1, True, True)
                                #print("iNewBaseStability civic single 7: transition to democracy",iNewBaseStability, iPlayer)
                self.setParameter(iPlayer, iParCivics1, False, iNewBaseStability - iTempCivicThreshold)

                iTempExpansionThreshold = iNewBaseStability
                iNumPlayerCities = pPlayer.getNumCities()
                if (iNumPlayerCities < 8):
                        pass
                else:
                        iNewBaseStability -= (iNumPlayerCities-5)*(iNumPlayerCities-5)/9
                        #print("iNewBaseStability number of cities",iNewBaseStability, iPlayer)
                self.setParameter(iPlayer, iParExpansion1, False, iNewBaseStability - iTempExpansionThreshold)


                if (self.getCombatResultTempModifier(iPlayer) != 0):
                        iTempExpansionThreshold = iNewBaseStability
                        iNewBaseStability += max(-20, min(20,self.getCombatResultTempModifier(iPlayer)))
                        self.setParameter(iPlayer, iParExpansion1, True, iNewBaseStability - iTempExpansionThreshold) 
                        #print("iNewBaseStability combat result", iNewBaseStability, iPlayer)
                        if (self.getCombatResultTempModifier(iPlayer) <= -4 -(iEraModifier/2)): #great loss
                                self.setStability(iPlayer, self.getStability(iPlayer) -1)
                                self.setParameter(iPlayer, iParDiplomacyE, True, -1)
                                #print("Stability: combat result - great loss", self.getCombatResultTempModifier(iPlayer), iPlayer)
                        if (abs(self.getCombatResultTempModifier(iPlayer)) >= 4):
                                self.setCombatResultTempModifier(iPlayer, self.getCombatResultTempModifier(iPlayer)/2)
                        else:
                                self.setCombatResultTempModifier(iPlayer, 0)
                                                        
                if (pPlayer.getAnarchyTurns() != 0):
                        iTempCivicsThreshold = self.getStability(iPlayer)
                        if (self.getStability(iPlayer) > 24):
                                #print("Stability: anarchy permanent", self.getStability(iPlayer) - self.getStability(iPlayer)/8, iPlayer)
                                self.setStability(iPlayer, self.getStability(iPlayer) - self.getStability(iPlayer)/8)                                
                        else:
                                #print("Stability: anarchy permanent", 3, iPlayer)
                                self.setStability(iPlayer, self.getStability(iPlayer)-3)
                        self.setParameter(iPlayer, iParCivicsE, True, self.getStability(iPlayer) - iTempCivicsThreshold)
                        iNewBaseStability -= (self.getStability(iPlayer)+30)/2
                        self.setParameter(iPlayer, iParCivics1, True, -(self.getStability(iPlayer)+30)/2) 
                        #print("iNewBaseStability anarchy",iNewBaseStability, iPlayer)
                        

                if (pPlayer.isGoldenAge()):
                        iNewBaseStability += 20
                        #print("iNewBaseStability golden",iNewBaseStability, iPlayer)
                        self.setParameter(iPlayer, iParEconomy1, True, 20) 
                
                
                  
                ##print ("iNewBaseStability", iNewBaseStability)

                                
                self.setStability(iPlayer, self.getStability(iPlayer) - self.getBaseStabilityLastTurn(iPlayer) + iNewBaseStability)
                if (self.getStability(iPlayer) < -80):
                        self.setStability(iPlayer, -80)
                if (self.getStability(iPlayer) > 80):
                        self.setStability(iPlayer, 80)
                        
                self.setBaseStabilityLastTurn(iPlayer, iNewBaseStability)
                                 



        def onCityBuilt(self, iPlayer, x, y):

                iTempExpansionThreshold = self.getStability(iPlayer)
                iGameTurn = gc.getGame().getGameTurn()
                if (iGameTurn <= gc.getPlayer(iPlayer).getBirthTurn() + 20): #RFCRAND
                        self.setStability(iPlayer, self.getStability(iPlayer) + 3 )
                else:
                        self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                #print("Stability - city built", iPlayer)
                if (gc.getPlayer(iPlayer).getNumCities() == 1):
                        self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                        #print("Stability - capital built", iPlayer)
                if (gc.getPlayer(iPlayer).getCivics(5) == 27):
                        capital = gc.getPlayer(iPlayer).getCapitalCity()
                        iDistance = utils.calculateDistance(x, y, capital.getX(), capital.getY())
                        if (iDistance >= 15):
                                self.setStability(iPlayer, self.getStability(iPlayer) + 2 )
                                #print("Stability - civic 6th column resettlement", iPlayer)
                self.setParameter(iPlayer, iParExpansionE, True, self.getStability(iPlayer) - iTempExpansionThreshold) 
                             


        def onCityAcquired(self, owner, playerType, city, bConquest, bTrade):

                iGameTurn = gc.getGame().getGameTurn()
                #RFCRAND
                iBirthTurnModifier = 0
                if (playerType < iNumMajorPlayers):
                        iBirthTurnModifier = utils.getBirthTurnModifier(playerType) 
                if (owner < con.iNumPlayers):
                        iTotalCityLostModifier = 0                        
                        if (bTrade and (iGameTurn == gc.getPlayer(playerType).getBirthTurn()+iBirthTurnModifier or iGameTurn == gc.getPlayer(playerType).getBirthTurn()+iBirthTurnModifier+1 or iGameTurn == gc.getPlayer(playerType).getBirthTurn()+iBirthTurnModifier+2)): #RFCRAND
                                iTotalCityLostModifier = 3 #during a civ birth
                                if (not gc.getPlayer(owner).isHuman()):
                                        iTotalCityLostModifier += 1
                        elif (bTrade and playerType == self.getRebelCiv() and iGameTurn == self.getLatestRebellionTurn(playerType)):
                                iTotalCityLostModifier = 2 #during a civ resurrection
                        else:
                                iTotalCityLostModifier = max(-5,(16 - gc.getPlayer(owner).getNumCities())/2) #conquering 40 cities and immediately releasing them is an exploit - cap added
                                if (bTrade):                                        
                                        iTotalCityLostModifier += 2
                                        #self.setParameter(owner, iParDiplomacyE, True, -1)
                                        if (gc.getPlayer(owner).isHuman()): #anti-exploit
                                                if (city.isOccupation()):
                                                        self.setStability(owner, self.getStability(owner) - 3 ) 
                                                        self.setParameter(owner, iParDiplomacyE, True, -3)
                                                        self.setStability(playerType, self.getStability(playerType) + 3 )
                                                        self.setParameter(playerType, iParDiplomacyE, True, +3) 
                                #RFCRAND
                                #if (city.getX() == tCapitals[owner][0] and city.getY() == tCapitals[owner][1]):
                                if (city.getX() == gc.getPlayer(owner).getStartingPlot().getX() and city.getY() == gc.getPlayer(owner).getStartingPlot().getX()):
                                        iTotalCityLostModifier += 20
                                if (playerType == con.iBarbarian or playerType == con.iCeltia):
                                        iTotalCityLostModifier += 1                        
                        self.setParameter(owner, iParExpansionE, True, -iTotalCityLostModifier) 
                        self.setStability(owner, self.getStability(owner) - iTotalCityLostModifier )
                        #print("Stability - city lost", iTotalCityLostModifier, owner)
                        
                if (playerType < con.iNumPlayers):
                        iTempExpansionThreshold = self.getStability(playerType)
                        if (iGameTurn == gc.getPlayer(playerType).getBirthTurn()+iBirthTurnModifier or iGameTurn == gc.getPlayer(playerType).getBirthTurn()+iBirthTurnModifier+1 or iGameTurn == gc.getPlayer(playerType).getBirthTurn()+iBirthTurnModifier+2): #RFCRAND
                                self.setStability(playerType, self.getStability(playerType) + 3)
                        elif (owner >= con.iNumPlayers):
                                self.setStability(playerType, self.getStability(playerType) + max(0,min(5,(12 - gc.getPlayer(playerType).getNumCities())/2)) )
                        else:
                                self.setStability(playerType, self.getStability(playerType) + max(0,min(5,(12 - gc.getPlayer(playerType).getNumCities())/2)) )
                        #print("Stability - city acquired", playerType)
                        #Persian UP
                        if (playerType == con.iPersia and gc.getPlayer(playerType).getCivics(5) != 28):
                                if (bConquest):                                
                                        self.setStability(playerType, self.getStability(playerType) + 2)
                        
                        if (gc.getPlayer(playerType).getCivics(5) == 28):
                                if (bConquest):
                                        self.setStability(playerType, self.getStability(playerType) + 2 )
                                        #print("iNewBaseStability civic 6th column occupation",playerType)
                        if (owner < con.iNumPlayers):
                                if (city.getX() == gc.getPlayer(owner).getStartingPlot().getX() and city.getY() == gc.getPlayer(owner).getStartingPlot().getY()):  #RFCRAND
                                        self.setStability(playerType, self.getStability(playerType) + 3)
                                        #print("Stability - capital city acquired", playerType)
                        self.setParameter(playerType, iParExpansionE, True, self.getStability(playerType) - iTempExpansionThreshold) 
                            

                
     


        def onCityRazed(self, iOwner, playerType, city):
            
                if (iOwner < con.iNumPlayers):      
                        self.setStability(iOwner, self.getStability(iOwner) - 3 )
                        #print("Stability - city razed", -3, iOwner)
                        self.setParameter(iOwner, iParExpansionE, True, - 3)

                if (playerType < con.iNumPlayers):
                        iTempExpansionThreshold = self.getStability(playerType)                 
                        if (gc.getPlayer(playerType).getCivics(5) == 28):
                                self.setStability(playerType, self.getStability(playerType) - 2 ) #balance the +2 and makes 0 for city razed
                        self.setParameter(playerType, iParExpansionE, True, self.getStability(playerType) - iTempExpansionThreshold) 


                                                
        def onImprovementDestroyed(self, owner):

                if (owner < con.iNumPlayers and owner >= 0):
                        pass
                        #self.setStability(owner, self.getStability(owner) - 1 )
                        ##print("Stability - improvement destroyed", owner)


        def onTechAcquired(self, iTech, iPlayer):
            
                iTempCivicsThreshold = self.getStability(iPlayer)

                if (iTech == con.iMonotheism or \
                    #iTech == con.iCivilService or \
                    iTech == con.iNationalism or \
                    iTech == con.iConstitution or \
                    #iTech == con.iLiberalism or \ #already in base stability count
                    #iTech == con.iDemocracy or \ #already in base stability count
                    iTech == con.iFascism or \
                    iTech == con.iCommunism or \
                    iTech == con.iPhilosophy or \
                    #iTech == con.iAstronomy or \
                    iTech == con.iFission or \
                    #iTech == con.iFlight or \
                    iTech == con.iGenetics or \
                    iTech == con.iGunpowder or \
                    iTech == con.iSteamPower or \
                    #iTech == con.iRailroad or \
                    iTech == con.iIndustrialism or \
                    iTech == con.iRocketry):
                        self.setStability(iPlayer, self.getStability(iPlayer) - 2 )
                        #print("Stability - tech acquired --", iTech, iPlayer)
                elif (iTech == con.iTheology or \
                    iTech == con.iFeudalism or \
                    iTech == con.iArchery or \
                    iTech == con.iHorsebackRiding or \
                    iTech == con.iBronzeWorking or \
                    iTech == con.iIronWorking or \
                    iTech == con.iRifling or \
                    iTech == con.iAssemblyLine):
                        self.setStability(iPlayer, self.getStability(iPlayer) - 1 )
                        #print("Stability - tech acquired -", iTech, iPlayer)                        
                elif (iTech == con.iMysticism  or \
                    iTech == con.iMeditation or \
                    iTech == con.iPriesthood or \
                    iTech == con.iMonarchy or \
                    iTech == con.iLiterature or \
                    iTech == con.iCodeOfLaws or \
                    iTech == con.iDivineRight or \
                    iTech == con.iMilitaryTradition or \
                    iTech == con.iFishing or \
                    iTech == con.iAgriculture or \
                    iTech == con.iPottery or \
                    iTech == con.iWriting or \
                    iTech == con.iAlphabet or \
                    iTech == con.iCalendar or \
                    iTech == con.iCurrency or \
                    iTech == con.iBanking or \
                    iTech == con.iEducation or \
                    iTech == con.iPrintingPress or \
                    iTech == con.iBiology or \
                    iTech == con.iMedicine or \
                    iTech == con.iElectricity or \
                    iTech == con.iFiberOptics or \
                    iTech == con.iMining or \
                    iTech == con.iMasonry or \
                    iTech == con.iConstruction or \
                    iTech == con.iMachinery or \
                    iTech == con.iEngineering or \
                    iTech == con.iRefrigeration):
                        self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                        #print("Stability - tech acquired +", iTech, iPlayer)
                else:
                        #self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                        #print("Stability - tech acquired =", iTech, iPlayer)
                        pass

                if (iTech == con.iCompass or iTech == con.iAstronomy):
                        if (not gc.getPlayer(iPlayer).isHuman()):
                                if (iPlayer == con.iSpain or \
                                    iPlayer == con.iFrance or \
                                    iPlayer == con.iEngland or \
                                    iPlayer == con.iNetherlands or \
                                    iPlayer == con.iPortugal):
                                        self.setStability(iPlayer, self.getStability(iPlayer) + 3 ) #need them alive for accurate colonization
                                        print ("stability bonus for colonizers", iPlayer)
                if (iTech == con.iAstronomy or iTech == con.iMilitaryTradition):
                        if (not gc.getPlayer(iPlayer).isHuman()):
                                if (iPlayer == con.iGermany or \
                                    iPlayer == con.iRussia):
                                        self.setStability(iPlayer, self.getStability(iPlayer) + 2 )

                self.setParameter(iPlayer, iParCivicsE, True, self.getStability(iPlayer) - iTempCivicsThreshold)

        def onBuildingBuilt(self, iPlayer, iBuilding, city):

                iTempCitiesThreshold = self.getStability(iPlayer)
                if (iBuilding == con.iPalace): #palace
                        self.setStability(iPlayer, self.getStability(iPlayer) - 10 )
                        #print("Stability - palace built", iPlayer)
                elif (iBuilding > con.iPalace and iBuilding <= con.iForbiddenPalace): #palaces
                        self.setStability(iPlayer, self.getStability(iPlayer) + 5 )
                        #print("Stability - palace built", iPlayer)
                elif (iBuilding >= con.iHeroicEpic and iBuilding <= con.iOlympicPark): #wonder
                        self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                        #print("Stability - wonder built", iPlayer)
                        if (self.getGreatDepressionCountdown(iPlayer) >= 2):
                                self.setGreatDepressionCountdown(iPlayer, self.getGreatDepressionCountdown(iPlayer)-2)
                                #print("Stability - Great Depression reduced", iPlayer)
                elif (iBuilding == con.iJail or iBuilding == con.iIndianMausoleum): #jail
                        if (self.getStability(iPlayer) < 20):
                                if (gc.getPlayer(iPlayer).getCivics(0) == 3): #police state
                                        self.setStability(iPlayer, self.getStability(iPlayer) + 2 )
                                else:
                                        self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                        #print("Stability - jail built", iPlayer)
                elif (iBuilding == con.iCourthouse or iBuilding == con.iAztecSacrificialAltar or iBuilding == con.iSumerianZiggurat): #courthouse
                        if (not city.hasBuilding(con.iPalace) and not city.hasBuilding(con.iForbiddenPalace) and not city.hasBuilding(con.iSummerPalace)):
                                if (self.getStability(iPlayer) < 0):
                                        self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                                        #print("Stability - courthouse built", iPlayer)
                elif (iBuilding == con.iInterpol):
                        if (self.getStability(iPlayer) < 20):
                                self.setStability(iPlayer, self.getStability(iPlayer) + 2 )
                elif (iBuilding == con.iNationalSecurity):
                        if (self.getStability(iPlayer) < -10):
                                self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                elif (iBuilding == con.iIntelligenceAgency):
                        if (self.getStability(iPlayer) < -40):
                                self.setStability(iPlayer, self.getStability(iPlayer) + 1 )

                self.setParameter(iPlayer, iParCitiesE, True, self.getStability(iPlayer) - iTempCitiesThreshold)

                    


                            
        def onProjectBuilt(self, iPlayer, iProject):
            
                if (iProject <= con.iApolloProgram ): #no SS parts
                        self.setStability(iPlayer, self.getStability(iPlayer) + 1 )
                        self.setParameter(iPlayer, iParCitiesE, True, 2)
                        #print("Stability - project built", iPlayer)
                #pass




        def onCombatResult(self, argsList):

                pWinningUnit,pLosingUnit = argsList
                iWinningPlayer = pWinningUnit.getOwner()
                iLosingPlayer = pLosingUnit.getOwner()

                if (iWinningPlayer < con.iNumPlayers):  
                        self.setCombatResultTempModifier(iWinningPlayer, self.getCombatResultTempModifier(iWinningPlayer) + 1 )
                        #print("Stability - iWinningPlayer", self.getCombatResultTempModifier(iWinningPlayer), iWinningPlayer)
                if (iLosingPlayer < con.iNumPlayers):  
                        self.setCombatResultTempModifier(iLosingPlayer, self.getCombatResultTempModifier(iLosingPlayer) - 2 )
                        #print("Stability - iLosingPlayer", self.getCombatResultTempModifier(iLosingPlayer), iLosingPlayer)


        def onReligionFounded(self, iPlayer):

                self.setStability(iPlayer, self.getStability(iPlayer) - 2 )
                self.setParameter(iPlayer, iParCitiesE, True, -2)
                #print("Stability - onReligionFounded", iPlayer)


        def onCorporationFounded(self, iPlayer):

                self.setStability(iPlayer, self.getStability(iPlayer) - 2 )
                self.setParameter(iPlayer, iParCitiesE, True, -2)
                #print("Stability - onCorporationFounded", iPlayer)


        def onReligionSpread(self, iReligion, iPlayer):

                if (iPlayer < iNumPlayers):  
                        pPlayer = gc.getPlayer(iPlayer)
                        if (pPlayer.getStateReligion() != iReligion):
                                for iLoopCiv in range(iNumPlayers):
                                        if (gc.getTeam(pPlayer.getTeam()).isAtWar(iLoopCiv)):
                                                if (gc.getPlayer(iLoopCiv).getStateReligion() == iReligion):
                                                        self.setStability(iPlayer, self.getStability(iPlayer) - 1 )
                                                        self.setParameter(iPlayer, iParCitiesE, True, -1)
                                                        #print("Stability - onReligionSpread", iPlayer)
                                                        break

       	
        def checkImplosion(self, iGameTurn):
    
                if (iGameTurn > con.i350BC and iGameTurn % 10 == 5):
                        for iPlayer in range(iNumPlayers):
                                if (gc.getPlayer(iPlayer).isAlive() and iGameTurn >= (gc.getPlayer(iPlayer).getBirthTurn()+utils.getBirthTurnModifier(iPlayer) + 25) and not gc.getPlayer(iPlayer).isGoldenAge()): #RFCRAND
                                        if (self.getStability(iPlayer) < -40): #civil war
                                                print ("COLLAPSE: CIVIL WAR", gc.getPlayer(iPlayer).getCivilizationAdjective(0))
                                                if (iPlayer != utils.getHumanID()):
                                                        if (gc.getPlayer(utils.getHumanID()).canContact(iPlayer)):
                                                                CyInterface().addMessage(utils.getHumanID(), False, con.iDuration, gc.getPlayer(iPlayer).getCivilizationDescription(0) + " " + \
                                                                                                    CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
                                                        if (iGameTurn < con.i1400AD):
                                                                utils.pickFragmentation(iPlayer, iIndependent, iIndependent2, iBarbarian, False)
                                                        else:
                                                                utils.pickFragmentation(iPlayer, iIndependent, iIndependent2, -1, False)
                                                else:
                                                        if (gc.getPlayer(iPlayer).getNumCities() > 1):
                                                                CyInterface().addMessage(iPlayer, True, con.iDuration, CyTranslator().getText("TXT_KEY_STABILITY_CIVILWAR_HUMAN", ()), "", 0, "", ColorTypes(con.iRed), -1, -1, True, True)
                                                                utils.pickFragmentation(iPlayer, iIndependent, iIndependent2, -1, True)
                                                                utils.setStartingStabilityParameters(iPlayer)
                                                                self.setGNPold(iPlayer, 0)
                                                                self.setGNPnew(iPlayer, 0)
                                                                
                                                return






