# Rhye's and Fall of Civilization - Religions management

from CvPythonExtensions import *
import CvUtil
import PyHelpers       
import Popup
import cPickle as pickle     	
import Consts as con
import RFCUtils

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer
utils = RFCUtils.RFCUtils()

### Constants ###

iArabia = con.iArabia
iNumPlayers = con.iNumPlayers
iBarbarian = con.iBarbarian
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iCeltia = con.iCeltia

i2250BC = con.i2250BC
i2085BC = con.i2085BC
i1800BC = con.i1800BC
i600BC = con.i600BC
i483BC = con.i483BC
i479BC = con.i479BC
i33AD = con.i33AD
i622AD = con.i622AD



# initialise religion variables to religion indices from XML
iJudaism = con.iJudaism 
iChristianity = con.iChristianity
iIslam = con.iIslam
iHinduism = con.iHinduism
iBuddhism = con.iBuddhism
iConfucianism = con.iConfucianism
iTaoism = con.iTaoism

iMissionary_Jewish = con.iJewishMissionary
iMissionary_Christian = con.iChristianMissionary
iMissionary_Islamic = con.iIslamicMissionary
iMissionary_Hindu = con.iHinduMissionary
iMissionary_Buddhist = con.iBuddhistMissionary
iMissionary_Confucian = con.iConfucianMissionary
iMissionary_Taoist = con.iTaoistMissionary


# initialise coordinates

tJerusalem = (73, 38)
tJewishTL = (68, 34)
tJewishBR = (80, 42)
tVaranasiTL = (91, 37)
tVaranasiBR = (94, 40)
tBodhgayaTL = (92, 38)
tBodhgayaBR = (95, 40)
tBuddhistTL = (87, 33)
tBuddhistBR = (102, 44)
tHenanTL = (101, 43)
tHenanBR = (104, 46)
tSEAsiaTL = (97, 31)
tSEAsiaBR = (107, 46)
tAsiaTL = (83, 28)
tAsiaBR = (1, 66)
tEuropeTL = (48, 33)
tEuropeBR = (72, 65)
tQufuTL = (102, 44)
tQufuBR = (106, 46)
tMecca = (75, 33)



class Religions:

##################################################
### Secure storage & retrieval of script data ###
################################################
		
        def getSeed( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iSeed']

        def setSeed( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['iSeed'] = gc.getGame().getSorenRandNum(100, 'Seed for random delay')
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )        


#######################################
### Main methods (Event-Triggered) ###
#####################################  

        def setup(self):
                self.setSeed()
                

       	
        def checkTurn(self, iGameTurn):

                #print ("JUDAISM", i2085BC + 48*self.getSeed()/100)
                #popup = Popup.PyPopup() 
                #popup.setBodyString(  'JUDAISM %d' %(i2085BC + 48*self.getSeed()/100))
                #popup.launch()
                if (not gc.getGame().isReligionFounded(iJudaism)):
                        iIndianModifier = 0
                        if (gc.getPlayer(con.iIndia).isHuman()):
                                iIndianModifier = 15 #for the UHV
                        if (iGameTurn == i2250BC + 30*self.getSeed()/100 + iIndianModifier): #Judaism up to 1500BC
                                #RFCRAND
                                lJerusalem = [utils.getJerusalemLocation(0), utils.getJerusalemLocation(1)]
                                lJewishTL = [max(0,lJerusalem[0]-8), max(0,lJerusalem[1]-8)]
                                lJewishBR = [min(lJerusalem[0]+8,CyMap().getGridWidth()) , min(lJerusalem[1]+8,CyMap().getGridHeight())]
                                pJerusalem = gc.getMap().plot(lJerusalem[0], lJerusalem[1])                
                                #if (not pJerusalem.getPlotCity().isNone()):                            
                                if (pJerusalem.getPlotCity() != None):                        
                                        if (pJerusalem.getPlotCity().getOwner() == iIndependent or pJerusalem.getPlotCity().getOwner() == iIndependent2 or pJerusalem.getPlotCity().getOwner() == iBarbarian):
                                                self.foundReligion(lJerusalem, iJudaism)
                                                return
                                tCity = self.selectRandomCityAreaCiv(lJewishTL, lJewishBR, iIndependent)
                                self.foundReligion(tCity, iJudaism)
                                return
                            
                                tCity = self.selectRandomCityAreaCiv((0, 0), (gc.getMap().getGridWidth(), gc.getMap().getGridHeight()), iIndependent)
                                if (tCity != False):
                                        self.foundReligion(tCity, iJudaism)                                        
                                else:
                                        tCity = self.selectRandomCityAreaCiv((0, 0), (gc.getMap().getGridWidth(), gc.getMap().getGridHeight()), iIndependent2)
                                        if (tCity != False):
                                                self.foundReligion(tCity, iJudaism)
                    

                if (not gc.getGame().isReligionFounded(iChristianity)):
                        if (iGameTurn == i33AD + 8*self.getSeed()/100): #Christianity up to 190AD (15 = 330AD)
                                #RFCRAND
                                lJerusalem = [utils.getJerusalemLocation(0), utils.getJerusalemLocation(1)]
                                pJerusalem = gc.getMap().plot(lJerusalem[0], lJerusalem[1])                
                                #if (not pJerusalem.getPlotCity().isNone()):                            
                                if (pJerusalem.getPlotCity() != None):                        
                                        if (pJerusalem.getPlotCity().getOwner() == iIndependent or pJerusalem.getPlotCity().getOwner() == iIndependent2 or pJerusalem.getPlotCity().getOwner() == iBarbarian):
                                                #RFCRAND
                                                tCity = lJerusalem
                                                bChristianResult = self.foundReligion(tCity, iChristianity)                                                
                                        else:
                                                tCity = self.selectRandomCityReligionCiv(iJudaism, iIndependent)
                                                bChristianResult = self.foundReligion(tCity, iChristianity)
                                        if (bChristianResult == False):
                                                tCity = self.selectRandomCityReligionCiv(iJudaism, iIndependent2)
                                                bChristianResult = self.foundReligion(tCity, iChristianity)
                                        if (bChristianResult == False):
                                                tCity = self.selectRandomCityReligionCiv(iJudaism, iCeltia)
                                                bChristianResult = self.foundReligion(tCity, iChristianity)
                                        if (bChristianResult == False):
                                                tCity = self.selectRandomCityReligionCiv(iJudaism, iBarbarian)
                                                bChristianResult = self.foundReligion(tCity, iChristianity)
                                        if (bChristianResult == True):
                                                self.spreadReligion(tCity, 3, iMissionary_Christian)   
 
          
                if (CyMap().getSeaLevel() != 4):  #not very low
                        if (utils.getInThisGame(con.iArabia) == True):
                                if (iGameTurn == gc.getPlayer(con.iArabia).getBirthTurn()+1): #RFCRAND
                                        if (gc.getGame().isReligionFounded(iIslam)):
                                                for pyCity in PyPlayer(iArabia).getCityList():
                                                        if (pyCity.GetCy().isHolyCityByType(iIslam)):
                                                                if (gc.getPlayer(pyCity.GetCy().getOwner()).isHuman() == 0):
                                                                        print ("spreading Islam", iMissionary_Islamic)
                                                                        #self.spreadReligion( tMecca, 4, iMissionary_Islamic)
                                                                        self.spreadReligion( (pyCity.GetCy().getX(), pyCity.GetCy().getY()), 4, iMissionary_Islamic) 
#RFCRAND
##                if (iGameTurn == 151):
##                        if (not gc.getPlayer(0).isPlayable()): #late start condition
##                                pMecca = gc.getMap().plot(tMecca[0], tMecca[1])                
##                                if (not pMecca.getPlotCity().isNone()):                            
##                                        if (pMecca.getPlotCity().getOwner() == con.iArabia):
##                                                self.foundReligion(tMecca, iIslam)


        def foundReligion(self, tPlot, iReligion):
                if (tPlot != False):
                        plot = gc.getMap().plot( tPlot[0], tPlot[1] )                
                        #if (not plot.getPlotCity().isNone()):
                        if (plot.getPlotCity() != None):
                                #if (gc.getPlayer(city.getOwner()).isHuman() == 0):
                                #if (not gc.getGame().isReligionFounded(iReligion)):
                                gc.getGame().setHolyCity(iReligion, plot.getPlotCity(), True)
                                return True
                        else:
                                return False
                            
                return False


        def selectRandomCityCiv(self, iCiv):
                if (gc.getPlayer(iCiv).isAlive()):
                        cityList = []
                        for pyCity in PyPlayer(iCiv).getCityList():
                                cityList.append(pyCity.GetCy())
                        iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
                        city = cityList[iCity]
                        return (city.getX(), city.getY())
                return False
            

        def selectRandomCityArea(self, tTopLeft, tBottomRight):
                cityList = []
                for x in range(tTopLeft[0], tBottomRight[0]+1):
                        for y in range(tTopLeft[1], tBottomRight[1]+1):
                                pCurrent = gc.getMap().plot( x, y )
                                if ( pCurrent.isCity()):
                                        cityList.append(pCurrent.getPlotCity())
                if (cityList):
                        iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
                        city = cityList[iCity]
                        return (city.getX(), city.getY())
                else:
                        return False


        def selectRandomCityAreaCiv(self, tTopLeft, tBottomRight, iCiv):
                cityList = []
                for x in range(tTopLeft[0], tBottomRight[0]+1):
                        for y in range(tTopLeft[1], tBottomRight[1]+1):
                                pCurrent = gc.getMap().plot( x, y )
                                if ( pCurrent.isCity()):
                                        if (pCurrent.getPlotCity().getOwner() == iCiv):
                                                cityList.append(pCurrent.getPlotCity())
                if (cityList):
                        iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
                        city = cityList[iCity]
                        return (city.getX(), city.getY())
                else:
                        return False



        def selectRandomCityReligion(self, iReligion):
                if (gc.getGame().isReligionFounded(iReligion)):
                        cityList = []
                        for iPlayer in range(iNumPlayers):
                                for pyCity in PyPlayer(iPlayer).getCityList():
                                        if pyCity.GetCy().isHasReligion(iReligion):
                                                cityList.append(pyCity.GetCy())                                        
                        iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
                        city = cityList[iCity]
                        return (city.getX(), city.getY())
                return False


        def selectRandomCityReligionCiv(self, iReligion, iCiv):
                if (gc.getGame().isReligionFounded(iReligion)):
                        cityList = []
                        for iPlayer in range(iNumPlayers):
                                for pyCity in PyPlayer(iPlayer).getCityList():
                                        if pyCity.GetCy().isHasReligion(iReligion):
                                                if (pyCity.GetCy().getOwner() == iCiv):                            
                                                        cityList.append(pyCity.GetCy())
                        if (cityList):
                                iCity = gc.getGame().getSorenRandNum(len(cityList), 'random city')
                                city = cityList[iCity]
                                return (city.getX(), city.getY())
                return False


        def spreadReligion(self, tCoords, iNum, iMissionary):
                city = gc.getMap().plot( tCoords[0], tCoords[1] ).getPlotCity()
                #print city
                #print city.getOwner()
                utils.makeUnit(iMissionary, city.getOwner(), tCoords, iNum)


                    
