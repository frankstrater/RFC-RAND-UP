# Rhye's and Fall of Civilization - Dynamic resources

from CvPythonExtensions import *
import CvUtil
import PyHelpers  
import Popup
import Consts as con

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

### Constants ###


# initialise bonuses variables

iHorse = con.iHorse
iBanana = con.iBanana
iCorn = con.iCorn
iCow = con.iCow
iPig = con.iPig
iSheep = con.iSheep
iWheat = con.iWheat
iSugar = con.iSugar
iWine = con.iWine
iCotton = con.iCotton
iDye = con.iDye
iRice = con.iRice
     

class Resources:
       	
        def checkTurn(self, iGameTurn):


                if (iGameTurn == 5): #otherwise it's picked by Portugal at the beginning
                        gc.getMap().plot(49, 43).setImprovementType(con.iHut)


                if (iGameTurn == con.i450AD): #(dye added later to prevent Carthaginian UHV exploit)
                        gc.getMap().plot(53, 51).setBonusType(iDye) #France
                        gc.getMap().plot(53, 55).setBonusType(iDye) #England
                if (not gc.getPlayer(0).isPlayable()): #late start condition
                        if (iGameTurn == con.i600AD): 
                                gc.getMap().plot(53, 51).setBonusType(iDye) #France
                                gc.getMap().plot(53, 55).setBonusType(iDye) #England
                    
                if (iGameTurn == con.i1100AD):
                        #gc.getMap().plot(71, 30).setBonusType(iSugar) #Egypt
                        gc.getMap().plot(72, 24).setBonusType(iSugar) #East Africa
                        gc.getMap().plot(70, 17).setBonusType(iSugar) #Zimbabwe
                        gc.getMap().plot(68, 11).setBonusType(iSugar) #South Africa

                        gc.getMap().plot(66, 23).setBonusType(iBanana) #Central Africa
                        gc.getMap().plot(67, 21).setBonusType(iBanana) #Central Africa

                if (iGameTurn == con.i1200AD):
                        gc.getMap().plot(57, 52).setBonusType(iWheat) #Amsterdan
                        
                if (iGameTurn == con.i1600AD):
                        gc.getMap().plot(28, 46).setBonusType(iCow) #Washington area
                        gc.getMap().plot(30, 49).setBonusType(iCow) #New York area
                        gc.getMap().plot(25, 49).setBonusType(iCow) #Lakes
                        gc.getMap().plot(24, 43).setBonusType(iCow) #Jacksonville area
                        gc.getMap().plot(18, 46).setBonusType(iCow) #Colorado 
                        gc.getMap().plot(11, 47).setBonusType(iCow) #California
                        gc.getMap().plot(20, 45).setBonusType(iCow) #Texas
                        gc.getMap().plot(37, 14).setBonusType(iCow) #Argentina
                        gc.getMap().plot(33, 11).setBonusType(iCow) #Argentina
                        gc.getMap().plot(35, 10).setBonusType(iCow) #Pampas

                        gc.getMap().plot(24, 43).setBonusType(iCotton) #near Florida
                        gc.getMap().plot(23, 45).setBonusType(iCotton) #Louisiana
                        gc.getMap().plot(22, 44).setBonusType(iCotton) #Louisiana
                        
                        gc.getMap().plot(22, 49).setBonusType(iPig) #Lakes
                        
                        gc.getMap().plot(21, 50).setBonusType(iWheat) #Canadian border
                        gc.getMap().plot(19, 48).setBonusType(iWheat) #Midwest

                        gc.getMap().plot(22, 33).setBonusType(iBanana) #Guatemala
                        gc.getMap().plot(27, 31).setBonusType(iBanana) #Colombia
                        gc.getMap().plot(43, 23).setBonusType(iBanana) #Brazil
                        gc.getMap().plot(39, 26).setBonusType(iBanana) #Brazil

                        gc.getMap().plot(49, 44).setBonusType(iCorn) #Galicia
                        gc.getMap().plot(54, 48).setBonusType(iCorn) #France
                        gc.getMap().plot(67, 47).setBonusType(iCorn) #Romania
                       

                if (iGameTurn == con.i1700AD):
                        gc.getMap().plot(26, 45).setBonusType(iHorse) #Washington area                        
                        gc.getMap().plot(21, 48).setBonusType(iHorse) #Midwest
                        gc.getMap().plot(19, 45).setBonusType(iHorse) #Texas
                        gc.getMap().plot(40, 25).setBonusType(iHorse) #Brazil
                        gc.getMap().plot(33, 10).setBonusType(iHorse) #Buenos Aires area
                        gc.getMap().plot(32, 8).setBonusType(iHorse) #Pampas

                        gc.getMap().plot(27, 36).setBonusType(iSugar) #Caribbean
                        gc.getMap().plot(39, 25).setBonusType(iSugar) #Brazil
                        gc.getMap().plot(37, 20).setBonusType(iSugar) #inner Brazil

                        gc.getMap().plot(107, 50).setBonusType(iCorn) #Manchuria

                if (iGameTurn == con.i1850AD):
                        gc.getMap().plot(12, 45).setBonusType(iWine) #California
                        gc.getMap().plot(31, 10).setBonusType(iWine) #Andes

                        gc.getMap().plot(114, 11).setBonusType(iSheep) #Australia
                        gc.getMap().plot(116, 13).setBonusType(iSheep) #Australia
                        gc.getMap().plot(121, 6).setBonusType(iSheep) #New Zealand

                        gc.getMap().plot(19, 41).setBonusType(iHorse) #Mexico

                        gc.getMap().plot(58, 47).setBonusType(iRice) #Vercelli
                        gc.getMap().plot(12, 49).setBonusType(iRice) #California




                
                #setImprovementType(ImprovementType eNewValue)
                #setPlotType(PlotType eNewValue, BOOL bRecalculate, BOOL bRebuildGraphics)
                #setTerrainType(TerrainType eNewValue, BOOL bRecalculate, BOOL bRebuildGraphics)


                        


            




                        
