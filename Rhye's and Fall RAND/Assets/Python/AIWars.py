# Rhye's and Fall of Civilization - AI Wars

from CvPythonExtensions import *
import CvUtil
import PyHelpers        # LOQ
import Popup
import cPickle as pickle
import Consts as con
import RFCUtils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer	# LOQ
utils = RFCUtils.RFCUtils()

### Constants ###


iStartTurn = con.i600BC
iMinIntervalEarly = 15
iMaxIntervalEarly = 30
iMinIntervalLate = 40
iMaxIntervalLate = 60
iThreshold = 100
iMinValue = 30
iNumPlayers = con.iNumMajorPlayers
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iNumTotalPlayers = con.iNumTotalPlayers






      
  
class AIWars:

        def getAttackingCivsArray( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lAttackingCivsArray'][iCiv]

        def setAttackingCivsArray( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lAttackingCivsArray'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )                
                
        def getNextTurnAIWar( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iNextTurnAIWar']

        def setNextTurnAIWar( self, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iNextTurnAIWar'] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def setup(self):
                #RFCRAND
                self.setNextTurnAIWar(iStartTurn + gc.getGame().getSorenRandNum(iMaxIntervalEarly-iMinIntervalEarly, 'random turn'))



        def checkTurn(self, iGameTurn):

                #turn automatically peace on between independent cities and all the major civs
                if (iGameTurn % 20 == 7):
                        utils.restorePeaceHuman(con.iIndependent2, False)
                if (iGameTurn % 20 == 14):
                        utils.restorePeaceHuman(con.iIndependent, False)
                if (iGameTurn % 60 == 55 and iGameTurn > 50):
                        utils.restorePeaceAI(con.iIndependent, False)
                if (iGameTurn % 60 == 30 and iGameTurn > 50):
                        utils.restorePeaceAI(con.iIndependent2, False)
                #turn automatically war on between independent cities and some AI major civs
                if (iGameTurn % 13 == 6 and iGameTurn > 50): #1 turn after restorePeace()
                        utils.minorWars(con.iIndependent)
                if (iGameTurn % 13 == 11 and iGameTurn > 50): #1 turn after restorePeace()
                        utils.minorWars(con.iIndependent2)
#RFCRAND - missing Celtia here?

                if (iGameTurn == con.i1500AD or iGameTurn == con.i1850AD):
                        for iLoopCiv in range( iNumPlayers ):
                                self.setAttackingCivsArray(iLoopCiv, max(0,self.getAttackingCivsArray(iLoopCiv) - con.tAggressionLevel[iLoopCiv])) 

                     
                if (iGameTurn == self.getNextTurnAIWar()):
                    
                        if (iGameTurn > con.i1600AD): #longer periods due to globalization of contacts
                                iMinInterval = iMinIntervalLate
                                iMaxInterval = iMaxIntervalLate
                        else:
                                iMinInterval = iMinIntervalEarly
                                iMaxInterval = iMaxIntervalEarly

                        #skip if in a world war already
                        if (iGameTurn > con.i1500AD):
                                numCivsAtWar = 0
                                gc.getGame().countCivPlayersAlive()
                                for iLoopCiv in range( iNumPlayers ):
                                        tLoopCiv = gc.getTeam(gc.getPlayer(iLoopCiv).getTeam())
                                        if (tLoopCiv.getAtWarCount(True) != 0):
                                                numCivsAtWar += 1
                                if (numCivsAtWar*100/gc.getGame().countCivPlayersAlive() > 50): #more than half at war with someone
                                        print("Skipping AIWar (WW)")
                                        self.setNextTurnAIWar(iGameTurn + iMinInterval + gc.getGame().getSorenRandNum(iMaxInterval-iMinInterval, 'random turn'))
                                        return                                                             
                            
                        iCiv, iTargetCiv = self.pickCivs()
                        if (iTargetCiv >= 0 and iTargetCiv <= iNumTotalPlayers):
                                self.initWar(iCiv, iTargetCiv, iGameTurn, iMaxInterval, iMinInterval)
                                return
                        else:
                                print ("AIWars iTargetCiv missing", iCiv)
                                iCiv, iTargetCiv = self.pickCivs()
                                if (iTargetCiv >= 0 and iTargetCiv <= iNumTotalPlayers):
                                        self.initWar(iCiv, iTargetCiv, iGameTurn, iMaxInterval, iMinInterval)
                                        return
                                else:
                                        print ("AIWars iTargetCiv missing again", iCiv)

                        #make sure we don't miss this
                        print("Skipping AIWar")
                        self.setNextTurnAIWar(iGameTurn + iMinInterval + gc.getGame().getSorenRandNum(iMaxInterval-iMinInterval, 'random turn'))


        def pickCivs(self): 
                iCiv = -1
                iTargetCiv = -1
                iCiv = self.chooseAttackingPlayer()
                if (iCiv >= 0 and iCiv <= iNumPlayers):
                        iTargetCiv = self.checkGrid(iCiv)
                        return (iCiv, iTargetCiv)
                else:
                        print ("AIWars iCiv missing", iCiv)
                        return (-1, -1)

        def initWar(self, iCiv, iTargetCiv, iGameTurn, iMaxInterval, iMinInterval): 
                gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(iTargetCiv, True, -1) ##False?
                self.setNextTurnAIWar(iGameTurn + iMinInterval + gc.getGame().getSorenRandNum(iMaxInterval-iMinInterval, 'random turn'))
                print("Setting AIWar", iCiv, "attacking", iTargetCiv)

##        def initArray(self):
##                for k in range( iNumPlayers ):
##                        grid = []                
##                        for j in range( 68 ):
##                                line = []
##                                for i in range( 124 ):        
##                                        line.append( gc.getPlayer(iCiv).getSettlersMaps( CyMap().getGridHeight()-1-j, i ) )
##                                grid.append( line )
##                        self.lSettlersMap.append( grid )
##                print self.lSettlersMap




        def chooseAttackingPlayer(self): 
                #finding max teams ever alive (countCivTeamsEverAlive() doesn't work as late human starting civ gets killed every turn)
                iMaxCivs = iNumPlayers
                for i in range( iNumPlayers ):
                        j = iNumPlayers -1 - i
                        if (gc.getPlayer(j).isAlive()):
                                iMaxCivs = j
                                break 
                #print ("iMaxCivs", iMaxCivs)
                
                if (gc.getGame().countCivPlayersAlive() <= 2):
                        return -1
                else:
                        iRndnum = gc.getGame().getSorenRandNum(iMaxCivs, 'attacking civ index') 
                        #print ("iRndnum", iRndnum)
                        iAlreadyAttacked = -100
                        iMin = 100
                        iCiv = -1
                        for i in range( iRndnum, iRndnum + iMaxCivs ):
                                iLoopCiv = i % iMaxCivs
                                if (gc.getPlayer(iLoopCiv).isAlive() and not gc.getPlayer(iLoopCiv).isHuman()):
                                        if (utils.getPlagueCountdown(iLoopCiv) >= -10 and utils.getPlagueCountdown(iLoopCiv) <= 0): #civ is not under plague or quit recently from it
                                                iAlreadyAttacked = self.getAttackingCivsArray(iLoopCiv)
                                                if (utils.isAVassal(iLoopCiv)):
                                                        iAlreadyAttacked += 1 #less likely to attack
                                                if (iLoopCiv == con.iPortugal or iLoopCiv == con.iNetherlands):
                                                        iAlreadyAttacked += 1 #less likely to attack, would cripple them
                                                #check if a world war is already in place
                                                iNumAlreadyWar = 0
                                                tLoopCiv = gc.getTeam(gc.getPlayer(iLoopCiv).getTeam())
                                                for kLoopCiv in range( iNumPlayers ):
                                                        if (tLoopCiv.isAtWar(kLoopCiv)):
                                                                iNumAlreadyWar += 1
                                                if (iNumAlreadyWar >= 5):
                                                        iAlreadyAttacked += 2 #much less likely to attack
                                                elif (iNumAlreadyWar >= 3):
                                                        iAlreadyAttacked += 1 #less likely to attack
                                                            
                                                if (iAlreadyAttacked < iMin):
                                                        iMin = iAlreadyAttacked
                                                        iCiv = iLoopCiv
                        #print ("attacking civ", iCiv)
                        if (iAlreadyAttacked != -100):
                                self.setAttackingCivsArray(iCiv, iAlreadyAttacked + 1)                        
                                return iCiv
                        else:
                                return -1
                return -1
                    
             

        def checkGrid(self, iCiv):
                pCiv = gc.getPlayer(iCiv)
                tCiv = gc.getTeam(pCiv.getTeam())
                lTargetCivs = []
                #lTargetCivs = con.l0ArrayTotal

                #clean it, sometimes it takes old values in memory
                for k in range( iNumTotalPlayers ):
                        lTargetCivs.append(0)
                        #lTargetCivs[k] = 0

                ##set alive civs to 1 to differentiate them from dead civs
                for k in range( iNumPlayers ):
                        if (gc.getPlayer(k).isAlive() and tCiv.isHasMet(k)): #canContact here?
                                if (lTargetCivs[k] == 0):
                                        lTargetCivs[k] = 1
                for k in range( iNumTotalPlayers ):
                        if (k >= iNumPlayers):
                                if (gc.getPlayer(k).isAlive() and tCiv.isHasMet(k)):
                                        lTargetCivs[k] = 1

                ##set master or vassal to 0
                for k in range( iNumPlayers ):                                
                        if (gc.getTeam(gc.getPlayer(k).getTeam()).isVassal(iCiv) or tCiv.isVassal(k)):
                                 lTargetCivs[k] = 0

                #if already at war
                for k in range( iNumTotalPlayers ): 
                        if (tCiv.isAtWar(k)):
                                lTargetCivs[k] = 0

                lTargetCivs[iCiv] = 0
                                
                for j in range( CyMap().getGridHeight() ): 
                        for i in range( CyMap().getGridWidth() ):                                      
                                iOwner = gc.getMap().plot( i, j ).getOwner()
                                if (iOwner >= 0 and iOwner < iNumTotalPlayers and iOwner != iCiv):
                                        if (lTargetCivs[iOwner] > 0):
                                                #RFCRAND
                                                for iLoopX in (i-1, i+2):
                                                        for iLoopY in (j-1, j+2):
                                                                if (gc.getMap().plot( i, j ).getOwner() == iCiv):
                                                                        lTargetCivs[iOwner] += (20+10*(con.tAggressionLevel))/2
                                                                        break
                                                                        break
                                                
                #there are other routines for this
                lTargetCivs[iIndependent] /= 3
                lTargetCivs[iIndependent2] /= 3

                #can they attack civs with lost contact?
                for k in range( iNumPlayers ): 
                        if (not pCiv.canContact(k)):
                                lTargetCivs[k] /= 8

                #print(lTargetCivs)
                
                #normalization
                iMaxTempValue = -1
                for k in range( iNumTotalPlayers ):
                        if (lTargetCivs[k] > iMaxTempValue):
                                iMaxTempValue = lTargetCivs[k]
                #print(iMaxTempValue)
                if (iMaxTempValue > 0):
                        for k in range( iNumTotalPlayers ):
                                if (lTargetCivs[k] > 0):
                                        #lTargetCivs[k] *= 500 #non va!
                                        #lTargetCivs[k] / iMaxTempValue
                                        lTargetCivs[k] = lTargetCivs[k]*500/iMaxTempValue
                                        
                #print(lTargetCivs)
                
                for iLoopCiv in range( iNumTotalPlayers ):

                        if (lTargetCivs[iLoopCiv] <= 0):
                                continue
                            
                        #add a random value
                        if (lTargetCivs[iLoopCiv] <= iThreshold):
                                lTargetCivs[iLoopCiv] += gc.getGame().getSorenRandNum(100, 'random modifier')
                        if (lTargetCivs[iLoopCiv] > iThreshold):
                                lTargetCivs[iLoopCiv] += gc.getGame().getSorenRandNum(300, 'random modifier')
                        #balanced with attitude
                        attitude = 2*(pCiv.AI_getAttitude(iLoopCiv) - 2)
                        if (attitude > 0):
                                lTargetCivs[iLoopCiv] /= attitude
                        #exploit plague
                        if (utils.getPlagueCountdown(iLoopCiv) > 0 or utils.getPlagueCountdown(iLoopCiv) < -10 and not (gc.getGame().getGameTurn() <= gc.getPlayer(iLoopCiv).getBirthTurn() + 20)): #RFCRAND
                                lTargetCivs[iLoopCiv] *= 3
                                lTargetCivs[iLoopCiv] /= 2

                        #balanced with master's attitude
                        for j in range( iNumTotalPlayers ):
                                if (tCiv.isVassal(j)):
                                        attitude = 2*(gc.getPlayer(j).AI_getAttitude(iLoopCiv) - 2)
                                        if (attitude > 0):
                                                lTargetCivs[iLoopCiv] /= attitude

                        #if already at war 
                        if (not tCiv.isAtWar(iLoopCiv)):
                                #consider peace counter
                                iCounter = min(7,max(1,tCiv.AI_getAtPeaceCounter(iLoopCiv)))
                                if (iCounter <= 7):
                                        lTargetCivs[iLoopCiv] *= 20 + 10*iCounter
                                        lTargetCivs[iLoopCiv] /= 100
                                        
                        #if under pact
                        if (tCiv.isDefensivePact(iLoopCiv)):
                                lTargetCivs[iLoopCiv] /= 4
                        #if friend of a friend
##                        for jLoopCiv in range( iNumTotalPlayers ):
##                                if (tCiv.isDefensivePact(jLoopCiv) and gc.getTeam(gc.getPlayer(iLoopCiv).getTeam()).isDefensivePact(jLoopCiv)):
##                                        lTargetCivs[iLoopCiv] /= 2
                                
                        #no suicide
                        if (iCiv == con.iNetherlands):
                                if (iLoopCiv == con.iFrance or iLoopCiv == con.iGermany):
                                        lTargetCivs[iLoopCiv] *= 1
                                        lTargetCivs[iLoopCiv] /= 2
                        if (iCiv == con.iPortugal):
                                if (iLoopCiv == con.iSpain):
                                        lTargetCivs[iLoopCiv] *= 1
                                        lTargetCivs[iLoopCiv] /= 2
                                
                                
                #print(lTargetCivs)
                
                #find max
                iMaxValue = 0
                iTargetCiv = -1
                for iLoopCiv in range( iNumTotalPlayers ):
                        if (lTargetCivs[iLoopCiv] > iMaxValue):
                                iMaxValue = lTargetCivs[iLoopCiv]
                                iTargetCiv = iLoopCiv

                #print ("maxvalue", iMaxValue)
                #print("target civ", iTargetCiv)

                if (iMaxValue >= iMinValue):
                        return iTargetCiv
                return -1

                                        
	    
        def forgetMemory(self, iTech, iPlayer):
                if (iTech == con.iCommunism or iTech == con.iMassMedia):
                        for iLoopCiv in range( iNumPlayers ):
                                pPlayer = gc.getPlayer(iPlayer)
                                if (pPlayer.AI_getMemoryCount(iLoopCiv,0) > 0):
                                        pPlayer.AI_changeMemoryCount(iLoopCiv,0,-1)
                                if (pPlayer.AI_getMemoryCount(iLoopCiv,1) > 0):
                                        pPlayer.AI_changeMemoryCount(iLoopCiv,1,-1)


