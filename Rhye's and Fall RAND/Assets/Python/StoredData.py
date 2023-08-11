# Rhye's and Fall of Civilization - Stored Data

from CvPythonExtensions import *
import CvUtil
import PyHelpers  
import cPickle as pickle

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer	


class StoredData:

        def setupScriptData( self ):
                """Initialise the global script data dictionary for usage."""
                scriptDict = {      #------------RiseAndFall
                                    'iNewCiv': -1,
                                    'iNewCivFlip': -1,
                                    'iOldCivFlip': -1,
                                    'tTempTopLeft': -1,
                                    'tTempBottomRight': -1,
                                    'iSpawnWar': 0, #if 1, add units and declare war. If >=2, do nothing
                                    'bAlreadySwitched': 0,
                                    'lColonistsAlreadyGiven': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #active players
                                    'lAstronomyTurn': [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500], #active players
                                    'lNumCities': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players to contain Byzantium too
                                    'lLastTurnAlive': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players to contain Byzantium too
                                    'lSpawnDelay': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #active players
                                    'lFlipsDelay': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'iBetrayalTurns': 0,
                                    'lLatestRebellionTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'iRebelCiv': 0,
                                    'lExileData': [-1, -1, -1, -1, -1],
                                    'tTempFlippingCity': -1,
                                    'lCheatersCheck': [0, -1],
                                    'lBirthTurnModifier': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lDeleteMode': [-1, -1, -1], #first is a bool, the other values are capital coordinates
                                    'lFirstContactConquerors': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #RFCRAND
                                    'bCheatMode': False,
                                    #------------Religions
                                    'iSeed': -1,
                                    #------------UP
                                    'iImmigrationTurnLength': 0,
                                    'iImmigrationCurrentTurn': 0,
                                    'iLatestFlipTurn': 0,
                                    'lLatestRazeData': [-1, -1, -1, -1, -1],
                                    #------------AIWars
                                    'lAttackingCivsArray': [0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0],
                                    'iNextTurnAIWar': -1,
                                    #------------Congresses
                                    'bCongressEnabled': False,
                                    'iCivsWithNationalism': 0,
                                    'bUNbuilt': False,
                                    'lInvitedNations': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                                    'lVotes': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lTempActiveCiv': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                    'lTempReqCity': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                    'iLoopIndex': 0,
                                    'lTempReqCityHuman': [-1, -1, -1, -1, -1],
                                    'tempReqCityNI': -1,
                                    'tempActiveCivNI': -1,
                                    'lTempAttackingCivsNI': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                                    'iNumNationsTemp': 0,
                                    'lBribe' : [-1, -1, -1],
                                    'lCivsToBribe': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                    'tTempFlippingCityCongress': -1,
                                    'lMemory': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players + barbarians (minors and barbs are not used, but necessary for not going out of range)
                                    #------------Plague
                                    'lPlagueCountdown': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players + barbarians
                                    'lGenericPlagueDates': [-1, -1, -1, -1],# -1],
                                    'lFirstContactPlague': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], #total players + barbarians
                                     #------------Victories
                                    'lGoals': [[-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1],
                                               [-1, -1, -1]],
                                    'lReligionFounded': [-1, -1, -1, -1, -1, -1, -1],
                                    'iEnslavedUnits': 0,
                                    'iRazedByMongols': 0,
                                    'lEnglishEras': [-1, -1],
                                    'lGreekTechs': [-1, -1, -1],
                                    'lNewWorld': [-1, -1], #first founded; circumnavigated (still unused)
                                    'iNumSinks': 0,
                                    'lBabylonianTechs': [-1, -1, -1],                                    
                                    #'iMediterraneanColonies': 0,
                                    'iEnglishColonies': 0, #RFCRAND
                                    'iRussianColonies': 0, #RFCRAND
                                    'iPortugueseColonies': 0,
                                    'iFrenchColonies': 0, #RFCRAND
                                    'lWondersBuilt': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'l2OutOf3': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                                    #------------Stability
                                    'lBaseStabilityLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lPartialBaseStability': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lStability': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lOwnedPlotsLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lOwnedCitiesLastTurn': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lCombatResultTempModifier': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lGNPold': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lGNPnew': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lGreatDepressionCountdown': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lStatePropertyCountdown': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lDemocracyCountdown': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    'lStabilityParameters': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2+3+2+3+3
                                    'lLastRecordedStabilityStuff': [0, 0, 0, 0, 0, 0], # total + 5 parameters
                                    #RFCRAND
                                    'lWorldShapeInfo': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #rolls, atlanticLine, innerSea, forceContinents on very low
                                    'lWrap': [-1, -1],
                                    'lEurasiaInfo': [0, 0, 0, 0, 0, 0, 0, 0], #x(W), x(E), y(S), y(N), ID
                                    'lAfricaInfo': [0, 0, 0, 0, 0, 0, 0, 0], #x(W), x(E), y(S), y(N), ID
                                    'lAmericaInfo': [0, 0, 0, 0, 0, 0, 0, 0, 0], #x(W), x(E), y(S), y(N), IDn, IDs
                                    'lIsland1Info': [0, 0, 0, 0, 0, 0, 0, 0], #x(W), x(E), y(S), y(N), ID
                                    'lIsland2Info': [0, 0, 0, 0, 0, 0, 0, 0], #x(W), x(E), y(S), y(N), ID
                                    'lBordersCoordinates': [[-1, -1, -1, -1], #x(W), x(E), y(S), y(N) #3x2 world
                                                            [-1, -1, -1, -1],
                                                            [-1, -1, -1, -1],
                                                            [-1, -1, -1, -1],
                                                            [-1, -1, -1, -1],
                                                            [-1, -1, -1, -1],
                                                            [-1, -1, -1, -1]],
                                    'lRandomContinents': [1, 1, 1, 1, 1, 1],
                                    'lEmptyContinentInfo': [0, 0, 0, 0, 0, 0, 0], #x(W), x(E), y(S), y(N)
                                    'lInThisGame': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True], #total players + barbarians
                                    'lJerusalemLocation': [-1, -1],
                                    'lFlipsReceived': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #total players + barbarians
                                    'lEarlyRandomLeaders': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #for very low
                                    'iLongSeed': -1,
                                    #RFCRAND City Lists Pointers
                                    'lCityListsPointers':  [[0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0],
                                                           [0, 0, 0, 0]],
				}
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
