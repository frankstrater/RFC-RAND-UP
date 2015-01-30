
from CvPythonExtensions import *
import CvUtil
import PyHelpers  
import Consts as con
import CvMapGeneratorUtil
import RFCUtils
utils = RFCUtils.RFCUtils()
import Pots

import StoredData
import cPickle as pickle

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

     

class RandomRFC:

#--------------------------------------------------------------------------

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

        def getEmptyContinentInfo( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lEmptyContinentInfo'][iParameter]

        def setEmptyContinentInfo( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lEmptyContinentInfo'][iParameter] = iNewValue
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
                
#--------------------------------------------------------------------------
       	
        def setup(self):
                #return

                Map = gc.getMap()
                iGridX = CyMap().getGridWidth()
                iGridY = CyMap().getGridHeight()

                #self.cleanDesertMarks(Map, iGridX, iGridY)                
                print("Processing oceans...")
                self.searchAtlantis(Map, iGridX, iGridY)
                print("Processing ice...")
                self.meltIce(Map, iGridX, iGridY)
                self.secureAutoPlay(Map, iGridX, iGridY)
                print("Processing seas...")
                self.checkContinentsDistance(Map, iGridX, iGridY)
                self.addIce(Map, iGridX, iGridY) #must be after continents distance
                self.smoothShapes(Map, iGridX, iGridY)
                self.correctRivers(Map, iGridX, iGridY)
                print("Processing deserts...")
                self.markSmallDeserts(Map, iGridX, iGridY)
                self.markSemiDeserts(Map, iGridX, iGridY)
                self.formNewDeserts(Map, iGridX, iGridY)
                self.processFloodPlains(Map, iGridX, iGridY)
                print("Processing mountains...")
                self.createMountainChains(Map, iGridX, iGridY)  
                self.createHillChains(Map, iGridX, iGridY)
                self.openBlockedPlots(Map, iGridX, iGridY)
                print("Processing marshes...")
                self.improveColdRegions(Map, iGridX, iGridY)
                self.createMarshes(Map, iGridX, iGridY)
                self.improveWarmRegions(Map, iGridX, iGridY) #must be after marshes
                print("Processing jungles...")
                self.replaceJungles(Map, iGridX, iGridY)
                self.openJunglePassage(Map, iGridX, iGridY)
                print("Processing resources...")
                self.processEarthResources(Map, iGridX, iGridY)
                self.processSingleResources(Map, iGridX, iGridY)
                #self.processResourcesClusters(Map, iGridX, iGridY) #not needed anymore
                self.printMapInfo(Map, iGridX, iGridY)                
                self.markMapInfo(Map, iGridX, iGridY)                                
                print("Rebuilding landscape...")
                gc.getMap().rebuildLandscape()  #must be before areaID recording but after markMapInfo
                print("Registering areas ID...")
                self.recordAreaIDs(Map, iGridX, iGridY)
                print("Processing civs...")
                Pots.Pots().setup()
                gc.getGame().setupBirthTurnModifiers()
                print("Assigning starting plots...")
                self.reassignStartingPlots(Map, iGridX, iGridY)
                self.cleanContacts()



        def searchAtlantis(self, Map, iGridX, iGridY):
                if (Map.getSeaLevel() <= 3):
                        return
                #print("debug percent", Map.getLandPlots()*100/(Map.getGridWidth()*Map.getGridHeight()))
                if (Map.getLandPlots()*100/(Map.getGridWidth()*Map.getGridHeight()) > 36):
                        print("above 36%")
                        return
                iSize = 11
                if (int(CyMap().getWorldSize()) == 1):
                        iSize = 12
                if (int(CyMap().getWorldSize()) == 2):
                        iSize = 15
                for x in range(6,iGridX-6-iSize):
                        for y in range(4,iGridY-4-iSize):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getTerrainType() == con.iOcean):
                                        #check a box
                                        bLand = False
                                        iSeaIceCounter = 0
                                        for iBoxX in range (x, x+iSize):
                                                for jBoxY in range (y, y+iSize):
                                                        pLoopBox = Map.plot( iBoxX, jBoxY )
                                                        if (pLoopBox.getFeatureType() == 0):
                                                                iSeaIceCounter += 1
                                                        if (pLoopBox.getTerrainType() != con.iOcean or pLoopBox.getFeatureType() > 0 or pLoopBox.getBonusType(-1) != -1):
                                                                bLand = True                                                                
                                                                #print("searching", x, y, bLand, iBoxX, jBoxY, pLoopBox.getTerrainType(), pLoopBox.getFeatureType(), pLoopBox.getBonusType(-1))
                                                                break
                                                                break
                                        if (iSeaIceCounter > 8):   #partially covered
                                                bLand = True   
                                        if (bLand == False):
                                                if (Map.getLandPlots()*100/(Map.getGridWidth()*Map.getGridHeight()) > 36):
                                                        print("now above 36%")
                                                        return
                                                print ("Atlantis", x, y)
                                                self.addAtlantis(Map, iGridX, iGridY, x, y, iSize)

        def addAtlantis(self, Map, iGridX, iGridY, startX, startY, iSize):
                bCopyTileFound = False
                while (bCopyTileFound == False):
                        rndX = gc.getGame().getSorenRandNum(iGridX-20, 'X') + 10
                        rndY = gc.getGame().getSorenRandNum(iGridY-20, 'X') + 10
                        pCopy = Map.plot( rndX, rndY )
                        if (not pCopy.isWater()):
                                if (pCopy.area().getNumTiles() > 100):
                                        if (not Map.plot( rndX+1, rndY ).isWater() and not Map.plot( rndX, rndY+1 ).isWater() and not Map.plot( rndX+1, rndY+1 ).isWater()):
                                                bCopyTileFound = True
                                                print("bCopyTileFound", rndX, rndY)

                #fat cross shape
                iCorderSize = 4
                if (int(CyMap().getWorldSize()) == 1):
                        iCorderSize = 4
                if (int(CyMap().getWorldSize()) == 2):
                        iCorderSize = 5
                
                for x in range(startX+1+iCorderSize,startX+iSize-1-iCorderSize):
                        for y in range(startY+1,startY+1+iCorderSize):
                                self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)
                for x in range(startX+1,startX+iSize-1):
                        for y in range(startY+1+iCorderSize,startY+iSize-1-iCorderSize):
                                self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)
                for x in range(startX+1+iCorderSize,startX+iSize-1-iCorderSize):
                        for y in range(startY+iSize-1-iCorderSize,startY+iSize-1):
                                self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)

                #central area
                for x in range(startX+1+iCorderSize/2,startX+iSize-1-iCorderSize/2):
                        for y in range(startY+1+iCorderSize/2,startY+iSize-1-iCorderSize/2):
                                self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)
                                
                #25% for each corner: 1 to 3
                iNumCorners = 0
                if (gc.getGame().getSorenRandNum(4, '') == 0):
                        iNumCorners += 1
                        for x in range(startX+1,startX+1+iCorderSize):
                                for y in range(startY+1,startY+1+iCorderSize):
                                        self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)
                if (gc.getGame().getSorenRandNum(4, '') == 0):
                        iNumCorners += 1
                        for x in range(startX+iSize-1-iCorderSize,startX+iSize-1):
                                for y in range(startY+1,startY+1+iCorderSize):
                                        self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)
                if (gc.getGame().getSorenRandNum(4, '') == 0):
                        iNumCorners += 1
                        for x in range(startX+1,startX+1+iCorderSize):
                                for y in range(startY+iSize-1-iCorderSize,startY+iSize-1):
                                        self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)
                if ((gc.getGame().getSorenRandNum(4, '') == 0 or iNumCorners == 0) and iNumCorners != 3):
                        for x in range(startX+iSize-1-iCorderSize,startX+iSize-1):
                                for y in range(startY+iSize-1-iCorderSize,startY+iSize-1):
                                        self.copyAndPaste(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)                        
                              
                for x in range(startX+1,startX+iSize-1):
                        for y in range(startY+1,startY+iSize-1):
                                self.copyAndPasteRivers(Map, rndX+x-(startX+1), rndY+y-(startY+1), x, y)                                
                                                        
        def copyAndPaste(self, Map, x1, y1, x2, y2):
                p1 = Map.plot( x1, y1 )
                p2 = Map.plot( x2, y2 )
                if (p1.isPeak()):
                        if (gc.getGame().getSorenRandNum(2, '') == 0):
                                p2.setPlotType(PlotTypes.PLOT_HILLS, True, True)
                        else:
                                p2.setPlotType(p1.getPlotType(), True, True)
                else:
                        p2.setPlotType(p1.getPlotType(), True, True)
                p2.setTerrainType(p1.getTerrainType(), True, True)
                if (p1.getFeatureType() != con.iSeaIce):
                        p2.setFeatureType(p1.getFeatureType(), 0)
                        p2.setBonusType(p1.getBonusType(-1))
                
                if (p2.getLatitude() < 45):
                        if (p2.getTerrainType() == con.iSnow):
                                p2.setTerrainType(con.iDesert, True, True)
                                p2.setBonusType(-1)
                        if (p2.getTerrainType() == con.iTundra):
                                p2.setTerrainType(con.iPlains, True, True)
                                #p2.setBonusType(-1)
                elif (p2.getLatitude() < 63):
                        if (p2.getTerrainType() == con.iSnow):
                                p2.setTerrainType(con.iTundra, True, True)
                                p2.setBonusType(-1)
                        if (p2.getTerrainType() == con.iTundra):
                                p2.setTerrainType(con.iPlains, True, True)
                                #p2.setBonusType(-1)
                        if (p2.getTerrainType() == con.iDesert):
                                p2.setTerrainType(con.iTundra, True, True)
                                p2.setFeatureType(-1, 0)
                elif (p2.getLatitude() < 72):
                        if (p2.getTerrainType() == con.iDesert):
                                p2.setTerrainType(con.iTundra, True, True)
                                p2.setFeatureType(-1, 0)
                        if (p2.getFeatureType() == con.iJungle):
                                p2.setFeatureType(-1, 0)
                                p2.setBonusType(-1)
                else:
                        if (p2.getTerrainType() == con.iDesert):
                                p2.setTerrainType(con.iTundra, True, True)
                                p2.setFeatureType(-1, 0)
                                p2.setBonusType(-1)
                        if (p2.getTerrainType() == con.iGrass):
                                p2.setTerrainType(con.iTundra, True, True)
                                p2.setFeatureType(-1, 0)
                                p2.setBonusType(-1)
                        if (p2.getTerrainType() == con.iPlains):
                                p2.setTerrainType(con.iTundra, True, True)
                                p2.setFeatureType(-1, 0)
                                p2.setBonusType(-1)
                        if (p2.getFeatureType() == con.iJungle):
                                p2.setFeatureType(-1, 0)
                                p2.setBonusType(-1)
                            

        def copyAndPasteRivers(self, Map, x1, y1, x2, y2):
                p1 = Map.plot( x1, y1 )
                p2 = Map.plot( x2, y2 )
                if (p2.isWater()):
                        return
                if (p1.isNOfRiver() and not Map.plot( x1, y1-1 ).isWater() and not Map.plot( x2, y2-1 ).isWater()):
                        if (p2.area().getNumTiles() >= 5):
                                p2.setNOfRiver(True, p1.getRiverWEDirection())                                
                if (p1.isWOfRiver() and not Map.plot( x1+1, y1 ).isWater() and not Map.plot( x2+1, y2 ).isWater()):
                        if (p2.area().getNumTiles() >= 5):
                                p2.setWOfRiver(True, p1.getRiverNSDirection())
                #if (utils.isSofRiver(x1, x2):
                        
        

        
                
        def meltIce(self, Map, iGridX, iGridY):
                if (Map.getClimate() == con.iCold):
                        return

                iThreshold = 5
                if (Map.getClimate() == con.iTropical):
                        iThreshold = 3
                elif (Map.getClimate() == con.iArid):
                        iThreshold = 4
                if (self.getWrap(1) == False):
                        for x in range(iGridX):
                                for y in range(iThreshold, iGridY-iThreshold):
                                        pCurrent = Map.plot( x, y ) 
                                        if (pCurrent.getFeatureType() == con.iSeaIce):
                                                pCurrent.setFeatureType(-1, 0)

                ##open polar passage

                if (Map.getSeaLevel() == 1 or Map.getSeaLevel() == 2):                        
                        iWestX = self.getEurasiaInfo(0)
                        iEastX = self.getEurasiaInfo(1)
                        iRoll1 = self.getWorldShapeInfo(0)
                        iTop = iGridY-1
                        iBottom = iGridY-iThreshold-1
                        if (iRoll1 == 1):
                                iBottom = 0
                                iTop = iThreshold+1

                        self.openPassage(Map, iGridX, iGridY, iWestX, iWestX+3*(iEastX-iWestX)/10, iBottom, iTop, False, False, -1, -1)
                        self.openPassage(Map, iGridX, iGridY, iWestX+7*(iEastX-iWestX)/10, iEastX, iBottom, iTop, False, False, -1, -1)

                        iTop = iGridY-1
                        iBottom = iGridY-iThreshold-2
                        if (iRoll1 == 1):
                                iBottom = 0
                                iTop = iThreshold+2

                        self.openPassage(Map, iGridX, iGridY, iWestX, iWestX+(iEastX-iWestX)/5, iBottom, iTop, False, False, -1, -1)
                        self.openPassage(Map, iGridX, iGridY, iWestX+4*(iEastX-iWestX)/5, iEastX, iBottom, iTop, False, False, -1, -1)

                                
                        iTop = iGridY-1
                        iBottom = iGridY-iThreshold-2
                        if (iRoll1 == 1):
                                iBottom = 0
                                iTop = iThreshold+2

                        self.openPassage(Map, iGridX, iGridY, iWestX, iWestX+(iEastX-iWestX)/10, iBottom, iTop, False, False, -1, -1)
                        self.openPassage(Map, iGridX, iGridY, iWestX+9*(iEastX-iWestX)/10, iEastX, iBottom, iTop, False, False, -1, -1)
                elif (Map.getSeaLevel() == 3 and self.getWrap(1) == False):
                        NSRoll = gc.getGame().getSorenRandNum(2, '')
                        print("Polar passage =", NSRoll)
                        iTop = iGridY-2
                        iBottom = iTop-3
                        if (NSRoll == 1):
                                iBottom = 1
                                iTop = iBottom+3
                        self.openPassage(Map, iGridX, iGridY, 0, iGridX, iBottom, iTop, False, False, -1, -1)
                        
                        iTop = iBottom
                        if (NSRoll == 1):
                                iBottom = iTop
                        for iX in range(iGridX-1):
                                shapeRoll = gc.getGame().getSorenRandNum(3, '')
                                iBottom = iTop-shapeRoll
                                if (NSRoll == 1):
                                        iTop = iBottom+shapeRoll
                                if (shapeRoll > 0):
                                        self.openPassage(Map, iGridX, iGridY, iX, iX+1, iBottom, iTop, False, False, -1, -1)
                        
        def addIce(self, Map, iGridX, iGridY):
                if (self.getWrap(0) == False): #create vertical layers
                        iThickness = 1
                        if (Map.getClimate() == con.iCold):
                                iThickness = 3
                        if (Map.getClimate() == con.iTropical):
                                iThickness = 0
                        elif (Map.getClimate() == con.iArid):
                                iThickness = 1
                        if (iGridY > 60): #high
                                iThickness += 1
                        for x in range(iThickness+3+1):
                                for y in range(iGridY):
                                        pCurrent = Map.plot( x, y )
                                        if (x < iThickness): #100%
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iThickness): #75%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 1):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iThickness+1): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iThickness+2): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                        for x in range(iGridX-iThickness-3,iGridX):
                                for y in range(iGridY):
                                        pCurrent = Map.plot( x, y )
                                        if (x >= iGridX-iThickness): #100%
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX-iThickness-1): #75%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 1):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX-iThickness-2): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX-iThickness-3): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                                        
                if (self.getWrap(0) == False and self.getWrap(1) == False): #create angles
                        iThickness = iGridY*3/4
                        if (Map.getClimate() == con.iCold):
                                iThickness += 4
                        if (Map.getClimate() == con.iTropical):
                                iThickness -= 2
                        for x in range(0,iThickness+1):
                                for y in range(0,iThickness+1):
                                        pCurrent = Map.plot( x, y )
                                        iX = x-0
                                        iY = y-0
                                        if (iX*iY < iThickness): #100%
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+3): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+6): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                        for x in range(iGridX-iThickness-1, iGridX):
                                for y in range(0,iThickness+1):
                                        pCurrent = Map.plot( x, y )
                                        iX = iGridX-x-1
                                        iY = y-0
                                        if (iX*iY < iThickness): #100%
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+3): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+6): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                        for x in range(0,iThickness+1):
                                for y in range(iGridY-iThickness-1, iGridY):
                                        pCurrent = Map.plot( x, y )
                                        iX = x-0
                                        iY = iGridY-y-1
                                        if (iX*iY < iThickness): #100%
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+3): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+6): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                        for x in range(iGridX-iThickness-1, iGridX):
                                for y in range(iGridY-iThickness-1, iGridY):
                                        pCurrent = Map.plot( x, y )
                                        iX = iGridX-x-1
                                        iY = iGridY-y-1
                                        if (iX*iY < iThickness): #100%
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+3): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (iX*iY < iThickness+6): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)

                if (self.getWrap(0) == True and self.getWrap(1) == True): #create central ice
                        iThickness = 1
                        if (Map.getClimate() == con.iCold):
                                iThickness = 3
                        if (Map.getClimate() == con.iTropical):
                                iThickness = 0
                        elif (Map.getClimate() == con.iArid):
                                iThickness = 1
                        iThickness += 4
                        if (iGridY > 60): #high
                                iThickness += 1
                        for x in range(iGridX/2-iThickness-3,iGridX/2+iThickness+3+1):
                                for y in range(iGridY/2-iThickness-3,iGridY/2+iThickness+3+1):
                                        pCurrent = Map.plot( x, y )
                                        if (x < iGridX/2+iThickness and x >= iGridX/2-iThickness and y < iGridY/2+iThickness and y >= iGridY/2-iThickness): #100%
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX/2+iThickness): #75%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 1):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX/2+iThickness+1): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX/2+iThickness+2): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX/2-iThickness-1): #75%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 1):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX/2-iThickness-2): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (x == iGridX/2-iThickness-3): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (y == iGridY/2+iThickness): #75%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 1):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (y == iGridY/2+iThickness+1): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (y == iGridY/2+iThickness+2): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (y == iGridY/2-iThickness-1): #75%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 1):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (y == iGridY/2-iThickness-2): #50%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 2):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        elif (y == iGridY/2-iThickness-3): #25%
                                                if (gc.getGame().getSorenRandNum(4, '') >= 3):
                                                        pCurrent.setFeatureType(con.iSeaIce, 0)
                                        if (pCurrent.getFeatureType() == con.iSeaIce):
                                                if (not pCurrent.isWater()):
                                                        pCurrent.setTerrainType(con.iSnow, True, True)
                                        


        def secureAutoPlay(self, Map, iGridX, iGridY):
                if (gc.getActivePlayer().getBirthTurn > 0 and (self.getWrap(0) == False or self.getWrap(1) == False)): #non-starters
                        #3 radius box for avoiding contact with other civs (and possibly culture
                        for x in range (0,3+1):
                                for y in range (0, 3+1):
                                        Map.plot(x, y).setFeatureType(con.iSeaIce, 0)
                        for x in range (iGridX-3,iGridX):
                                for y in range (0, 3+1):
                                        Map.plot(x, y).setFeatureType(con.iSeaIce, 0)
                        for x in range (0,3+1):
                                for y in range (iGridY-3, iGridY):
                                        Map.plot(x, y).setFeatureType(con.iSeaIce, 0)
                        for x in range (iGridX-3,iGridX):
                                for y in range (iGridY-3, iGridY):
                                        Map.plot(x, y).setFeatureType(con.iSeaIce, 0)               



                                        
                 
        def openPassage(self, Map, iGridX, iGridY, iWestX, iEastX, iBottom, iTop, bCoastToOcean, bCheckArea, iCentreX, iCentreY):       
                for iLoopX in range (iWestX, iEastX+1):
                        for iLoopY in range (iBottom, iTop+1):
                                pCurrent = Map.plot( iLoopX%iGridX, iLoopY%iGridY )
                                #debug
                                #pCurrent.setFeatureType(con.iFallout, 0)
                                #if(iCentreX == 2 and iCentreY == 47):# and bCheckArea == True):
                                #        pCurrent.setFeatureType(con.iSeaIce, 0)
                                #        print("areas", bCheckArea, Map.plot( iCentreX, iCentreY ).area().getID(), pCurrent.area().getID())
                                if (not pCurrent.isWater()):
                                        if (bCheckArea == False or Map.plot( iCentreX, iCentreY ).area().getID() != pCurrent.area().getID()):
                                                pCurrent.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
                                                pCurrent.setTerrainType(con.iCoast, True, True)
                                                pCurrent.setFeatureType(-1, 0)
                                                pCurrent.setBonusType(-1)
                                                if (pCurrent.isGoody):
                                                        pCurrent.removeGoody()
                                                #debug
                                                #if(iCentreX == 2 and iCentreY == 47):# and bCheckArea == True):
                                                #        pCurrent.setFeatureType(con.iSeaIce, 0)
                                                #pCurrent.setFeatureType(con.iFallout, 0)
                                
                                if (bCoastToOcean):
                                        if (pCurrent.isWater()):
                                                if (not pCurrent.isAdjacentToLand()):
                                                        pCurrent.setTerrainType(con.iOcean, True, True)
                                                        pCurrent.setBonusType(-1)


        def checkHorizontalDistance(self, Map, iGridX, iGridY, iWestX, iEastX, iBottom, iTop):
                #print("checkHorizontalDistance", iWestX, iEastX)
                iOriginalWestX = iWestX
                iOriginalEastX = iEastX
                for iLoopY in range (iBottom, iTop+1):
                        iVariation = (iLoopY / 5) % 4
                        if ((iLoopY / 20) % 2 == 1):
                                iVariation = 3 - iVariation
                        iWestX = iOriginalWestX + iVariation -1
                        iEastX = iOriginalEastX + iVariation -1
                        #left to right
                        for i in range(iEastX-iWestX):
                                pCurrentW = Map.plot( (iWestX+i)%iGridX, iLoopY%iGridY )
                                #print((iWestX+i)%iGridX, iLoopY%iGridY)
                                if (not pCurrentW.isWater()):
                                        iThickerTriangle = 0
                                        if (i == iEastX-iWestX-1):
                                                iThickerTriangle = 1
                                        #if the next two are water (to make sure it's not a lake, check above and below); or if it's the last one in the range
                                        if ((Map.plot( (iWestX+i+1)%iGridX, iLoopY).isWater() and \
                                             Map.plot( (iWestX+i+2)%iGridX, iLoopY).isWater() and \
                                            (Map.plot( (iWestX+i+1)%iGridX, (iLoopY-1)%iGridY).isWater() or Map.plot( (iWestX+i+1)%iGridX, (iLoopY+1)%iGridY).isWater())) or \
                                            (i == iEastX-iWestX-1)):
##                                                if ((iWestX+i)%iGridX == 73 and iLoopY%iGridY == 57):
##                                                    print("2-47")
##                                                if ((iWestX+i)%iGridX == 73 and iLoopY%iGridY == 58):
##                                                    print("3-46")
                                                #triangle
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+5, iWestX+i+6, iLoopY-5, iLoopY+5, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+4, iWestX+i+6, iLoopY-iThickerTriangle-3, iLoopY+iThickerTriangle+3, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+3, iWestX+i+6, iLoopY-iThickerTriangle-2, iLoopY+iThickerTriangle+2, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+2, iWestX+i+6, iLoopY-iThickerTriangle-1, iLoopY+iThickerTriangle+1, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+1, iWestX+i+6, iLoopY-iThickerTriangle, iLoopY+iThickerTriangle, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                #half-sphere
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+1, iWestX+i+3, iLoopY-5, iLoopY+5, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+1, iWestX+i+4, iLoopY-4, iLoopY+4, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+1, iWestX+i+5, iLoopY-3, iLoopY+3, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iWestX+i+1, iWestX+i+6, iLoopY-1, iLoopY+1, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
                                                break
##                        #right to left
##                        for i in range(iEastX-iWestX):
##                                pCurrentW = Map.plot( (iEastX-i)%iGridX, iLoopY%iGridY )
##                                #print((iWestX+i)%iGridX, iLoopY%iGridY)
##                                if (not pCurrentW.isWater()):
##                                        iThickerTriangle = 0
##                                        if (i == iEastX-iWestX-1):
##                                                iThickerTriangle = 1
##                                        #if the next two are water (to make sure it's not a lake, check above and below); or if it's the last one in the range
##                                        if ((Map.plot( (iEastX-i-1)%iGridX, iLoopY).isWater() and \
##                                             Map.plot( (iEastX-i-2)%iGridX, iLoopY).isWater() and \
##                                            (Map.plot( (iEastX-i-1)%iGridX, (iLoopY-1)%iGridY).isWater() or Map.plot( (iEastX-i-1)%iGridX, (iLoopY+1)%iGridY).isWater())) or \
##                                            (i == iEastX-iWestX-1)):
##                                                #triangle
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-6, iEastX-i-5, iLoopY-5, iLoopY+5, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-6, iEastX-i-4, iLoopY-iThickerTriangle-3, iLoopY+iThickerTriangle+3, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-6, iEastX-i-3, iLoopY-iThickerTriangle-2, iLoopY+iThickerTriangle+2, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-6, iEastX-i-2, iLoopY-iThickerTriangle-1, iLoopY+iThickerTriangle+1, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-6, iEastX-i-1, iLoopY-iThickerTriangle, iLoopY+iThickerTriangle, True, False, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                #half-sphere
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-3, iEastX-i-1, iLoopY-5, iLoopY+5, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-4, iEastX-i-1, iLoopY-4, iLoopY+4, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-5, iEastX-i-1, iLoopY-3, iLoopY+3, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                self.openPassage(Map, iGridX, iGridY, iEastX-i-6, iEastX-i-1, iLoopY-1, iLoopY+1, True, True, (iWestX+i)%iGridX, iLoopY%iGridY)
##                                                break


        def checkVerticalDistance(self, Map, iGridX, iGridY, iWestX, iEastX, iBottom, iTop):
                #print("checkVerticalDistance", iBottom, iTop)
                iOriginalTop = iTop
                iOriginalBottom = iBottom
                for iLoopX in range (iWestX, iEastX+1):
                        iVariation = (iLoopX / 5) % 4
                        if ((iLoopX / 20) % 2 == 1):
                                iVariation = 3 - iVariation
                        iTop = iOriginalTop + iVariation -1
                        iBottom = iOriginalBottom + iVariation -1
                        #down to up
                        for i in range(iTop-iBottom):
                                pCurrentS = Map.plot( iLoopX%iGridX, (iBottom+i)%iGridY )
                                if (not pCurrentS.isWater()):
                                        iThickerTriangle = 0
                                        if (i == iTop-iBottom-1):
                                                iThickerTriangle = 1
                                        #if the next two are water (to make sure it's not a lake, check left and right); or if it's the last one in the range
                                        if ((Map.plot( iLoopX, (iBottom+i+1)%iGridY).isWater() and \
                                             Map.plot( iLoopX, (iBottom+i+2)%iGridY).isWater() and \
                                            (Map.plot( (iLoopX-1)%iGridX, (iBottom+i+1)%iGridY).isWater() or Map.plot( (iLoopX+1)%iGridX, (iBottom+i+1)%iGridY).isWater())) or \
                                            (i == iTop-iBottom-1)):
                                                #triangle
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-5, iLoopX+5, iBottom+i+5, iBottom+i+6, True, False, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-iThickerTriangle-3, iLoopX+iThickerTriangle+3, iBottom+i+4, iBottom+i+6, True, False, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-iThickerTriangle-2, iLoopX+iThickerTriangle+2, iBottom+i+3, iBottom+i+6, True, False, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-iThickerTriangle-1, iLoopX+iThickerTriangle+1, iBottom+i+2, iBottom+i+6, True, False, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-iThickerTriangle, iLoopX+iThickerTriangle, iBottom+i+6, iBottom+i+1, True, False, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                #half-sphere
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-5, iLoopX+5, iBottom+i+1, iBottom+i+3, True, True, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-4, iLoopX+4, iBottom+i+1, iBottom+i+4, True, True, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-3, iLoopX+3, iBottom+i+1, iBottom+i+5, True, True, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                self.openPassage(Map, iGridX, iGridY, iLoopX-1, iLoopX+1, iBottom+i+1, iBottom+i+6, True, True, iLoopX%iGridX, (iBottom+i)%iGridY)
                                                break
                                            

        def checkContinentsDistance(self, Map, iGridX, iGridY):
            

                
                if (Map.getSeaLevel() == 1 or Map.getSeaLevel() == 2): #high or medium likelyhood

                        roll2 = self.getWorldShapeInfo(1)
                        push = 3
                        pacificX = iGridX*0
                        if (roll2 == 0):
                                pacificX = 0 + push
                        else:
                                pacificX = 0 - push
                        self.checkHorizontalDistance(Map, iGridX, iGridY, int(pacificX)-4, int(pacificX)+3, 0, iGridY)
                        
                        atlanticLine = self.getWorldShapeInfo(9)
                        atlanticX = iGridX*atlanticLine
                        push = 3
                        if (roll2 == 0):
                                atlanticX = atlanticX - push
                        else:
                                atlanticX = atlanticX + push
                        self.checkHorizontalDistance(Map, iGridX, iGridY, int(atlanticX)-4, int(atlanticX)+3, 0, iGridY)
                        
                elif (Map.getSeaLevel() >= 3): #low

                        if (self.getWorldShapeInfo(10) == 1): #inner sea
                                return

                        if (Map.getSeaLevel() == 4 and self.getWorldShapeInfo(11) == 0): #very low
                                if (gc.getGame().getSorenRandNum(5, "odds") == 0): #20% of panagea or close continents
                                        return
                            
                        push = 3
                        pacificX = iGridX*0 - push

                        self.checkHorizontalDistance(Map, iGridX, iGridY, int(pacificX)-4, int(pacificX)+3, 0, iGridY)

                        if (Map.getSeaLevel() == 4 and self.getWorldShapeInfo(11) == 0): #very low
                                if (gc.getGame().getSorenRandNum(5, "odds") == 0): #another 20% of panagea or close continents
                                        return

                        iSkipAttempts = 0
                        
                        for iBorder in range(7):
                                iWestX = self.getBordersCoordinates(iBorder, 0)
                                if (iWestX != -1):

                                        #may skip the third world
                                        
                                        continentLinks = [[0, 2],
                                                          [1, 3],
                                                          [2, 4],
                                                          [3, 5],
                                                          [0, 1],
                                                          [2, 3],
                                                          [4, 5]]
                                        #   1   3
                                        # 4   5   6
                                        #   0   2

                                        if (Map.getSeaLevel() == 4 and self.getWorldShapeInfo(11) == 0): #very low
                                                if (gc.getGame().getSorenRandNum(10, "odds") == 0): #10% of stopping for each remaining
                                                        continue

                                        if (self.getRandomContinents(continentLinks[iBorder][0]) == 0 and self.getRandomContinents(continentLinks[iBorder][1]) == 0): #both old world
                                                iSkipAttempts += 1
                                                skipRoll = gc.getGame().getSorenRandNum(3-iSkipAttempts, 'skip')
                                                if (skipRoll == 0 ):
                                                        print("skippingContinentsDistance", continentLinks[iBorder], "attempt", iSkipAttempts)
                                                        continue                                                    
                                    
                                        iEastX = self.getBordersCoordinates(iBorder, 1)
                                        iBottomY = self.getBordersCoordinates(iBorder, 2)
                                        
                                        iTopY = self.getBordersCoordinates(iBorder, 3)
                                        if (iWestX == iEastX):
                                                push = 3
                                                iWestX = iWestX - push
                                                print("iWestX", iWestX)
                                                self.checkHorizontalDistance(Map, iGridX, iGridY, iWestX-4, iWestX+3, iBottomY, iTopY)
                                        elif (iBottomY == iTopY):
                                                push = 3
                                                iBottomY = iBottomY - push
                                                print("iBottomY",iBottomY)
                                                self.checkVerticalDistance(Map, iGridX, iGridY, iWestX, iEastX, iBottomY-4, iBottomY+3)
                                        print(iWestX, iEastX, iBottomY, iTopY, "iBorder", iBorder)
                                        



                                

        def smoothShapes(self, Map, iGridX, iGridY):
                for iX in range(iGridX):
                        for iY in range(iGridY):
                                pCurrent = Map.plot( iX, iY )
                                if (not pCurrent.isWater() and pCurrent.isCoastalLand()): 
                                        #first horizontally
                                        bStraightLand = True
                                        for iLoopX in range(iX-2, iX+3):
                                                pLoop = Map.plot( iLoopX%iGridX, iY%iGridY )
                                                if (pLoop.isWater()):
                                                        bStraightLand = False
                                        if (bStraightLand):
                                                #first down
                                                bStraightUpperCoast = True
                                                for iLoopX in range(iX-2, iX+3):
                                                        pLoop = Map.plot( iLoopX%iGridX, (iY+1)%iGridY )
                                                        if (not pLoop.isWater()):
                                                                bStraightUpperCoast = False
                                                #then up
                                                if (not bStraightUpperCoast):
                                                        bStraightLowerCoast = True
                                                        for iLoopX in range(iX-2, iX+3):
                                                                pLoop = Map.plot( iLoopX%iGridX, (iY-1)%iGridY )
                                                                if (not pLoop.isWater()):
                                                                        bStraightLowerCoast = False
                                                                        
                                                if (bStraightUpperCoast or bStraightLowerCoast):
                                                        plotList = []
                                                        floodRoll = gc.getGame().getSorenRandNum(5, 'inner flood')
                                                        if (floodRoll >= 1):
                                                                plotList.append(pCurrent)
                                                                if (floodRoll == 2):
                                                                        if (bStraightUpperCoast):
                                                                                pCurrent = Map.plot( iX, (iY-1)%iGridY )
                                                                        elif (bStraightLowerCoast):
                                                                                pCurrent = Map.plot( iX, (iY+1)%iGridY )
                                                                if (floodRoll == 3):
                                                                        pCurrent = Map.plot( (iX+1)%iGridX, iY )
                                                                if (floodRoll == 4):
                                                                        pCurrent = Map.plot( (iX-1)%iGridX, iY )
                                                                plotList.append(pCurrent)
                                                        
                                                        for pPlot in plotList:
                                                                if (pPlot.getBonusType(-1) == -1):
                                                                        #print("pPlot:", pPlot.getX(), pPlot.getY())
                                                                        if (not pPlot.isNOfRiver() and not pPlot.isWOfRiver() and not utils.isEofRiver(pPlot.getX(), pPlot.getY()) and not utils.isSofRiver(pPlot.getX(), pPlot.getY())):
                                                                                pPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
                                                                                pPlot.setTerrainType(con.iCoast, True, True)
                                                                                pPlot.setFeatureType(-1, 0)
                                                                                if (pPlot.isGoody):
                                                                                        pPlot.removeGoody()
                                                                        
                                        #then vertically
                                        bStraightLand = True
                                        for iLoopY in range(iY-2, iY+3):
                                                pLoop = Map.plot( iX%iGridX, iLoopY%iGridY )
                                                if (pLoop.isWater()):
                                                        bStraightLand = False
                                        if (bStraightLand):
                                                #first check at left
                                                bStraightLeftCoast = True
                                                for iLoopY in range(iY-2, iY+3):
                                                        pLoop = Map.plot( (iX-1)%iGridX, iLoopY%iGridY )
                                                        if (not pLoop.isWater()):
                                                                bStraightLeftCoast = False
                                                #then at right
                                                if (not bStraightLeftCoast):
                                                        bStraightRightCoast = True
                                                        for iLoopY in range(iY-2, iY+3):
                                                                pLoop = Map.plot( (iX+1)%iGridX, iLoopY%iGridY )
                                                                if (not pLoop.isWater()):
                                                                        bStraightRightCoast = False

                                                                        
                                                if (bStraightLeftCoast or bStraightRightCoast):
                                                        plotList = []
                                                        floodRoll = gc.getGame().getSorenRandNum(5, 'inner flood')
                                                        if (floodRoll >= 1):
                                                                plotList.append(pCurrent)
                                                                if (floodRoll == 2):
                                                                        if (bStraightLeftCoast):
                                                                                pCurrent = Map.plot( (iX+1)%iGridX, iY )
                                                                        elif (bStraightRightCoast):
                                                                                pCurrent = Map.plot( (iX-1)%iGridX, iY )
                                                                if (floodRoll == 3):
                                                                        pCurrent = Map.plot( iX, (iY+1)%iGridY )
                                                                if (floodRoll == 4):
                                                                        pCurrent = Map.plot( iX, (iY-1)%iGridY )
                                                                plotList.append(pCurrent)
                                                        
                                                        for pPlot in plotList:
                                                                if (pPlot.getBonusType(-1) == -1):
                                                                        #print("pPlot:", pPlot.getX(), pPlot.getY())
                                                                        if (not pPlot.isNOfRiver() and not pPlot.isWOfRiver() and not utils.isEofRiver(pPlot.getX(), pPlot.getY()) and not utils.isSofRiver(pPlot.getX(), pPlot.getY())):
                                                                                pPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
                                                                                pPlot.setTerrainType(con.iCoast, True, True)
                                                                                pPlot.setFeatureType(-1, 0)
                                                                                if (pPlot.isGoody):
                                                                                        pPlot.removeGoody()


                                                                                          

        def correctRivers(self, Map, iGridX, iGridY):
                for iX in range(iGridX):
                        for iY in range(iGridY):
                                pCurrent = Map.plot( iX, iY )
                                if (pCurrent.isNOfRiver() and Map.plot( iX, (iY-1)%iGridY ).isWater()):
                                        pCurrent.setNOfRiver(False, CardinalDirectionTypes.NO_CARDINALDIRECTION)
                                if (pCurrent.isWOfRiver() and Map.plot( (iX+1)%iGridX, iY ).isWater()):
                                        pCurrent.setWOfRiver(False, CardinalDirectionTypes.NO_CARDINALDIRECTION)


                                

                
        def cleanDesertMarks(self, Map, iGridX, iGridY): #debug
                for x in range(iGridX):
                        for y in range(iGridY):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getFeatureType() == con.iSeaIce or pCurrent.getFeatureType() == con.iFallout):
                                        pCurrent.setFeatureType(-1, 0)


                                        
        def markSmallDeserts(self, Map, iGridX, iGridY):
                for x in range(2, iGridX-2):
                        for y in range(2, iGridY-2):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getTerrainType() == con.iDesert):
                                        iNumSurroundingDeserts = 0
                                        for loopX in range (x-2, x+3):
                                                for loopY in range (y-2, y+3):
                                                        if (Map.plot( loopX, loopY ).getTerrainType() == con.iDesert):
                                                                iNumSurroundingDeserts += 1
                                        if (iNumSurroundingDeserts <= 4): #5? 
                                                pCurrent.setFeatureType(con.iSeaIce, 0)
                                                

        def markSemiDeserts(self, Map, iGridX, iGridY):
                for x in range(2, iGridX-2):
                        for y in range(2, iGridY-2):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getTerrainType() == con.iPlains or pCurrent.getTerrainType() == con.iGrass):
                                        iNumSurroundingDeserts = 0
                                        for loopX in range (x-1, x+2):
                                                for loopY in range (y-1, y+2):
                                                        if (Map.plot( loopX, loopY ).getTerrainType() == con.iDesert and not Map.plot( loopX, loopY ).getFeatureType() == con.iSeaIce):
                                                                iNumSurroundingDeserts += 1
                                        if (iNumSurroundingDeserts >= 3):
                                                pCurrent.setFeatureType(con.iFallout, 0)
                                        elif (iNumSurroundingDeserts >= 2):
                                                if (Map.getClimate() != con.iCold):# and Map.getClimate() != con.iTropical):
                                                        if (not pCurrent.getFeatureType() == con.iJungle): #and pCurrent.getBonusType(-1) == -1?
                                                                if (y <= iGridY*65/100 and y >= iGridY*35/100):
                                                                        pCurrent.setFeatureType(con.iFallout, 0)

        def formNewDeserts(self, Map, iGridX, iGridY):
                for x in range(1, iGridX-1):
                        for y in range(1, iGridY-1):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getTerrainType() == con.iDesert and pCurrent.getFeatureType() == con.iSeaIce):
                                            pCurrent.setTerrainType(con.iPlains, True, True)
                                            pCurrent.setFeatureType(-1, 0)
                                                
                                if ((pCurrent.getTerrainType() == con.iPlains or pCurrent.getTerrainType() == con.iGrass) and pCurrent.getFeatureType() == con.iFallout):
                                            pCurrent.setTerrainType(con.iDesert, True, True)
                                            pCurrent.setFeatureType(-1, 0)
                                            if (pCurrent.getBonusType(-1) == con.iCow or \
                                                pCurrent.getBonusType(-1) == con.iRice or \
                                                pCurrent.getBonusType(-1) == con.iWheat or \
                                                pCurrent.getBonusType(-1) == con.iPig or \
                                                pCurrent.getBonusType(-1) == con.iSilk or \
                                                pCurrent.getBonusType(-1) == con.iSpices):
                                                    pCurrent.setBonusType(-1)


        def processFloodPlains(self, Map, iGridX, iGridY):
                for x in range(1, iGridX-1):
                        for y in range(1, iGridY-1):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getTerrainType() == con.iDesert and pCurrent.getFeatureType() == con.iFloodPlains):
                                        if (gc.getGame().getSorenRandNum(2, 'roll') == 0):
                                                if (x < iGridX/2 or y < iGridY/2): #to create some diversity, not just N and W
                                                        if (not pCurrent.isNOfRiver() and not pCurrent.isWOfRiver()):
                                                                pCurrent.setFeatureType(-1, 0)
                                                elif (x > iGridX/2 or y < iGridY/2):
                                                        if (not pCurrent.isNOfRiver() and pCurrent.isWOfRiver()):
                                                                pCurrent.setFeatureType(-1, 0)
                                                elif (x > iGridX/2 or y > iGridY/2):
                                                        if (pCurrent.isNOfRiver() and pCurrent.isWOfRiver()):
                                                                pCurrent.setFeatureType(-1, 0)
                                                elif (x < iGridX/2 or y > iGridY/2):
                                                        if (pCurrent.isNOfRiver() and not pCurrent.isWOfRiver()):
                                                                pCurrent.setFeatureType(-1, 0)
                                if (pCurrent.getTerrainType() == con.iDesert and (pCurrent.isNOfRiver() or pCurrent.isWOfRiver() or utils.isEofRiver(pCurrent.getX(), pCurrent.getY()) or utils.isSofRiver(pCurrent.getX(), pCurrent.getY()))):
                                        if (pCurrent.getBonusType(-1) == con.iCow or pCurrent.getBonusType(-1) == con.iSheep or pCurrent.getBonusType(-1) == con.iPig or pCurrent.getBonusType(-1) == con.iWheat or pCurrent.getBonusType(-1) == con.iRice or pCurrent.getBonusType(-1) == con.iSugar):
                                                pCurrent.setBonusType(-1)

 

        def createMountainChains(self, Map, iGridX, iGridY):
                for x in range(1, iGridX-1):
                        for y in range(1, iGridY-1):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.isHills() and pCurrent.getBonusType(-1) == -1 and not pCurrent.isGoody()):
                                        iNumSurroundingReliefs = 0
                                        for loopX in range (x-1, x+2):
                                                for loopY in range (y-1, y+2):
                                                        if (Map.plot( loopX, loopY ).isPeak() or Map.plot( loopX, loopY ).isHills()):
                                                                iNumSurroundingReliefs += 1
                                        if (iNumSurroundingReliefs >= 2):
                                                pCurrent.setPlotType(PlotTypes.PLOT_PEAK, True, True)
                                                pCurrent.setFeatureType(-1, 0)
                                                #pCurrent.setTerrainType(con.iTerrainPeak, True, True)




        def createHillChains(self, Map, iGridX, iGridY):
                for x in range(1, iGridX-1):
                        for y in range(1, iGridY-1):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.isFlatlands()):
                                        iNumSurroundingPeaks = 0
                                        for loopX in range (x-1, x+2):
                                                for loopY in range (y-1, y+2):
                                                        if (Map.plot( loopX, loopY ).isPeak()):
                                                                iNumSurroundingPeaks += 1
                                        if (iNumSurroundingPeaks >= 4 and pCurrent.getBonusType(-1) == -1 and not pCurrent.isGoody()):
                                                pCurrent.setPlotType(PlotTypes.PLOT_PEAK, True, True)
                                                pCurrent.setFeatureType(-1, 0)
                                        elif (iNumSurroundingPeaks >= 2):
                                                pCurrent.setPlotType(PlotTypes.PLOT_HILLS, True, True)
                                                #pCurrent.setTerrainType(con.iTerrainHills, True, True)
                                                if (pCurrent.getFeatureType() == con.iFloodPlains):
                                                        pCurrent.setFeatureType(-1, 0)
                                        

        def openBlockedPlots(self, Map, iGridX, iGridY):
                for x in range(1, iGridX-2):
                        for y in range(1, iGridY-2):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.isPeak()):
                                        pRight = Map.plot( x+1, y )
                                        if (not pRight.isPeak()):
                                                iNumSurroundingPeaks = 0
                                                for loopX in range ((x+1)-1, (x+1)+2):
                                                        for loopY in range (y-1, y+2):
                                                                if (Map.plot( loopX, loopY ).isPeak()):
                                                                        iNumSurroundingPeaks += 1
                                                if (iNumSurroundingPeaks == 8):
                                                        pCurrent.setPlotType(PlotTypes.PLOT_HILLS, True, True)
                                                        #print("opening", x, y)



        def improveColdRegions(self, Map, iGridX, iGridY): 
                if (Map.getSeaLevel() <= 1): #high and very high
                        #gulf drift
                        minLonPercent = 0.36
                        maxLonPercent = 0.64
                        minLatPercent = 0.73
                        maxLatPercent = 0.96
                        if (Map.getClimate() == con.iCold):
                                minLatPercent = minLatPercent - 0.08
                                maxLatPercent = maxLatPercent - 0.08
                        if (Map.getClimate() == con.iTropical):
                                minLatPercent = minLatPercent + 0.02
                                maxLatPercent = maxLatPercent + 0.02
                        minPlotX = int(iGridX * minLonPercent)
                        maxPlotX = int(iGridX * maxLonPercent)
                        minPlotY = int(iGridY * minLatPercent)
                        maxPlotY = int(iGridY * maxLatPercent)
                        for x in range(minPlotX, maxPlotX+1):
                                for y in range(minPlotY, maxPlotY+1):
                                        pCurrent = Map.plot( x, y )
                                        if (pCurrent.getTerrainType() == con.iTundra):
                                                pCurrent.setTerrainType(con.iGrass, True, True)
                                        if (pCurrent.getTerrainType() == con.iSnow):
                                                pCurrent.setTerrainType(con.iTundra, True, True)
                                                if (pCurrent.isNOfRiver() or pCurrent.isWOfRiver() or utils.isEofRiver(pCurrent.getX(), pCurrent.getY()) or utils.isSofRiver(pCurrent.getX(), pCurrent.getY())):
                                                        pCurrent.setTerrainType(con.iGrass, True, True)
                                        if (pCurrent.getFeatureType() == con.iSeaIce):
                                                pCurrent.setFeatureType(-1, 0)
                        if (Map.getClimate() != con.iCold):
                                for x in range(minPlotX-2, maxPlotX+1+2):
                                        for y in range(iGridY-4, iGridY-2):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getFeatureType() == con.iSeaIce):
                                                        pCurrent.setFeatureType(-1, 0)
                                for x in range(minPlotX+5, maxPlotX+1-5):
                                        for y in range(iGridY-4, iGridY-1):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getFeatureType() == con.iSeaIce):
                                                        pCurrent.setFeatureType(-1, 0)
                        


                        iShift = 5
                        if (int(CyMap().getWorldSize()) == 1): #standard
                                iShift -= 1
                        if (Map.getClimate() == con.iTropical):
                                iShift = 3
                        if (Map.getClimate() == con.iArid):
                                iShift = 3
                        if (int(CyMap().getWorldSize()) == 0): #small
                                iShift -= 1                        
                        #north-west
                        minLonPercent = 0.01
                        maxLonPercent = 0.21
                        minLatPercent = 0.75
                        maxLatPercent = 0.90
                        if (Map.getClimate() == con.iTropical):
                                minLatPercent = minLatPercent + 0.02
                                maxLatPercent = maxLatPercent + 0.02
                        minPlotX = int(iGridX * minLonPercent)
                        maxPlotX = int(iGridX * maxLonPercent)
                        minPlotY = int(iGridY * minLatPercent)
                        maxPlotY = int(iGridY * maxLatPercent)
                        
                        for x in range(minPlotX, maxPlotX+1):
                                for y in range(minPlotY, maxPlotY+1):
                                        pCurrent = Map.plot( x, y )
                                        p5above = Map.plot( x, y+iShift )
                                        if (not pCurrent.isWater() and not p5above.isWater()):
                                                if (p5above.getTerrainType() == con.iTundra):
                                                        pCurrent.setTerrainType(con.iTundra, True, True)
                                                if (p5above.getTerrainType() == con.iSnow):
                                                        pCurrent.setTerrainType(con.iSnow, True, True)
                                                        pCurrent.setFeatureType(-1, 0)
                                                if (p5above.getBonusType(-1) != -1 or p5above.getTerrainType() == con.iSnow):
                                                        if (not pCurrent.isPeak()):
                                                                pCurrent.setBonusType(p5above.getBonusType(-1)) #deletes old bonus
                                                        p5above.setBonusType(-1)
                        #Siberia
                        minLonPercent = 0.75
                        maxLonPercent = 0.91
                        minLatPercent = 0.75
                        maxLatPercent = 0.90
                        if (Map.getClimate() == con.iTropical):
                                minLatPercent = minLatPercent + 0.02
                                maxLatPercent = maxLatPercent + 0.02
                        minPlotX = int(iGridX * minLonPercent)
                        maxPlotX = int(iGridX * maxLonPercent)
                        minPlotY = int(iGridY * minLatPercent)
                        maxPlotY = int(iGridY * maxLatPercent)
                        for x in range(minPlotX, maxPlotX+1):
                                for y in range(minPlotY, maxPlotY+1):
                                        pCurrent = Map.plot( x, y )
                                        p5above = Map.plot( x, y+iShift )
                                        if (not pCurrent.isWater() and not p5above.isWater()):
                                                if (p5above.getTerrainType() == con.iTundra):
                                                        pCurrent.setTerrainType(con.iTundra, True, True)
                                                if (p5above.getTerrainType() == con.iSnow):
                                                        pCurrent.setTerrainType(con.iSnow, True, True)
                                                        pCurrent.setFeatureType(-1, 0)
                                                if (p5above.getBonusType(-1) != -1 or p5above.getTerrainType() == con.iSnow):
                                                        if (not pCurrent.isPeak()):
                                                                pCurrent.setBonusType(p5above.getBonusType(-1)) #deletes old bonus
                                                        p5above.setBonusType(-1)
                                                
        def improveWarmRegions(self, Map, iGridX, iGridY):
                if (Map.getSeaLevel() <= 1): #high and very high
                        #SE Asia
                        minLonPercent = 0.79
                        maxLonPercent = 0.91
                        minLatPercent = 0.36
                        maxLatPercent = 0.47
                        if (Map.getClimate() == con.iTropical):
                                minLatPercent = minLatPercent + 0.02
                                maxLatPercent = maxLatPercent + 0.02
                        minPlotX = int(iGridX * minLonPercent)
                        maxPlotX = int(iGridX * maxLonPercent)
                        minPlotY = int(iGridY * minLatPercent)
                        maxPlotY = int(iGridY * maxLatPercent)
                        for x in range(minPlotX, maxPlotX+1):
                                for y in range(minPlotY, maxPlotY+1):
                                        pCurrent = Map.plot( x, y )
                                        if (not pCurrent.isPeak()):
                                                if (pCurrent.getTerrainType() == con.iGrass and pCurrent.getBonusType(-1) == -1):
                                                        if (gc.getGame().getSorenRandNum(2, 'roll') == 0):    
                                                                pCurrent.setFeatureType(con.iJungle, 0)   
                                                if ((pCurrent.getTerrainType() == con.iPlains or pCurrent.getTerrainType() == con.iDesert) and pCurrent.getBonusType(-1) == -1):
                                                        if (gc.getGame().getSorenRandNum(3, 'roll') == 0):    
                                                                pCurrent.setFeatureType(con.iJungle, 0)
                                                                pCurrent.setTerrainType(con.iGrass, True, True)
                        #Mexico (same as SE Asia)
                        minLonPercent = 0.10
                        maxLonPercent = 0.18
                        minLatPercent = 0.49
                        maxLatPercent = 0.56
                        if (Map.getClimate() == con.iTropical):
                                minLatPercent = minLatPercent + 0.02
                                maxLatPercent = maxLatPercent + 0.02
                        minPlotX = int(iGridX * minLonPercent)
                        maxPlotX = int(iGridX * maxLonPercent)
                        minPlotY = int(iGridY * minLatPercent)
                        maxPlotY = int(iGridY * maxLatPercent)
                        for x in range(minPlotX, maxPlotX+1):
                                for y in range(minPlotY, maxPlotY+1):
                                        pCurrent = Map.plot( x, y )
                                        if (not pCurrent.isPeak()):
                                                if (pCurrent.getTerrainType() == con.iGrass and pCurrent.getBonusType(-1) == -1):
                                                        if (gc.getGame().getSorenRandNum(2, 'roll') == 0):       
                                                                pCurrent.setFeatureType(con.iJungle, 0)   
                                                if ((pCurrent.getTerrainType() == con.iPlains or pCurrent.getTerrainType() == con.iDesert) and pCurrent.getBonusType(-1) == -1):
                                                        if (gc.getGame().getSorenRandNum(3, 'roll') == 0):       
                                                                pCurrent.setFeatureType(con.iJungle, 0)
                                                                pCurrent.setTerrainType(con.iGrass, True, True)                                                    
                        #Sahara
                        minLonPercent = 0.40
                        maxLonPercent = 0.71
                        minLatPercent = 0.39
                        maxLatPercent = 0.49
                        minPlotX = int(iGridX * minLonPercent)
                        maxPlotX = int(iGridX * maxLonPercent)
                        minPlotY = int(iGridY * minLatPercent)
                        maxPlotY = int(iGridY * maxLatPercent)
                        for x in range(minPlotX, maxPlotX+1):
                                for y in range(minPlotY, maxPlotY+1):
                                        pCurrent = Map.plot( x, y )
                                        if (pCurrent.getTerrainType() == con.iPlains and pCurrent.getBonusType(-1) == -1):
                                                if (gc.getGame().getSorenRandNum(2, 'roll') == 0):   #50%  
                                                        pCurrent.setFeatureType(-1, 0)
                                                        pCurrent.setTerrainType(con.iDesert, True, True)
                                        if (pCurrent.getTerrainType() == con.iGrass and pCurrent.getBonusType(-1) == -1):
                                                if (gc.getGame().getSorenRandNum(3, 'roll') >= 1):  #66% 
                                                        pCurrent.setFeatureType(-1, 0)
                                                        pCurrent.setTerrainType(con.iDesert, True, True)

                        #China
                        minLonPercent = 0.85
                        maxLonPercent = 0.97
                        minLatPercent = 0.50
                        maxLatPercent = 0.63
                        minPlotX = int(iGridX * minLonPercent)
                        maxPlotX = int(iGridX * maxLonPercent)
                        minPlotY = int(iGridY * minLatPercent)
                        maxPlotY = int(iGridY * maxLatPercent)
                        for x in range(minPlotX, maxPlotX+1):
                                for y in range(minPlotY, maxPlotY+1):
                                        pCurrent = Map.plot( x, y )
                                        if (pCurrent.getTerrainType() == con.iDesert):
                                                if (gc.getGame().getSorenRandNum(3, 'roll') >= 1):   
                                                        pCurrent.setTerrainType(con.iPlains, True, True)
                                                else:
                                                        pCurrent.setTerrainType(con.iGrass, True, True)
                                                if (pCurrent.getFeatureType() == con.iOasis or pCurrent.getFeatureType() == con.iFloodPlains):
                                                        pCurrent.setFeatureType(-1, 0)


                                                    
        def createMarshes(self, Map, iGridX, iGridY):
                for x in range(iGridX):
                      for y in range(iGridY):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.isRiverSide() and \
                                    (pCurrent.getFeatureType() == con.iJungle or pCurrent.getTerrainType() == con.iTundra)):
                                        bPass = True
                                        if (pCurrent.getBonusType(-1) != -1):
                                                marshRoll = gc.getGame().getSorenRandNum(3, 'no_marsh')                                                
                                                if (marshRoll == 0 and (Map.getClimate() == con.iTemperate)):
                                                        bPass = False
                                                if (marshRoll <= 1 and (Map.getClimate() == con.iArid or Map.getClimate() == con.iCold)):
                                                        bPass = False
                                                #print("marshroll", marshRoll, bPass, x, y)
                                                #no roll for tropical
                                        else:
                                                marshRoll = gc.getGame().getSorenRandNum(6, 'no_marsh')                                                
                                                if (marshRoll == 0 and (Map.getClimate() == con.iTemperate)):
                                                        bPass = False
                                                if (marshRoll <= 2 and (Map.getClimate() == con.iArid or Map.getClimate() == con.iCold)):
                                                        bPass = False
                                                #print("marshroll", marshRoll, bPass, x, y)
                                                #no roll for tropical
                                        if (bPass):
                                                if (pCurrent.isCoastalLand()):
                                                        if (Map.plot( x+1, y ).isWater() and Map.plot( x, y+1 ).isWater()):
                                                                bPass = False
                                                        elif (Map.plot( x, y+1 ).isWater() and Map.plot( x-1, y ).isWater()):
                                                                bPass = False
                                                        elif (Map.plot( x-1, y ).isWater() and Map.plot( x, y-1 ).isWater()):
                                                                bPass = False
                                                        elif (Map.plot( x, y-1 ).isWater() and Map.plot( x+1, y ).isWater()):
                                                                bPass = False
                                                        elif (Map.plot( x+1, y ).isWater() and Map.plot( x, y+1 ).getTerrainType() == con.iMarsh):
                                                                bPass = False
                                                        elif (Map.plot( x, y+1 ).isWater() and Map.plot( x-1, y ).getTerrainType() == con.iMarsh):
                                                                bPass = False
                                                        elif (Map.plot( x-1, y ).isWater() and Map.plot( x, y-1 ).getTerrainType() == con.iMarsh):
                                                                bPass = False
                                                        elif (Map.plot( x, y-1 ).isWater() and Map.plot( x+1, y ).getTerrainType() == con.iMarsh):
                                                                bPass = False
                                                        elif (Map.plot( x+1, y ).getTerrainType() == con.iMarsh and Map.plot( x, y+1 ).isWater()):
                                                                bPass = False
                                                        elif (Map.plot( x, y+1 ).getTerrainType() == con.iMarsh and Map.plot( x-1, y ).isWater()):
                                                                bPass = False
                                                        elif (Map.plot( x-1, y ).getTerrainType() == con.iMarsh and Map.plot( x, y-1 ).isWater()):
                                                                bPass = False
                                                        elif (Map.plot( x, y-1 ).getTerrainType() == con.iMarsh and Map.plot( x+1, y ).isWater()):
                                                                bPass = False
                                        if (bPass):
                                                if (Map.plot( x+1, y ).getTerrainType() == con.iSnow):
                                                        bPass = False
                                                elif (Map.plot( x, y+1 ).getTerrainType() == con.iSnow):
                                                        bPass = False
                                                elif (Map.plot( x-1, y ).getTerrainType() == con.iSnow):
                                                        bPass = False
                                                elif (Map.plot( x, y-1 ).getTerrainType() == con.iSnow):
                                                        bPass = False
                                                        
                                        if (bPass):
                                                #print("turning into marsh",x,y)
                                                pCurrent.setPlotType(PlotTypes.PLOT_LAND, True, True)
                                                pCurrent.setTerrainType(con.iMarsh, True, True)
                                                pCurrent.setFeatureType(con.iMud, 0)
                                                pCurrent.setBonusType(con.iSwamp)
                                                if (pCurrent.isGoody):
                                                        pCurrent.removeGoody()


        def replaceJungles(self, Map, iGridX, iGridY):
                if (Map.getClimate() == con.iTropical): 
                        for x in range(iGridX):
                                for y in range(iGridY):
                                        pCurrent = Map.plot( x, y )
                                        if (pCurrent.getLatitude() >= 43):
                                                if (pCurrent.getFeatureType() == con.iJungle):
                                                        pCurrent.setFeatureType(con.iForest, 0)
                                        else:
                                                if (pCurrent.getBonusType(-1) == con.iPig or pCurrent.getBonusType(-1) == con.iHorse \
                                                    or pCurrent.getBonusType(-1) == con.iMarble or pCurrent.getBonusType(-1) == con.iStone \
                                                    or pCurrent.getBonusType(-1) == con.iCow or pCurrent.getBonusType(-1) == con.iSheep ):
                                                        pCurrent.setFeatureType(-1, 0)
                                                        for iLoopX in range(x-1, x+2):
                                                                for iLoopY in range(y-1, y+2):
                                                                        pLoop = Map.plot( iLoopX%iGridX, iLoopY )
                                                                        if (pLoop.getFeatureType() == con.iJungle and pLoop.getBonusType(-1) == -1):
                                                                                pLoop.setFeatureType(con.iForest, 0)
                                                        

                                                



        def openJunglePassage(self, Map, iGridX, iGridY):
                iDistance = 10
                iPassageWidth = 3
                iStart =  gc.getGame().getSorenRandNum(iDistance-iPassageWidth, '')
                if (Map.isWrapX() == True): 
                        for x in range(iPassageWidth+1,iGridX-(iPassageWidth+1)):
                                for y in range(iGridY/4,iGridY*3/4):
                                        if (x%iDistance == iStart):
                                                if (gc.getGame().getSorenRandNum(3, '') >= 1):
                                                        pCurrent = Map.plot( x, y )
                                                        if (pCurrent.getFeatureType() == con.iJungle):
                                                                if (gc.getGame().getSorenRandNum(2, 'forest roll') == 0):
                                                                        pCurrent.setFeatureType(con.iForest, 0)
                                                                else:
                                                                        pCurrent.setFeatureType(-1, 0)
                                                        if (gc.getGame().getSorenRandNum(2, 'plains roll') == 0):
                                                                if (pCurrent.getTerrainType() == con.iGrass):
                                                                        pCurrent.setTerrainType(con.iPlains, True, True)
                                        if (x%iDistance == iStart+1):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getFeatureType() == con.iJungle):
                                                        if (gc.getGame().getSorenRandNum(2, 'forest roll') == 0):
                                                                pCurrent.setFeatureType(con.iForest, 0)
                                                        else:
                                                                pCurrent.setFeatureType(-1, 0)
                                                if (gc.getGame().getSorenRandNum(2, 'plains roll') == 0):
                                                        if (pCurrent.getTerrainType() == con.iGrass):
                                                                pCurrent.setTerrainType(con.iPlains, True, True)                                                        
                                        if (x%iDistance == iStart+2):
                                                if (gc.getGame().getSorenRandNum(3, '') >= 1):
                                                        pCurrent = Map.plot( x, y )
                                                        if (pCurrent.getFeatureType() == con.iJungle):
                                                                if (gc.getGame().getSorenRandNum(2, 'forest roll') == 0):
                                                                        pCurrent.setFeatureType(con.iForest, 0)
                                                                else:
                                                                        pCurrent.setFeatureType(-1, 0)
                                                        if (gc.getGame().getSorenRandNum(2, 'plains roll') == 0):
                                                                if (pCurrent.getTerrainType() == con.iGrass):
                                                                        pCurrent.setTerrainType(con.iPlains, True, True)                                                        
                if (Map.isWrapY() == True): 
                        for x in range(iGridX/4,iGridX*3/4):
                                for y in range(iPassageWidth+1,iGridY-(iPassageWidth+1)):
                                        if (y%iDistance == iStart):
                                                if (gc.getGame().getSorenRandNum(3, '') >= 1):
                                                        pCurrent = Map.plot( x, y )
                                                        if (pCurrent.getFeatureType() == con.iJungle):
                                                                if (gc.getGame().getSorenRandNum(2, 'forest roll') == 0):
                                                                        pCurrent.setFeatureType(con.iForest, 0)
                                                                else:
                                                                        pCurrent.setFeatureType(-1, 0)
                                                        if (gc.getGame().getSorenRandNum(2, 'plains roll') == 0):
                                                                if (pCurrent.getTerrainType() == con.iGrass):
                                                                        pCurrent.setTerrainType(con.iPlains, True, True)
                                        if (y%iDistance == iStart+1):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getFeatureType() == con.iJungle):
                                                        if (gc.getGame().getSorenRandNum(2, 'forest roll') == 0):
                                                                pCurrent.setFeatureType(con.iForest, 0)
                                                        else:
                                                                pCurrent.setFeatureType(-1, 0)
                                                if (gc.getGame().getSorenRandNum(2, 'plains roll') == 0):
                                                        if (pCurrent.getTerrainType() == con.iGrass):
                                                                pCurrent.setTerrainType(con.iPlains, True, True)                                                        
                                        if (y%iDistance == iStart+2):
                                                if (gc.getGame().getSorenRandNum(3, '') >= 1):
                                                        pCurrent = Map.plot( x, y )
                                                        if (pCurrent.getFeatureType() == con.iJungle):
                                                                if (gc.getGame().getSorenRandNum(2, 'forest roll') == 0):
                                                                        pCurrent.setFeatureType(con.iForest, 0)
                                                                else:
                                                                        pCurrent.setFeatureType(-1, 0)
                                                        if (gc.getGame().getSorenRandNum(2, 'plains roll') == 0):
                                                                if (pCurrent.getTerrainType() == con.iGrass):
                                                                        pCurrent.setTerrainType(con.iPlains, True, True) 
                                                



        def processEarthResources(self, Map, iGridX, iGridY):
                likelihood = int(Map.getSeaLevel())
                bRemoveHorses = False
                bRemoveElephants = False
                bRemoveCattle = False
                bSwapCorn = False
                bSwapWheatRice = False
                bSwapBanana = False
                bSwapWineSilk = False
                bPoorAfrica = False
                bVeryPoorAfrica = False
               

                if (likelihood <= 1):
                        bRemoveHorses = True
                        bRemoveElephants = True
                        bRemoveCattle = True
                        bSwapBanana = True
                        bSwapCorn = True
                        bSwapWheatRice = True
                        bSwapWineSilk = True
                        bPoorAfrica = True
                        bVeryPoorAfrica = True
                if (likelihood == 2):
                        bRemoveHorses = True
                        bRemoveElephants = True
                        bRemoveCattle = False
                        bSwapBanana = False
                        bSwapCorn = True
                        bSwapWheatRice = False
                        bSwapWineSilk = False
                        bPoorAfrica = True
                        bVeryPoorAfrica = False
                if (likelihood >= 3):
                        return
                                
                iEurasiaWestX = self.getEurasiaInfo(0)
                iEurasiaEastX = self.getEurasiaInfo(1)
                iAmericaWestX = self.getAmericaInfo(0)
                iAmericaEastX = self.getAmericaInfo(1)
                iAmericaSouthY = self.getAmericaInfo(2)
                iAmericaNorthY = self.getAmericaInfo(3)
                iAfricaWestX = self.getAfricaInfo(0)
                iAfricaEastX = self.getAfricaInfo(1)
                iAfricaSouthY = self.getAfricaInfo(2)
                iAfricaNorthY = self.getAfricaInfo(3)
                print(iAmericaWestX, iAmericaEastX+1, iAmericaSouthY, iAmericaNorthY+1)
                for x in range(iAmericaWestX, iAmericaEastX+1):
                        for y in range(iAmericaSouthY, iAmericaNorthY+1):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getBonusType(-1) == con.iHorse and bRemoveHorses):
                                        pCurrent.setBonusType(-1)
                                elif (pCurrent.getBonusType(-1) == con.iIvory and bRemoveElephants):
                                        pCurrent.setBonusType(-1)
                                elif (pCurrent.getBonusType(-1) == con.iCow and bRemoveCattle):
                                        pCurrent.setBonusType(-1)                              

                #must use lists cos it's buggy            
                if (bSwapCorn):
                        plotList1 = []
                        plotList2 = []
                        for x in range(iGridX):
                                for y in range(iGridY):
                                        if (x < iAmericaWestX or x > iAmericaEastX):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getBonusType(-1) == con.iCorn):
                                                        plotList1.append(pCurrent)
                                                        #pCurrent.setBonusType(con.iWheat)
                                                        #pCurrent.setFeatureType(-1, 0)
                                        if (x >= iAmericaWestX and x <= iAmericaEastX):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getBonusType(-1) == con.iWheat or pCurrent.getBonusType(-1) == con.iRice or pCurrent.getBonusType(-1) == con.iPig):
                                                        plotList2.append(pCurrent)
                                                        #print(x,y,"app")
                                                        #pCurrent.setBonusType(con.iCorn)
                                                        #pCurrent.setFeatureType(-1, 0)
                        for pCurrent in plotList1:
                                rndnum = gc.getGame().getSorenRandNum(2, 'wheat/rice')
                                if (rndnum <=1 or pCurrent.getTerrainType() == con.iDesert):
                                        pCurrent.setBonusType(con.iWheat)
                                else:
                                        pCurrent.setBonusType(con.iRice)

                                pCurrent.setBonusType(con.iWheat)
                                pCurrent.setFeatureType(-1, 0)
                        for pCurrent in plotList2:
                                pCurrent.setBonusType(con.iCorn)
                                pCurrent.setFeatureType(-1, 0)

                        if (bSwapWheatRice):
                                for pCurrent in plotList1:
                                        if (pCurrent.getX() < (iEurasiaEastX-iEurasiaWestX)*2/3+iEurasiaWestX or pCurrent.getTerrainType() == con.iDesert):
                                                pCurrent.setBonusType(con.iWheat)
                                        else:
                                                pCurrent.setBonusType(con.iRice)

                if (bSwapWineSilk):
                        plotList3 = []
                        for x in range(iGridX):
                                for y in range(iGridY):                                        
                                        if (x < iAmericaWestX or x > iAmericaEastX):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getTerrainType() == con.iPlains):
                                                        if (pCurrent.getBonusType(-1) == con.iWine or pCurrent.getBonusType(-1) == con.iSilk):
                                                                plotList3.append(pCurrent)
                        for pCurrent in plotList3:
                                if (pCurrent.getX() < (iEurasiaEastX-iEurasiaWestX)/2+iEurasiaWestX):
                                        pCurrent.setBonusType(con.iWine)
                                        #print("swapped wine")
                                else:
                                        pCurrent.setBonusType(con.iSilk)
                                        #print("swapped silk")



                                                        
                        
                #Map.plot( 67, 39 ).setBonusType(con.iWheat)
                
                if (bSwapBanana):
                        plotList1 = []
                        plotList2 = []
                        for x in range(iGridX):
                                for y in range(iGridY):                                        
                                        if (x >= iAmericaWestX and x <= iAmericaEastX):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getFeatureType() == con.iJungle):
                                                        if (pCurrent.getBonusType(-1) == con.iBanana):
                                                                plotList1.append(pCurrent)                                         
                                        if (x < iAmericaWestX or x > iAmericaEastX):
                                                pCurrent = Map.plot( x, y )
                                                if (pCurrent.getFeatureType() == con.iJungle):
                                                        if (pCurrent.getBonusType(-1) == con.iGold):
                                                                plotList2.append(pCurrent)
                        for pCurrent in plotList1:
                                pCurrent.setBonusType(con.iGold) 
                        for pCurrent in plotList2:
                                pCurrent.setBonusType(con.iBanana)

                        
                                                                
                if (bPoorAfrica or bVeryPoorAfrica):
                        for x in range(iAfricaWestX, iAfricaEastX+1):
                                for y in range(iAfricaSouthY, iAfricaNorthY+1):
                                        pCurrent = Map.plot( x, y )
                                        if (bPoorAfrica):
                                                if (pCurrent.getBonusType(-1) == con.iRice or pCurrent.getBonusType(-1) == con.iWheat):
                                                        pCurrent.setBonusType(-1)
                                        if (bVeryPoorAfrica):
                                                if (pCurrent.getBonusType(-1) == con.iCow or pCurrent.getBonusType(-1) == con.iPig):
                                                        pCurrent.setBonusType(-1)
                        for x in range(iAfricaWestX, iAfricaEastX+1):
                                for y in range(iAfricaSouthY, (iAfricaNorthY-iAfricaSouthY)/2+iAfricaSouthY+1):
                                       if (pCurrent.getBonusType(-1) == con.iHorse):
                                                pCurrent.setBonusType(-1)

                                        
        def processSingleResources(self, Map, iGridX, iGridY):
                for x in range(iGridX):
                        for y in range(iGridY):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getFeatureType() == con.iJungle):
                                        if (pCurrent.getBonusType(-1) == con.iPig or pCurrent.getBonusType(-1) == con.iRice):
                                                pCurrent.setFeatureType(-1, 0)
                                if (pCurrent.getFeatureType() == con.iSeaIce):
                                        pCurrent.setBonusType(-1)
                        
        def processResourcesClusters(self, Map, iGridX, iGridY):
                for x in range(iGridX-1):
                        for y in range(1, iGridY-1):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.getBonusType(-1) != -1 and pCurrent.getBonusType(-1) != con.iSwamp):
                                        iBonus = pCurrent.getBonusType(-1)
                                        if (Map.plot( x+1, y ).getBonusType(-1) == iBonus):
                                                removeRoll = gc.getGame().getSorenRandNum(3, 'remove')
                                                if (removeRoll <= 1):
                                                        Map.plot( x+1, y ).setBonusType(-1)
                                        if (Map.plot( x+1, y+1 ).getBonusType(-1) == iBonus):
                                                removeRoll = gc.getGame().getSorenRandNum(3, 'remove')
                                                if (removeRoll <= 1):
                                                        Map.plot( x+1, y+1 ).setBonusType(-1)
                                        if (Map.plot( x, y+1 ).getBonusType(-1) == iBonus):
                                                removeRoll = gc.getGame().getSorenRandNum(3, 'remove')
                                                if (removeRoll <= 1):
                                                        Map.plot( x, y+1 ).setBonusType(-1)
                                        if (Map.plot( x, y-1 ).getBonusType(-1) == iBonus):
                                                removeRoll = gc.getGame().getSorenRandNum(3, 'remove')
                                                if (removeRoll <= 1):
                                                        Map.plot( x, y-1 ).setBonusType(-1)
                                                

        def printMapInfo(self, Map, iGridX, iGridY):
                print ("Land:", Map.getLandPlots(), ":", Map.getLandPlots()*100/(Map.getGridWidth()*Map.getGridHeight()), "%")
                iTotSettleable = 0
                for x in range(iGridX):
                        for y in range(iGridY):
                                #pCurrent = Map.plot( x, y )
                                player = gc.getPlayer(0)
                                if (player.canFound(x,y)):
                                        iTotSettleable += 1
                print ("Settleable:", iTotSettleable)
                print ("Climate:", Map.getClimate())
                print ("Sea level:", Map.getSeaLevel())


        def recordAreaIDs(self, Map, iGridX, iGridY):
            
                if (Map.getSeaLevel() <= 2): #high or medium likeliness
                    
                        self.setEurasiaInfo(4,self.MonteCarlo(Map, \
                                                              self.getEurasiaInfo(0), \
                                                              self.getEurasiaInfo(1), \
                                                              self.getEurasiaInfo(2), \
                                                              self.getEurasiaInfo(3)))
                        self.setAfricaInfo(4,self.MonteCarlo(Map, \
                                                              self.getAfricaInfo(0), \
                                                              self.getAfricaInfo(1), \
                                                              self.getAfricaInfo(2), \
                                                              self.getAfricaInfo(3)))
                        #North America
                        self.setAmericaInfo(4,self.MonteCarlo(Map, \
                                                              self.getAmericaInfo(0), \
                                                              self.getAmericaInfo(1), \
                                                              iGridY/2, \
                                                              self.getAmericaInfo(3)))
                        #South America
                        self.setAmericaInfo(5,self.MonteCarlo(Map, \
                                                              self.getAmericaInfo(0), \
                                                              self.getAmericaInfo(1), \
                                                              self.getAmericaInfo(2), \
                                                              iGridY/2))
                        if (self.getWorldShapeInfo(7) == 2 or self.getWorldShapeInfo(7) == 4):
                                self.setIsland1Info(4,self.MonteCarlo(Map, \
                                                                      self.getIsland1Info(0), \
                                                                      self.getIsland1Info(1), \
                                                                      self.getIsland1Info(2), \
                                                                      self.getIsland1Info(3)))
                        if (self.getWorldShapeInfo(7) == 3 or self.getWorldShapeInfo(7) == 4):                        
                                self.setIsland2Info(4,self.MonteCarlo(Map, \
                                                                      self.getIsland2Info(0), \
                                                                      self.getIsland2Info(1), \
                                                                      self.getIsland2Info(2), \
                                                                      self.getIsland2Info(3)))

                  

                elif (Map.getSeaLevel() == 3 or self.getWorldShapeInfo(11) == 1): #low
                        continentWidth = int(CyMap().getGridWidth()/3)
                        continentWidth = continentWidth - continentWidth/20
                        continentHeight = int(CyMap().getGridHeight()/2)
                        continentHeight = continentHeight + continentHeight/15

                        newWorldCounter = 0
                        continentCounter = 0
                        for i in range(3):
                                continentWestX = 0 + i*continentWidth
                                for j in range(2):
                                        continentSouthY = 0 + j*continentHeight - continentHeight/30
                                        if (self.getRandomContinents(continentCounter) == 1):

                                                print(continentWestX)
                                                print(continentWestX+continentWidth)
                                                print(continentSouthY)
                                                print(continentSouthY+continentHeight)

##                                                self.setAmericaInfo(0, continentWestX)
##                                                self.setAmericaInfo(1, continentWestX+continentWidth)
##                                                self.setAmericaInfo(2, continentSouthY)
##                                                self.setAmericaInfo(3, continentSouthY+continentHeight)
                                                
                                                self.setAmericaInfo(4+newWorldCounter,self.MonteCarlo(Map, \
                                                                    continentWestX, \
                                                                    continentWestX+continentWidth, \
                                                                    continentSouthY, \
                                                                    continentSouthY+continentHeight))
                                                
                                                newWorldCounter = newWorldCounter + 1
                                        continentCounter = continentCounter + 1





                                


                                   

        def MonteCarlo(self, Map, iWestX, iEastX, iSouthY, iNorthY):
                iHit = 0
                tempID = 0
                iCounter = 0
                iThreshold = 5
                while (iHit <= iThreshold):
                        rndX = gc.getGame().getSorenRandNum((iEastX-iWestX)/2, 'X') + iWestX + (iEastX-iWestX)/4
                        rndY = gc.getGame().getSorenRandNum((iNorthY-iSouthY)/2, 'X') + iSouthY + (iNorthY-iSouthY)/4
                        pCurrent = Map.plot( rndX, rndY )
                        if (not pCurrent.isWater()):
                                for iLoopArea in utils.getAreas():
                                        if (pCurrent.area().getID() == iLoopArea.getID()):
                                                if (tempID == iLoopArea.getID()):
                                                        iHit += 1
                                                else:
                                                        tempID = iLoopArea.getID()
                                                        iHit = 0
                        iCounter += 1
                        if (iCounter > 20):
                                iThreshold = 3
                        if (iCounter > 40):
                                iThreshold = 2
                        if (iCounter > 80):
                                print("infinite loop", iWestX, iEastX, iSouthY, iNorthY)
                                break
                return tempID
                
                                

        def markMapInfo(self, Map, iGridX, iGridY):

                iTerrain = con.iTundra

                #check the equator
            
                if ((Map.isWrapX() == True and Map.isWrapY() == False) or (Map.isWrapX() == False and Map.isWrapY() == True)):
                        if (self.getWorldShapeInfo(0) == 1):
                                CyMap().plot(10, 0).setPlotType(PlotTypes.PLOT_PEAK, True, True) #flag used to quickly check latitude from the DLL
                                CyMap().plot(10, 0).setTerrainType(iTerrain, True, True)
                                #CyMap().plot(10, 0).setFeatureType(0, 0)

                #necessary because yield (including salt lakes) are initially set with equator at south
                oceanID = Map.plot( 0, 0 ).area().getID()
                for x in range(iGridX):
                        for y in range(iGridY):
                                pCurrent = Map.plot( x, y )
                                if (pCurrent.isWater()):
                                        if (pCurrent.area().getID() != oceanID):
                                                pCurrent.updateYield()

                #now new world position
                                                        
                if (Map.getSeaLevel() <= 2): #high or medium likeliness                             
                        if (self.getWorldShapeInfo(1) == 0):
                                CyMap().plot(15, 0).setPlotType(PlotTypes.PLOT_PEAK, True, True)
                                CyMap().plot(15, 0).setTerrainType(iTerrain, True, True)
                                #CyMap().plot(15, 0).setFeatureType(0, 0)
                                CyMap().plot(16, 0).setPlotType(PlotTypes.PLOT_PEAK, True, True)
                                CyMap().plot(16, 0).setTerrainType(iTerrain, True, True)
                                #CyMap().plot(16, 0).setFeatureType(0, 0)
                        else:
                                CyMap().plot(19, 0).setPlotType(PlotTypes.PLOT_PEAK, True, True)
                                CyMap().plot(19, 0).setTerrainType(iTerrain, True, True)
                                #CyMap().plot(19, 0).setFeatureType(0, 0)
                                CyMap().plot(20, 0).setPlotType(PlotTypes.PLOT_PEAK, True, True)
                                CyMap().plot(20, 0).setTerrainType(iTerrain, True, True)
                                #CyMap().plot(20, 0).setFeatureType(0, 0)
                                
                elif (Map.getSeaLevel() == 3): #low
                        continentWidth = int(CyMap().getGridWidth()/3)
                        continentWidth = continentWidth - continentWidth/20
                        continentHeight = int(CyMap().getGridHeight()/2)
                        continentHeight = continentHeight + continentHeight/15

                        continentCounter = 0
                        for i in range(3):
                                continentWestX = 0 + i*continentWidth
                                for j in range(2):
                                        continentSouthY = 0 + j*continentHeight - continentHeight/30
                                        if (self.getRandomContinents(continentCounter) == 1):
                                            
                                                CyMap().plot(15+continentCounter, 0).setPlotType(PlotTypes.PLOT_PEAK, True, True)
                                                CyMap().plot(15+continentCounter, 0).setTerrainType(4, True, True)
                                                #CyMap().plot(15+continentCounter, 0).setFeatureType(0, 0)

                                        continentCounter = continentCounter + 1

                if (Map.getSeaLevel() >= 3): #low and very low
                        iUnhabitatedContinentRoll = gc.getGame().getSorenRandNum(15, 'roll') #40% of 1 empty continent
                        if (iUnhabitatedContinentRoll < 6):
                                continentWidth = int(CyMap().getGridWidth()/3)
                                continentHeight = int(CyMap().getGridHeight()/2)
                                iCounter = 0
                                for i in range(3):
                                        continentWestX = 0 + i*continentWidth
                                        for j in range(2):
                                                continentSouthY = 0 + j*continentHeight
                                                if (iCounter == iUnhabitatedContinentRoll):
                                                        self.setEmptyContinentInfo(0, continentWestX)
                                                        self.setEmptyContinentInfo(1, continentWestX+continentWidth)
                                                        self.setEmptyContinentInfo(2, continentSouthY)
                                                        self.setEmptyContinentInfo(3, continentSouthY+continentHeight)
                                                        print("Empty continent: ",iUnhabitatedContinentRoll)
                                                        return
                                                iCounter += 1
                                        

        def reassignStartingPlots(self, Map, iGridX, iGridY):
            
                #Rhye - isValid moved to Utils, needs to be called from Riseandfall
            
##                def isValid(playerID, x, y):
##
##                        map = CyMap()
##                        pPlot = map.plot(x, y)
##                        
##                        if (pPlot.getArea() != map.findBiggestArea(False).getID()):
##                                return False
##
##                        return True




##                for iLoopCiv in range(con.iNumMajorPlayers):
##                        gc.getPlayer(iLoopCiv).setStartingPlot(None, True)

##                for iLoopArea in utils.getAreas():
##                        CyMap().updateMinOriginalStartDist(iLoopArea)

##                for iLoopCiv in range(con.iNumMajorPlayers):
##                        gc.getPlayer(iLoopCiv).AI_updateFoundValues(True) #already in findStartingPlot                                        

                

                #need to store here variables cos iterating calls will kill the process
                lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents = utils.loadRandomWorldInfo()
                print("lRolls",lRolls)
	
                for iLoopCiv in range(con.iNumMajorPlayers):                        
                        #pResult=Map.plotByIndex(CvMapGeneratorUtil.findStartingPlot(iLoopCiv, isValid))
                        if (utils.getInThisGame(iLoopCiv) == True):
                                if (gc.getPlayer(iLoopCiv).getBirthTurn() == 0): # or gc.getPlayer(iLoopCiv).isHuman()):
                                        pResult=Map.plotByIndex(CvMapGeneratorUtil.findStartingPlot(iLoopCiv, lEurasia, lIsland1, lIsland2, lAfrica, lAmerica, lRolls, lRandomContinents, utils.isValid))
                                        con.tCapitals[iLoopCiv]=(pResult.getX(), pResult.getY())
                                        pResult.setStartingPlot(True)
                                        gc.getPlayer(iLoopCiv).setStartingPlot(pResult, True)
                                        
                                        print(iLoopCiv, "starting plot", con.tCapitals[iLoopCiv])
                                        
        ##                                tempSquare = utils.checkBounds(pResult.getX()-3, pResult.getY()-3, pResult.getX()+4, pResult.getY()+4)
        ##                                con.tCoreAreasTL[iLoopCiv]=((tempSquare[0], tempSquare[1]))
        ##                                con.tCoreAreasTL[iLoopCiv]=((tempSquare[2], tempSquare[3]))
        ##                                tempSquare = utils.checkBounds(pResult.getX()-4, pResult.getY()-4, pResult.getX()+5, pResult.getY()+5)
        ##                                con.tNormalAreasTL[iLoopCiv]=((tempSquare[0], tempSquare[1]))
        ##                                con.tNormalAreasTL[iLoopCiv]=((tempSquare[2], tempSquare[3]))

                for iLoopCiv in range(con.iNumMajorPlayers):
                        print(gc.getPlayer(iLoopCiv).getCivilizationShortDescription(0), "birth turn", gc.getPlayer(iLoopCiv).getBirthTurn())


        def cleanContacts(self):
                iCiv = utils.getHumanID()
                teamCiv = gc.getTeam(gc.getPlayer(iCiv).getTeam())

                for iOtherCiv in range(con.iNumTotalPlayers):
                        if (iOtherCiv != iCiv):
                               teamCiv.cutContact(iOtherCiv)

                        
