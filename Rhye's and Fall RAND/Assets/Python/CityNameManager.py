# -*- coding: cp1252 -*-
# Rhye's and Fall of Civilization - City naming and renaming management

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Popup
import Consts as con
import cPickle as pickle #RFCRAND
import RFCUtils #RFCRAND
utils = RFCUtils.RFCUtils() #RFCRAND

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

### Constants ###




# initialise player variables to player IDs from WBS
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
      



#RFCRAND

tForceCapital = (
0, #Egypt
0, #India
0, #China 
0, #Babylonia
-1, #Greece
0, #Persia
1, #Carthage
0, #Rome
0, #Japan
0, #Ethiopia
0, #Maya
-1, #Vikings
0, #Arabia
0, #Khmer
-1, #Spain
0, #France
1, #England
0, #Germany
-1, #Russia
1, #Holland
0, #Mali
1, #Portugal
0, #Inca
0, #Mongolia
0, #Aztecs
-1, #Turkey
1 #America
) 


##################
### City lists ###
################## 


tCityLists = (
#Egypt
((
"Niwt-Rst",#Thebes
"Ineb Hedj",#Memphis
"Abdju",#Abydos
"Iunu",#Heliopolis
"Yebu",#Elephantine
"Henen-Nesut",#Heracleopolis
"Khaset",#Xois
"Sekhem",#Letopolis
"Per-Usir",#Busiris
"Per-Bast",#Bubastis
"Hebenu",#Antinooplis
"Hut-Repyt",#Athribis
"Khemenu",#Hermopolis
"Zawty",#Asyut
"Nekhen",#Heirakonpolis
"Tjeny",#Thinis
"Shedyet",#Crocodilopolis
"Gebtu",#Coptos
"Akhetaten",
"-1"
),(
"Per-Wadjet",#Buto
"Djanet",#Tanis
"Per-Atum",#Pithom
"Djedet",#Mendes
"Pi-Ramesses", #"Hatwaret",#Avaris
"Djebnetjer",#Sebennytos
"-1"
),(
"Kadesh",
"Dapur",#supposedly in Syria
"-1"
),(
"Zemar",#in Lebanon
"Gaza",
"Gebal",#Byblos
"-1"
)),
#India
((
"Dilli",#(2000 B.C.)(Capital)
"Lahore",#(2000 B.C.)(in pakistan)
"Varanasi",#(1000 B.C.)
"Nagpur",#(700 B.C.)(Note:Line over the a!)
"Takshashila",#(518 B.C.)
"Patliputra",#(490 B.C.)
"Ujjaini",#(400 B.C.)
"Agra",#(150 A.D. or 1504 A.D.)
"Bengaluru",#(500 A.D.)
"Dhaka",#(600 A.D.)
"Raipur",#(800 A.D.)
"Bhopal",#(1000 A.D.)
"Lakhnau",#(1350 A.D.?)
"Indore",#(Mughal Times)
"Amritsr",#(1574 A.D.)
"Bhagyanagar",#"Hyderabad",#(1591 A.D.)
"Jaipur",#(1727)
"-1"
),(
"Chittagong",#(ancient times)
"Mumbai",#(250 B.C.)
"Cochin",
"Calcutta",#(0 A.D.)
"Chennai",#(0 A.D.)
"Karachi",#(712 A.D.?)(in pakistan)
"Visakhapatnam",#(500 B.C.)
"Orugallu",#(300 B.C.)
"Govapuri",#(200 B.C.)
"Tanjapuri",#(0 A.D.)
"Surat",#(1400's)
"Berhampur",
"Kakinada",
"Pitikapuram",
"Thiruvananthapuram",#(1000 B.C.)
"-1"
),(
"Badulla",#(Ancient Times)
"Galle",#(1400 B.C.)
"Anuradhapura",#(400 B.C.)
"Kurunegala",#(1200's)
"Kandy",#(1300's)
"Ratnapura",
"-1"
),(
"Male",#(ancient times)
"Kolon Thota",#(0 A.D.)
"Trincomalee",#(400 B.C.)
"Jaffna",
"Sri Jayawardenapura-Kotte",#(ancient times)
"-1"
)),
#China
((
"Beijing",# founded in 1045 BC
"Xi'an",#(Chang'an) founded in 1000s BC
"Luoyang",#770BC
"Kaifeng",#700sBC (flourish in 1000ADs, before invade of Mongols)
"Suzhou",#541BC
"Yangzhou",#486BC (flourish in 1000ADs, before invade of Mongols)
"Nanjing",#472BC
"Taiyuan",# 453 BC (flooded several times intentionally)
"Chengdu",#311BC (a city never completely destroyed, have a mass earthquake recently)
"Shenyang",# BC301~296
"Lanzhou",#241
"Chongqing",#(BC 1100s but named Chongqing in 1189)
"Wuhan",#(BC 1500s but disappear in BC 1100s, 3 cities together renamed Wuhan in 1927)
"Wulumuqi",#(Urumqi) 1755 AD (So we call there "new horizon")
"Changchun", # 1800 AD
"-1"
),(
"Hangzhou",#(Lin'an) 221BC
"Guangzhou",#(Canton) 214BC
"Ningbo",# 821AD
"Xianmen",#(Amoy) 1387AD
"Tianjin",#(Tientsin) 1404AD
"Shanghai",# 1553AD
"Qingdao",#(Tsintao) 1891AD (Former German Colony)
"Macau",# (Aomen ??) Maybe 1557AD (Who knows what Portuguese did there?)
"Xianggang",#1841AD
"Dalian",#1899AD (Former Russian Colony)
"Shenzhen",#1980AD (the fastest growing cities, use 20 years from a small villige to a city with 11 million population)
"-1"
),(
"Lasa",#(Lhasa) 633 AD (Not ours that time, but Tibet belong to China since the domination of Mogols 700years ago)
"Pyongyang",
"-1"
),(
"Haikou",#several hundreds years ago
"Sanya",#Sanya
"Taibei",#1875AD (Taiwan was invaded by Niederlander, Spainish and Japanese, but it's part of China undoubtly, no matter it's PRC or ROC)
"Taichung",#Taizhong 1705 AD
"Gaoxiong",#Kaohsiung
"-1"
)),
#Babylonia
((
"Babil&#251;",
"Uruk",#Erech
"Larsa",#Lasar
"Ninua",
"Shushan",
"Nippur",
"Akkad",#Agade
"Eshnunna",
"Kish",
"Isin",
"Zariqum",
"Opis",
"Borsippa",#Barsippa
"Anatho",
"Sippar",
"Zuruban",
"Calchu",#Assyrian city of Nimrud.
"Cuthah",#Assyrian or Iranian plateau city.
"Mari",#west of original Babylonian power.
"Thapsacus",#tributary from Syria.
"-1"
),(
"Eridu",
"Ur",
"Lagash",
"Kesh",#not the same as Kish
"-1"
),(
"-1",
"-1"
),(
"Raphia",
"-1"
)),
#Greece
((
"Sparte",#(1100 BC)
"Delphoi",
"Mykenai",
"Olympia",
"Thebai",
"Larisa",#(400 B.C.)
"Argos Orestikon",#Macedonian
"Aegae",#Macedonian
"Stageira",
"Trikka",
"Tomis",#now Constantia (Romania)
"-1"
),(
"Athenai",#(1000 B.C.)(Capital)
"Korinthos",
"Argos",
"Rhodos",
"Ilion",#also Troy
"Knossos",
"Miletos",
"Megara",
"Pergamon",
"Ephesos",
"Halicarnassos",
"Heraclea",
"Patras",#(3000 B.C.), ancient Patrai. Important in Mycenian times
"Pylos",
"Epidavros",#also Epidaurus
"Thessaloniki",#(315 B.C.)
"Mytilene",
"Arta",#(295 B.C.), ancient Amvrakia
"Kerkyra",
"-1"
),(
"-1"
),(
"Naxos",#735 BC - oldest Greek colony in Sicily
"Olbia",#also Pontic Olbia, on the Black Sea
"Alexandreia",
"Kyrene",
"Berenikis",
"Seleukeia",
"Antiokheia",
#"Trapezos",#756 BC - given to Turkey's list on the grounds that it's in the Turkish heartland
"Tyras",#in Ukraine
"Syrakousai",#Syracuse
"Rhegion",#now Reggio (Italy)
"Phanagoria",#in Crimea
"Theodosia",#now Feodosiya (Ukraine) - in Crimea
"Alalia",#in Corsica
"Hyele",#also Elea
"Emporion",#in Spain
"Antipolis",#now Antibes (France)
"Kimmerikon",#in Ukraine (Crimea)
"-1"
)),
#Persia
((
"Parsa",#Persepolis
"Pathragada",# first Persian capital, founded by Cyrus. Ancient Pasargadae
"Ecbatana",#ancient Hamadan
"Sirajis",#also Shiraz
"Rhagae",
"Arbela",#ancient Arbil
"Balkh",#also Bactra
#"Samarkand",#capital of Sogdiana. Greeks called it Maracanda
"Margu",#ancient Merv
"Aspadana",#ancient Isfahan
"Tisfun",#Parthian capital
"Anshan",
"Verkana",
#"Pura",
#"Hecatompylos",
"Sirajis",
"Phrada",
"Gaba",
"Margu",
"Kangavar",
"Arzuhina",
"Syrinx",
"-1"
),(
#"Harmozia",#ancient Minab
"Armuza",
"Gogana",
"Sisidona",
"Taoce",
"Apostana",
"Pylora",
"Badis",
"Mosarna",
"Karbis",
"Rhizana",
"Canasida",
"-1"
),(
"Sparda",#Persian name for Sardis
"Tushpa",#modern Van (Turkey)
"Pteria",#in Turkey
"Gordion",#in Turkey
"Daskyleion",
"Pushpapura",#modern Peshawar (Afghanistan)
"Cunaxa",#in Iraq
"Erebuni",#modern Yerevan (Armenia)
"Gangra",#capital of Paphlagonia
"Perga",#in Turkey
"Buxarak",
"Kapisa",
"Ortospana",
"Cyreskhata",
"-1"
),(
"Tarshush",#"Tarsus",#capital of Cilicia
"Salamis",#in Cyprus
"Issus",
"-1"
)),
#Carthage
((
"Utica",
"Zama",
"Sicca",#(El Kef)
"Sarim Batim",#(Constantine, Algeria)
"Sitifis",#(Setif)
"-1"
),(
"Qart-Hadasht",#(Carthage)
"Hippo",#(Annaba)
"Kerkouane",
"Lpqy",
"Oea",#(Tripoli)
"Thapsus",
"Tingi",#(Tangier)
"Ikosim",#(Algiers)
"Rusadir",
"Tacape",
"Sabratha",
"Iol",#(Chercell)
"Tipasa",
"Lixus",
"Hadrametum",
"Thanae",
"-1"
),(
"Carmo",#(Carmona)
"Helmantica",#(Salamanca)
"Elibyrge",#(Grenada)
"-1"
),(
#"Malaka",#(Malaga)
"Gades",#(C&#225;diz)
"Ziz",#(Palermo)
"Sexi",#(Almu&#241;&#233;car)
"Abdera",
"Karalis",#(Cagliari)
"Olbia",
"Melita",#(Malta)
"Motya",
"Lilybaeum",
"Qart Hadasht",#(Nova Carthago)
"Sur", #Tyre
"Gebal", #Byblos
"Sidon",
"Arvad", #Arados
"-1"
)),
#Rome
((
"Roma",# founded 753 b.C.
"Arretium",# (Arezzo) founded IX century b.C., conquered 295 b.C.
#"Tarquinii",# (Tarquinia) conquered 281 b.C.
"Mediolanum",# (Milano) founded 600 b.C., conquered 222 b.C.
"Capua",# founded 800 b.C., annexed 343 b.C.
"Beneventum",# (Benevento) founded VII century b.C., conquered 268 b.C.
#"Faesulae",# (Fiesole) annexed III century b.C.
"Felsina",# – Bononia (Bologna) founded 534 b.C., conquered 189 b.C.
"Brixia",# (Brescia) founded VI century b.C., annexed 189 b.C.
"Parma",# founded VI century b.C., annexed 183 b.C.
"Perusia",# (Perugia) founded VI century b.C., annexed 89 b.C.
"Verona",# annexed 89 b.C.
"Placentia",# (Piacenza) founded 218 b.C.
"Ticinum",# (Pavia) founded 189 b.C.
"Forum Livii",#(Forlì) founded 188 b.C.
"Aquileia",#founded 181 b.C.
"Florentia",# (Firenze) founded 59 b.C.
"Augusta Taurinorum",#(Torino) founded 29 b.C.
"Augusta Praetoria",#(Aosta) founded 25 b.C.
"Cremona",
"-1"
),(
"Neapolis",# (Napoli) founded V century b.C., conquered 326 b.C.
#"Ostia",# founded 633 b.C.
"Rhegium",# (Reggio Calabria) founded VIII century b.C., annexed 341 b.C.
"Genua",# (Genova) founded XX century b.C., refounded 203 b.C.
"Pisae",# (Pisa) founded VI century b.C., annexed 180 b.C.
"Pompeii",
"Ravenna",
"Tarentum",# (Taranto) founded 706 b.C., conquered 272 b.C.
"Brundisium",# (Brindisi) founded ?, conquered 267 b.C.
"Ariminum",
"Antium",# (Anzio) annexed V century b.C.?
"Ancona",# founded 387 b.C., annexed 113 b.C.
"Hadria",
"Sipontum",
"-1"
),(
"Sirmium",
"Singidunum",
"Sardica",
"Aquincum",
"Aguntum",
#"Naissus",
"Aemona",
"Nicopolis",
"Hadrianopolis",
"Italica",# (206 BCE)
"Emerita Augusta",# (25 BCE)
"Bracara Augusta",# (20 BCE)
"Augusta Treverorum",# (16 BCE)
"Metellinum",# (80 BCE)
"Corinthiensis",# (44 BCE)
#"Lugdunum",# (43 BCE)
"Augusta Rauracorum",# (15 BCE)
"Augusta Vindelicorum",# (15 BCE)
"Augusta Suessionum",# (Augustus)
"Camulodunom",# (43 CE)
"Eboracum",# (71 CE)
"-1"
),(
"Dyrrachium",# (229 BCE)
"Colonia Iunonia",#/Carthago (122 BCE)
"Narbo Martius",# (118 BCE)
"Tarraco",# (?)
"Thapsus",# (46 BCE)
"Patras",# (Augustus)
"Nicomedia",
"Saguntum",
"Narbo",
"Salonae",
"Nicaea",
"Narona",
"Arelate",
#Nova Roma/Constantinopolis (330 CE)
"-1"
)),
#Japan
((
"Kyouto",# (capital, 6th century, originally Heian-kyo)
"Nara", #(710)
"Nagano",# (642)
"Fukushima",# (12th century)
"Yamaguchi",# (14th century)
"Matsumoto",# (15th century)
"Takayama",# (16th century)
"Morioka",# (1597)
"Nagaoka",# (1616)
"-1"
),(
"Edo",# (1457, Tokyo after 1603)
"Oosaka",# (3rd century)
"Fukuoka",# (ancient times)
"Kobe",# (3rd century)
"Kagoshima",# (14th century)
"Nagasaki",# (before 16th century)
"Hiroshima",# (1589)
"Sendai",# (1600)
"Nagoya",# (1610)
"Shimonoseki",# (18th century)
"Yokohama",# (19th century)
"-1"
),(
"Sapporo",# (late 19th century)
"Shinyou",# (ancient, Japanese after 1905, also Shenyang [Mukden is Manchurian])
"Toyohara",# (1905)
"-1"
),(
"Naha",# (ancient times)
"Hakodate",# (1454)
"Kushiro",# (1869)
"Otomari",# (1905)
"Keijo",# (conquered 1910, Japanese name for Seoul)
"-1"
)),
#Ethiopia
((
"Aksum",# - capital of the ancient country of Aksum (coincidentally).
"Yeha",# - may have been the capital of the D'mt kingdom (8th century BC).
"Hawulti",# - evidently an important city of the Aksumite kingdom.
"Qohaito",# - may have been Aksum's summer capital.
"Matara",# - major Aksumite city.
"Lalibela",# - either originally Roha or Adefa. Renamed after King Lalibela, who was born there. Second-holiest city in the country to Ethiopians after Aksum.
"Asmara",# - founded in the 12th century during Solomonic dynasty.
"Debre Berhan",# - founded by Zara Yakob as his capital (1456).
"Gondar",# - capital from 1635 until 1855.
"Adowa",# - gained importance in the 17th century as a trade route between Gonder and the coast.
"Makale",# - founded 13th century, not important until the 19th.
"Addis Ababa",# - founded 1886 by Menelik II.
"Dessye",# - founded 1882.
"Dire Dawa",# - founded 1902.
"-1"
),(
"Adulis",# - main port of Aksum. Now capital of Eritrea.
"Avalitis",# - modern Assab.
"Massawa",# - Overshadowed by Adulis most of its history.
"-1"
),(
"Saphar",# - Zafar, Yemen. Part of the Aksumite Kingdom at its height.
"Harerge",# - also Harar. Capital of the Islamic kingdom of Adal.
"Bonga",# - capital of the kingdom of Kaffa, 14th to 19th centuries.
"-1"
),(
"Muza",# - site in modern Saudi Arabia. Part of ancient Aksum.
"Zeila",# - capital of the sultanate of Ifat.
"Suakin",# - in Sudan.
"-1"
)),
#Maya
((
"Yax Mutal",#also Tik’al or Mutul
"Chich'en Itz&#225;",
"Xukpi",#also Cop&#225;n
"Oxhuitza",#also Caracol
#"El Mirador",#major pre-Classical site, 6th century BC to 1st century AD
"Uxmal",
"Lakamha", #"Palenque",
"Hux Witik",
"Uaxactun",
"Quirigu&#225;",
"Oxte'tuun", #"Calakmul",
"Izapa",#major pre-Classical site
"Seibal",
"Yokib",#also Piedras Negras
"Pa' Chan",#also Yaxchilan
"Maxam",#also Naranjo
"Bonampak",
"Dzibilchalt&#250;n",
"Chinkultic",
"Sayil",
"Edzn&#225;",#also Etzn&#225;
"Po'", #"Tonin&#225;",
"Kaminaljuyu",
"-1"
),(
"Tulum",#also Zama
"Lamanain",#major pre-Classical site, founded ca. 16th century BC
"Tayasal",#also Pet&#233;n Itz&#225; (on Lake Pet&#233;n Itz&#225;)
"Jaina",#island on the coast - Mayan town built there
"Cob&#225;",#on Lake Macanxoc
"Hochob",
"Lim Ni Punit",
"-1"
),(
"-1",
"-1"
),(
"-1",
"-1"
)),
#Vikings
((
"Birka",
"Viborg",
"Uppsala",
"Jelling",
"Roskilde",
"V&#228;ster&#229;s",
"S&#246;dert&#228;lje",
"Lund",
"Skien",
"Randers",
"Hedeby", #Haithabu
"Sigtuna",
"Schleswig",
"Skara",
"Link&#246;ping",
"&#214;rebro",
"Odense",
"&#197;lborg",
"-1"
),(
"Nidaros",
"Oslo",
"Stockholm",
"Bergen",
"Helsingborg",
"Kalmar",
"Stavanger",
"K&#248;benhavn",
"T&#248;nsberg",
"Ribe",
"&#197;rhus",
"Aalborg",
"Malm&#246;",
"Waterford",
"Swansea",
"Sarpsborg",
"Visby",
"K&#248;ge",
"K&#246;pingsvik",
"Kaupang"
"G&#246;teborg ",
"Trelleborg",
"Harstad",
"-1"
),(
"Cork",
"Limerick",
"Wexford",
"Skarðaborg",
"Grobina",#originally Grobin
"Holmg&#229;rd",
"Timerevo",
"-1"
),(
"Reykjavik",
"T&#243;rshavn",
"Vinland",
"Kirkwall",
"Klaksv&#237;k",
"Helluland",
"Markland",
"Hjaltland",
"Arklow",
"Brattahl&#237;ð",
"Hafnarfj&#246;rður",
"Reay",
"-1"
)),
#Arabia
((
"Makkah",
"Al-Madinah",
"Dimashq",
"Baghdad",
"Najran",
"Mosul",
"Ar-Riyad",
"Halab",
"Sanaa",
"Amman",
"-1"
),(
"Jeddah",
"Al-Basrah",
"Gaza",
"Beirut",
"Masqat",
"Aden",
"Al-Qatif",
"Abu-Dhabi",
"Dubai",
"Al-Kuwait",
"Ad-Dammam",
"Salalah",
"Jazan",
#"Sa&#239;da",#Sidon
"-1"
),(
"Aswan",
"Al Qayrawan",
"Fas",
"G&#225;rnata",
"Harar",
"Al-Khartum",
"Sabha",
"-1"
),(
#"Al-Iskhandariya",
"Al-Jazair",
"Tunis",
"Wahran",
"Dar-Beida",
"Rabbat",
#"Maqadishu",
"Zanji-bar",
"Tobruk",
"-1"
)),
#Khmer
((
"Angkor",
"Yasodharapura",# - first Khmer capital built at Angkor. Sanskrit translation: "Holy City", or "Capital City" by extension.
"Isanapura",# - capital of the Khmer kingdom of Chenla.
"Hariharalaya",# - another former capital.
"Sambhupura",# - captured by Jayavarman II. On the Mekong.
"Phnom Penh",# - current capital, after Koh Ker.
"Mahendraparvata",# - founded by Jayavarman II.
"Lovek",# - capital in the sixteenth century.
"Ba Phnom",
"Suryaparvata",
"Shrestapura",
"Aninditapura",#
"Pursat",
"Koh Ker",# - capital under Jayavarman IV and Hasavarman II.
"Phimai",# - also Pimai.
"Udong",
"Mahanokor",# - could also be Wat Nokor?
"Siem Reap",# - means "defeat of Siam".
"Beng Melea",# - Ancient Khmer city.
"Batdambang",# - founded in the 11th century.
"Lomphat",
"Kampong Svay",# - another ancient Khmer city.
"Kracheh",# - also called Krati&#233;.
"-1"
),(
"Prey Nokor",# - Now Ho Chi Minh City (Saigon). Main Khmer port until the 17th century.
"Chaudoc",# - Now in southern Vietnam.
"Kampot",#
"-1"
),(
"Klong Thom",# - supposedly in modern Thailand.
"-1"
),(
"Indrapura",# - Cham city conquered by the Khmer. Today's Dong Duong in Vietnam.
"Kauthara",# - Another Cham city captured by the Khmer, around 945. Now Nha Trang (Vietnam)
"-1"
)),
#Spain
((
"Madrid",
"Sevilla",
"Toledo",
"Zaragoza",
"Santiago",
"Salamanca",
"Pamplona",
"C&#243;rdoba",
"Granada",
"Badajoz",
"Le&#243;n",
"Oviedo",
"Vitoria",
"Bilbao",
"Albacete",
"Burgos",
"-1"
),(
"Barcelona",
"Valencia",
"La Coru&#241;a",
"Santander",
"Malaga",
"Alicante",
"Huelva",
"Almer&#237;a",
"Ceuta",
"Melilla",
"Tenerife",
"Ibiza",
"-1"
),(
"Guadalajara",
"La Paz",
"Medell&#237;n",
"Bogot&#225;",
"Monterrey",
"Villa Hermosa",
"Asunci&#243;n",
"Puebla",
"Chihuahua",
"Concepci&#243;n",
"Santa F&#233;",
"San Antonio",
"Hermosillo",
"Las Vegas",
"Rosario",
"-1"
),(
"Santo Domingo",
"La Habana",
"Veracruz",
"Lima",
"San Juan",
"Buenos Aires",
"Campeche",
"Caracas",
"Santa Marta",
"San Salvador",
"Guatemala",
"Cartagena de Indias",
"Montevideo",
#"Los Angeles",
"Sacremento",#(1839)
"San Diego",
"Villa Cisneros",#(Western Sahara)
"El Aai&#250;n",#(Western Sahara)
"-1"
)),
#France
((
"Paris",#(52 B.C.)
"Lyon",#(100 B.C.)
"Orl&#233;ans",
"Avignon",#(Roman Times)
"Reims",#(496 A.D.)
"Tours",
"Chartres",
"Toulouse",
"Angers",
"Rennes",
"Besan&#231;on",
"Dijon",
"Poitiers",
"Amiens",
"Metz",
"Clermont-Ferrand",
"Rouen",
"Limoges",
"-1"
),(
"Marseille",#(100-0 B.C.)
"Bordeaux",#(350 B.C.)
"Brest",
"Le Havre",
"Nantes",
"Nice",
"Toulon",
"Calais",
"La Rochelle",
"Montpellier",
"La Roche-sur-Yon",
"Saint-Nazaire",
"Caen",
"Perpignan",
"Biarritz",
"Dunkerque",
"-1"
),(
"Qu&#233;bec", #(1608)
"B&#226;ton-Rouge", #(1699)
"St.Louis", #(1703)
"Fort D&#233;troit", #(1701)
"Tadoussac", #(1599)
"Fort Toulouse", #(1717)
"Fort Niagara", #(1726)
"Fort Dauphin",
"Sault Ste-Marie", #(1668)
"Sa&#252;l", #
"Trois-Rivi&#232;res",
"Fort-Lamy",
"Bangui",
"-1"
),(
"Cayenne", #(1604)
"Port Royal", #(1605)
"Montr&#233;al", #(1642)
"Fort Caroline", #(1564)
"Nouvelle Orleans", #(1718)
"Fort-de-France", #(1638)
"Basse-Terre", #(1643)
"Mobile", #(1702)
"Biloxi", #(1699)
"Port-au-Prince", #(1749)
"Kourou",
"Libreville",
"Philippeville",
"Abidjan",
"Conakry",
"Pointe-&#224;-Pitre",
"Cap-Fran&#231;ais",
"Noum&#233;a", #(1864)
"Saint-Louis-du-S&#233;n&#233;gal",
"-1"
)),
#England
((
"York",# 71, Roman
"Oxford", #720
"Birmingham", #c. 600
"Manchester", #79, Roman
"Nottingham",#c. 550
"Coventry", #1043
"Newcastle",#120, Roman
"Glasgow", #c. 550; Scottish, not English
"Colchester", #(pre-Roman fortress of Cunobelin + Cassevellaunus and the Catuvellauni - also Rome's largest town in Britain until Boudicca offed it - still significant well into the middle ages, still bearing a Dutch Quarter from Tudor times),
"Lincoln", #c. 650
#The following cities are considerably less important than cities in the same geographic zone. They are back-ups roughly ranked according to modern-day signficance. I imagine in most game they will never be built
"Leeds",
"Bath", #43, Roman
"Cambridge", #40, Roman. Cambridge has an important university but is otherwise insignificant.
"Chelmsford", #(one of the largest towns in medieval England - temporary capital during the Peasant's Revolt)
"Leicester",
"Norwich", #c. 650
"Middlesbrough", #686
"Canterbury", #prehistoric. Only important in Anglo-Saxon times. Its Archbishopric hasn't given it any political or economic significance.
"Derby",
"Blackburn",
"Wolverhampton",
"-1"
),(
#The following cities are roughly ranked according to how close they are to London, in order to encourage an in-game settlement pattern that vaguely corresponds with real-world geography
"London",#43, Roman
"Southampton", #c 50, Roman
"Portsmouth", #1180
"Bristol",# 1000
#"Gloucester", #48, Roman
#"Exeter", #50, Roman
"Cardiff",#55, Roman; Welsh, not English
"Liverpool", #1207
"Edinburgh",#c. 600; Scottish
"Ipswich", #(rich Tudor port) c. 620
"King's Lynn", #(prestigious in Tudor England)
"Hull", #1150
"Plymouth", #1235
"Belfast",#1609; founded by English and Scottish settlers
"Falmouth", #Cornish Aberfal, became English in the 8th century.#(lesser known port which was fairly prominent in the Napoleonic era)
"Dundee",#prehistoric, Scottish
"Aberdeen", #c. 750; Scottish
"Inverness", #Scottish
#The following cities are considerably less important than cities in the same geographic zone. They are back-ups roughly ranked according to modern-day signficance. I imagine in most games they will never be built
"Ipswich",#c. 620,
"Brighton", #c. 1000
"Hastings", #pre-historic
"Aberystwyth", # Welsh
"Penzance", #(site of the Armada's landing - little else but still more historical than Blackpool)
"Blackpool",#c. 1500. This place has never been more than a holiday resort
"-1"
),(
#"Philadelphia", #1682, USA;
"Toronto", #1787, Canada
"Edmonton", #1790, Canada
"Ottawa", #1800, Canada
"Winnipeg", #1809, Canada
"Hamilton",#1815, Canada
"Ladysmith", #1850, South Africa; founded by Boers but annexed within a year
"Maseru",#1869, Lesotho
"Alice Springs", #c. 1870, Australia
"Kimberley", #1871, South Africa
"Upington",#1871, South Africa
"Regina",#1882, Canada
"Salisbury",#1890, capital of Zimbabwe
"Blantyre",#1891, Malawi
"Livingstone", #c. 1895, Zambia
"Nairobi",#1899, Nigeria
"Canberra",#1924 (date of first residents), Australia
"-1"
),(
"Jamestown",#1607, USA
#"Boston",#1630, USA
"Providence",#1636, USA
"Bridgetown",#1654, Barbados
"Kingston",#1692, Jamaica
#"Baltimore",#1729, USA
"Sydney",#1788, Australia
"Brisbane",#1824, Australia
"Melbourne",#1835, Australia
"Adelaide",#1837, Australia
"Wellington", #1839, New Zealand
"Auckland", #1840, New Zealand
"Christchurch", #1840, New Zealand
"Victoria", #1843, Canada
"Stanley", #1843, Falkland Islands
"Vancouver", #1863, Canada
"Port Elizabeth",#1820, South Africa
"Durban",#1824, South Africa
"Perth",#1829, Australia
"Darwin", #1869, Australia
"Port Moresby", #1873, Papua New Guinea
"Nassau",#c. 1650, Bahamas; originally "Charles Town"
"Bathurst",#1816, now Banjul, The Gambia
"Halifax",#1749, Canada
"Georgetown",# 1781, Guyana
"St. John's", #1632, Antigua
"Hobart",#1803, Australia
"-1"
)),
#Germany
((
"Berlin", #(1157)(Capital)
"Wien", #(200 B.C.)
"M&#252;nchen", #(1158)
"Frankfurt", #(794) there are two frankfurts in germany, one called "Frankfurt am Main" the second called "Frankfurt an der Oder", the first is the historic more important (imo)
"K&#246;ln",
"Prag", # cz: "Praha" , again added, i know this could lead to controversies, but it´s also the second city in the HRE list of BTS and one of the importants town in the HRE, and the capital of bohemia, the perhaps strongest kingdom in the early times of the HRE, also having kings of bohemia emperors of the HRE (eg. Charles IV) and also later a important part of the Habsburg Monarchy, almost becoming the third crown of the habsburger, if not included i would also vote for removing all now polish cities like Danzig, Ellbing, Breslau and the slovak capital Pressburg (Bratislava)
"Aachen", # (765) (HRE)
"Salzburg", #(700's)
"Dortmund", #(880)
"Stuttgart", #(950)
"Leipzig", #(1015)
"N&#252;rnburg", #(1050)
"D&#252;sseldorf", #(1135)
"Hannover", #(1200's)
"Dresden", #(1206)
"Essen", #(700's)
"Trier", #(16 BC) (considered as olderst german town)
"Mainz",
"Worms",
"Augsburg",
"Breslau", #(1000's), comment, see Prag
"Pressburg", #(1000's), comment, see Prag
"Magdeburg",
"W&#252;rzburg",
"Ulm",
"Karlsruhe",
"Halle",
"Potsdam",
"Luxemburg",
"Braunschweig",
"Schwerin",
"Goslar",
"Wittenberg", #officially "Lutherstadt Wittenberg"
"Klausenburg",
"-1"
),(
"Bremen", #(150)
"Hamburg", #(808)
"K&#246;nigsberg", #(1255)(Prussian Capital)(now Kaliningrad, Russia)
"L&#252;beck", #(700)
"Danzig", #(980), comment, see Prag
"Ellbing", #(890)(now Poland: Elblag), comment, see Prag
"Rostock", #(1000's)
"Oldenburg", #(1108)(low german: Ollnburg)
"Stralsund", #(1168)
"Greifswald", #(1199) fixed typo (ie -> ei)
"Kiel", #(1233)
"Wismar",# (1000)
"Stettin",
"Memel",
"Wilhelmshaven", #(1869)
"-1"
),(
"Weidmannsheil", #(1850)
"Wituland", #(1858)
"L&#252;deritzbucht", #(1883)
"Bismarckburg",
"Otjimbingwe", #(1849)
"Yaounde", #(1888)
"Bujumbura", #(1889)
"Kigali", #(1907)
"-1"
),(
"Klein Venedig", #(1529)
"Gro&#223; Friedrichsburg", #(1683)
"Krabbeninsel", #(1689)
"Tertholen", #(1696)
#"Bagamoyo", #(1700's)
"Sebeib", #(1884)
"Kaiser-Wilhelmsland", #(1884)
"Marshallinseln", #(1885)
"Swakopmund", #(1892)
"Helgoland", #the only island not in immediate vicinity to the mainland (formerly Danish and British), therefore called germanies only "high see" island
"Theresa", # Austrian Colony, one of the Nicobar islands
"Fort Jakob",#(1651)
"Neu Kurland",#(1654) The Duchy of Courland's colonies in the Gambia and Tobago
"Neu Schwabenland",
"Neu Braunfels",
"-1"
)),
#Russia
((
"Moskva",#1147 (Landlocked Capital)
"Novgorod",#950s or so
"Kiev",# - Really Damn Old
"Jaroslavl'",#1010 or so
"Tver'",# - 1164
"Smolensk",#863 or so
"Carycin",#1589
"Samara",#1586
"Tula",#1300s
"Vladimir",#1108 or so
"Perm'",#1647
"Pskov",#903 or so
"Voronezh",#1585
"Novosibirsk",
"Rostov",# 862 or so
"Kursk",
"Izhevsk",#1760
"Nizhnij Novgorod",# – 1221
"-1"
),(
"Sankt-Peterburg", # (Coastal Capital) – 1703
"Novokholmogory",#1584 Archangelsk
"Astrakhan'",
"Rostov-na-Donu",#1794
"Sevastopol'",# (now Ukrainian) 1783
"Odessa",# (ditto)
"Novorossijsk",# (Black Sea) – 1838
"Sochi", #1864
"Murmansk", #1916
#"Vladivostok",
"Petropavlovsk",# - Kamchatsky
"Magadan",
"Yalta",# (Ukrainian now)
"-1"
),(
"Jakutsk",# – 1632
"Ekaterinburg",# – 1723
"Irkutsk",# – 1652
"Khabarovsk",# – 1858
"Novosibirsk",# – 1893
"Cheljabinsk",# -1763
"Tobol'sk",# – 1585
"Tjumen'",# – 1586
"Tomsk",# – 1604
"Krasnojarsk",# – 1628
"Omsk",# – 1716
"Barnaul",# – 1730
"Kemerovo",# – 1918
"Vostok",#(Inland Antarctic station)
"Buyukly",#(inland Sakhalin)
"Yuzhno-Sakhalinsk",# (post WW2 name), oblast capital.
"-1"
),(
"Novoarkhangel'sk",# – 1804 (Alaska, major settlement)
"Vladivostok",# – 1860
"Okhotsk",# - 1643
"Voskresenskaja",# (Seward, under the USA) – 1793
"Konstantinovsky",# – 1793
"Slavorossija",# – 1796
"Fort Ross",#  – 1812
"Voskresenskaya",# (should shange to Seward when captured by USA)
"Pavlovskaya Gavan'",# (1792)
"Juzhno-Kuril'sk",# (Japanese name: Furukamappu)
"Port Chichagov",# – around 1800 (?)
"Korsakov",# (largest town, coastal) (Sakhalin)
"Alexandrovka",# (non-minor town) (Sakhalin)
"Kodiak",# (Alaska, major settlement)
"Unalaska",# (Alaska, major settlement)
"Mikhailovsk",# (Alaska, major settlement)
"Mirnyy",# (Coastal Antarctic stations)
"Molodyozhnaya",# (Coastal Antarctic stations)
"Novolazarevskaya",# (Coastal Antarctic stations)
"Magadan",# – 1930s
"Petropavlovsk–Kamchatskij",# – 1740
"-1"
)),
#Netherlands
((
"Utrecht",
"Nijmegen",
"Maastricht",
"Delft",
"Leiden",
"Haarlem",
"'s-Hertogenbosch",#also Den Bosch
"Deventer",
"Groningen",
"Leeuwarden",
"Breda",
"Eindhoven",
"Gouda",
"Alkmaar",
"Tilburg",
"-1"
),(
"Amsterdam",
"Rotterdam",
"'s-Gravenhage",# now Den Haag (=The Hague). Fierabras thinks 's-Gravenhage' fits better with the naming convention Rhye is using and that 's-Gravenhage (= the count's hedge) is more consistent with 's-Hertogenbosch (= the duke's forest), which is also known as Den Bosch.
"Den Helder",# (Historical important)
"Den Briel",# (Historical important)
"Veere",# (Historical important)
"Middelburg",# (Historical important, VOC HQ, currently non coastal)
"IJmuiden",
"Vlissingen",
"Terneuzen",
"Delfzijl",
"-1"
),(
"Bloemenfontein",
"Johannesburg",
"Windhoek",
"Pretoria",
"Stellenbosch",
"Fort Nassau",
"Fort Oranje",
"Fort Zeelandia", # (many costal colonies are named likewise)
"Noortwijck", # (New York area)
"-1"
),(
"Kaapstad", # (in RFC Kaapstadt)
"Nieuw Amsterdam", # (not only New York)
"Nieuw Rotterdam",
"Walvisbaai", # (= whale Bay)
"Batavia", # (= Djakatra)
"Oranjestad",
"Willemstad",
"Mauritsstad",
"Pietermaritzburg",
"Stabroek",
"Paramaribo",
"Deshima", # (artificial island in Japan in the 1600's, Dutch tradingpost until the 1800's, also 't eyland Schisma)
"-1"
)),
#Mali
((
"Timbuktu",
"Niani",# - the actual capital of Mali
"Kangaba",# - pre Malian Empire capital
"Jenne",#
"Gao",#
"Taghaza",#
"Walata",#
"Tadmekka",#
"Wadan",#
"Awdaghost",#
"Teodeni",#
"Bilma",#
"Agades",#
"Titchitt",#
"Kirina",#
"Takedda",#
"Kita",#
"Kulikoro",#
"Kumbi Saleh",# (G)
"Kukiya",# (S)
"Kitsina",#, also called Katsina (S)
"Kano",# (S)
"Zaria",# (S)
"Segu",# (S)
"Arawan",# (S)
"Hombori",# (S)
"Rano",# (S)
"Tondib",#i (S)
"Diara",# (S)
"Bamba",# (S)
"Bussa",# (S)
"Say",# (S)
"-1"
),(
"Accra",# (G)
"Nioro",# (G)
"-1"
),(
"-1",
"-1"
),(
"-1",
"-1"
)),
#Portugal
((
"Guimar&#227;es",
"Braga",
"Coimbra",
"Bragan&#231;a",
"&#201;vora",
#"Silves",
"Santar&#233;m",
"Leiria",
"Viseu",
"Lamego",
"Beja",
"Guarda",
"Covilh&#227;",
"M&#233;rtola", #( was once an important river harbor)
"Tomar",
"Alcoba&#231;a", 
"Portalegre", 
"Ponte de Lima", 
"Castelo Branco",
"Chaves", 
"Estremoz", 
"Castelo Branco",
"Tomar",
"-1"
),(
"Lisboa",
"Oporto",
"Silves", #(this, not Faro, was the original capital of Algarve and an important coastal city until its river became silted)
"Faro",
"Lagos",
"Set&#250;bal",
"Ponta Delgada",
"Funchal",
"Tavira",
"Aveiro",
"Alc&#225;cer do Sal", #(an old coastal city, eventually its harbor was transfered to Setúbal as the river's estuary became silted)
"Viana do Castelo",
"Figueira da Foz",
"Almada", 
"Caminha", 
"Sesimbra", 
"-1"
),(
"S&#227;o Paulo",
"S&#227;o Salvador",#(Congo)
"Diamantina",
"Vila Rica",
"Bel&#233;m",
"Ouro Preto",
"Tete",#(Mozambique)
"Huambo",#(Nova Lisboa, Angola)
"Cuiab&#225;",
"Cuito Cuanavale",#(Angola)
"Malv&#233;rnia",#(Mozambique)
"Vila Pery", #(Mozambique)
"Vila Junqueiro",#(Mozambique)
"Vila Cabral",#(Mozambique)
"S&#225; da Bandeira",#(Angola)
"Vila Luso",#(Angola)
"Cidade de Minas", #post-independence period?
"Manaus", #(Amazon River, might be considered part of the brazilian period)
"Oerias", #the capital of a state in the middle of Colonial Brazil
"Alpargatas",#An old city in the Northeast region
"-1"
),(
"Goa",#(pangim/panaji/panjim in India)
"Luanda",
"Rio de Janeiro",
"Porto Seguro",
"Recife",
"Macau",
"Arguim", #Mauretania
"S&#227;o Jorge da Mina", 
"Olinda", 
"Benguela", #Angola
"Quelimane", #Mozambique
"Mo&#231;ambique", #(island of)
"Angra do Hero&#237;smo", #(added)
"D&#237;li",# (in Timor-Leste)
#"Vit&#243;ria",
"Rio Grande de S&#227;o Pedro",#pampa in south brazil
"Bissau",#Guin&#233;-Bissau
"Louren&#231;o Marques",# (Maputo in Mo&#231;ambique)
"Dam&#227;o",# (Daman in India)
#Some important coastal cities, conquered/developed/occupied but not founded by the portuguese:
#"Ceuta", #(currently spanish)
#"Malaca", #(Malasia)
#"Ormuz", #(Hormuz in Iran)
"-1"
)),
#Inca
((
"Qusqu",
"Machu-Pikchu",
"Quitu",
"Ariqipaya",
"Wantar Chawin",# (oldest settlement in America, should be renamed as Chav&#237;n de Hu&#225;ntar if conquered by Spain))
"Kashamarka", #(Cajamarca)
"Huamanga",
"Willkapampa", #(should be renamed to Vilcabamba if conquered by Spain)
"Ullantaytanpu",
"Andahuailas",
"Waras", #(Huaraz)
"Tomebamba",
"Ku&#233;lap",
"-1"
),(
"Chan-Chan",
"Nazca",
"Tiyawanaku",# (used to be on Titicaca, but as close as what the original Incan knew as a sea)
"Tucume",
"Pachacamaq",
"Punu",# (on Titicaca, but as close as what the original Incan knew as a sea, should be renamed as Puno if conquered by Spain)
"-1"
),(
"-1",
"-1"
),(
"-1",
"-1"
)),
#Mongolia
((
"Kharakhorum",#- 1220
"Ulaanbaatar",# - 1639
"Ulaan-Ude",# (Ulan-Ude) -1666
"Samarqand",# - 700BC-ish, also on Persian city-list
"Bukhara",# - 500BC-ish, leveled by the Mongols in 1220
"Tashkent",# – 400BC-ish, leveled by the Mongols in 1219
"Kasg&#225;r",# – 76BC-ish
"Urumqi",# – founded by the Tang Dynasty in 0AD-ish, dubbed Urumqi in 1954
"Lhasa",# - 641AD–ish
"Hohhot",#- 1580
"Amarbayasgalant",# – 1727
"Chojbalsan",# – 1800s #Choybalsan
"Chahar",# – 1912
"Sukhbaatar",# - 1940
"Darkhan",# - 1961
"Erdenet",# - 1975
"-1"
),(
"Khovsgol",# - 1931
"Khalkh Gol",# - site of major fighting in 1939
"Olkhon",# - 1987
"Uvs Nuur",# - Lake, permanent settlement in 1930s
"Hulun Nuur",# - Lake, permanent settlement in 1930s
"-1"
),(
"Sarai Berke",# – 1245-ish
"Shine Sarai",# (New Sarai, which was separate, while Sarai Berke and Sarai Batu were probably the same city) – before 1395
"Kazan",# - mid 1400s
"Khem-Beldyr",# – 1914
"-1"
),(
"Khazaran",# - Between 600 and 1000AD
"Astrakhan",# - existed in the 1200s
"Elista",# – 1865
"-1"
)),
#Aztec
((
"Tenochtitlan",
"Texcoco",
"Tlacopan",#also called Tacuba
"Cholula",
"Azcapotzalco",
"Chalco",
"Xochimilco",
"Colhuacan",
"Teotihuacan",
"Tlatelolco",
"Matlatzinco",#also called Calixtlahuaca
"Tultitl&#225;n",
"Ixtapaluca",
"CuauhnAhuac",
"Mitla",
"Ecatepec",
"Malinalco",
"Xallapan",
"Huexotla",
"Tequixquiac",
"Tamu&#237;n",
"Mixquic",
"Coatlinchan",
"-1"
),(
"Cempoala",
"T&#250;xpam",
"Acapulco",
"-1"
),(
"-1",
"-1"
),(
"-1",
"-1"
)),
#Turkey
((
"S&#246;g&#252;t", #first capital
"Edirne",#(? by Greeks)
"Bursa",#(202 B.C. by Greeks)
"Konya",#(3000-1500 B.C.)
"Angora",#(1200 B.C.)(Current Capital)
"Erzurum",#(Ancient times)
"Eskisehir", #(1000 BC)
"Denizli",#(Prehistoric Times by Greeks)
"Kars",#(before 800)
"Ayintap",#(1500-1000 B.C.)
"Malatya",#(1400 B.C.)
"Diyar-i Bekr",#(1200 B.C.)
"Adana",#modern Antioch
"-1"
),(
"Istanbul",#(Capital)(founded 330 A.D. by Romans and 667 B.C. by Greeks)
"Izmir",#(1500 B.C.)
"Trabzon",#(756 B.C. by Greeks)
"Kayseri",
"Alanya",#(625 B.C.)
"Samsun",#(500 B.C. by Greeks)
"Iskenderun",#(333 B.C.)
"Antalya",#(150 B.C. by Greeks)
"Mersin",#(8000 B.C./1200 B.C.)
"Karadeniz Eregli",#(Ancient times by Greeks)
"Izmit",#(200BC) also called Nicomedia
"Bandirma",#(Recently)
"-1"
),(
"Varna",#Bulgaria, under Turkish rule for 400 years
"Sofya",#Sofia, Bulgaria, see Varna above
"B&#252;kres",#(1459). Bucharest.Under Ottoman influence until 1850s
"Temesvar",#Now Timisoara (Romania)
"Saraybosna",#(1461) Now Sarajevo
"Moha&#231;",#in Hungary
#"Budin",#Turkish name for Buda (now Budapest)
"Prizren",#major Ottoman city in Europe. Now in Kosovo
"-1"
),(
"Kefe",#also Caffa. Major Black Sea port
"Azak",#also called Azov
#"Benghazi",#in Libya
"Baku",#in Azerbaijan
"-1"
)),
#America
((
#+means initially founded by England
#++means initially founded by France
#+++means initially founded by Spain or Mexico
#++++means initially founded by the Netherlands
"Detroit",# ca 1701+
"Chicago",# ca 1770+
"Kansas City",# (1714)
"Pittsburgh",# ca 1758+
"Nashville",# (1779)
"Cincinnati",# ca 1788
"Buffalo",# ca 1789
"Cleveland",# ca 1796
"Indianapolis",# (1821)
"Atlanta",# ca 1837
"Minneapolis",#?(1837)
"Dallas",# ca 1841
"Salt Lake City",# ca 1847
"Denver",# ca 1858
"Duluth",# ca 1857
"Phoenix",# ca 1881
#"Las Vegas",# ca 1905
"-1"
),(
"Washington",# ca 1790 (capital)
"New York",# ca 1624++++ (also potentially an English settlement)
"Boston",# ca 1630+
"Philadelphia",# ca 1681+
#"New Orleans",# ca 1718 (potentially Spanish as well)
#"San Diego",# ca 1769+++
"Los Angeles",# ca 1771+++
"Jacksonville",#(1791)
"San Francisco",# ca 1776+++
"Miami",# ca 1825
"Houston",# ca 1837
"Portland",#(1843)(not on ocean but close enough)
"Oakland",#(1848)
"Seattle",# ca 1851
"Virginia Beach",
"-1"
),(
"Juneau",# (alaska) 1881
"Fairbanks",#(1903)
"Gamboa",#(1911, Panama)
"Camp Darby",#(Italy)
"Camp Ederle",#(Italy)
"Fort Gulick",#(Panama)
"Fort Sherman",#(Panama)
"Quarry Heights",#(Panama)
"Fort Clayton",#(Panama)
"Fort Kobbe",#(Panama)
"-1"
),(
"Saint Thomas",# ca 1657
"Guam",# ca 1668
"Monrovia",
"Freetown",
"American Samoa",#: ca 1830s
"Midway",#(1867)
"Honolulu",#: ca 1898 (Hawaii was annexed as a territory in 1898, although was arguably influenced/claimed by America earlier).
"Anchorage",#: ca 1914
"Unalaska",#(1933)
"Saipan",#(1986)
"Fort Amador",#(Panama)
"-1"
)))
    


class CityNameManager:  


        def getCityListsPointers( self, iCiv, j ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lCityListsPointers'][iCiv][j]

        def setCityListsPointers( self, iCiv, j, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lCityListsPointers'][iCiv][j] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )




        def assignName(self, city):
                """Names a city depending on its plot"""
                iOwner = city.getOwner()
                if (iOwner < iNumMajorPlayers):
                        #RFCRAND
                        cityX = city.getX()
                        cityY = city.getY()
                        iArea = 0;  # 0 = non-coastal; 1 = coastal; 2 = non-coastal in another continent; 3 = coastal in another continent
                        pCurrent = gc.getMap().plot( cityX, cityY )
                        ownersCapital = gc.getPlayer(iOwner).getCapitalCity()
                        dist = utils.calculateDistance(cityX, cityY, ownersCapital.getX(), ownersCapital.getY())
                        if ((pCurrent.area().getID() != ownersCapital.area().getID() and dist > CyMap().getGridWidth()/8) or dist > CyMap().getGridWidth()/4):
                                iArea = 2
                        if (city.isCoastal(7)):
                                iArea = iArea + 1
                        if (gc.getPlayer(iOwner).getNumCities() == 1 and tForceCapital[iOwner] != -1):
                                iArea = tForceCapital[iOwner]                                
                        #print('iArea', iArea)
                        cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                        
                        #if empty, check other lists before moving to the random list
                        if (cityName == "-1" and iArea == 0):
                                print('k')
                                iArea = 1
                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                if (cityName == "-1"):
                                        iArea = 2
                                        cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                        if (cityName == "-1"):
                                                iArea = 3
                                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                        elif (cityName == "-1" and iArea == 1):
                                iArea = 0
                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                if (cityName == "-1"):
                                        iArea = 3
                                        cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                        if (cityName == "-1"):
                                                iArea = 2
                                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                        elif (cityName == "-1" and iArea == 2):
                                iArea = 3
                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                if (cityName == "-1"):
                                        iArea = 0
                                        cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                        if (cityName == "-1"):
                                                iArea = 1
                                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                        elif (cityName == "-1" and iArea == 3):
                                iArea = 2
                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                if (cityName == "-1"):
                                        iArea = 1
                                        cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]
                                        if (cityName == "-1"):
                                                iArea = 0
                                                cityName = tCityLists[iOwner][iArea][self.getCityListsPointers(iOwner, iArea)]

                        if (cityName != "-1"):
                                city.setName(cityName, False)
                                self.setCityListsPointers(iOwner, iArea, self.getCityListsPointers(iOwner,iArea)+1)




        def renameCities(self, city, iNewOwner):
                """Renames a city depending on its owner"""

                sName = city.getName()

                if (iNewOwner == iEgypt):                                                        
                        if (sName == 'Yerushalayim' or sName == 'Aelia Capitolina' or sName == 'Urushalim' or sName == 'Hierousalem'):
                                city.setName('Aarru-Hetep', False)
                        elif (sName == 'Jerusalem' or sName == 'Qods' or sName == 'Kud&#252;s' or sName == 'Hierusalem'):
                                city.setName('Al-Quds', False)
                        elif sName == 'Qidshu':
                                city.setName('Kadesh', False)
                        elif sName == 'Elath':
                                city.setName('Etsion-Gaber', False)
                        elif (sName == 'Berenikis' or sName == 'Berenice' or sName == 'Hesperides' or sName == 'Bingazi' or sName == 'Benghazi'):
                                city.setName('Bangazi', False)
                        elif (sName == 'Khartoum' or sName == 'Hartum'):
                                city.setName('Al-Hartum', False)
                        elif (sName == 'Al-Iskandariya' or sName == 'Alexandria' or sName == 'Iskenderiye'):
                                city.setName('Eskendereyya', False)
                        elif (sName == 'Cairo' or sName == 'Al-Qahirah' or sName == 'Kahire'):
                                city.setName('El-Qahirah', False)
                        elif (sName == 'Al-Kharijah'):
                                city.setName('El-Kharijah', False)
                        elif (sName == 'Al-Uqsur' or sName == 'Luksor' or sName == 'Luxor'):
                                city.setName('El-Uqsur', False)
                        elif (sName == 'Al-Hartum'):
                                city.setName('El-Hartum', False)
                        elif (sName == 'Al-Jawf'):
                                city.setName('El-Jawf', False)
                        elif sName == 'Serabit Al-Khadem':
                                city.setName('Serabit El-Khadem', False)
                        elif (sName == 'Arae' or sName == 'Arae Philaenorum'):
                                city.setName('Ras Lanuf', False)
                        elif (sName == 'Anabucis' or sName == 'Automala' or sName == 'Al-Uqaylah'):
                                city.setName('El Agheila', False)
                                
                elif (iNewOwner == iIndia):       
                        if sName == 'Madras':
                                city.setName('Chennai', False)
                        elif sName == 'Coedeloer':
                                city.setName('Cuddalore', False)
                        elif (sName == 'Tranquebar' or sName == 'Trankebar'):
                                city.setName('Tharangambadi', False)
                        elif sName == 'Frederiksnagore':
                                city.setName('Serampore', False)
                        elif (sName == 'Pondicherry' or sName == 'Pondich&#233;ry'):
                                city.setName('Puducherry', False)
                        elif (sName == 'Bombay' or sName == 'Bombaim' or sName == 'Bonbei' or sName == 'Munbai'):
                                city.setName('Mumbai', False)
                        elif (sName == 'Debal' or sName == 'Mirat ul Memalik' or sName == 'Barbarikon' or sName == 'Barbaricum'):
                                city.setName('Kolachi', False)
                        elif (sName == 'New Delhi' or sName == 'Delhi' or sName == 'Deli'):
                                city.setName('Dilli', False)
                        elif (sName == 'Azimabad' or sName == 'Palibothra' or sName == 'Huazhicheng' or sName == 'Kashijou'):
                                city.setName('Patna', False) #Pataliputra
                        elif sName == 'Dacca':
                                city.setName('Dhaka', False)
                        #Khmer
                        elif sName == 'Da Nang':
                                city.setName('Indrapura', False)
                        elif sName == 'Qui Nhon':
                                city.setName('Vijaya', False)
                        elif sName == 'Phan Rang':
                                city.setName('Panduranga', False)
                        elif sName == 'Nha Trang':
                                city.setName('Kauthara', False)

                elif (iNewOwner == iChina): 
                        if (sName == 'Khanbaliq' or sName == 'Pekin' or sName == 'Hokkin'):
                                city.setName('Beijing', False)
                        elif sName == 'Shinkyo':
                                city.setName('Changchun', False)
                        elif (sName == 'Chach' or sName == 'Shash' or sName == 'Tashkent' or sName == 'Binkath'):
                                city.setName('Cheshih', False)
                        elif (sName == 'Seoul' or sName == 'Hanseong' or sName == 'Keijou' or sName == 'Seul'):
                                city.setName('Hancheng', False)
                        elif sName == 'Port Edward':
                                city.setName('Weihai', False)
                        elif (sName == 'Cant&#227;o' or sName == 'Canton' or sName == 'Koushuu'):
                                city.setName('Guangzhou', False)
                        elif (sName == 'Laoag' or sName == 'Raoagu'):
                                city.setName('Laowo', False)
                        elif (sName == 'Vladivostok' or sName == 'Urajio' or sName == 'Port May'):
                                city.setName('Fuladiwosituoke', False)
                        elif (sName == 'Singapura' or sName == 'Singapur' or sName == 'Singapore' or sName == 'Shounantou'):
                                city.setName('Xinjiapo', False)
                        elif (sName == 'Mukden' or sName == "Shin'you"):
                                city.setName('Shenyang', False)
                        elif (sName == 'Dilli' or sName == 'Delhi' or sName == 'New Delhi'):
                                city.setName('Deli', False)
                        elif (sName == 'Macao' or sName == 'Macau' or sName == 'Makao'):
                                city.setName('Aomen', False)
                        elif (sName == 'Hong Kong' or sName == 'Honkon' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Xianggang', False)
                        elif (sName == 'Takao' or sName == 'Kaohsiung'):
                                city.setName('Gaoxiong', False)
                        elif (sName == 'Taihoku'):
                                city.setName('Taibei', False)
                        elif (sName == "Dal'nij" or sName == 'Dairen'):
                                city.setName('Dalian', False)
                        elif (sName == 'Rome' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Roma'):
                                city.setName('Daqin', False)
                        elif (sName == 'Shanhai'):
                                city.setName('Shanghai', False)
                        elif (sName == 'Chichiharu'):
                                city.setName('Qiqihaer', False)
                        elif (sName == 'Fukushuu'):
                                city.setName('Fuzhou', False)
                        elif (sName == 'Seitou' or sName == 'Tsingtau'):
                                city.setName('Qingdao', False)
                        elif (sName == 'Chonjin'):
                                city.setName('Chongjin', False)
                        elif (sName == 'Uonsan' or sName == 'Genzan'):
                                city.setName('Wonsan', False)
                        elif (sName == 'Kinshuu' or sName == "Czin'chzhou"):
                                city.setName('Jinzhou', False)
                        elif (sName == 'Kuishuu'):
                                city.setName('Hangzhou', False)
                        elif (sName == 'Nankin'):
                                city.setName('Nanjing', False)
                        elif (sName == 'Kaihou'):
                                city.setName('Kaifeng', False)
                        elif (sName == 'Anyou'):
                                city.setName('Anyang', False)
                        elif (sName == 'Kyokufu'):
                                city.setName('Qufu', False)
                        elif (sName == 'Nanshou'):
                                city.setName('Nanchang', False)
                        elif (sName == 'Heihouku'):
                                city.setName('Pingfang', False)
                        elif (sName == 'Seian'):
                                city.setName("Xi'an", False)
                        elif (sName == 'Rakuyou'):
                                city.setName('Luoyang', False)
                        elif (sName == 'Chousa'):
                                city.setName('Changsha', False)
                        elif (sName == 'Jousai'):
                                city.setName('Chongqing', False)
                        elif (sName == 'Kyou'):
                                city.setName('Guiyang', False)
                        elif (sName == 'Nannei'):
                                city.setName('Nannei', False)
                        elif (sName == 'Konmei'):
                                city.setName('Kunming', False)
                        elif (sName == 'Ranshuu'):
                                city.setName('Lanzhou', False)
                        elif (sName == 'Anzan'):
                                city.setName('Anshan', False)
                        elif (sName == 'Seito'):
                                city.setName('Changdu', False)
                        elif (sName == 'Bukan'):
                                city.setName('Wuhan', False)
                        elif (sName == 'Hakuniuu'):
                                city.setName('Hegang', False)
                        elif (sName == 'Botankou' or sName == "Mudan'czjan"):
                                city.setName('Mudanjiang', False)
                        elif (sName == 'Pataliputra' or sName == 'Patna' or sName == 'Palibothra' or sName == 'Azimabad' or sName == 'Kashijou'):
                                city.setName('Huazhicheng', False)
                        elif (sName == 'Tsuuryou'):
                                city.setName('Tungliao', False)
                        elif (sName == 'Goshuu'):
                                city.setName('Wuzhow', False)
                        elif (sName == 'Shunsen' or sName == "Chunchkhon"):
                                city.setName('Chuncheon', False)
                        elif (sName == 'Fuzan'):
                                city.setName('Pusan', False)
                        elif (sName == 'Hakuryoku' or sName == 'Khabarovsk'):
                                city.setName('Boli', False)
                        elif (sName == 'Choukakou'):
                                city.setName('Zhangjiakou', False)
                        elif (sName == 'Nekka'):
                                city.setName('Jehol', False)
                        elif (sName == 'Hairaru' or sName == 'Hulun'):
                                city.setName('Hailaer', False)
                        elif (sName == 'Heijo' or sName == "Pkhen'jan"):
                                city.setName('Pyongyang', False)
                        #Japan
                        elif (sName == 'Oosaka'):
                                city.setName('Daban', False)
                        elif (sName == 'Edo' or sName == 'Toukyou' or sName == 'Tokio'):
                                city.setName('Jianghu', False)
                        elif (sName == 'Yokohama'):
                                city.setName('Hengbin', False)
                        elif (sName == 'Nagoya'):
                                city.setName('Mingguwu', False)
                        elif (sName == 'Sapporo'):
                                city.setName('Zahuang', False)
                        elif (sName == 'Kyouto' or sName == "Kioto"):
                                city.setName('Jingdu', False)
                        elif (sName == 'Niigata'):
                                city.setName('Xinxi', False)
                        elif (sName == 'Kushiro'):
                                city.setName('Chuanlu', False)
                        elif (sName == 'Kagoshima' or sName == "Kagosima"):
                                city.setName("Lu'erdao", False)
                        elif (sName == 'Akita'):
                                city.setName('Qiutian', False)
                        elif (sName == 'Hiroshima'):
                                city.setName('Guangdao', False)
                        elif (sName == 'Nagasaki'):
                                city.setName('Changqi', False)
                        elif (sName == 'Fukuoka'):
                                city.setName('Fugang', False)
                        elif (sName == 'Hakata'):
                                city.setName('Boduo', False)
                        elif (sName == 'Aomori'):
                                city.setName('Qingsen', False)
                        elif (sName == 'Toyohara'):
                                city.setName('Fengyuan', False)
                        elif (sName == 'Matsuyama'):
                                city.setName('Songshan', False)
                        elif (sName == 'Nagano'):
                                city.setName('Changye', False)
                        elif (sName == 'Sendai'):
                                city.setName('Xiantai', False)
                        elif (sName == 'Nara'):
                                city.setName('Nailiang', False)
                        #Khmer
                        elif sName == 'Indrapura':
                                city.setName('Da Nang', False)
                        elif sName == 'Vijaya':
                                city.setName('Qui Nhon', False)
                        elif sName == 'Panduranga':
                                city.setName('Phan Rang', False)
                        elif sName == 'Kauthara':
                                city.setName('Nha Trang', False)

                elif (iNewOwner == iBabylonia): 
                        if (sName == 'Shush' or sName == 'Seleukeia Susiana' or sName == 'Seleucia ad Eulaeum' or sName == 'Susa'):
                                city.setName('Shushan', False)
                        elif sName == 'Kadesh':
                                city.setName('Qidshu', False)
                        elif sName == 'Etsion-Gaber':
                                city.setName('Elath', False)
                        elif sName == 'Bagdat':
                                city.setName('Baghdad', False)
                        if (sName == 'Yerushalayim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Hierousalem' or sName == 'Hierusalem'):
                                city.setName('Urushalim', False)
                        elif (sName == 'Jerusalem' or sName == 'Qods' or sName == 'Kud&#252;s' or sName == 'Hierusalem'):
                                city.setName('Al-Quds', False)
                        elif (sName == 'Babirush' or sName == 'Babel' or sName == 'Babil' or sName == 'Babilon' or sName == 'Babylon' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babil&#251;', False)

                elif (iNewOwner == iPersia): 
                        if (sName == 'Ierusalim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Hierousalem'):
                                city.setName('Yerushalayim', False)
                        elif (sName == 'Jerusalem' or sName == 'Al-Quds' or sName == 'Kud&#252;s' or sName == 'Hierusalem'):
                                city.setName('Qods', False)
                        elif (sName == 'Shushan' or sName == 'Seleukeia Susiana' or sName == 'Seleucia ad Eulaeum' or sName == 'Susa'):
                                city.setName('Shush', False)
                        elif (sName == 'Marakanda' or sName == 'Samarkand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Samarqand', False)
                        elif sName == 'Rhagae':
                                city.setName('Ragha', False)
                        elif sName == 'Persepolis':
                                city.setName('Parsa', False)
                        elif sName == 'Pasargadae':
                                city.setName('Pathragada', False)
                        elif sName == 'Ecbatana':
                                city.setName('Hangmatana', False)
                        elif sName == 'Bactra':
                                city.setName('Bhakri', False)
                        elif sName == 'Ctesiphon':
                                city.setName('Tisfun', False)
                        elif sName == 'Zadrakarta':
                                city.setName('Tureng Tepe', False)
                        elif sName == 'Hekatompilos':
                                city.setName('Sauloe', False)
                        elif sName == 'Dur Untash':
                                city.setName('Chogha Zanbil', False)
                        elif sName == 'Tahran':
                                city.setName('Tehran', False)	
                        elif (sName == 'Babil&#251;' or sName == 'Babel' or sName == 'Babil' or sName == 'Babilon' or sName == 'Babylon' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babirush', False)
                        elif (sName == 'Pataliputra' or sName == 'Patna' or sName == 'Palibothra' or sName == 'Huazhicheng' or sName == 'Kashijou'):
                                city.setName('Azimabad', False)
                        elif sName == 'Bhagyanagar':
                                city.setName('Hyderabad', False)

                elif (iNewOwner == iGreece): 
                        if (sName == 'Niwt-Rst' or sName == 'Diospolis Magna'):
                                city.setName('Diospolis Megale', False)
                        elif sName == 'Per-Wadjet':
                                city.setName('Buto', False)
                        elif sName == 'Ineb Hedj':
                                city.setName('Memphis', False)
                        elif sName == 'Abdju':
                                city.setName('Abydos', False)
                        elif (sName == 'Iunu' or sName == 'Per-Atum'):
                                city.setName('Heliopolis', False)
                        elif sName == 'Yebu':
                                city.setName('Elephantine', False)
                        elif (sName == 'Sin' or sName == 'Sena' or sName == 'Pelusium'):
                                city.setName('Pelousion', False)
                        elif sName == 'Ragha':
                                city.setName('Rhagae', False)
                        elif sName == 'Tisfun':
                                city.setName('Ctesiphon', False)
                        elif sName == 'Parsa':
                                city.setName('Persepolis', False)
                        elif sName == 'Pathragada':
                                city.setName('Pasargadae', False)
                        elif (sName == 'Shushan' or sName == 'Shush' or sName == 'Seleucia ad Eulaeum' or sName == 'Susa'):
                                city.setName('Seleukeia Susiana', False)
                        elif (sName == 'Sur' or sName == 'Tyrus' or sName == 'As-Sur'):
                                city.setName('T&#253;ros', False)
                        elif sName == 'Lpqy':
                                city.setName('Lepcis', False)
                        elif sName == 'Lixus':
                                city.setName('Lixos', False)
                        elif (sName == 'Ziz' or sName == 'Panormus' or sName == 'Balharm' or sName == 'Palermo'):
                                city.setName('Panormos', False) 
                        elif (sName == 'Gadir' or sName == 'Qart-Gadir' or sName == 'Gades' or sName == 'Al-Qadiz' or sName == 'Cadix' or sName == 'C&#225;dis' or sName == 'C&#225;diz'):
                                city.setName('Gadeira', False)
                        elif (sName == 'Qart-Hadasht' or sName == 'Carthago'):
                                city.setName('Karkhedon', False) 
                        elif sName == 'Merv':
                                city.setName('Margiana', False)
                        elif sName == 'Ecbatana':
                                city.setName('Hangmatana', False)
                        elif (sName == 'Samarkand' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Marakanda', False)
                        elif (sName == 'Jerusalem' or sName == 'Yerushalayim' or sName == 'Kud&#252;s' or sName == 'Urshalim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Urushalim' or sName == 'Al-Quds' or sName == 'Qods' or sName == 'Hierusalem'):
                                city.setName('Hierousalem', False)
                        elif sName == 'Bhakri':
                                city.setName('Bactra', False)
                        elif (sName == 'Babil&#251;' or sName == 'Babel' or sName == 'Babil' or sName == 'Babilon' or sName == 'Babirush' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babylon', False)
                        elif sName == 'Sauloe':
                                city.setName('Hekatompilos', False)
                        elif sName == 'Tureng Tepe':
                                city.setName('Zadrakarta', False)
                        elif sName == 'Tisfun':
                                city.setName('Ctesiphon', False)
                        elif (sName == 'Massilia' or sName == 'Marseille' or sName == 'Marsella' or sName == 'Marsiliya'):
                                city.setName('Massalia', False)
                        elif sName == 'Dyrrachium':
                                city.setName('Epidamnos', False)
                        elif (sName == 'Athenae' or sName == 'Atina' or sName == 'Athen' or sName == 'Athens' or sName == 'Atenas' or sName == 'Ath&#232;nes'):
                                city.setName('Athenai', False)
                        elif (sName == 'Sparta' or sName == 'Esparta'):
                                city.setName('Sparte', False)
                        elif sName == 'Corinthus':
                                city.setName('Korinthos', False)
                        elif sName == 'Delphi':
                                city.setName('Delphoi', False)
                        elif sName == "Pi-Ramesses":
                                city.setName('Avaris', False)
                        elif sName == 'Djanet':
                                city.setName('Tanis', False)
                        elif sName == 'Attalea':
                                city.setName('Attaleia', False)
                        elif (sName == 'Anavarin' or sName == 'Navarino'):
                                city.setName('Neokastron', False)
                        elif sName == 'Inebahti':
                                city.setName('Naupactus', False)
                        elif sName == 'Gebal':
                                city.setName('Byblos', False)
                        elif sName == 'Paraetonium':
                                city.setName('Paraitonion', False)
                        elif sName == 'Cyrene':
                                city.setName('Kyrene', False)
                        elif sName == 'Syracusae':
                                city.setName('Syrakousai', False)
                        elif (sName == 'Moncastrum' or sName == 'Tiraspol' or sName == 'Akkerman' or sName == 'Wei&#223;enburg'):
                                city.setName('Tyras', False)
                        elif (sName == 'Miklagard' or sName == 'Bizantiya'):
                                city.setName('Byzantion', False) 
                        elif (sName == 'Qustantiniyah' or sName == 'Konstantinopel' or sName == 'Constantinopolis' or sName == 'Miklagard' or sName == 'Istanbul' or sName == "Konstantinopol'" or sName == "Car'grad" or sName == 'Stambul'):
                                city.setName('Konstantinoupolis', False) 
                        elif (sName == 'Trapezus' or sName == 'Tarabizun' or sName == 'Trabzon'):
                                city.setName('Trapezon', False)
                        elif (sName == 'Milid' or sName == 'Melitene' or sName == 'Malatya'):
                                city.setName('Malateia', False)
                        elif (sName == 'Mazaka' or sName == 'Caesarea Mazaca' or sName == 'Kayseri'):
                                city.setName('Kaisareia', False)
                        elif (sName == 'Karlsburg' or sName == 'Apulum' or sName == 'Balgrad'):
                                city.setName('Apulon', False)
                        elif (sName == 'Tomis' or sName == 'Konstanca' or sName == 'K&#246;stendsche' or sName == 'Kustendje'):
                                city.setName('Konstantia', False)
                        elif sName == 'Mycenae':
                                city.setName('Mykenai', False)
                        elif (sName == 'Kolachi' or sName == 'Debal' or sName == 'Barbaricum' or sName == 'Karachi' or sName == 'Mirat ul Memalik'):
                                city.setName('Barbarikon', False)
                        elif (sName == 'Chersonesus' or sName == 'Khersones'):
                                city.setName('Chersonesos', False) 
                        elif sName == 'Tiran':
                                city.setName('Tirana', False)
                        elif (sName == 'Venedig' or sName == 'Venise' or sName == 'Venecia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venetia', False)
                        elif (sName == 'Iadera' or sName == 'Zadar'):
                                city.setName('Zantar', False) 
                        elif (sName == 'Wien' or sName == 'Vena' or sName == 'Vindobona' or sName == 'Viyana'):
                                city.setName('Vienne', False)
                        elif (sName == 'Laibach' or sName == 'Ljubljana' or sName == 'Aemona Iulia'):
                                city.setName('Emona', False)
                        elif (sName == 'Split' or sName == 'Spalatum'):
                                city.setName('Aspalathos', False)
                        elif (sName == 'Beograd' or sName == 'Singidunum' or sName == 'Belgrad'):
                                city.setName('Singidun', False)
                        elif (sName == 'Dimitrof&#231;e' or sName == 'Sirmium' or sName == 'Syrmisch Mitrowitz' or sName == 'Sremska Mitrovica'):
                                city.setName('Sirmion', False)
                        elif (sName == 'Felicitas Julia' or sName == 'Allis Ubbo' or sName == "Al-'Ishbunah"):
                                city.setName('Olissipo', False)
                        elif (sName == 'Ninua' or sName == 'Ninova' or sName == 'Ninawa'):
                                city.setName('Nineve', False)
                        elif sName == 'Artashat':
                                city.setName('Artaxata', False)
                        elif (sName == 'Khalpe' or sName == 'Halab' or sName == 'Halep'):
                                city.setName('Beroea', False)
                        elif (sName == 'Al-Iskandariya' or sName == 'Alexandria' or sName == 'Iskenderiye' or sName == 'Eskendereyya'):
                                city.setName('Alexandreia', False)
                        elif sName == 'Zawty':
                                city.setName('Asyut', False)
                        elif sName == 'Nekhen':
                                city.setName('Hierakonpolis', False)
                        elif sName == 'Per-Bastet':
                                city.setName('Bubastis', False)
                        elif sName == 'Khmun':
                                city.setName('Hermopolis', False)
                        elif sName == 'Brundisium':
                                city.setName('Brentesion', False)
                        elif (sName == 'Pataliputra' or sName == 'Patna' or sName == 'Azimabad' or sName == 'Huazhicheng' or sName == 'Kashijou'):
                                city.setName('Palibothra', False)
                        elif (sName == 'Anabucis'):
                                city.setName('Automala', False)

                elif (iNewOwner == iCarthage): 
                        if (sName == 'Byblos' or sName == 'Jbeil'):
                                city.setName('Gebal', False)
                        elif (sName == 'Lepcis' or sName == 'Leptis Magna'):
                                city.setName('Lpqy', False)
                        elif (sName == 'Panormos' or sName == 'Panormus' or sName == 'Balharm' or sName == 'Palermo'):
                                city.setName('Ziz', False)  
                        elif (sName == 'Gades' or sName == 'Cad&#225;z' or sName == 'Gadeira' or sName == 'Al-Qadiz' or sName == 'Cadix' or sName == 'C&#225;dis'):
                                city.setName('Qart-Gadir', False)
                        elif (sName == 'Karkhedon' or sName == 'Qartaj' or sName == 'Kartaca' or sName == 'Carthago'):
                                city.setName('Qart-Hadasht', False) 
                        elif sName == 'Hippo Regius':
                                city.setName('Hippo', False)
                        elif sName == 'Iol Caesarea':
                                city.setName('Iol', False)
                        elif (sName == 'Regio Tripolitana' or sName == 'Tripolis'):
                                city.setName('Oea', False)
                        elif (sName == 'Felicitas Julia' or sName == 'Olissipo' or sName == "Al-'Ishbunah"):
                                city.setName('Allis Ubbo', False)

                elif (iNewOwner == iRome): 
                        if sName == 'Per-Wadjet':
                                city.setName('Buto', False)
                        elif sName == 'Abdju':
                                city.setName('Abydos', False)
                        elif (sName == 'Niwt-Rst' or sName == 'Diospolis Megale'):
                                city.setName('Diospolis Magna', False)
                        elif (sName == 'Sin' or sName == 'Sena' or sName == 'Pelusion'):
                                city.setName('Pelusium', False)
                        elif sName == 'Ineb Hedj':
                                city.setName('Memphis', False)
                        elif (sName == 'Iunu' or sName == 'Per-Atum'):
                                city.setName('Heliopolis', False)
                        elif sName == 'Yebu':
                                city.setName('Elephantine', False)
                        elif sName == 'Poseidonia':
                                city.setName('Paestum', False)
                        elif sName == 'Taras':
                                city.setName('Tarentum', False)
                        elif (sName == 'Rhegion' or sName == 'Riv&#224;h' or sName == 'R&#237;joles' or sName == 'Reggio') :
                                city.setName('Rhegium Julii', False)
                        elif (sName == 'Melpum' or sName == 'Mailand' or sName == 'Mil&#225;n' or sName == 'Milan'):
                                city.setName('Mediolanum', False)
                        elif (sName == 'Lutetia' or sName == 'Paris' or sName == 'Parijs'):
                                city.setName('Lutetia Parisiorum', False)
                        elif (sName == 'Burdeos' or sName == 'Bordeaux'):
                                city.setName('Burdigala', False)
                        elif sName == 'Tarragona':
                                city.setName('Tarraco', False)
                        elif (sName == 'Hippo' or sName == 'Annaba' or sName == 'B&#244;ne'):
                                city.setName('Hippo Regius', False)
                        elif (sName == 'Byzantion' or sName == 'Miklagard' or sName == 'Bizantiya' or sName == 'Konstantinoupolis' or sName == 'Qustantiniyah' or sName == 'Konstantinopel'  or sName == 'Istanbul' or sName == "Konstantinopol'" or sName == "Car'grad" or sName == 'Stambul'):
                                city.setName('Constantinopolis', False) 
                        elif (sName == 'Qart-Hadasht' or sName == 'Karkhedon'):
                                city.setName('Carthago', False)
                        elif sName == 'Qart Hadasht':
                                city.setName('Nova Carthago', False)
                        elif (sName == 'Ziz' or sName == 'Panormos' or sName == 'Balharm' or sName == 'Palermo'):
                                city.setName('Panormus', False)
                        elif sName == 'Iol':
                                city.setName('Iol Caesarea', False)
                        elif (sName == 'Gadir' or sName == 'Qart-Gadir' or sName == 'Gadeira' or sName == 'Al-Qadiz' or sName == 'Cadix' or sName == 'C&#225;dis' or sName == 'C&#225;diz'):
                                city.setName('Gades', False)
                        elif sName == 'Lpqy':
                                city.setName('Leptis Magna', False)
                        elif sName == 'Lixos':
                                city.setName('Lixus', False)
                        elif (sName == 'Yerushalayim' or sName == 'Ierusalim' or sName == 'Aarru-Hetep' or sName == 'Urushalim' or sName == 'Hierousalem'):
                                city.setName('Aelia Capitolina', False)
                        elif (sName == 'Jerusalem' or sName == 'Al-Quds' or sName == 'Qods' or sName == 'Urshalim' or sName == 'Kud&#252;s'):
                                city.setName('Hierusalem', False)
                        elif (sName == 'Babil&#251;' or sName == 'Babel' or sName == 'Babil' or sName == 'Babilon' or sName == 'Babirush' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babylon', False)
                        elif (sName == 'Shushan' or sName == 'Shush' or sName == 'Seleukeia Susiana' or sName == 'Susa'):
                                city.setName('Seleucia ad Eulaeum', False)
                        elif (sName == 'Sur' or sName == 'T&#253;ros' or sName == 'As-Sur'):
                                city.setName('Tyrus', False)
                        elif sName == 'Emporion':
                                city.setName('Emporiae', False)
                        elif sName == 'Odessos':
                                city.setName('Odessus', False)
                        elif sName == 'Naissos':
                                city.setName('Naissus', False)
                        elif sName == 'Berenikis':
                                city.setName('Berenice', False)
                        elif sName == 'Ikonion':
                                city.setName('Iconium', False)
                        elif sName == 'Ankyra':
                                city.setName('Ancyra', False)
                        elif sName == 'Antiokeia tes Pisidias':
                                city.setName('Antiochia Pisidiae', False)
                        elif sName == 'Antiokheia Megale':
                                city.setName('Antiochia ad Orontem', False)
                        elif sName == 'Halikarnassos':
                                city.setName('Halikarnassus', False)
                        elif sName == 'Ephesos':
                                city.setName('Ephesus', False)
                        elif sName == 'Ilion':
                                city.setName('Ilium', False)
                        elif (sName == 'Al-Iskandariya' or sName == 'Alexandreia' or sName == 'Iskenderiye' or sName == 'Eskendereyya'):
                                city.setName('Alexandria', False)
                        elif sName == 'Tisfun':
                                city.setName('Ctesiphon', False)
                        elif (sName == 'Massalia' or sName == 'Marseille' or sName == 'Marsella' or sName == 'Marsiliya'):
                                city.setName('Massilia', False)
                        elif sName == 'Epidamnos':
                                city.setName('Dyrrachium', False)
                        elif (sName == 'Athenai' or sName == 'Atina' or sName == 'Athen' or sName == 'Athens' or sName == 'Atenas' or sName == 'Ath&#232;nes'):
                                city.setName('Athenae', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif sName == 'Korinthos':
                                city.setName('Corinthus', False)
                        elif sName == 'Delphoi':
                                city.setName('Delphi', False)
                        elif (sName == 'Lyon' or sName == 'Lugodunon'):
                                city.setName('Lugdunum', False)
                        elif sName == "Pi-Ramesses":
                                city.setName('Avaris', False)
                        elif sName == 'Djanet':
                                city.setName('Tanis', False)
                        elif sName == 'Attaleia':
                                city.setName('Attalea', False)
                        elif (sName == 'Anavarin' or sName == 'Neokastron'):
                                city.setName('Navarino', False)
                        elif (sName == 'Laibach' or sName == 'Ljubljana' or sName == 'Emona'):
                                city.setName('Aemona Iulia', False)
                        elif (sName == 'Karlsburg' or sName == 'Apulon' or sName == 'Balgrad'):
                                city.setName('Apulum', False)
                        elif (sName == 'Napoca' or sName == 'Cluj-Napoca' or sName == 'Klausenburg' or sName == 'Kalosvar'):
                                city.setName('Castrum Clus', False)
                        elif sName == 'Gordion':
                                city.setName('Gordium', False)
                        elif sName == 'Paraitonion':
                                city.setName('Paraetonium', False)
                        elif sName == 'Kyrene':
                                city.setName('Cyrene', False)
                        elif sName == 'Syrakousai':
                                city.setName('Syracusae', False)
                        elif (sName == 'Tyras' or sName == 'Tiraspol' or sName == 'Akkerman' or sName == 'Wei&#223;enburg'):
                                city.setName('Moncastrum', False)
                        elif (sName == 'Trapezon' or sName == 'Tarabizun' or sName == 'Trabzon'):
                                city.setName('Trapezus', False)
                        elif (sName == 'Rome' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Roma', False)
                        elif sName == 'Amisos':
                                city.setName('Amisus', False)
                        elif (sName == 'Milid' or sName == 'Malateia' or sName == 'Malatya'):
                                city.setName('Melitene', False)
                        elif (sName == 'Mazaka' or sName == 'Kaisareia' or sName == 'Kayseri'):
                                city.setName('Caesarea Mazaca', False)
                        elif (sName == 'Aix-la-Chapelle' or sName == 'Aachen' or sName == 'Aken'):
                                city.setName('Aquisgranum', False)
                        elif (sName == 'Nijmegen' or sName == 'Nim&#232;gue'):
                                city.setName('Batavodurum', False)
                        elif (sName == 'Bambalunah' or sName == 'Pamplona' or sName == 'Pampelune'):
                                city.setName('Pompaelo', False)
                        elif (sName == 'Konstantia' or sName == 'Konstanca' or sName == 'K&#246;stendsche' or sName == 'Kustendje'):
                                city.setName('Tomis', False)
                        elif (sName == 'Wien' or sName == 'Vena' or sName == 'Vienne' or sName == 'Viyana'):
                                city.setName('Vindobona', False)
                        elif sName == 'Pise':
                                city.setName('Pisae', False)
                        elif (sName == 'Samarkand' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Marakanda', False)
                        elif (sName == 'Mainz' or sName == 'Mogontiacum' or sName == 'Mayence'):
                                city.setName('Moguntiacum', False)
                        elif (sName == 'Damasia' or sName == 'Augsburg'):
                                city.setName('Augusta Vindelicorum', False)
                        elif (sName == 'Agley' or sName == 'Oglej' or sName == 'Aquil&#233;e'):
                                city.setName('Aquileia', False)
                        elif (sName == 'Pompeji' or sName == 'Pompeya' or sName == 'Pomp&#233;i'):
                                city.setName('Pompeii', False)
                        elif sName == 'Oea':
                                city.setName('Tripolis', False)
                        elif (sName == 'Alexandreia ad Issum' or sName == 'Al-Iskandarun' or sName == 'Iskenderun'):
                                city.setName('Alexandretta', False)
                        elif (sName == 'Budapest' or sName == 'Budin' or sName == 'Ak Ink'):
                                city.setName('Aquincum', False)
                        elif sName == 'Mykenai':
                                city.setName('Mycenae', False)
                        elif (sName == 'Kolachi' or sName == 'Debal' or sName == 'Barbarikon' or sName == 'Karachi' or sName == 'Mirat ul Memalik'):
                                city.setName('Barbaricum', False)
                        elif sName == 'Santander':
                                city.setName('Victoriae Iuliobrigensium', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mexico' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexicopolis', False)
                        elif (sName == 'Chersonesos' or sName == 'Khersones'):
                                city.setName('Chersonesus', False) 
                        elif sName == 'Tiran':
                                city.setName('Tirana', False)
                        elif (sName == 'Burtuqal' or sName == 'Porto' or sName == 'Oporto'):
                                city.setName('Portus Cale', False)
                        elif (sName == 'Frankfurt' or sName == 'Francfort' or sName == 'Frankfort'):
                                city.setName('Bona Mansio', False)
                        elif (sName == 'Venedig' or sName == 'Venise' or sName == 'Venecia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venetia', False)
                        elif (sName == 'Zantar' or sName == 'Zadar'):
                                city.setName('Iadera', False) 
                        elif (sName == 'Split' or sName == 'Aspalathos'):
                                city.setName('Spalatum', False)
                        elif (sName == 'Beograd' or sName == 'Singidun' or sName == 'Belgrad'):
                                city.setName('Singidunum', False)
                        elif (sName == 'Dimitrof&#231;e' or sName == 'Sirmion' or sName == 'Syrmisch Mitrowitz' or sName == 'Sremska Mitrovica'):
                                city.setName('Sirmium', False)
                        elif (sName == 'Toledo' or sName == 'Tulaytulah'):
                                city.setName('Toletum', False)
                        elif (sName == 'Balansiyyah' or sName == 'Valencia' or sName == 'Valence'):
                                city.setName('Valentia', False)
                        elif (sName == 'Saraqustah' or sName == 'Zaragoza'):
                                city.setName('Caesaraugusta', False)
                        elif (sName == 'Faro' or sName == "'Uhshunubah"):
                                city.setName('Ossonoba', False)
                        elif (sName == 'Lisboa' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == "Al-'Ishbunah" or sName == 'Lisbonne' or sName == 'Lissabon' or sName == 'Lisbon'):
                                city.setName('Felicitas Julia', False)
                        elif sName == 'Sala':
                                city.setName('Sala Colonia', False)
                        elif (sName == 'Ninua' or sName == 'Ninova' or sName == 'Ninawa'):
                                city.setName('Nineve', False)
                        elif sName == 'Artashat':
                                city.setName('Artaxata', False)
                        elif (sName == 'C&#243;rdoba' or sName == 'Qurtuba' or sName == 'C&#243;rdova'):
                                city.setName('Corduba', False)
                        elif (sName == 'Hamburg' or sName == 'Hamborg' or sName == 'Hambourg'):
                                city.setName('Hamburgum', False)
                        elif (sName == 'Ajaccio'):
                                city.setName('Adiacium', False)
                        elif (sName == 'Berlin' or sName == 'Berlijn'):
                                city.setName('Berolinum', False)
                        elif sName == 'Zawty':
                                city.setName('Asyut', False)
                        elif sName == 'Nekhen':
                                city.setName('Hierakonpolis', False)
                        elif sName == 'Per-Bastet':
                                city.setName('Bubastis', False)
                        elif sName == 'Khmun':
                                city.setName('Hermopolis', False)
                        elif sName == 'Klagenfurt':
                                city.setName('Virunum', False)
                        elif sName == 'Gen&#232ve':
                                city.setName('Genava', False)
                        elif (sName == 'Brentesion' or sName == 'Brindisi'):
                                city.setName('Brundisium', False)
                        elif sName == 'Angers':
                                city.setName('Iuliomagus', False)
                        elif sName == 'Barion':
                                city.setName('Barium', False)
                        elif sName == 'Arae':
                                city.setName('Arae Philaenorum', False)
                        elif (sName == 'Automala'):
                                city.setName('Anabucis', False)
                        elif (sName == 'Hannover' or sName == 'Hanovre'):
                                city.setName('Hannovera', False)
                        elif (sName == 'Gdansk' or sName == 'Danswijk' or sName == 'Danzig'):
                                city.setName('Gedanum', False)
                        elif (sName == 'K&#246;nigsberg' or sName == 'Kaliningrad'):
                                city.setName('Calininopolis', False)
                        elif (sName == 'Warschau' or sName == 'Varsovia'):
                                city.setName('Warszawa', False)
                        elif (sName == 'Tallinn' or sName == 'Tallin' or sName == 'Revalia'):
                                city.setName('Reval', False)
                        elif (sName == 'Helsinki' or sName == 'Helsingfors' or sName == "Khel'sinki"):
                                city.setName('Helsingia', False)
                        elif (sName == 'Dresde' or sName == 'Dresden'):
                                city.setName('Dresda', False)
                        elif (sName == 'Rostock'):
                                city.setName('Rostochium', False)
                        elif (sName == 'Krakau' or sName == 'Krak&#243;w'):
                                city.setName('Cracovia', False)
                        elif sName == ('Colonia Agrippina' or sName == 'Keulen'):
                                city.setName('K&#246;ln', False)

                elif (iNewOwner == iJapan): 
                        if (sName == 'Daban'):
                                city.setName('Oosaka', False)
                        elif (sName == 'Jianghu' or sName == 'Tokio'):
                                city.setName('Toukyou', False)  #Edo?
                        elif (sName == 'Hengbin'):
                                city.setName('Yokohama', False)
                        elif (sName == 'Mingguwu'):
                                city.setName('Nagoya', False)
                        elif (sName == 'Zahuang'):
                                city.setName('Sapporo', False)
                        elif (sName == 'Jingdu' or sName == "Kioto"):
                                city.setName('Kyouto', False)
                        elif (sName == 'Xinxi'):
                                city.setName('Niigata', False)
                        elif (sName == 'Chuanlu'):
                                city.setName('Kushiro', False)
                        elif (sName == "Lu'erdao" or sName == "Kagosima"):
                                city.setName('Kagoshima', False)
                        elif (sName == 'Qiutian'):
                                city.setName('Akita', False)
                        elif (sName == 'Guangdao'):
                                city.setName('Hiroshima', False)
                        elif (sName == 'Changqi'):
                                city.setName('Nagasaki', False)
                        elif (sName == 'Fugang'):
                                city.setName('Fukuoka', False)
                        elif (sName == 'Boduo'):
                                city.setName('Hakata', False)
                        elif (sName == 'Qingsen'):
                                city.setName('Aomori', False)
                        elif (sName == 'Fengyuan'):
                                city.setName('Toyohara', False)
                        elif (sName == 'Songshan'):
                                city.setName('Matsuyama', False)
                        elif (sName == 'Changye'):
                                city.setName('Nagano', False)
                        elif (sName == 'Xiantai'):
                                city.setName('Sendai', False)
                        elif (sName == 'Nailiang'):
                                city.setName('Nara', False)
                        #gaikoku
                        elif (sName == 'Pyongyang' or sName == "Pkhen'jan"):
                                city.setName('Heijo', False)
                        elif (sName == 'Seoul' or sName == 'Hanseong' or sName == 'Hancheng' or sName == 'Seul'):
                                city.setName('Keijou', False)
                        elif sName == 'Changchun':
                                city.setName('Shinkyo', False)
                        elif (sName == 'Vladivostok' or sName == 'Haishenwai' or sName == 'Fuladiwosituoke' or sName == 'Port May'):
                                city.setName('Urajio', False)
                        elif (sName == 'Khanbaliq' or sName == 'Beijing' or sName == 'Pekin'):
                                city.setName('Hokkin', False)
                        elif (sName == "Juzhno-Kuri'lsk"):
                                city.setName('Furukamappu', False)								
                        elif (sName == "Dal'nij" or sName == 'Dalian' or sName == 'Sanshan'):
                                city.setName('Dairen', False)
                        elif (sName == 'Shanghai'):
                                city.setName('Shanhai', False)
                        elif (sName == 'Qiqihaer'):
                                city.setName('Chichiharu', False)
                        elif (sName == 'Fuzhou'):
                                city.setName('Fukushuu', False)
                        elif (sName == 'Qingdao' or sName == 'Tsingtau'):
                                city.setName('Seitou', False)
                        elif (sName == 'Chongjin'):
                                city.setName('Seishin', False)
                        elif (sName == 'Wonsan'):
                                city.setName('Genzan', False)
                        elif (sName == 'Jinzhou' or sName == "Czin'chzhou"):
                                city.setName('Kinshuu', False)
                        elif (sName == 'Hangzhou'):
                                city.setName('Kuishuu', False)
                        elif (sName == 'Guangzhou' or sName == 'Cant&#227;o' or sName == 'Canton'):
                                city.setName('Koushuu', False)
                        elif (sName == 'Nanjing'):
                                city.setName('Nankin', False)
                        elif (sName == 'Kaifeng'):
                                city.setName('Kaihou', False)
                        elif (sName == 'Anyang'):
                                city.setName("An'you", False)
                        elif (sName == 'Haojing' or sName == 'Macau' or sName == 'Aomen' or sName == 'Macao'):
                                city.setName('Makao', False)
                        elif (sName == 'Qufu'):
                                city.setName('Kyokufu', False)
                        elif (sName == 'Hong Kong' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Honkon', False)
                        elif (sName == 'Nanchang'):
                                city.setName('Nanshou', False)
                        elif (sName == 'Pingfang'):
                                city.setName('Heihouku', False)
                        elif (sName == "Chang'an" or sName == "Xi'an"):
                                city.setName('Seian', False)
                        elif (sName == 'Luoyang'):
                                city.setName('Rakuyou', False)
                        elif (sName == 'Changsha'):
                                city.setName('Chousa', False)
                        elif (sName == 'Chongqing'):
                                city.setName('Jousai', False)
                        elif (sName == 'Guiyang'):
                                city.setName('Kyou', False)
                        elif (sName == 'Shenyang' or sName == 'Mukden'):
                                city.setName("Shin'you", False)
                        elif (sName == 'Nanning'):
                                city.setName('Nannei', False)
                        elif (sName == 'Kunming'):
                                city.setName('Konmei', False)
                        elif (sName == 'Lanzhou'):
                                city.setName('Ranshuu', False)
                        elif (sName == 'Anshan'):
                                city.setName('Anzan', False)
                        elif (sName == 'Changdu'):
                                city.setName('Seito', False)
                        elif (sName == 'Wuhan'):
                                city.setName('Bukan', False)
                        elif (sName == 'Davao'):
                                city.setName('Dabao', False)
                        elif (sName == 'Jayakarta' or sName == 'Batavia'):
                                city.setName('Jakaruta', False)
                        elif (sName == 'Manila'):
                                city.setName('Manira', False)
                        elif (sName == 'Laoag' or sName == 'Laowo'):
                                city.setName('Raoagu', False)
                        elif (sName == 'Korsakov'):
                                city.setName('Otomari', False)
                        elif (sName == 'Kaohsiung' or sName == 'Gaoxiong'):
                                city.setName('Takao', False)
                        elif (sName == 'Taibei'):
                                city.setName('Taihoku', False)
                        elif (sName == 'Hegang'):
                                city.setName('Hakuniuu', False)
                        elif (sName == 'Mudanjiang' or sName == "Mudan'czjan"):
                                city.setName('Botankou', False)
                        elif (sName == 'Singapura' or sName == 'Xinjiapo' or sName == 'Singapur' or sName == 'Singapore'):
                                city.setName('Shounantou', False)
                        elif (sName == 'Chuncheon' or sName == "Chunchkhon"):
                                city.setName('Shunsen', False)
                        elif (sName == 'Pusan'):
                                city.setName('Fuzan', False)
                        elif (sName == 'Boli' or sName == 'Khabarovsk'):
                                city.setName('Hakuryoku', False)
                        elif (sName == 'Zhangjiakou'):
                                city.setName('Choukakou', False)
                        elif (sName == 'Jehol'):
                                city.setName('Nekka', False)
                        elif (sName == 'Hailaer' or sName == 'Hulun'):
                                city.setName('Hairaru', False)
                        elif (sName == 'Jakutsk'):
                                city.setName('Yakuttsuku', False)
                        elif (sName == 'San Francisco' or sName == 'San-Francisko'):
                                city.setName('Sanfuranshisuko', False)
                        elif (sName == 'Vancouver' or sName == 'Vankuver'):
                                city.setName('Bankuubaa', False)
                        elif (sName == 'Seattle' or sName == 'Siehtl'):
                                city.setName('Shiatoru', False)
                        elif (sName == 'Los-Andzheles' or sName == 'Los Angeles'):
                                city.setName('Rosu', False)
                        elif (sName == 'Washington' or sName == 'Vashington'):
                                city.setName('Washinton', False)
                        elif (sName == 'Nieuw Amsterdam' or sName == 'New York' or sName == "N'yu-York"):
                                city.setName('Nyuu Yooku', False)
                        elif (sName == 'Pataliputra' or sName == 'Patna' or sName == 'Palibothra' or sName == 'Huazhicheng' or sName == 'Azimabad'):
                                city.setName('Kashijou', False)
                        elif (sName == 'Fort Dauphin' or sName == 'Tolanaro'):
                                city.setName('Toranaro', False)
                        elif (sName == 'Quelimane'):
                                city.setName('Kerimane', False)
                        elif (sName == 'Sofala'):
                                city.setName('Sofara', False)
                        elif (sName == 'Dilli' or sName == 'Delhi' or sName == 'New Delhi' or sName == 'Deli'):
                                city.setName('Derii', False)
                        elif (sName == 'Bombay' or sName == 'Bombaim'):
                                city.setName('Bonbei', False)
                        elif (sName == 'Mumbai'):
                                city.setName('Munbai', False)
                        elif (sName == "Juzhno-Kuril'sk"):
                                city.setName('Furukamappu', False)
                        elif (sName == "Kusiro"):
                                city.setName("Kushiro", False)
                        elif (sName == "Khakodate"):
                                city.setName("Hakodate", False)
                        elif (sName == "Nakha"):
                                city.setName("Naha", False)

                elif (iNewOwner == iEthiopia): 
                        if sName == 'Maqadishu':
                                city.setName('Muqdisho', False)
                        elif (sName == 'Fort Gouraud'):
                                city.setName('Fderik', False)
                        elif (sName == 'Fort Polignac'):
                                city.setName('Illizi', False)
                        elif (sName == 'Salisbury'):
                                city.setName('Harare', False)

                elif (iNewOwner == iVikings): 
                        if (sName == 'Byzantion' or sName == 'Constantinopolis' or sName == 'Konstantinoupolis' or sName == 'Istanbul' or sName == 'Konstantinopel' or sName == "Konstantinopol'" or sName == "Car'grad" or sName == 'Stambul'):
                                city.setName('Miklagard', False)
                        elif sName == 'Gothenburg':
                                city.setName('G&#246;teborg', False)
                        elif (sName == 'Dublin' or sName == '&#193;th Cliath'):
                                city.setName('Dubh Linn', False)
                        elif sName == 'Staraja Lagoda':
                                city.setName('Aldeigjuborg', False)
                        elif (sName == 'Nowgorod' or sName == 'Novgorod'):
                                city.setName('Holmg&#229;rd', False)
                        elif sName == 'Staraja Lagoda':
                                city.setName('Kiev', False)
                        elif sName == 'Derby':
                                city.setName('Deoraby', False)
                        elif sName == 'York':
                                city.setName('J&#243;rvik', False)
                        elif sName == 'Kirkwall':
                                city.setName('Kirkjuvagr', False)
                        elif (sName == 'Kopenhagen' or sName == 'Copenhagen' or sName == 'Copenhague' or sName == 'Hafnia'):
                                city.setName('Kj&#248;bmandehavn', False)
                        elif (sName == 'Hedeby' or sName == 'Haithabu'):
                                city.setName('Heithabyr', False)
                        elif (sName == 'Anse-aux-M&#233;duses' or sName == 'Anse aux Meadows'):
                                city.setName('Vinland', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexico', False)
                        elif (sName == 'Havana' or sName == 'La Havane' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('Havanna', False)
                        elif sName == 'Wilmington':
                                city.setName('Fort Kristina', False)
                        elif (sName == 'Nueva Orleans' or sName == 'Nouvelle Orl&#233;ans' or sName == 'Nova Orle&#227;es'):
                                city.setName('New Orleans', False)
                        elif sName == 'Saint Thomas':
                                city.setName('Sankt Thomas', False)
                        elif sName == 'Wiborg':
                                city.setName('Vyborg', False)
                        elif (sName == 'Helsinki' or sName == "Khel'sinki" or sName == 'Helsingia'):
                                city.setName('Helsingfors', False)
                        elif (sName == 'Tharangambadi' or sName == 'Tranquebar'):
                                city.setName('Trankebar', False)
                        elif sName == 'Serampore':
                                city.setName('Frederiksnagore', False)
                        elif sName == 'Osu':
                                city.setName('Fort Christiansborg', False)
                        elif sName == 'Keta':
                                city.setName('Fort Prinsensten', False)
                        elif sName == 'Takoradi':
                                city.setName('Fort Witsten', False)
                        elif (sName == 'Venetia' or sName == 'Venise' or sName == 'Venecia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venedig', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif (sName == 'Tallinn' or sName == 'Tallin' or sName == 'Revalia'):
                                city.setName('Reval', False)

                elif (iNewOwner == iArabia): 
                        if (sName == 'Jerusalem' or sName == 'Yerushalayim' or sName == 'Ierusalim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Kud&#252;s' or sName == 'Hierusalem' or sName == 'Urushalim' or sName == 'Qods' or sName == 'Hierousalem'): 
                                city.setName('Al-Quds', False)
                        elif (sName == 'Tingi' or sName == 'Tanger' or sName == 'T&#225;nger'):
                                city.setName('Tanja', False)
                        elif sName == 'Pax Iulia':
                                city.setName('Beja', False)
                        elif (sName == 'Lisboa' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == 'Felicitas Julia' or sName == 'Lisbonne' or sName == 'Lissabon' or sName == 'Lisbon'):
                                city.setName("Al-'Ishbunah", False)
                        elif (sName == 'Hippo' or sName == 'Hippo Regius' or sName == 'B&#244;ne'):
                                city.setName('Annaba', False)
                        elif (sName == 'Margiana' or sName == 'Margus'):
                                city.setName('Merv', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tripoli' or sName == 'Tripolis' or sName == 'Trablus'):
                                city.setName('Tarabulus', False)
                        elif sName == 'Cirta':
                                city.setName('Qusantinah', False)
                        elif sName == 'Damaskos':
                                city.setName('Dimashq', False)
                        elif (sName == 'Berenikis' or sName == 'Berenice' or sName == 'Hesperides' or sName == 'Bingazi' or sName == 'Benghazi'):
                                city.setName('Bangazi', False)
                        elif sName == 'Siwa':
                                city.setName('Siwah', False)
                        elif (sName == 'Ziz' or sName == 'Panormos' or sName == 'Panormus' or sName == 'Palermo'):
                                city.setName('Balharm', False)
                        elif sName == 'Kabura':
                                city.setName('Kabul', False)
                        elif sName == 'Bhakri':
                                city.setName('Balkh', False)
                        elif sName == 'Neyshabur':
                                city.setName('Nishapur', False)
                        elif sName == 'Hangmatana':
                                city.setName('Hamadan', False)
                        elif (sName == 'Marakanda' or sName == 'Samarkand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Samarqand', False)
                        elif sName == 'Casablanca':
                                city.setName('Dar Beida', False)
                        elif sName == 'S.Cruz de Mar Peque&#241;a':
                                city.setName('Sidi Ifni', False)
                        elif (sName == 'Sur' or sName == 'T&#253;ros' or sName == 'Tyrus'):
                                city.setName('As-Sur', False)
                        elif (sName == 'Cairo' or sName == 'Memphis' or sName == 'Ineb Hedj' or sName == 'Kahire'):
                                city.setName('Al-Qahirah', False)
                        elif (sName == "Pi-Ramesses" or sName == 'Avaris'):
                                city.setName("Tell El-Dab'a", False)
                        elif (sName == 'Djanet' or sName == 'Tanis'):
                                city.setName('San El-Hagar', False)
                        elif sName == 'Akabe':
                                city.setName('Al-Aqabah', False)
                        elif sName == 'Musul':
                                city.setName('Mosul', False)
                        elif (sName == 'Halep' or sName == 'Aleppo'):
                                city.setName('Halab', False)
                        elif (sName == 'Cezayir' or sName == 'Alger'):
                                city.setName('Al-Jazair', False)
                        elif sName == 'Tunus':
                                city.setName('Tunis', False)
                        elif (sName == 'Iskenderiye' or sName == 'Alexandreia' or sName == 'Alexandria' or sName == 'Eskendereyya'):
                                city.setName('Al-Iskandariya', False)
                        elif sName == 'Sam':
                                city.setName('Dimashq', False)
                        elif (sName == 'Mekke' or sName == 'Mecca'):
                                city.setName('Makkah', False)
                        elif sName == 'Medine':
                                city.setName('Madinah', False)
                        elif sName == 'Bagdat':
                                city.setName('Baghdad', False)
                        elif (sName == 'Byblos' or sName == 'Gebal'):
                                city.setName('Jbeil', False)
                        elif sName == 'Hippo Diarrhytus':
                                city.setName('Binzart', False)
                        elif sName == 'Kandahar':
                                city.setName('Qandahar', False)
                        elif (sName == 'Ninua' or sName == 'Ninova' or sName == 'Nineve'):
                                city.setName('Ninawa', False)
                        elif sName == 'Kalhu':
                                city.setName('Nimrud', False)
                        elif (sName == 'Qart-Hadasht' or sName == 'Kartaca' or sName == 'Karkhedon' or sName == 'Carthago'):
                                city.setName('Qartaj', False)
                        elif (sName == 'Babil&#251;' or sName == 'Babel' or sName == 'Babylon' or sName == 'Babilon' or sName == 'Babirush' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babil', False)
                        elif (sName == 'Sin' or sName == 'Sena' or sName == 'Pelusium' or sName == 'Pelusion'):
                                city.setName('Tell El-Farama', False)
                        elif (sName == 'Buto' or sName == 'Per-Wadjet'):
                                city.setName('Kem Kasir', False)
                        elif (sName == 'Kadesh' or sName == 'Qidshu'):
                                city.setName('Tell Nebi Mend', False)
                        elif sName == 'Serabit':
                                city.setName('Serabit Al-Khadem', False)
                        elif (sName == 'Paraetonium' or sName == 'Paraitonion'):
                                city.setName('Marsa Matruh', False)
                        elif sName == 'Xou':
                                city.setName('Sakha', False)
                        elif (sName == 'Etsion-Gaber' or sName == 'Elath'):
                                city.setName('Umm Rashrash', False)
                        elif (sName == 'Per-Wadjet' or sName == 'Buto'):
                                city.setName('Kem Kasir', False)
                        elif (sName == 'Niwt-Rst' or sName == 'Diospolis Megale' or sName == 'Diospolis Magna' or sName == 'Luksor' or sName == 'Luxor'):
                                city.setName('Al-Uqsur', False)
                        elif (sName == 'Per-Atum' or sName == 'Heliopolis'):
                                city.setName('Tell-Hisn', False)
                        elif sName == 'Mut':
                                city.setName('Mut al-Khorab', False)
                        elif sName == 'Kumma':
                                city.setName('Semna', False)
                        elif (sName == 'Malaka' or sName == 'M&#225;laga'):
                                city.setName('Malaqah', False)
                        elif (sName == 'Byzantion' or sName == 'Miklagard'):
                                city.setName('Bizantiya', False)
                        elif (sName == 'Constantinopolis' or sName == 'Konstantinoupolis' or sName == 'Konstantinopel' or sName == "Konstantinopol'" or sName == "Car'grad"):
                                city.setName('Qustantiniyah', False)
                        elif (sName == 'Rusadir' or sName == 'Melilla'):
                                city.setName('Maliliyah', False)
                        elif (sName == 'Angora' or sName == 'Ankyra' or sName == 'Ancyra' or sName == 'Ankara'):
                                city.setName('Anqarah', False)	
                        elif sName == 'Sevilla':
                                city.setName('Ishbiliya', False)
                        elif sName == 'C&#243;rdoba':
                                city.setName('Qurtubah', False)	
                        elif sName == 'Tehran':
                                city.setName('Tahran', False)	
                        elif (sName == 'Trapezon' or sName == 'Trapezus' or sName == 'Trabzon'):
                                city.setName('Tarabizun', False)
                        elif (sName == 'Chach' or sName == 'Cheshih' or sName == 'Binkath'):
                                city.setName('Shash', False)
                        elif (sName == 'Iol Caesarea' or sName == 'Iol'):
                                city.setName('Sharshal', False)
                        elif (sName == 'Abdju' or sName == 'Abydos'):
                                city.setName('Arabet', False)
                        elif sName == 'Imu':
                                city.setName('Kom El-Hisn', False)
                        elif (sName == 'Lpqy' or sName == 'Leptis Magna' or sName == 'Lepcis'):
                                city.setName('Libdeh Al-Kubra', False)
                        elif (sName == 'Villa Cisneros' or sName == 'Dakhla'):
                                city.setName('ad-Dakhla', False)
                        elif (sName == 'Persepolis' or sName == 'Parsa'):
                                city.setName('Takht-e Jamshid', False)
                        elif (sName == 'Cyrene' or sName == 'Kyrene'):
                                city.setName('Shahat', False)
                        elif sName == 'Sirajis':
                                city.setName('Shiraz', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif sName == 'Almer&#237;a':
                                city.setName('Al-Mariyat', False)
                        elif (sName == 'Or&#225;n' or sName == 'Oran'):
                                city.setName('Wahran', False)
                        elif (sName == 'Bug&#2237;a' or sName == 'B&#233;ja&#239;a'):
                                city.setName('Bijayah', False)
                        elif sName == 'Siwa':
                                city.setName('Siwah', False)
                        elif (sName == 'Venedig' or sName == 'Venise' or sName == 'Venecia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Venetia' or sName == 'Venedik'):
                                city.setName('Al-Bundukiyya', False)
                        elif (sName == 'Toletum' or sName == 'Toledo'):
                                city.setName('Tulaytulah', False)
                        elif sName == 'Madrid':
                                city.setName('Al-Magrit', False)
                        elif (sName == 'Valentia' or sName == 'Valencia' or sName == 'Valence'):
                                city.setName('Balansiyyah', False)
                        elif (sName == 'Caesaraugusta' or sName == 'Zaragoza'):
                                city.setName('Saraqustah', False)
                        elif (sName == 'Pompaelo' or sName == 'Pamplona' or sName == 'Pampelune'):
                                city.setName('Bambalunah', False)
                        elif (sName == 'Portus Cale' or sName == 'Porto' or sName == 'Oporto'):
                                city.setName('Burtuqal', False)
                        elif (sName == 'Faro' or sName == 'Ossonoba'):
                                city.setName("'Uhshunubah", False)
                        elif sName == 'Akhetaten':
                                city.setName("Al-'Amarna", False) 
                        elif (sName == "Kuveyt" or sName == "Kuwait City"):
                                city.setName('Al-Kuwait', False)
                        elif sName == 'Siraz':
                                city.setName("Shiraz", False)
                        elif sName == 'Basra':
                                city.setName("Al-Basrah", False)
                        elif (sName == "Riyad" or sName == "Riyadh"):
                                city.setName('Ar-Riyad', False)
                        elif sName == 'Necef':
                                city.setName("An-Najaf", False)
                        elif sName == 'Amman':
                                city.setName("'Amman", False)
                        elif sName == 'Hurgada':
                                city.setName("Al-Ghardaqah", False)
                        elif sName == "Tobruk":
                                city.setName('Tubruq', False)
                        elif (sName == 'Sala' or sName == 'Sala Colonia'):
                                city.setName('Chellah', False)
                        elif (sName == 'Mogador' or sName == 'Essaouira'):
                                city.setName('Es-Sauirah', False)
                        elif (sName == 'Praga' or sName == 'Prag' or sName == 'Praha'):
                                city.setName('Birag', False)
                        elif sName == 'Safakes':
                                city.setName('Safaqis', False)
                        elif (sName == 'Tacape' or sName == 'Gabes' or sName == 'Gab&#232;s'):
                                city.setName('Qabis', False)
                        elif (sName == 'Khartoum' or sName == 'Hartum'):
                                city.setName('Al-Hartum', False)
                        elif (sName == 'C&#243;rdoba' or sName == 'Corduba' or sName == 'C&#243;rdova'):
                                city.setName('Qurtuba', False)
                        elif (sName == 'Massalia' or sName == 'Massilia' or sName == 'Marseille' or sName == 'Marsella'):
                                city.setName('Marsiliya', False)
                        elif (sName == 'Santiago'):
                                city.setName('Sant Yaqub', False)
                        elif (sName == 'Rome' or sName == 'Rom' or sName == 'Roma' or sName == 'Daqin'):
                                city.setName('Rumiya', False)
                        elif (sName == 'Kolachi' or sName == 'Mirat ul Memalik' or sName == 'Barbarikon' or sName == 'Barbaricum' or sName == 'Karachi'):
                                city.setName('Debal', False)
                        elif (sName == 'Athenae' or sName == 'Athenai' or sName == 'Athen' or sName == 'Athens' or sName == 'Atenas' or sName == 'Ath&#232;nes'):
                                city.setName('Atina', False)
                        elif sName == 'Lazkiye':
                                city.setName("Al-Ladhiqiyah", False)
                        elif (sName == 'Pataliputra' or sName == 'Patna' or sName == 'Palibothra' or sName == 'Huazhicheng' or sName == 'Kashijou'):
                                city.setName('Azimabad', False)
                        elif sName == 'Bhagyanagar':
                                city.setName('Hyderabad', False)
                        elif sName == 'Muscat':
                                city.setName('Masqat', False)
                        elif (sName == 'Arae' or sName == 'Arae Philaenorum'):
                                city.setName('Ras Lanuf', False)
                        elif (sName == 'Anabucis' or sName == 'Automala' or sName == 'El Agheila'):
                                city.setName('Al-Uqaylah', False)
                        elif (sName == 'Rhegion' or sName == 'Rhegium Julii' or sName == 'R&#237;joles' or sName == 'Reggio') :
                                city.setName('Riv&#224;h', False)
                        elif (sName == 'Gadir' or sName == 'Qart-Gadir' or sName == 'Gades' or sName == 'Gadeira' or sName == 'C&#225;dis' or sName == 'C&#225;diz' or sName == 'Cadix'):
                                city.setName('Al-Qadiz', False)
                        #Turkey
                        if (sName == 'Amisos' or sName == 'Amisus'):
                                city.setName('Samsun', False)
                        elif (sName == 'Milid' or sName == 'Malateia' or sName == 'Melitene'):
                                city.setName('Malatya', False)
                        elif (sName == 'Mazaka' or sName == 'Caesarea Mazaca' or sName == 'Kaisareia'):
                                city.setName('Kayseri', False)
                        elif (sName == 'Antiokheia Megale' or sName == 'Antiochia ad Orontem' or sName == 'Antakya'):
                                city.setName('Antakiyyah', False)
                        elif (sName == 'Alexandreia ad Issum' or sName == 'Iskenderun' or sName == 'Alexandretta'):
                                city.setName('Al-Iskandarun', False)
                        elif (sName == 'Ikonion' or sName == 'Iconium'):
                                city.setName('Konya', False)
                        elif (sName == 'Khalpe' or sName == 'Beroea' or sName == 'Halep'):
                                city.setName('Halab', False)
                        #Ethiopia
                        elif sName == 'Muqdisho':
                                city.setName('Maqadishu', False)

                elif (iNewOwner == iKhmer): 
                        if (sName == 'Malacca' or sName == 'Malakka' or sName == 'Malaca'):
                                city.setName('Bandar Melaka', False)
                        elif (sName == 'Singapur' or sName == 'Xinjiapo' or sName == 'Singapore' or sName == 'Shounantou'):
                                city.setName('Singapura', False)
                        elif (sName == 'Jakaruta' or sName == 'Batavia'):
                                city.setName('Jayakarta', False)
                        elif (sName == 'Manira'):
                                city.setName('Manila', False)
                        elif (sName == 'Dabao'):
                                city.setName('Davao', False)
                        elif (sName == 'Raoagu' or sName == 'Laowo'):
                                city.setName('Laoag', False)

                elif (iNewOwner == iSpain): 
                        if (sName == 'Gadir' or sName == 'Qart-Gadir' or sName == 'Gades' or sName == 'Gadeira' or sName == 'Al-Qadiz' or sName == 'Cadix' or sName == 'C&#225;dis'):
                                city.setName('C&#225;diz', False)
                        elif (sName == 'Toletum' or sName == 'Tulaytulah'):
                                city.setName('Toledo', False)
                        elif (sName == 'Valentia' or sName == 'Balansiyyah' or sName == 'Valence'):
                                city.setName('Valencia', False)
                        elif sName == 'Tarraco':
                                city.setName('Tarragona', False)
                        elif (sName == 'Caesaraugusta' or sName == 'Saraqustah'):
                                city.setName('Zaragoza', False)
                        elif sName == 'Brigantium':
                                city.setName('La Coru&#241;a', False)
                        elif sName == 'Hispalis':
                                city.setName('Sevilla', False)
                        elif sName == 'Asturica Augusta':
                                city.setName('Astorga', False)		
                        elif sName == 'Emerita Augusta':
                                city.setName('M&#233;rida', False)	
                        elif (sName == 'Emporion' or sName == 'Emporiae'):
                                city.setName('Ampurias', False)
                        elif sName == 'Saguntum':
                                city.setName('Sagunto', False)	
                        elif (sName == 'Nova Carthago' or sName == 'Qart Hadasht'):
                                city.setName('Cartagena', False)	
                        elif (sName == 'Rusadir' or sName == 'Maliliyah'):
                                city.setName('Melilla', False)	
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Mexico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Ciudad de M&#233;xico', False)
                        elif (sName == 'Melpum' or sName == 'Mailand' or sName == 'Mediolanum' or sName == 'Milan'):
                                city.setName('Mil&#225;n', False)
                        elif sName == 'Numantia':
                                city.setName('Numancia', False)
                        elif (sName == 'Tingi' or sName == 'Tanger' or sName == 'Tanja'):
                                city.setName('T&#225;nger', False)
                        elif (sName == 'Malaka' or sName == 'Malaqah'):
                                city.setName('M&#225;laga', False)
                        elif sName == 'Ishbiliya':
                                city.setName('Sevilla', False)
                        elif sName == 'Qurtubah':
                                city.setName('C&#243;rdoba', False)
                        elif sName == 'St. Augustine':
                                city.setName('San Agust&#237;n', False)	
                        elif (sName == 'Panormos' or sName == 'Panormus' or sName == 'Balharm' or sName == 'Ziz'):
                                city.setName('Palermo', False)  
                        elif (sName == 'Rome' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Roma', False)
                        elif (sName == 'Iol Caesarea' or sName == 'Iol' or sName == 'Sharshal'):
                                city.setName('Cherchell', False)
                        elif (sName == 'Massalia' or sName == 'Massilia' or sName == 'Marseille' or sName == 'Marsiliya'):
                                city.setName('Marsella', False)
                        elif sName == 'Bracara Augusta':
                                city.setName('Braga', False)
                        elif (sName == 'Felicitas Julia' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == "Al-'Ishbunah" or sName == 'Lisbonne' or sName == 'Lissabon' or sName == 'Lisbon'):
                                city.setName('Lisboa', False)
                        elif (sName == 'Pompaelo' or sName == 'Pampelune' or sName == 'Bambalunah'):
                                city.setName('Pamplona', False)
                        elif sName == 'Dar Beida':
                                city.setName('Casablanca', False)
                        elif sName == 'Sidi Ifni':
                                city.setName('S.Cruz de Mar Peque&#241;a', False)
                        elif sName == 'Pax Iulia':
                                city.setName('Beja', False)
                        elif (sName == 'Samarkand' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Marakanda' or sName == 'Afrasiyab'):
                                city.setName('Samarcanda', False)
                        elif (sName == 'ad-Dakhla' or sName == 'Dakhla'):
                                city.setName('Villa Cisneros', False)
                        elif (sName == 'Saint Domingue' or sName == 'Dakhla'):
                                city.setName('Santo Domingo', False)
                        elif (sName == 'Li&#232;ge' or sName == 'Luik' or sName == 'L&#252;ttich'):
                                city.setName('Lieja', False)
                        elif (sName == 'Sint-Helena' or sName == 'Saint Helena'):
                                city.setName('Santa Helena', False)
                        elif (sName == 'Cap Horn' or sName == 'Kaap Hoorn' or sName == 'Cape Horn'):
                                city.setName('Cabo de Hornos', False)
                        elif (sName == 'Pompeji' or sName == 'Pompeii' or sName == 'Pomp&#233;i'):
                                city.setName('Pompeya', False)
                        elif (sName == 'Athenae' or sName == 'Athenai' or sName == 'Athen' or sName == 'Athens' or sName == 'Atina' or sName == 'Ath&#232;nes'):
                                city.setName('Atenas', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tarabulus' or sName == 'Tripolis' or sName == 'Trablus'):
                                city.setName('Tripoli', False)
                        elif (sName == 'Sparte' or sName == 'Sparta'):
                                city.setName('Esparta', False)
                        elif (sName == 'Bandar Melaka' or sName == 'Malakka' or sName == 'Malacca'):
                                city.setName('Malaca', False)
                        elif (sName == 'Corunha' or sName == 'The Groyne' or sName == 'La Corogne'):
                                city.setName('La Coru&#241;a', False)
                        elif (sName == 'Burdigala' or sName == 'Bordeaux'):
                                city.setName('Burdeos', False)
                        elif (sName == 'Havana' or sName == 'Havanna' or sName == 'La Havane' or sName == 'Gavana'):
                                city.setName('La Habana', False)
                        elif (sName == 'New Orleans' or sName == 'Nouvelle Orl&#233;ans' or sName == 'Nova Orle&#227;es'):
                                city.setName('Nueva Orleans', False)
                        elif (sName == 'Klein-Venedig'):
                                city.setName('Venezuela', False)
                        elif (sName == 'Trefel&#237;n'):
                                city.setName('Trevelin', False)
                        elif (sName == 'Porth Madryn'):
                                city.setName('Puerto Madryn', False)
                        elif sName == 'Lle Cul':
                                city.setName('Villa La Angostura', False)
                        elif sName == 'Spatzenkutter':
                                city.setName('Asunci&#243;n', False)
                        elif sName == 'Holtzel':
                                city.setName('Colonia Nievas', False)
                        elif sName == 'Dehler':
                                city.setName('Colonia San Miguel', False)
                        elif sName == 'Hildmann':
                                city.setName('Santa Trinidad', False)
                        elif sName == 'Onuba':
                                city.setName('Huelva', False)
                        elif (sName == 'Barcino' or sName == 'Barcelone'):
                                city.setName('Barcelona', False)
                        elif sName == 'Al-Mariyat':
                                city.setName('Almer&#237;a', False)
                        elif (sName == 'Cape of Good Hope' or sName == 'Capo de Boa Esperan&#231;a' or sName == 'Cap de Bonne-Esp&#233;rance' or sName == 'Kap der Guten Hoffnung' or sName == 'Kaap de Goede Hoop'):
                                city.setName('Cabo de Buena Esperanza', False)
                        elif (sName == 'Wahran' or sName == 'Oran'):
                                city.setName('Or&#225;n', False)
                        elif (sName == 'Bijayah' or sName == 'B&#233;ja&#239;a'):
                                city.setName('Bug&#2237;a', False)
                        elif sName == 'Victoriae Iuliobrigensium':
                                city.setName('Santander', False)
                        elif sName == 'Helmantica':
                                city.setName('Salamanca', False)
                        elif (sName == 'Portus Cale' or sName == 'Porto' or sName == 'Burtuqal'):
                                city.setName('Oporto', False)
                        elif (sName == 'Ossonoba' or sName == "'Uhshunubah"):
                                city.setName('Faro', False)
                        elif (sName == 'Venedig' or sName == 'Venise' or sName == 'Venetia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venecia', False)
                        elif sName == 'Al-Magrit':
                                city.setName('Madrid', False)
                        elif (sName == 'Mogador' or sName == 'Es-Sauirah'):
                                city.setName('Essaouira', False)
                        elif sName == 'Brigantium':
                                city.setName('Betanzos', False)
                        elif sName == 'Maynilad':
                                city.setName('Manila', False)
                        elif (sName == 'Qurtuba' or sName == 'Corduba' or sName == 'C&#243;rdova'):
                                city.setName('C&#243;rdoba', False)
                        elif (sName == 'Sant Yaqub'):
                                city.setName('Santiago', False)
                        elif (sName == 'Santa Fe'):
                                city.setName('Santa F&#233;', False)
                        elif (sName == 'Dilli' or sName == 'Deli' or sName == 'New Delhi' or sName == 'Derii'):
                                city.setName('Delhi', False)
                        elif (sName == 'Singapura' or sName == 'Xinjiapo' or sName == 'Singapore' or sName == 'Shounantou'):
                                city.setName('Singapur', False)
                        elif (sName == 'Haojing' or sName == 'Macau' or sName == 'Aomen' or sName == 'Makao'):
                                city.setName('Macao', False)
                        elif (sName == 'New Iberia' or sName == 'Nouvelle-Ib&#233;rie'):
                                city.setName('Nueva Iberia', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif sName == 'Col&#244;nia do Sacramento':
                                city.setName('Colonia del Sacramento', False)
                        elif sName == 'Yokib':
                                city.setName('Piedras Negras', False)
                        elif (sName == 'Mbanza Kongo' or sName == 'S.Salvador do Congo'):
                                city.setName('S.Salvador de Congo', False)
                        elif (sName == 'Brentesion' or sName == 'Brindisi'):
                                city.setName('Brundisium', False)
                        elif (sName == 'Port Solitude' or sName == 'Port St. Louis'):
                                city.setName('Puerto Soledad', False)
                        elif (sName == 'Parijs' or sName == 'Paris'):
                                city.setName('Par&#237;s', False)
                        #inca
                        elif sName == 'Quitu':
                                city.setName('Quito', False)
                        elif sName == 'Tucume':
                                city.setName('T&#250;cume', False)
                        elif sName == 'Chan-Chan':
                                city.setName('Chanchan', False) #Trujillo
                        elif sName == 'Pachacamaq':
                                city.setName('Pachacamac', False)
                        elif sName == 'Machu-Pikchu':
                                city.setName('Machu Picchu', False)
                        elif sName == 'Qusqu':
                                city.setName('Cuzco', False)
                        elif sName == 'Ariqipaya':
                                city.setName('Arequipa', False)
                        elif sName == 'Tiyawanaku':
                                city.setName('Tiahuanaco', False) #Tihuanaku? #Tiwanaku? #Puno?
                        elif sName == 'Caqonatambu':
                                city.setName('Limatambo', False)
                        elif sName == 'Coqimpu':
                                city.setName('Coquimbo', False)
                        elif sName == 'Ullantaytanpu':
                                city.setName('Ollantaytambo', False)
                        elif sName == 'Vitcos':
                                city.setName('Piura', False)
                        elif sName == 'Andahuailas':
                                city.setName('Andahuaylas', False)
                        elif sName == 'Acari':
                                city.setName('Atico', False)
                        elif sName == 'Lluli':
                                city.setName('Juli', False)
                        elif sName == 'Chuqiapu':
                                city.setName('Chuquiapo', False)
                        elif sName == 'Huanuqupampa':
                                city.setName('Huanucopampa', False)
                        elif sName == 'Tambuqcucha':
                                city.setName('Tamboccocha', False)
                        elif sName == 'Waras':
                                city.setName('Huaraz', False)
                        elif sName == 'Cacsamalca':
                                city.setName('Caxamalca', False)
                        elif sName == 'Sauza':
                                city.setName('Sausa', False)
                        elif sName == 'Tampupuca':
                                city.setName('Tambocolorado', False)
                        elif sName == 'Huaqa':
                                city.setName('Huaca', False)
                        elif sName == 'Chuitu':
                                city.setName('Chuito', False)
                        elif sName == 'Kashamarka':
                                city.setName('Cajamarca', False)
                        elif sName == 'Lauricucha':
                                city.setName('Hu&#225;nuco', False)
                        elif sName == 'Tomebamba':
                                city.setName('Cuenca', False)
                        elif sName == 'Jauja':
                                city.setName('Sausa', False)
                        elif sName == 'Willkapampa':
                                city.setName('Vilcabamba', False)
                        elif sName == 'Wantar Chawin':
                                city.setName('Chav&#237;n de Hu&#225;ntar', False)
                        elif sName == 'Punu':
                                city.setName('Puno', False)	
                        elif (sName == 'G&#234;nes' or sName == 'Genua'):
                                city.setName('G&#233;nova', False)
                        elif (sName == 'Manira'):
                                city.setName('Manila', False)
                        elif (sName == "Chich'en Itz&#225;"):
                                city.setName('Ciudad Real', False)
                        elif (sName == "Huaxyacac"):
                                city.setName('Oaxaca', False)
                        elif (sName == "Oxhuitza" or sName == 'Caracol'):
                                city.setName('El Caracol', False)
                        elif (sName == 'Rhegion' or sName == 'Riv&#224;h' or sName == 'Rhegium Julii' or sName == 'Reggio') :
                                city.setName('R&#237;joles', False)

                elif (iNewOwner == iFrance): 
                        if (sName == 'Lutetia' or sName == 'Lutetia Parisiorum' or sName == 'Parijs' or sName == 'Par&#237;s'):
                                city.setName('Paris', False)
                        elif sName == 'Rotomagus':
                                city.setName('Rouen', False)
                        elif (sName == 'Lugdunum' or sName == 'Lugodunon'):
                                city.setName('Lyon', False)
                        elif sName == 'Aquae Sextiae':
                                city.setName('Aix-en-Provence', False)
                        elif (sName == 'Massalia' or sName == 'Massilia' or sName == 'Marsella' or sName == 'Marsiliya'):
                                city.setName('Marseille', False)
                        elif sName == 'Turonensis':
                                city.setName('Tours', False)
                        elif sName == 'Aurelia':
                                city.setName('Orl&#233;ans', False)
                        elif sName == 'Lapurdum':
                                city.setName('Bayonne', False)
                        elif (sName == 'Burdigala' or sName == 'Burdeos'):
                                city.setName('Bordeaux', False)
                        elif sName == 'Narbo Martius':
                                city.setName('Narbonne', False)
                        elif sName == 'Limonum':
                                city.setName('Poitiers', False)
                        elif sName == 'Tolosa':
                                city.setName('Toulouse', False)
                        elif sName == 'Caesarodunum':
                                city.setName('Tours', False)
                        elif sName == 'Portus Namnetum':
                                city.setName('Nantes', False)
                        elif sName == 'Gesocribate':
                                city.setName('Brest', False)
                        elif sName == 'Condate Redonum':
                                city.setName('Rennes', False)
                        elif sName == 'Augustodurum':
                                city.setName('Bayeux', False)
                        elif sName == 'Durocoturum':
                                city.setName('Reims', False)
                        elif sName == 'Cenabum Aureliani':
                                city.setName('Orl&#233;ans', False)
                        elif sName == 'Vesontio':
                                city.setName('Besan&#231;on', False)
                        elif sName == 'Lousonna':
                                city.setName('Lausanne', False)
                        elif (sName == 'Argentoratus' or sName == 'Stra&#223;burg'):
                                city.setName('Strasbourg', False)
                        elif sName == 'Augusta Treverorum':
                                city.setName('Tr&#232;ves', False)
                        elif sName == 'Gesoriacum':
                                city.setName('Boulogne', False)
                        elif (sName == 'Nijmegen' or sName == 'Batavodurum'):
                                city.setName('Nim&#232;gue', False)
                        elif sName == 'Iuliomagus':
                                city.setName('Angers', False)
                        elif sName == 'Nemausus':
                                city.setName('N&#238;mes', False)
                        elif (sName == 'Melpum' or sName == 'Mailand' or sName == 'Mediolanum' or sName == 'Mil&#225;n'):
                                city.setName('Milan', False)
                        elif sName == 'Genava':
                                city.setName('Gen&#232ve', False)
                        elif sName == 'Castra Regina':
                                city.setName('Ratisbonne', False)
                        elif (sName == 'Aachen' or sName == 'Aquisgranum' or sName == 'Aken'):
                                city.setName('Aix-la-Chapelle', False)
                        elif (sName == 'Copenhagen' or sName == 'Kopenhagen' or sName == 'Kj&#248;bmandehavn' or sName == 'Hafnia'):
                                city.setName('Copenhague', False)
                        elif (sName == 'Al-Jazair' or sName == 'Cezayir'):
                                city.setName('Alger', False)
                        elif (sName == 'Tingi' or sName == 'T&#225;nger' or sName == 'Tanja'):
                                city.setName('Tanger', False)
                        elif (sName == 'Dubh Linn' or sName == '&#193;th Cliath'):
                                city.setName('Dublin', False)
                        elif (sName == 'Heithabyr' or sName == 'Haithabu'):
                                city.setName('Hedeby', False)
                        elif (sName == 'Epidamnos' or sName == 'Dyrrachium' or sName == 'Durr&#235;s' or sName == 'Drach' or sName == 'Dira&#231'):
                                city.setName('Duras', False)
                        elif (sName == 'Moguntiacum' or sName == 'Mogontiacum' or sName == 'Mainz'):
                                city.setName('Mayence', False)
                        elif (sName == 'Roma' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Rome', False)
                        elif sName == 'Bremen':
                                city.setName('Br&#234;me', False)
                        elif (sName == 'Iol Caesarea' or sName == 'Iol' or sName == 'Sharshal'):
                                city.setName('Cherchell', False)
                        elif (sName == 'Panormos' or sName == 'Panormus' or sName == 'Balharm' or sName == 'Ziz'):
                                city.setName('Palermo', False) 
                        elif (sName == 'Samarkand' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Samarcanda' or sName == 'Marakanda' or sName == 'Afrasiyab'):
                                city.setName('Samarcande', False) 
                        elif (sName == 'Santo Domingo' or sName == 'Dakhla'):
                                city.setName('Saint Domingue', False)
                        elif (sName == 'Brussels' or sName == 'Br&#252;ssel' or sName == 'Brussel'):
                                city.setName('Bruxelles', False)
                        elif (sName == 'Lieja' or sName == 'Luik' or sName == 'L&#252;ttich'):
                                city.setName('Li&#232;ge', False)
                        elif (sName == 'Hamburg' or sName == 'Hamborg' or sName == 'Hamburgum'):
                                city.setName('Hambourg', False)
                        elif (sName == 'Knob Lake'):
                                city.setName('Lac Knob', False)
                        elif (sName == 'Quebec City'):
                                city.setName('Qu&#233;bec', False)
                        elif (sName == 'Sa&#245; Lu&#237;s'):
                                city.setName('Saint Louis', False)
                        elif (sName == 'New Orleans' or sName == 'Nueva Orleans' or sName == 'Nova Orle&#227;es'):
                                city.setName('Nouvelle Orl&#233;ans', False)
                        elif (sName == 'Cabo de Hornos' or sName == 'Kaap Hoorn' or sName == 'Cape Horn'):
                                city.setName('Cap Horn', False)
                        elif (sName == 'Little Chute'):
                                city.setName('La Petite Chute', False)
                        elif (sName == 'Vinland' or sName == 'Anse aux Meadows'):
                                city.setName('Anse-aux-M&#233;duses', False)
                        elif (sName == 'Agley' or sName == 'Oglej' or sName == 'Aquileia'):
                                city.setName('Aquil&#233;e', False)
                        elif (sName == 'Londinium' or sName == 'London' or sName == 'Londen'):
                                city.setName('Londres', False)
                        elif (sName == 'Pompeji' or sName == 'Pompeii' or sName == 'Pompeya'):
                                city.setName('Pomp&#233;i', False)
                        elif (sName == 'Athenae' or sName == 'Athenai' or sName == 'Athen' or sName == 'Athens' or sName == 'Atina' or sName == 'Atenas'):
                                city.setName('Ath&#232;nes', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tarabulus' or sName == 'Tripolis' or sName == 'Trablus'):
                                city.setName('Tripoli', False)
                        elif (sName == 'Sparta' or sName == 'Esparta'):
                                city.setName('Sparte', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexico', False)
                        elif (sName == 'Fderik'):
                                city.setName('Fort Gouraud', False)
                        elif (sName == 'Illizi'):
                                city.setName('Fort Polignac', False)
                        elif (sName == 'Havana' or sName == 'Havanna' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('La Havane', False)
                        elif (sName == 'Klein-Venedig'):
                                city.setName('Venezuela', False)
                        elif sName == 'Sankt Thomas':
                                city.setName('Saint Thomas', False)
                        elif (sName == 'Guangzhou' or sName == 'Cant&#227;o' or sName == 'Koushuu'):
                                city.setName('Canton', False)
                        elif (sName == 'Cape of Good Hope' or sName == 'Capo de Boa Esperan&#231;a' or sName == 'Cabo de Buena Esperanza' or sName == 'Kap der Guten Hoffnung' or sName == 'Kaap de Goede Hoop'):
                                city.setName('Cap de Bonne-Esp&#233;rance', False)
                        elif (sName == 'Bijayah' or sName == 'Bug&#2237;a'):
                                city.setName('B&#233;ja&#239;a', False)
                        elif (sName == 'Or&#225;n' or sName == 'Wahran'):
                                city.setName('Oran', False)
                        elif (sName == 'Tharangambadi' or sName == 'Trankebar'):
                                city.setName('Tranquebar', False)
                        elif (sName == 'Venedig' or sName == 'Venecia' or sName == 'Venetia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venise', False)
                        elif (sName == 'Wien' or sName == 'Vena' or sName == 'Vindobona' or sName == 'Viyana'):
                                city.setName('Vienne', False)
                        elif sName == 'Arguim':
                                city.setName('Arguin', False)
                        elif (sName == 'Corunha' or sName == 'The Groyne' or sName == 'La Coru&#241;a'):
                                city.setName('La Corogne', False)
                        elif (sName == 'Pompaelo' or sName == 'Pamplona' or sName == 'Bambalunah'):
                                city.setName('Pampelune', False)
                        elif (sName == 'Pondicherry' or sName == 'Puducherry'):
                                city.setName('Pondich&#233;ry', False)
                        elif (sName == 'Tacape' or sName == 'Gabes' or sName == 'Qabis'):
                                city.setName('Gab&#232;s', False)
                        elif (sName == 'Barcino' or sName == 'Barcelona'):
                                city.setName('Barcelone', False)
                        elif (sName == 'M&#252;nchen'):
                                city.setName('Munich', False)
                        elif (sName == 'Haojing' or sName == 'Macau' or sName == 'Aomen' or sName == 'Makao'):
                                city.setName('Macao', False)
                        elif (sName == 'New Iberia' or sName == 'Nueva Iberia'):
                                city.setName('Nouvelle-Ib&#233;rie', False)
                        elif (sName == 'Adiacium'):
                                city.setName('Ajaccio', False)
                        elif (sName == 'Dilli' or sName == 'Deli' or sName == 'New Delhi' or sName == 'Derii'):
                                city.setName('Delhi', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif sName == 'Bang Makok':
                                city.setName('Bangkok', False)
                        elif sName == 'Jabuuti':
                                city.setName('Djibouti', False)
                        elif (sName == 'B&#226;ton Rouge'):
                                city.setName('Baton Rouge', False)
                        elif (sName == 'Hippo' or sName == 'Annaba' or sName == 'Hippo Regius'):
                                city.setName('B&#244;ne', False)
                        elif (sName == 'Fort Panmure'):
                                city.setName('Fort Rosalie', False)
                        elif (sName == 'Diaroritum'):
                                city.setName('Rennes-le-Ch&#226;teau', False)
                        elif (sName == 'G&#233;nova' or sName == 'Genua'):
                                city.setName('G&#234;nes', False)
                        elif (sName == 'Frankfurt' or sName == 'Bona Mansio' or sName == 'Frankfort'):
                                city.setName('Francfort', False)
                        elif (sName == 'Brentesion' or sName == 'Brindisi'):
                                city.setName('Brundisium', False)
                        elif (sName == 'Port Solitude' or sName == 'Puerto Soledad'):
                                city.setName('Port St. Louis', False)
                        elif (sName == 'Pittsburgh'):
                                city.setName('Fort Duquesne', False)
                        elif (sName == 'Hannover' or sName == 'Hannovera'):
                                city.setName('Hanovre', False)
                        elif (sName == 'Toranaro' or sName == 'Tolanaro'):
                                city.setName('Fort Dauphin', False)
                        elif (sName == 'Rhegion' or sName == 'Riv&#224;h' or sName == 'Rhegium Julii' or sName == 'R&#237;joles') :
                                city.setName('Reggio', False)
                        elif (sName == 'Balansiyyah' or sName == 'Valencia' or sName == 'Valentia'):
                                city.setName('Valence', False)
                        elif (sName == 'Lisboa' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == "Al-'Ishbunah" or sName == 'Felicitas Julia' or sName == 'Lissabon' or sName == 'Lisbon'):
                                city.setName('Lisbonne', False)
                        if (sName == 'Gadir' or sName == 'Qart-Gadir' or sName == 'Gades' or sName == 'Gadeira' or sName == 'Al-Qadiz' or sName == 'C&#225;diz' or sName == 'C&#225;dis'):
                                city.setName('Cadix', False)
			
                elif (iNewOwner == iEngland): 
                        if (sName == 'Londinium' or sName == 'Londres' or sName == 'Londen'):
                                city.setName('London', False)
                        elif sName == 'Ebracum':
                                city.setName('York', False)
                        elif sName == 'Aquae Sulis':
                                city.setName('Bath', False)
                        elif sName == 'Durovernum':
                                city.setName('Canterbury', False)
                        elif sName == 'Venta Belgarum':
                                city.setName('Winchester', False)
                        elif sName == 'Isca Dumnoniorum':
                                city.setName('Exeter', False)
                        elif sName == 'Deva':
                                city.setName('Chester', False)
                        elif sName == 'Camulodunum':
                                city.setName('Colchester', False)
                        elif sName == 'Isca Silurum':
                                city.setName('Caerleon', False)
                        elif sName == 'Mancunium':
                                city.setName('Manchester', False)
                        elif sName == 'Luguvallium':
                                city.setName('Carlisle', False)
                        elif (sName == 'Eblana' or sName == 'Dubh Linn'):
                                city.setName('Dublin', False)
                        elif sName == 'Luguvallium':
                                city.setName('Carlisle', False)
                        elif (sName == 'Melpum' or sName == 'Mailand' or sName == 'Mediolanum' or sName == 'Mil&#225;n'):
                                city.setName('Milan', False)
                        elif sName == 'G&#246;teborg':
                                city.setName('Gothenburg', False)
                        elif (sName == 'Copenhague' or sName == 'Kopenhagen' or sName == 'Kj&#248;bmandehavn'):
                                city.setName('Copenhagen', False)
                        elif (sName == 'Nieuw Amsterdam' or sName == "N'yu-York" or sName == 'Nyuu Yooku'):
                                city.setName('New York', False)
                        elif (sName == 'Dubh Linn' or sName == '&#193;th Cliath'):
                                city.setName('Dublin', False)
                        elif sName == 'Deoraby':
                                city.setName('Derby', False)
                        elif sName == 'J&#243;rvik':
                                city.setName('York', False)
                        elif sName == 'Kirkjuvagr':
                                city.setName('Kirkwall', False)
                        elif sName == 'San Agust&#237;n':
                                city.setName('St. Augustine', False)
                        elif sName == 'B&#233;al Feirste':
                                city.setName('Belfast', False)
                        elif sName == 'Kaapstadt':
                                city.setName('Cape Town', False)
                        elif (sName == 'Santa Helena' or sName == 'Sint-Helena'):
                                city.setName('Saint Helena', False)
                        elif (sName == 'Bruxelles' or sName == 'Br&#252;ssel' or sName == 'Brussel'):
                                city.setName('Brussels', False)
                        elif (sName == 'Lac Knob'):
                                city.setName('Knob Lake', False)
                        elif (sName == 'Qu&#233;bec'):
                                city.setName('Quebec City', False)
                        elif (sName == 'Nueva Orleans' or sName == 'Nouvelle Orl&#233;ans' or sName == 'Nova Orle&#227;es'):
                                city.setName('New Orleans', False)
                        elif (sName == 'Cabo de Hornos' or sName == 'Kaap Hoorn' or sName == 'Cap Horn'):
                                city.setName('Cape Horn', False)
                        elif (sName == 'Fort Zeelandia' or sName == 'Paramaribo'):
                                city.setName('Fort Willoughby', False)
                        elif sName == 'Fort Goede Hoop':
                                city.setName('Hartford', False)
                        elif sName == 'Beverwyck':
                                city.setName('Albany', False)
                        elif sName == 'Fort Beversreede':
                                city.setName('Philadelphia', False)
                        elif sName == 'Wilmington':
                                city.setName('Nieuwer-Amstel', False)
                        elif (sName == 'La Petite Chute'):
                                city.setName('Little Chute', False)
                        elif (sName == 'Vinland' or sName == 'Anse-aux-M&#233;duses'):
                                city.setName('Anse aux Meadows', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexico City', False)
                        elif (sName == 'Athenae' or sName == 'Athenai' or sName == 'Athen' or sName == 'Ath&#232;nes' or sName == 'Atina' or sName == 'Atenas'):
                                city.setName('Athens', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tarabulus' or sName == 'Tripolis' or sName == 'Trablus'):
                                city.setName('Tripoli', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif (sName == 'Jekabforts'):
                                city.setName('Fort James', False)
                        elif sName == 'Novo-Arkhangelsk':
                                city.setName('Sitka', False)
                        #elif sName == "Krepost' Ross":
                        #        city.setName("Fort Ross", False)
                        elif (sName == 'Havanna' or sName == 'La Havane' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('Havana', False)
                        elif sName == 'Fort Kristina':
                                city.setName('Wilmington', False)
                        elif (sName == 'Klein-Venedig'):
                                city.setName('Venezuela', False)
                        elif sName == 'Sankt Thomas':
                                city.setName('Saint Thomas', False)
                        elif sName == 'Fort D&#233;troit':
                                city.setName('Detroit', False)
                        elif sName == 'Weihai':
                                city.setName('Port Edward', False)
                        elif (sName == 'Guangzhou' or sName == 'Cant&#227;o' or sName == 'Koushuu'):
                                city.setName('Canton', False)
                        elif (sName == 'Cap de Bonne-Esp&#233;rance' or sName == 'Capo de Boa Esperan&#231;a' or sName == 'Cabo de Buena Esperanza' or sName == 'Kap der Guten Hoffnung' or sName == 'Kaap de Goede Hoop'):
                                city.setName('Cape of Good Hope', False)
                        elif sName == 'Fort Frontenac':
                                city.setName('Kingston', False)
                        elif (sName == 'Venedig' or sName == 'Venecia' or sName == 'Venetia' or sName == 'Venise' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venice', False)
                        elif (sName == 'Hierusalem' or sName == 'Yerushalayim' or sName == 'Ierusalim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Kud&#252;s' or sName == 'Urshalim' or sName == 'Hierousalem' or sName == 'Urushalim' or sName == 'Al-Quds' or sName == 'Qods'): 
                                city.setName('Jerusalem', False)
                        elif (sName == 'Al-Iskandariya' or sName == 'Alexandreia' or sName == 'Iskenderiye' or sName == 'Eskendereyya'):
                                city.setName('Alexandria', False)
                        elif (sName == 'Al-Qahirah' or sName == 'Memphis' or sName == 'Ineb Hedj' or sName == 'Kahire' or sName == 'El-Qahirah'):
                                city.setName('Cairo', False)
                        elif sName == 'Arguim':
                                city.setName('Arguin', False)
                        elif (sName == 'Corunha' or sName == 'La Corogne' or sName == 'La Coru&#241;a'):
                                city.setName('The Groyne', False)
                        elif sName == "Tubruq":
                                city.setName('Tobruk', False)
                        elif (sName == 'Pondich&#233;ry' or sName == 'Puducherry'):
                                city.setName('Pondicherry', False)
                        elif (sName == 'Mumbai' or sName == 'Bombaim' or sName == 'Bonbei' or sName == 'Munbai'):
                                city.setName('Bombay', False)
                        elif (sName == 'Al-Hartum' or sName == 'Hartum'):
                                city.setName('Khartoum', False)
                        elif sName == 'Neu Braunfels':
                                city.setName('New Braunfels', False)
                        elif (sName == 'Bandar Melaka' or sName == 'Malakka' or sName == 'Malaca'):
                                city.setName('Malacca', False)
                        elif (sName == 'Fort Rouill&#233;' or sName == 'Fort Toronto'):
                                city.setName('Toronto', False)
                        elif (sName == 'M&#252;nchen'):
                                city.setName('Munich', False)
                        elif (sName == 'Berenikis' or sName == 'Berenice' or sName == 'Hesperides' or sName == 'Bingazi' or sName == 'Bangazi'):
                                city.setName('Benghazi', False)
                        elif (sName == 'Singapura' or sName == 'Xinjiapo' or sName == 'Singapur' or sName == 'Shounantou'):
                                city.setName('Singapore', False)
                        elif (sName == 'Haojing' or sName == 'Macao' or sName == 'Aomen' or sName == 'Makao'):
                                city.setName('Macau', False)
                        elif (sName == 'Nouvelle-Ib&#233;rie' or sName == 'Nueva Iberia'):
                                city.setName('New Iberia', False)
                        elif (sName == 'Fort Rouge'):
                                city.setName('Winnipeg', False)
                        elif (sName == 'Kolachi' or sName == 'Debal' or sName == 'Barbarikon' or sName == 'Barbaricum' or sName == 'Mirat ul Memalik'):
                                city.setName('Karachi', False)
                        elif (sName == 'Dilli' or sName == 'Delhi' or sName == 'Deli' or sName == 'Derii'):
                                city.setName('New Delhi', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif (sName == 'B&#226;ton Rouge'):
                                city.setName('Baton Rouge', False)
                        elif (sName == 'Fort Rosalie'):
                                city.setName('Fort Panmure', False)
                        elif (sName == 'Niwt-Rst' or sName == 'Diospolis Megale' or sName == 'Diospolis Magna' or sName == 'Luksor' or sName == 'Al-Uqsur'):
                                city.setName('Luxor', False)
                        elif (sName == 'Kolkata'):
                                city.setName('Calcutta', False)
                        elif (sName == 'Bengaluru'):
                                city.setName('Bangalore', False)
                        elif (sName == 'Mumbai' or sName == 'Bombaim' or sName == 'Bonbei' or sName == 'Munbai'):
                                city.setName('Bombay', False)
                        elif (sName == 'Yangon'):
                                city.setName('Rangoon', False)
                        elif (sName == 'Port St. Louis' or sName == 'Puerto Soledad'):
                                city.setName('Port Solitude', False)
                        elif (sName == 'Roodt Eylandt'):
                                city.setName('Rhode Island', False)
                        elif (sName == 'Nieuw Brunswyck'):
                                city.setName('New Brunswick', False)
                        elif (sName == 'Fort Duquesne'):
                                city.setName('Pittsburgh', False)
                        elif (sName == 'Renault'):
                                city.setName('Reno', False)
                        elif (sName == 'Dresden' or sName == 'Dresda'):
                                city.setName('Dresde', False)
                        elif (sName == "Elizavetinskaja Krepost'"):
                                city.setName('Fort Elizabeth', False)
                        elif (sName == "Oxhuitza" or sName == 'El Caracol'):
                                city.setName('Caracol', False)
                        elif sName == 'Dhaka':
                                city.setName('Dacca', False)
                        elif (sName == "'s-Gravenhage" or sName == 'Den Haag'):
                                city.setName('The Hague', False)
                        elif (sName == 'Lisboa' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == "Al-'Ishbunah" or sName == 'Felicitas Julia' or sName == 'Lissabon' or sName == 'Lisbonne'):
                                city.setName('Lisbon', False)

                elif (iNewOwner == iGermany): 
                        if sName == ('Colonia Agrippina' or sName == 'Keulen'):
                                city.setName('K&#246;ln', False)
                        elif sName == 'Lentia':
                                city.setName('Linz', False)
                        elif (sName == 'Augusta Vindelicorum' or sName == 'Damasia'):
                                city.setName('Augsburg', False)
                        elif (sName == 'Moguntiacum' or sName == 'Mogontiacum' or sName == 'Mayence'):
                                city.setName('Mainz', False)
                        elif (sName == 'Vienne' or sName == 'Vena' or sName == 'Vindobona' or sName == 'Viyana'):
                                city.setName('Wien', False)
                        elif (sName == 'Castra Regina' or sName == 'Ratisbonne'):
                                city.setName('Regensburg', False)
                        elif (sName == 'Argentoratus' or sName == 'Strasbourg'):
                                city.setName('Stra&#223;burg', False)
                        elif sName == 'Constantia':
                                city.setName('Konstanz', False)
                        elif sName == 'Virunum':
                                city.setName('Klagenfurt', False)
                        elif sName == 'Augusta Treverorum':
                                city.setName('Trier', False)
                        elif (sName == 'Emona' or sName == 'Ljubljana' or sName == 'Aemona Iulia'):
                                city.setName('Laibach', False)
                        elif (sName == 'Melpum' or sName == 'Milan' or sName == 'Mediolanum' or sName == 'Mil&#225;n'):
                                city.setName('Mailand', False)
                        elif sName == 'Genava':
                                city.setName('Genf', False)
                        elif (sName == 'Dresde' or sName == 'Dresda'):
                                city.setName('Dresden', False)
                        elif sName == 'Groningue':
                                city.setName('Groningen', False)
                        elif sName == 'Br&#234;me':
                                city.setName('Bremen', False)
                        elif (sName == 'Hambourg' or sName == 'Hamborg' or sName == 'Hamburgum'):
                                city.setName('Hamburg', False)
                        elif (sName == 'Francfort' or sName == 'Bona Mansio' or sName == 'Frankfort'):
                                city.setName('Frankfurt', False)
                        elif sName == 'Cassel':
                                city.setName('Kassel', False)
                        elif sName == 'Cobourg':
                                city.setName('Coburg', False)
                        elif (sName == 'Hanovre' or sName == 'Hannovera'):
                                city.setName('Hannover', False)
                        elif (sName == 'Aix-la-Chapelle' or sName == 'Aquisgranum' or sName == 'Aken'):
                                city.setName('Aachen', False)
                        elif (sName == 'Apulum' or sName == 'Apulon' or sName == 'Balgrad'):
                                city.setName('Karlsburg', False)
                        elif (sName == 'Napoca' or sName == 'Cluj-Napoca' or sName == 'Castrum Clus' or sName == 'Kalosvar'):
                                city.setName('Klausenburg', False)
                        elif sName == 'Gothenburg':
                                city.setName('G&#246;teborg', False)
                        elif (sName == 'Gdansk' or sName == 'Danswijk' or sName == 'Gedanum'):
                                city.setName('Danzig', False)
                        elif (sName == 'Kaliningrad' or sName == 'Calininopolis'):
                                city.setName('K&#246;nigsberg', False)
                        elif sName == 'Moskva':
                                city.setName('Moskau', False)
                        elif (sName == 'Dubh Linn' or sName == '&#193;th Cliath'):
                                city.setName('Dublin', False)
                        elif (sName == 'Epidamnos' or sName == 'Dyrrachium' or sName == 'Duras' or sName == 'Drach' or sName == 'Dira&#231'):
                                city.setName('Durr&#235;s', False)
                        elif (sName == 'Copenhague' or sName == 'Copenhagen' or sName == 'Kj&#248;bmandehavn' or sName == 'Hafnia'):
                                city.setName('Kopenhagen', False)
                        elif (sName == 'Heithabyr' or sName == 'Hedeby'):
                                city.setName('Haithabu', False)
                        elif (sName == 'Athenai' or sName == 'Atina' or sName == 'Athenae' or sName == 'Athens' or sName == 'Atenas' or sName == 'Ath&#232;nes'):
                                city.setName('Athen', False)
                        elif (sName == 'Panormos' or sName == 'Panormus' or sName == 'Balharm' or sName == 'Ziz'):
                                city.setName('Palermo', False)  
                        elif (sName == 'Roma' or sName == 'Rome' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Rom', False)
                        elif sName == 'Br&#234;me':
                                city.setName('Bremen', False)
                        elif (sName == 'Marakanda' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Samarkand', False)
                        elif (sName == 'Konstantia' or sName == 'Tomis' or sName == 'Konstanca' or sName == 'Kustendje'):
                                city.setName('K&#246;stendsche', False)
                        elif (sName == 'Byzantium' or sName == 'Bizantiya'):
                                city.setName('Byzantion', False)
                        elif (sName == 'Qustantiniyah' or sName == 'Constantinopolis' or sName == 'Konstantinoupolis' or sName == 'Istanbul' or sName == 'Miklagard' or sName == "Konstantinopol'" or sName == "Car'grad" or sName == 'Stambul'):
                                city.setName('Konstantinopel', False)
                        elif (sName == 'Aquil&#233;e' or sName == 'Oglej' or sName == 'Aquileia'):
                                city.setName('Agley', False)
                        elif (sName == 'Pomp&#233;i' or sName == 'Pompeii' or sName == 'Pompeya'):
                                city.setName('Pompeji', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif (sName == 'Massalia' or sName == 'Massilia' or sName == 'Marsella' or sName == 'Marsiliya'):
                                city.setName('Marseille', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tarabulus' or sName == 'Tripoli' or sName == 'Trablus'):
                                city.setName('Tripolis', False)
                        elif (sName == 'Fort James'):
                                city.setName('Jekabforts', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexicopolis' or sName == 'Mexico' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexiko-Stadt', False)
                        elif (sName == 'Havana' or sName == 'La Havane' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('Havanna', False)
                        elif (sName == 'Nueva Orleans' or sName == 'Nouvelle Orl&#233;ans' or sName == 'Nova Orle&#227;es'):
                                city.setName('New Orleans', False)
                        elif (sName == 'Venezuela'):
                                city.setName('Klein-Venedig', False)
                        elif (sName == 'S&#227;o Leopoldo'):
                                city.setName('S. Leopold', False)
                        elif (sName == 'Cape of Good Hope' or sName == 'Capo de Boa Esperan&#231;a' or sName == 'Cabo de Buena Esperanza' or sName == 'Cap de Bonne-Esp&#233;rance' or sName == 'Kaap de Goede Hoop'):
                                city.setName('Kap der Guten Hoffnung', False)
                        elif sName == 'Vyborg':
                                city.setName('Wiborg', False)
                        elif (sName == 'Burdigala' or sName == 'Burdeos'):
                                city.setName('Bordeaux', False)
                        elif (sName == 'Helsingfors' or sName == "Khel'sinki" or sName == 'Helsingia'):
                                city.setName('Helsinki', False)
                        elif (sName == 'Venetia' or sName == 'Venise' or sName == 'Venecia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venedig', False)
                        elif sName == 'Arguim':
                                city.setName('Arguin', False)
                        elif (sName == 'Pokesu' or sName == 'Fort Hollandia'):
                                city.setName('Gro&#223; Friedrichsburg', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif sName == 'Doliwa':
                                city.setName('Romasdorf', False)
                        elif sName == 'Dobruja':
                                city.setName('Dobrudscha', False)
                        elif sName == 'Kolomyia':
                                city.setName('Kolomea', False)
                        elif sName == 'Tonkoschurowka':
                                city.setName('Marienthal', False)
                        elif (sName == 'Spalatum' or sName == 'Aspalathos'):
                                city.setName('Split', False)
                        elif (sName == 'Salonae' or sName == 'Salona'):
                                city.setName('Solin', False)
                        elif (sName == 'Moncastrum' or sName == 'Tiraspol' or sName == 'Akkerman' or sName == 'Tyras'):
                                city.setName('Wei&#223;enburg', False)
                        elif sName == 'Tiran':
                                city.setName('Tirana', False)
                        elif (sName == 'Zantar' or sName == 'Iadera'):
                                city.setName('Zadar', False) 
                        elif sName == 'Klajpeda':
                                city.setName('Memel', False)
                        elif (sName == 'Warszawa' or sName == 'Varsovia'):
                                city.setName('Warschau', False)
                        elif (sName == 'Singidunum' or sName == 'Singidun' or sName == 'Beograd'):
                                city.setName('Belgrad', False)
                        elif (sName == 'Sirmium' or sName == 'Sirmion' or sName == 'Dimitrof&#231;e' or sName == 'Sremska Mitrovica'):
                                city.setName('Syrmisch Mitrowitz', False)
                        elif sName == "L'vov":
                                city.setName('Lemberg', False)
                        elif sName == 'Shirokolanovka':
                                city.setName('Landau', False)
                        elif sName == 'Brest-Litovsk':
                                city.setName('Brest-Litowsk', False)
                        elif (sName == 'Praga' or sName == 'Praha' or sName == 'Birag'):
                                city.setName('Prag', False)
                        elif sName == "Tver'":
                                city.setName('Twer', False)
                        elif (sName == 'Munich'):
                                city.setName('M&#252;nchen', False)
                        elif (sName == 'Haojing' or sName == 'Macau' or sName == 'Aomen' or sName == 'Makao'):
                                city.setName('Macao', False)
                        elif (sName == 'Berolinum' or sName == 'Berlijn'):
                                city.setName('Berlin', False)
                        elif sName == 'Traiectum Eruditum':
                                city.setName('Utrecht', False)
                        elif (sName == 'Nim&#232;gue' or sName == 'Batavodurum'):
                                city.setName('Nijmegen', False)
                        elif (sName == 'Bruxelles' or sName == 'Brussel' or sName == 'Brussels'):
                                city.setName('Br&#252;ssel', False)
                        elif (sName == 'Lieja' or sName == 'Luik' or sName == 'Li&#232;ge'):
                                city.setName('L&#252;ttich', False)
                        elif (sName == 'Krak&#243;w' or sName == 'Cracovia'):
                                city.setName('Krakau', False)
                        elif (sName == 'G&#234;nes' or sName == 'G&#233;nova'):
                                city.setName('Genua', False)
                        elif (sName == 'Reval' or sName == 'Tallin' or sName == 'Revalia'):
                                city.setName('Tallinn', False)
                        elif (sName == 'Kovno'):
                                city.setName('Kauen', False)
                        elif (sName == "Vil'na"):
                                city.setName('Wilna', False)
                        elif (sName == 'Szczecin'):
                                city.setName('Stettin', False)
                        elif (sName == 'Poznan'):
                                city.setName('Posen', False)
                        elif (sName == 'Novgorod' or sName == 'Holmg&#229;rd'):
                                city.setName('Nowgorod', False)
                        elif (sName == 'Wittenberg'):
                                city.setName('Lutherstadt Wittenberg', False)
                        elif (sName == 'Pruissisch Holland' or sName == 'Paslek'):
                                city.setName('Preu&#223;isch Holland', False)
                        elif (sName == 'Frederikstad'):
                                city.setName('Friedrichstadt', False)
                        elif (sName == 'Parijs' or sName == 'Par&#237;s'):
                                city.setName('Paris', False)
                        elif (sName == 'Qingdao' or sName == 'Seitou'):
                                city.setName('Tsingtau', False)
                        elif (sName == 'Rostochium'):
                                city.setName('Rostock', False)
                        elif (sName == "'s-Gravenhage" or sName == 'The Hague'):
                                city.setName('Den Haag', False)
                        elif (sName == 'Lisboa' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == "Al-'Ishbunah" or sName == 'Felicitas Julia' or sName == 'Lisbon' or sName == 'Lisbonne'):
                                city.setName('Lissabon', False)

                elif (iNewOwner == iRussia): 
                        if (sName == 'Singidunum' or sName == 'Singidun' or sName == 'Belgrad'):
                                city.setName('Beograd', False)
                        elif (sName == 'Emona' or sName == 'Laibach' or sName == 'Aemona Iulia'):
                                city.setName('Ljubljana', False)
                        elif (sName == 'Spalatum' or sName == 'Aspalathos'):
                                city.setName('Split', False)
                        elif (sName == 'Salonae' or sName == 'Salona'):
                                city.setName('Solin', False)
                        elif sName == 'Ragusium':
                                city.setName('Dubrovnik', False)
                        elif (sName == 'Sirmium' or sName == 'Sirmion' or sName == 'Dimitrof&#231;e' or sName == 'Syrmisch Mitrowitz'):
                                city.setName('Sremska Mitrovica', False)
                        elif (sName == 'Odessos' or sName == 'Odessus'):
                                city.setName('Varna', False)
                        elif (sName == 'Naissos' or sName == 'Naissus'):
                                city.setName('Nis', False)
                        elif sName == 'Philippopolis':
                                city.setName('Plovdiv', False)
                        elif (sName == 'Marakanda' or sName == 'Samarkant' or sName == 'Samarqand' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Samarkand', False)
                        elif (sName == 'Epidamnos' or sName == 'Dyrrachium' or sName == 'Duras' or sName == 'Dira&#231' or sName == 'Durr&#235;s'):
                                city.setName('Drach', False)
                        elif sName == 'Kefe':
                                city.setName('Feodosija', False)
                        elif sName == 'Bosna Saraj':
                                city.setName('Sarajevo', False)
                        elif sName == 'Aldeigjuborg':
                                city.setName('Staraja Ladoga', False)
                        elif (sName == 'Nowgorod' or sName == 'Holmg&#229;rd'):
                                city.setName('Novgorod', False)
                        elif sName == 'K&#246;nug&#229;rd':
                                city.setName('Kiev', False)
                        elif (sName == 'Danzig' or sName == 'Danswijk' or sName == 'Gedanum'):
                                city.setName('Gdansk', False)
                        elif (sName == 'K&#246;nigsberg' or sName == 'Calininopolis'):
                                city.setName('Kaliningrad', False)
                        elif sName == 'Moskau':
                                city.setName('Moskva', False)
                        elif (sName == 'Tyras' or sName == 'Moncastrum' or sName == 'Akkerman' or sName == 'Wei&#223;enburg'):
                                city.setName('Tiraspol', False) #Belgorod-Dnestrovskiy
                        elif (sName == 'Chach' or sName == 'Shash' or sName == 'Cheshih' or sName == 'Binkath' or sName == 'Toshkent'):
                                city.setName('Tashkent', False)
                        elif (sName == 'Apulum' or sName == 'Apulon' or sName == 'Karlsburg'):
                                city.setName('Balgrad', False)
                        elif (sName == 'Napoca' or sName == 'Klausenburg' or sName == 'Castrum Clus' or sName == 'Kalosvar'):
                                city.setName('Cluj-Napoca', False)
                        elif (sName == 'Konstantia' or sName == 'Tomis' or sName == 'K&#246;stendsche' or sName == 'Kustendje'):
                                city.setName('Konstanca', False)
                        elif sName == 'Romasdorf':
                                city.setName('Doliwa', False)
                        elif sName == 'Dobrudscha':
                                city.setName('Dobruja', False)
                        elif sName == 'Kolomea':
                                city.setName('Kolomyia', False)
                        elif sName == 'Pokrovsk':
                                city.setName('Engels', False)
                        elif sName == 'Katharinenstadt':
                                city.setName('Marx', False)
                        elif sName == 'Marienthal':
                                city.setName('Tonkoschurowka', False)
                        elif sName == 'Saryk Atov':
                                city.setName('Saratov', False)
                        elif (sName == 'Aquil&#233;e' or sName == 'Agley' or sName == 'Aquileia'):
                                city.setName('Oglej', False)
                        elif (sName == 'Byzantion' or sName == 'Miklagard' or sName == 'Bizantiya' or sName == 'Constantinopolis' or sName == 'Qustantiniyah' or sName == 'Konstantinopel'):
                                city.setName("Car'grad", False) 
                        elif (sName == 'Istanbul'):
                                city.setName('Stambul', False) #new one
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexico', False)
                        elif sName == 'Sitka':
                                city.setName("Novoarkhangel'sk", False)
                        #elif sName == "Fort Ross":
                        #        city.setName("Krepost' Ross", False)
                        elif (sName == 'Havanna' or sName == 'La Havane' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('Havana', False)
                        elif (sName == 'Chersonesos' or sName == 'Chersonesus'):
                                city.setName('Khersones', False)
                        elif sName == 'Tiran':
                                city.setName('Tirana', False)
                        elif (sName == 'Helsinki' or sName == 'Helsingfors' or sName == 'Helsingia'):
                                city.setName("Khel'sinki", False)
                        elif (sName == 'Venedig' or sName == 'Venecia' or sName == 'Venetia' or sName == 'Venise' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venice' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venecija', False)
                        elif (sName == 'Zantar' or sName == 'Iadera'):
                                city.setName('Zadar', False) 
                        elif (sName == 'Vienne' or sName == 'Wien' or sName == 'Vindobona' or sName == 'Viyana'):
                                city.setName('Vena', False)
                        elif sName == 'Memel':
                                city.setName('Klajpeda', False)
                        elif (sName == 'Warschau' or sName == 'Varsovia'):
                                city.setName('Warszawa', False)
                        elif sName == "Grozni":
                                city.setName('Groznyj', False)
                        elif sName == 'Lemberg':
                                city.setName("L'vov", False)
                        elif sName == 'Landau':
                                city.setName('Shirokolanovka', False)
                        elif sName == 'Brest-Litowsk':
                                city.setName('Brest-Litovsk', False)
                        elif (sName == 'Praga' or sName == 'Prag' or sName == 'Birag'):
                                city.setName('Praha', False)
                        elif sName == 'Artaxata':
                                city.setName('Artashat', False)
                        elif sName == 'Twer':
                                city.setName("Tver'", False)
                        elif (sName == 'Babil&#251;' or sName == 'Babel' or sName == 'Babil' or sName == 'Babylon' or sName == 'Babirush' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babilon', False)
                        elif (sName == 'Haishenwai' or sName == 'Urajiosutokku' or sName == 'Fuladiwosituoke' or sName == 'Port May'):
                                city.setName('Vladivostok', False)
                        elif (sName == 'Boli' or sName == 'Hakuryoku'):
                                city.setName('Khabarovsk', False)
                        elif (sName == 'Fuyori'):
                                city.setName('Nikolaevsk-na-Amure', False)
                        elif (sName == 'Tiflis'):
                                city.setName('Tbilisi', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif (sName == 'Furukamappu'):
                                city.setName("Juzhno-Kuri'lsk", False)
                        elif (sName == 'Sofya'):
                                city.setName('Sofia', False)							
                        elif (sName == 'B&#252;kres'):
                                city.setName('Bucuresti', False)	
                        elif (sName == 'Dairen' or sName == 'Dalian' or sName == 'Sanshan'):
                                city.setName("Dal'nij", False)
                        elif (sName == 'Krakau' or sName == 'Cracovia'):
                                city.setName('Krak&#243;w', False)
                        elif (sName == 'Otomari'):
                                city.setName('Korsakov', False)
                        elif (sName == 'Reval' or sName == 'Tallinn' or sName == 'Revalia'):
                                city.setName('Tallin', False)
                        elif (sName == 'Kauen'):
                                city.setName('Kovno', False)
                        elif (sName == 'Wilna'):
                                city.setName("Vil'na", False)
                        elif (sName == 'Stettin'):
                                city.setName('Szczecin', False)
                        elif (sName == 'Posen'):
                                city.setName('Poznan', False)
                        elif (sName == 'Pruissisch Holland' or sName == 'Preu&#223;isch Holland'):
                                city.setName('Paslek', False)
                        elif (sName == 'Konkolewo Hauland'):
                                city.setName('Kakolewo', False)
                        elif (sName == 'Cyty'):
                                city.setName('Chita', False)
                        elif (sName == 'Ulaan-Ude'):
                                city.setName('Ulan-Udeh', False)
                        elif (sName == 'Astrakhan'):
                                city.setName("Astrakhan'", False)
                        elif (sName == 'Kulsary'):
                                city.setName("Kul'sary", False)
                        elif (sName == 'Yakuttsuku'):
                                city.setName('Jakutsk', False)
                        elif (sName == 'San Francisco' or sName == 'Sanfuranshisuko'):
                                city.setName('San-Francisko', False)
                        elif (sName == 'Vancouver' or sName == 'Bankuubaa'):
                                city.setName('Vankuver', False)
                        elif (sName == 'Seattle' or sName == 'Shiatoru'):
                                city.setName('Siehtl', False)
                        elif (sName == 'Rosu' or sName == 'Los Angeles'):
                                city.setName('Los-Andzheles', False)
                        elif (sName == 'Washington' or sName == 'Washinton'):
                                city.setName('Vashington', False)
                        elif (sName == 'Nieuw Amsterdam' or sName == 'New York' or sName == 'Nyuu Yooku'):
                                city.setName("N'yu-York", False)
                        elif (sName == 'Fort Elizabeth'):
                                city.setName("Elizavetinskaja Krepost'", False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mexico' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mexicopolis'):
                                city.setName('Mekhiko', False)
                        elif (sName == 'Havana' or sName == 'Havanna' or sName == 'La Havane' or sName == 'La Habana'):
                                city.setName('Gavana', False)
                        elif (sName == 'Babirush' or sName == 'Babel' or sName == 'Babil' or sName == 'Babilon' or sName == 'Babylon' or sName == 'Babili' or sName == 'Babil&#251;'):
                                city.setName('Vavilon', False)
                        elif (sName == 'Hong Kong' or sName == 'Honkon' or sName == 'Xianggang'):
                                city.setName('Sjangan', False)
                        elif (sName == 'Furukamappu'):
                                city.setName("Juzhno-Kuril'sk", False)
                        elif (sName == 'Seward'):
                                city.setName("Voskresenskaja", False)
                        elif (sName == "Kushiro"):
                                city.setName("Kusiro", False)
                        elif (sName == "Hakodate"):
                                city.setName("Khakodate", False)
                        elif (sName == 'Kyouto' or sName == "Jingdu"):
                                city.setName('Kioto', False)
                        elif (sName == 'Edo' or sName == 'Toukyou' or sName == 'Jianghu'):
                                city.setName('Tokio', False)
                        elif (sName == 'Kagoshima' or sName == "Lu'erdao"):
                                city.setName("Kagosima", False)
                        elif (sName == "Naha"):
                                city.setName("Nakha", False)
                        elif (sName == 'Heijo' or sName == 'Pyongyang'):
                                city.setName("Pkhen'jan", False)
                        elif (sName == 'Shunsen' or sName == "Chunchkhon"):
                                city.setName('Chuncheon', False)
                        elif (sName == 'Seoul' or sName == 'Hanseong' or sName == 'Hancheng' or sName == 'Seul'):
                                city.setName('Keijou', False)
                        elif (sName == 'Khanbaliq' or sName == 'Beijing' or sName == 'Hokkin'):
                                city.setName('Pekin', False)
                        elif (sName == "Qara Qorum"):
                                city.setName("Karakorum", False)
                        elif (sName == 'Shenyang' or sName == "Shin'you"):
                                city.setName('Mukden', False)
                        elif (sName == 'Botankou' or sName == 'Mudanjiang'):
                                city.setName("Mudan'czjan", False)
                        elif (sName == 'Jinzhou' or sName == "Czin'chzhou"):
                                city.setName('Kinshuu', False)
                        elif (sName == 'Francfort' or sName == 'Bona Mansio' or sName == 'Frankfort'):
                                city.setName('Frankfurt', False)
                        elif (sName == 'Berolinum' or sName == 'Berlijn'):
                                city.setName('Berlin', False)
                        elif (sName == "Erkh&#252;&#252;"):
                                city.setName("Irkutsk", False)
                        elif (sName == 'Qazan'):
                                city.setName("Kazan'", False)
                        elif (sName == 'Ufu'):
                                city.setName("Ufa", False)

                if (iNewOwner == iNetherlands): 
                        if (sName == 'New York' or sName == "N'yu-York" or sName == 'Nyuu Yooku'):
                                city.setName('Nieuw Amsterdam', False)
                        elif sName == 'Br&#234;me':
                                city.setName('Bremen', False)
                        elif sName == 'Cape Town':
                                city.setName('Kaapstadt', False)
                        elif sName == 'Groningue':
                                city.setName('Groningen', False)
                        elif sName == 'Traiectum Eruditum':
                                city.setName('Utrecht', False)
                        elif (sName == 'Nim&#232;gue' or sName == 'Batavodurum'):
                                city.setName('Nijmegen', False)
                        elif (sName == 'Aix-la-Chapelle' or sName == 'Aquisgranum' or sName == 'Aachen'):
                                city.setName('Aken', False)
                        elif (sName == 'Bruxelles' or sName == 'Br&#252;ssel' or sName == 'Brussels'):
                                city.setName('Brussel', False)
                        elif (sName == 'Lieja' or sName == 'L&#252;ttich' or sName == 'Li&#232;ge'):
                                city.setName('Luik', False)
                        elif (sName == 'Hamburg' or sName == 'Hambourg' or sName == 'Hamburgum'):
                                city.setName('Hamborg', False)
                        elif (sName == 'Paris' or sName == 'Par&#237;s'):
                                city.setName('Parijs', False)
                        elif sName == 'Cuddalore':
                                city.setName('Coedeloer', False)
                        elif (sName == 'Cabo de Hornos' or sName == 'Cape Horn' or sName == 'Cap Horn'):
                                city.setName('Kaap Hoorn', False)
                        elif (sName == 'Santa Helena' or sName == 'Saint Helena'):
                                city.setName('Sint-Helena', False)
                        elif sName == 'Recife':
                                city.setName('Mauritsstad', False)
                        elif sName == 'Fortaleza':
                                city.setName('Fort Schoonenburgh', False)
                        elif (sName == 'Fort Willoughby' or sName == 'Paramaribo'):
                                city.setName('Fort Zeelandia', False)
                        elif sName == 'Georgetown':
                                city.setName('Stabroek', False)
                        elif sName == 'Hartford':
                                city.setName('Fort Goede Hoop', False)
                        elif sName == 'Albany':
                                city.setName('Beverwyck', False)
                        elif sName == 'Philadelphia':
                                city.setName('Fort Beversreede', False)
                        elif sName == 'Nieuwer-Amstel':
                                city.setName('Wilmington', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexicopolis' or sName == 'Mexico' or sName == 'Cidade do M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mekhiko'):
                                city.setName('Mexico-stad', False)
                        elif (sName == 'Bandar Melaka' or sName == 'Malacca'):
                                city.setName('Malakka', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tarabulus' or sName == 'Tripolis' or sName == 'Trablus'):
                                city.setName('Tripoli', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif (sName == 'Roma' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Rome', False)
                        elif (sName == 'Dubh Linn' or sName == '&#193;th Cliath'):
                                city.setName('Dublin', False)
                        elif (sName == 'Qart-Hadasht' or sName == 'Qartaj' or sName == 'Karkhedon' or sName == 'Kartaca' or sName == 'Kartaca'):
                                city.setName('Carthago', False)
                        elif (sName == 'Fort James'):
                                city.setName('Jekabforts', False)
                        elif (sName == 'Havanna' or sName == 'La Havane' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('Havana', False)
                        elif (sName == 'Nueva Orleans' or sName == 'Nouvelle Orl&#233;ans' or sName == 'Nova Orle&#227;es'):
                                city.setName('New Orleans', False)
                        elif (sName == 'Klein-Venedig'):
                                city.setName('Venezuela', False)
                        elif (sName == 'Cape of Good Hope' or sName == 'Capo de Boa Esperan&#231;a' or sName == 'Cabo de Buena Esperanza' or sName == 'Cap de Bonne-Esp&#233;rance' or sName == 'Kap der Guten Hoffnung'):
                                city.setName('Kaap de Goede Hoop', False)
                        elif (sName == 'Burdigala' or sName == 'Burdeos'):
                                city.setName('Bordeaux', False)
                        elif (sName == 'Venedig' or sName == 'Venecia' or sName == 'Venetia' or sName == 'Venise' or sName == 'Veneza' or sName == 'Venecija' or sName == 'Venice' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Veneti&#235;', False)
                        elif sName == 'Arguim':
                                city.setName('Arguin', False)
                        elif (sName == 'Pokesu' or sName == 'Gro&#223; Friedrichsburg'):
                                city.setName('Fort Hollandia', False)
                        elif (sName == 'Massalia' or sName == 'Massilia' or sName == 'Marsella' or sName == 'Marsiliya'):
                                city.setName('Marseille', False)
                        elif (sName == 'Munich'):
                                city.setName('M&#252;nchen', False)
                        elif (sName == 'Jakaruta' or sName == 'Jayakarta'):
                                city.setName('Batavia', False)
                        elif (sName == 'Singapura' or sName == 'Xinjiapo' or sName == 'Singapur' or sName == 'Shounantou'):
                                city.setName('Singapore', False)
                        elif (sName == 'Haojing' or sName == 'Macao' or sName == 'Aomen' or sName == 'Makao'):
                                city.setName('Macau', False)
                        elif (sName == 'Dilli' or sName == 'Deli' or sName == 'New Delhi' or sName == 'Derii'):
                                city.setName('Delhi', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif (sName == 'Copenhague' or sName == 'Copenhagen' or sName == 'Kj&#248;bmandehavn' or sName == 'Hafnia'):
                                city.setName('Kopenhagen', False)
                        elif (sName == 'Rhode Island'):
                                city.setName('Roodt Eylandt', False)
                        elif (sName == 'New Brunswyck'):
                                city.setName('Nieuw Brunswyck', False)
                        elif (sName == 'Lutherstadt Wittenberg'):
                                city.setName('Wittenberg', False)
                        elif (sName == 'Preu&#223;isch Holland' or sName == 'Paslek'):
                                city.setName('Pruissisch Holland', False)
                        elif (sName == 'Kakolewo'):
                                city.setName('Konkolewo Hauland', False)
                        elif (sName == 'Friedrichstadt'):
                                city.setName('Frederikstad', False)
                        elif (sName == 'Gdansk' or sName == 'Danzig' or sName == 'Gedanum'):
                                city.setName('Danswijk', False)
                        elif (sName == 'Berlin' or sName == 'Berolinum'):
                                city.setName('Berlijn', False)
                        elif (sName == 'Frankfurt' or sName == 'Francfort' or sName == 'Bona Mansio'):
                                city.setName('Frankfort', False)
                        elif (sName == 'Den Haag' or sName == 'The Hague'):
                                city.setName("'s-Gravenhage", False)
                        elif (sName == 'Londinium' or sName == 'London' or sName == 'Londres'):
                                city.setName('Londen', False)
                        elif sName == ('Colonia Agrippina' or sName == 'K&#246;ln'):
                                city.setName('Keulen', False)
                        elif (sName == 'Lisboa' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == "Al-'Ishbunah" or sName == 'Felicitas Julia' or sName == 'Lisbon' or sName == 'Lisbonne'):
                                city.setName('Lissabon', False)

                elif (iNewOwner == iMali): 
                        if sName == 'S.Cruz de Mar Peque&#241;a':
                                city.setName('Sidi Ifni', False)
                        elif (sName == 'Villa Cisneros' or sName == 'ad-Dakhla'):
                                city.setName('Dakhla', False)
                        elif (sName == 'Fort Gouraud'):
                                city.setName('Fderik', False)
                        elif (sName == 'Fort Polignac'):
                                city.setName('Illizi', False)
                        elif sName == 'Fort Christiansborg':
                                city.setName('Osu', False)
                        elif sName == 'Fort Prinsensten':
                                city.setName('Keta', False)
                        elif sName == 'Fort Witsten':
                                city.setName('Takoradi', False)
                        elif (sName == 'Fort Hollandia' or sName == 'Gro&#223; Friedrichsburg'):
                                city.setName('Pokesu', False)
                        elif (sName == 'Salisbury'):
                                city.setName('Harare', False)
                        elif (sName == 'Conakry'):
                                city.setName('Konakiri', False)

                if (iNewOwner == iPortugal): 
                        if (sName == 'Sint-Helena' or sName == 'Saint Helena'):
                                city.setName('Santa Helena', False)
                        elif (sName == 'Saint Louis'):
                                city.setName('Sa&#245; Lu&#237;s', False)
                        elif sName == 'Mauritsstad':
                                city.setName('Recife', False)
                        elif sName == 'Fort Schoonenburgh':
                                city.setName('Fortaleza', False)
                        elif (sName == 'Fort Willoughby' or sName == 'Fort Zeelandia'):
                                city.setName('Paramaribo', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Mexico City' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Cidade do M&#233;xico', False)
                        elif (sName == 'Bandar Melaka' or sName == 'Malakka' or sName == 'Malacca'):
                                city.setName('Malaca', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tarabulus' or sName == 'Tripolis' or sName == 'Trablus'):
                                city.setName('Tripoli', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif (sName == 'Athenae' or sName == 'Athenai' or sName == 'Athen' or sName == 'Athens' or sName == 'Atina' or sName == 'Ath&#232;nes'):
                                city.setName('Atenas', False)
                        elif (sName == 'La Coru&#241;a' or sName == 'The Groyne' or sName == 'La Corogne'):
                                city.setName('Corunha', False)
                        elif (sName == 'Havanna' or sName == 'La Havane' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('Havana', False)
                        elif (sName == 'New Orleans' or sName == 'Nouvelle Orl&#233;ans' or sName == 'Nueva Orleans'):
                                city.setName('Nova Orle&#227;es', False)
                        elif (sName == 'Klein-Venedig'):
                                city.setName('Venezuela', False)
                        elif (sName == 'S. Leopold'):
                                city.setName('S&#227;o Leopoldo', False)
                        elif (sName == 'Guangzhou' or sName == 'Canton' or sName == 'Koushuu'):
                                city.setName('Cant&#227;o', False)
                        elif (sName == 'Cape of Good Hope' or sName == 'Kaap de Goede Hoop' or sName == 'Cabo de Buena Esperanza' or sName == 'Cap de Bonne-Esp&#233;rance' or sName == 'Kap der Guten Hoffnung'):
                                city.setName('Capo de Boa Esperan&#231;a', False)
                        elif (sName == 'Portus Cale' or sName == 'Porto' or sName == 'Burtuqal'):
                                city.setName('Oporto', False)
                        elif (sName == 'Venedig' or sName == 'Venecia' or sName == 'Venetia' or sName == 'Venise' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Venice' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Veneza', False)
                        elif sName == 'Arguin':
                                city.setName('Arguim', False)
                        elif (sName == 'Ossonoba' or sName == "'Uhshunubah"):
                                city.setName('Faro', False)
                        elif (sName == 'Felicitas Julia' or sName == 'Allis Ubbo' or sName == 'Olissipo' or sName == "Al-'Ishbunah" or sName == 'Lisbonne' or sName == 'Lissabon' or sName == 'Lisbon'):
                                city.setName('Lisboa', False)
                        elif (sName == 'Essaouira' or sName == 'Es-Sauirah'):
                                city.setName('Mogador', False)
                        elif (sName == 'Mumbai' or sName == 'Bombay' or sName == 'Bonbei' or sName == 'Munbai'):
                                city.setName('Bombaim', False)
                        elif (sName == 'Qurtuba' or sName == 'Corduba' or sName == 'C&#243;rdoba'):
                                city.setName('C&#243;rdova', False)
                        elif sName == 'Colonia del Sacramento':
                                city.setName('Col&#244;nia do Sacramento', False)
                        elif (sName == 'Honkon' or sName == 'Xianggang' or sName == 'Gon Kong' or sName == 'Sjangan'):
                                city.setName('Hong Kong', False)
                        elif (sName == 'Mombasa'):
                                city.setName('Momba&#231;a', False)
                        elif (sName == 'Mbanza Kongo' or sName == 'S.Salvador de Congo'):
                                city.setName('S.Salvador do Congo', False)
                        elif (sName == 'Haojing' or sName == 'Macao' or sName == 'Aomen' or sName == 'Makao'):
                                city.setName('Macau', False)
                        elif (sName == 'Dilli' or sName == 'Delhi' or sName == 'New Delhi' or sName == 'Derii'):
                                city.setName('Deli', False)
                        elif (sName == 'Gadir' or sName == 'Qart-Gadir' or sName == 'Gades' or sName == 'Gadeira' or sName == 'Al-Qadiz' or sName == 'C&#225;diz' or sName == 'Cadix'):
                                city.setName('C&#225;dis', False)
                        elif (sName == 'Rome' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Roma', False)
                        #inca (spanish names)
                        elif sName == 'Quitu':
                                city.setName('Quito', False)
                        elif sName == 'Tucume':
                                city.setName('T&#250;cume', False)
                        elif sName == 'Chan-Chan':
                                city.setName('Chanchan', False) #Trujillo
                        elif sName == 'Pachacamaq':
                                city.setName('Pachacamac', False)
                        elif sName == 'Machu-Pikchu':
                                city.setName('Machu Picchu', False)
                        elif sName == 'Qusqu':
                                city.setName('Cuzco', False)
                        elif sName == 'Ariqipaya':
                                city.setName('Arequipa', False)
                        elif sName == 'Tiyawanaku':
                                city.setName('Tiahuanaco', False) #Tihuanaku? #Tiwanaku? #Puno?
                        elif sName == 'Caqonatambu':
                                city.setName('Limatambo', False)
                        elif sName == 'Coqimpu':
                                city.setName('Coquimbo', False)
                        elif sName == 'Ullantaytanpu':
                                city.setName('Ollantaytambo', False)
                        elif sName == 'Vitcos':
                                city.setName('Piura', False)
                        elif sName == 'Andahuailas':
                                city.setName('Andahuaylas', False)
                        elif sName == 'Acari':
                                city.setName('Atico', False)
                        elif sName == 'Lluli':
                                city.setName('Juli', False)
                        elif sName == 'Chuqiapu':
                                city.setName('Chuquiapo', False)
                        elif sName == 'Huanuqupampa':
                                city.setName('Huanucopampa', False)
                        elif sName == 'Tambuqcucha':
                                city.setName('Tamboccocha', False)
                        elif sName == 'Huaraz':
                                city.setName('Huaras', False)
                        elif sName == 'Cacsamalca':
                                city.setName('Caxamalca', False)
                        elif sName == 'Sauza':
                                city.setName('Sausa', False)
                        elif sName == 'Tampupuca':
                                city.setName('Tambocolorado', False)
                        elif sName == 'Huaqa':
                                city.setName('Huaca', False)
                        elif sName == 'Chuitu':
                                city.setName('Chuito', False)
                        elif sName == 'Cajamarca':
                                city.setName('Caiamarca', False)
                        elif sName == 'Lauricucha':
                                city.setName('Hu&#225;nuco', False)
                        elif sName == 'Tomebamba':
                                city.setName('Cuenca', False)
                        elif sName == 'Jauja':
                                city.setName('Sausa', False)
                        elif sName == 'Willkapampa':
                                city.setName('Vilcabamba', False)
                        elif sName == 'Wantar Chawin':
                                city.setName('Chav&#237;n de Hu&#225;ntar', False)
                        elif sName == 'Punu':
                                city.setName('Puno', False)	


                elif (iNewOwner == iInca):
                        pass
##                        if sName == 'Quito':
##                                city.setName('Quitu', False)
##                        elif sName == 'T&#250;cume':
##                                city.setName('Tucume', False)
##                        elif sName == 'Chanchan':
##                                city.setName('Chan-Chan', False)
##                        elif sName == 'Pachacamac':
##                                city.setName('Pachacamaq', False)
##                        elif sName == 'Machu Picchu':
##                                city.setName('Machu-Pikchu', False)
##                        elif sName == 'Cuzco':
##                                city.setName('Qusqu', False)
##                        elif sName == 'Arequipa':
##                                city.setName('Ariqipaya', False)
##                        elif sName == 'Tiahuanaco': #Tihuanaku?
##                                city.setName('Tiyawanaku', False)  #Tiwanaku?
##                        elif sName == 'Limatambo':
##                                city.setName('Caqonatambu', False)
##                        elif sName == 'Coquimbo':
##                                city.setName('Coqimpu', False)
##                        elif sName == 'Ollantaytambo':
##                                city.setName('Ullantaytanpu', False)
##                        elif sName == 'Piura':
##                                city.setName('Vitcos', False)
##                        elif sName == 'Andahuaylas':
##                                city.setName('Andahuailas', False)
##                        elif sName == 'Atico':
##                                city.setName('Acari', False)
##                        elif sName == 'Juli':
##                                city.setName('Lluli', False)
##                        elif sName == 'Chuquiapo':
##                                city.setName('Chuqiapu', False)
##                        elif sName == 'Huanucopampa':
##                                city.setName('Huanuqupampa', False)
##                        elif sName == 'Tamboccocha':
##                                city.setName('Tambuqcucha', False)
##                        elif sName == 'Huaraz':
##                                city.setName('Waras', False)
##                        elif sName == 'Caxamalca':
##                                city.setName('Cacsamalca', False)
##                        elif sName == 'Sausa':
##                                city.setName('Sauza', False)
##                        elif sName == 'Tambocolorado':
##                                city.setName('Tampupuca', False)
##                        elif sName == 'Huaca':
##                                city.setName('Huaqa', False)
##                        elif sName == 'Chuito':
##                                city.setName('Chuitu', False)
##                        elif sName == 'Cajamarca':
##                                city.setName('Kashamarka', False)
##                        elif sName == 'Hu&#225;nuco':
##                                city.setName('Lauricucha', False)
##                        elif sName == 'Cuenca':
##                                city.setName('Tomebamba', False)
##                        elif sName == 'Sausa':
##                                city.setName('Jauja', False)
##                        elif sName == 'Vilcabamba':
##                                city.setName('Willkapampa', False)
##                        elif sName == 'Chav&#237;n de Hu&#225;ntar':
##                                city.setName('Wantar Chawin', False)								
##                        elif sName == 'Puno':
##                                city.setName('Punu', False)	

                elif (iNewOwner == iMongolia): 
                        if (sName == 'Marakanda' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Samarkand', False)
                        elif (sName == 'Beijing' or sName == 'Pekin' or sName == 'Hokkin'):
                                city.setName('Khanbaliq', False)
                        elif (sName == 'Shash' or sName == 'Cheshih' or sName == 'Binkath'):
                                city.setName('Chach', False)
                        elif (sName == 'Shenyang' or sName == "Shin'you"):
                                city.setName('Mukden', False)
                        elif (sName == 'Tbilisi'):
                                city.setName('Tiflis', False)
                        elif (sName == 'Hailaer' or sName == 'Hairaru'):
                                city.setName('Hulun', False)
                        elif (sName == 'Chita'):
                                city.setName('Cyty', False)
                        elif (sName == 'Ulan-Udeh'):
                                city.setName('Ulaan-Ude', False)
                        elif (sName == "Astrakhan'"):
                                city.setName('Astrakhan', False)
                        elif (sName == "Kul'sary"):
                                city.setName('Kulsary', False)
                        elif (sName == "Karakorum"):
                                city.setName("Qara Qorum", False)
                        elif (sName == "Irkutsk"):
                                city.setName("Erkh&#252;&#252;", False)

                elif (iNewOwner == iTurkey): 
                        if (sName == 'Byzantion' or sName == 'Constantinopolis' or sName == 'Konstantinoupolis' or sName == 'Miklagard' or sName == 'Bizantiya' or sName == 'Qustantiniyah' or sName == 'Konstantinopel' or sName == "Konstantinopol'" or sName == "Car'grad"):
                                city.setName('Istanbul', False)
                                if (not gc.getPlayer(iTurkey).isHuman()):
                                        city.setHasRealBuilding((0), True) #palace
                                        apCityList = PyPlayer(iTurkey).getCityList()
                                        for pCity in apCityList:
                                                if (pCity.GetCy().getName() == "S&#246;g&#252;t"):
                                                        pCity.GetCy().setHasRealBuilding((0), False) #palace
                        elif sName == 'Nicomedia':
                                city.setName('Izmit', False)
                        elif (sName == 'Pergamon' or sName == 'Pergamum'):
                                city.setName('Bergama', False)
                        elif (sName == 'Trapezon' or sName == 'Trapezus' or sName == 'Tarabizun'):
                                city.setName('Trabzon', False)
                        elif (sName == 'Antiokheia Megale' or sName == 'Antiochia ad Orontem' or sName == 'Antakiyyah'):
                                city.setName('Antakya', False)
                        elif (sName == 'Ikonion' or sName == 'Iconium'):
                                city.setName('Konya', False)
                        elif (sName == 'Antiokeia tes Pisidias' or sName == 'Antiochia Pisidiae'):
                                city.setName('Aksehir', False)
                        elif (sName == 'Halikarnassos' or sName == 'Halikarnassus'):
                                city.setName('Bodrum', False)
                        elif (sName == 'Ephesos' or sName == 'Ephesus'):
                                city.setName('Efes', False)
                        elif sName == 'Nicaea':
                                city.setName('Iznik', False)
                        elif (sName == 'Samarkand' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Marakanda' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Samarqand', False)
                        elif (sName == 'Epidamnos' or sName == 'Dyrrachium' or sName == 'Duras' or sName == 'Drach' or sName == 'Durr&#235;s'):
                                city.setName('Dira&#231;', False)
                        elif sName == 'Sinope':
                                city.setName('Sinop', False)
                        elif sName == 'Hadrianopolis':
                                city.setName('Edirne', False)
                        elif sName == 'Edessa':
                                city.setName('Urfa', False)
                        elif (sName == 'Attaleia' or sName == 'Attalea'):
                                city.setName('Antalya', False)
                        elif sName == 'Al-Aqabah':
                                city.setName('Akabe', False)
                        elif (sName == 'Thessalonica' or sName == 'Thessaloniki'):
                                city.setName('Sel&#226;nik', False)
                        elif sName == 'Mosul':
                                city.setName('Musul', False)
                        elif sName == 'Halab':
                                city.setName('Halep', False)
                        elif (sName == 'Navarino' or sName == 'Neokastron'):
                                city.setName('Anavarin', False)
                        elif (sName == 'Al-Jazair' or sName == 'Alger'):
                                city.setName('Cezayir', False)
                        elif sName == 'Tunis':
                                city.setName('Tunus', False)
                        elif (sName == 'Al-Iskandariya' or sName == 'Alexandreia' or sName == 'Alexandria' or sName == 'Eskendereyya'):
                                city.setName('Iskenderiye', False)
                        elif (sName == 'Cairo' or sName == 'Memphis' or sName == 'Ineb Hedj' or sName == 'Al-Qahirah' or sName == 'El-Qahirah'):
                                city.setName('Kahire', False)
                        elif sName == 'Dimashq':
                                city.setName('Sam', False)
                        elif (sName == 'Makkah' or sName == 'Mecca'):
                                city.setName('Mekke', False)
                        elif sName == 'Madinah':
                                city.setName('Medine', False)
                        elif (sName == 'Jerusalem' or sName == 'Yerushalayim' or sName == 'Ierusalim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Urshalim' or sName == 'Hierusalem' or sName == 'Hierousalem' or sName == 'Urushalim' or sName == 'Al-Quds' or sName == 'Qods'):
                                city.setName('Kud&#252;s', False)
                        elif sName == 'Baghdad':
                                city.setName('Bagdat', False)
                        elif (sName == 'Singidunum' or sName == 'Singidun' or sName == 'Beograd'):
                                city.setName('Belgrad', False)
                        elif (sName == 'Athenae' or sName == 'Athenai' or sName == 'Athen' or sName == 'Athens' or sName == 'Atenas' or sName == 'Ath&#232;nes'):
                                city.setName('Atina', False)
                        elif sName == 'Naupactus':
                                city.setName('Inebahti', False)
                        elif (sName == 'Qart-Hadasht' or sName == 'Qartaj' or sName == 'Karkhedon' or sName == 'Carthago' or sName == 'Kartaca'):
                                city.setName('Kartaca', False)
                        elif (sName == 'Tyras' or sName == 'Moncastrum' or sName == 'Tiraspol' or sName == 'Wei&#223;enburg'):
                                city.setName('Akkerman', False)
                        elif (sName == 'Anqarah' or sName == 'Ankyra' or sName == 'Ancyra'):
                                city.setName('Angora', False)	
                        elif (sName == 'Chach' or sName == 'Shash' or sName == 'Cheshih' or sName == 'Binkath' or sName == 'Tashkent'):
                                city.setName('Toshkent', False)
                        elif (sName == 'Amisos' or sName == 'Amisus'):
                                city.setName('Samsun', False)
                        elif (sName == 'Milid' or sName == 'Malateia' or sName == 'Melitene'):
                                city.setName('Malatya', False)
                        elif (sName == 'Mazaka' or sName == 'Caesarea Mazaca' or sName == 'Kaisareia'):
                                city.setName('Kayseri', False)
                        elif (sName == 'Konstantia' or sName == 'Tomis' or sName == 'Konstanca' or sName == 'K&#246;stendsche'):
                                city.setName('Kustendje', False)
                        elif sName == 'Saratov':
                                city.setName('Saryk Atov', False)
                        elif (sName == 'Shushan' or sName == 'Shush' or sName == 'Seleukeia Susiana' or sName == 'Seleucia ad Eulaeum'):
                                city.setName('Susa', False)
                        elif sName == 'Parsa':
                                city.setName('Persepolis', False)
                        elif (sName == 'Alexandreia ad Issum' or sName == 'Al-Iskandarun' or sName == 'Alexandretta'):
                                city.setName('Iskenderun', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif (sName == 'Berenikis' or sName == 'Berenice' or sName == 'Hesperides' or sName == 'Bangazi' or sName == 'Benghazi'):
                                city.setName('Bingazi', False)
                        elif (sName == 'Oea' or sName == 'Regio Tripolitana' or sName == 'Tarabulus' or sName == 'Tripolis' or sName == 'Tripoli'):
                                city.setName('Trablus', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexico', False)
                        elif (sName == 'Niwt-Rst' or sName == 'Diospolis Megale' or sName == 'Diospolis Magna' or sName == 'Al-Uqsur' or sName == 'Luxor'):
                                city.setName('Luksor', False)
                        elif (sName == "Pi-Ramesses" or sName == 'Avaris'):
                                city.setName("Tell El-Dab'a", False)
                        elif sName == 'Tirana':
                                city.setName('Tiran', False)
                        elif (sName == 'Venedig' or sName == 'Venecia' or sName == 'Venetia' or sName == 'Venise' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Venice' or sName == 'Al-Bundukiyya' or sName == 'Veneza'):
                                city.setName('Venedik', False)
                        elif (sName == 'Zantar' or sName == 'Iadera'):
                                city.setName('Zadar', False)
                        elif (sName == 'Vienne' or sName == 'Wien' or sName == 'Vindobona' or sName == 'Vena'):
                                city.setName('Viyana', False) 
                        elif (sName == 'Sirmium' or sName == 'Sirmion' or sName == 'Syrmisch Mitrowitz' or sName == 'Sremska Mitrovica'):
                                city.setName('Dimitrof&#231;e', False)
                        elif (sName == "Al-Kuwait" or sName == "Kuwait City"):
                                city.setName('Kuveyt', False)
                        elif sName == "Shiraz":
                                city.setName('Siraz', False)
                        elif sName == "Al-Basrah":
                                city.setName('Basra', False)
                        elif (sName == "Ar-Riyad" or sName == "Riyadh"):
                                city.setName('Riyad', False)
                        elif sName == "An-Najaf":
                                city.setName('Necef', False)
                        elif sName == "'Amman":
                                city.setName('Amman', False)
                        elif sName == "Al-Ghardaqah":
                                city.setName('Hurgada', False)
                        elif sName == "Tubruq":
                                city.setName('Tobruk', False)
                        elif (sName == 'Budapest' or sName == 'Aquincum' or sName == 'Ak Ink'):
                                city.setName('Budin', False)
                        elif (sName == 'Napoca' or sName == 'Cluj-Napoca' or sName == 'Castrum Clus' or sName == 'Klausenburg'):
                                city.setName('Kalosvar', False)
                        elif sName == "Groznyj":
                                city.setName('Grozni', False)
                        elif (sName == 'Praga' or sName == 'Praha' or sName == 'Birag'):
                                city.setName('Prag', False)
                        elif sName == 'Safaqis':
                                city.setName('Safakes', False)
                        elif (sName == 'Tacape' or sName == 'Qabis' or sName == 'Gab&#232;s'):
                                city.setName('Gabes', False)
                        elif (sName == 'Khartoum' or sName == 'Al-Hartum'):
                                city.setName('Hartum', False)
                        elif (sName == 'Babil&#251;' or sName == 'Babel' or sName == 'Babylon' or sName == 'Babilon' or sName == 'Babirush' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babil', False)
                        elif (sName == 'Ninua' or sName == 'Nineve' or sName == 'Ninawa'):
                                city.setName('Ninova', False)
                        elif (sName == 'Tyrus' or sName == 'T&#253;ros' or sName == 'As-Sur'):
                                city.setName('Sur', False)
                        elif sName == 'Artaxata':
                                city.setName('Artashat', False)
                        elif (sName == 'Khalpe' or sName == 'Beroea' or sName == 'Halab'):
                                city.setName('Halep', False)
                        elif (sName == 'Kolachi' or sName == 'Debal' or sName == 'Barbarikon' or sName == 'Barbaricum' or sName == 'Karachi'):
                                city.setName('Mirat ul Memalik', False)
                        elif (sName == 'Tbilisi'):
                                city.setName('Tiflis', False)
                        elif (sName == 'Sofia'):
                                city.setName('Sofya', False)
                        elif (sName == 'B&#252;kres'):
                                city.setName('Bucuresti', False)	
                        elif (sName == 'Sin' or sName == 'Sena' or sName == 'Pelusium' or sName == 'Pelusion'):
                                city.setName('Tell el-Farama', False) #this is arabic
                        elif (sName == 'Rome' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Roma', False)
                        elif (sName == 'Buto' or sName == 'Per-Wadjet'):
                                city.setName('Kem Kasir', False)			
                        elif (sName == 'Baku'):
                                city.setName('Bak&#252;', False)
                        elif sName == 'Al-Ladhiqiyah':
                                city.setName("Lazkiye", False)
                        elif sName == 'Hattusas':
                                city.setName("Bogazk&#246;y", False)	
                        elif (sName == "Astrakhan'"):
                                city.setName('Astrakhan', False)
                        elif (sName == "Kul'sary"):
                                city.setName('Kulsary', False)
                        elif (sName == "Kazan'"):
                                city.setName('Qazan', False)
                        elif (sName == "Ufa"):
                                city.setName('Ufu', False)
						
                elif (iNewOwner == iAmerica): 
                        if (sName == 'Nieuw Amsterdam' or sName == "N'yu-York" or sName == 'Nyuu Yooku'):
                                city.setName('New York', False)
                        elif sName == 'San Agust&#237;n':
                                city.setName('St. Augustine', False)
                        elif sName == 'Charles Town':
                                city.setName('Charleston', False)
                        elif sName == 'Fort Caroline':
                                city.setName('Jacksonville', False)
                        elif (sName == 'Lac Knob'):
                                city.setName('Knob Lake', False)
                        elif (sName == 'Qu&#233;bec'):
                                city.setName('Quebec City', False)
                        elif (sName == 'Nueva Orleans' or sName == 'Nouvelle Orl&#233;ans' or sName == 'Nova Orle&#227;es'):
                                city.setName('New Orleans', False)
                        elif sName == 'Fort Goede Hoop':
                                city.setName('Hartford', False)
                        elif sName == 'Beverwyck':
                                city.setName('Albany', False)
                        elif sName == 'Fort Beversreede':
                                city.setName('Philadelphia', False)
                        elif sName == 'Wilmington':
                                city.setName('Nieuwer-Amstel', False)
                        elif (sName == 'La Petite Chute'):
                                city.setName('Little Chute', False)
                        elif (sName == 'Vinland' or sName == 'Anse-aux-M&#233;duses'):
                                city.setName('Anse aux Meadows', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexico City', False)
                        elif (sName == 'Londinium' or sName == 'Londres' or sName == 'Londen'):
                                city.setName('London', False)
                        elif (sName == 'Jekabforts'):
                                city.setName('Fort James', False)
                        #elif sName == "Krepost' Ross":
                        #        city.setName("Fort Ross", False)
                        elif (sName == 'Havanna' or sName == 'La Havane' or sName == 'La Habana' or sName == 'Gavana'):
                                city.setName('Havana', False)
                        elif sName == 'Fort Kristina':
                                city.setName('Wilmington', False)
                        elif (sName == 'Klein-Venedig'):
                                city.setName('Venezuela', False)
                        elif sName == 'Sankt Thomas':
                                city.setName('Saint Thomas', False)
                        elif sName == 'Fort D&#233;troit':
                                city.setName('Detroit', False)
                        elif sName == 'Novo-Arkhangelsk':
                                city.setName('Sitka', False)
                        elif sName == 'Fort Frontenac':
                                city.setName('Kingston', False)
                        elif (sName == 'Hierusalem' or sName == 'Yerushalayim' or sName == 'Ierusalim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Kud&#252;s' or sName == 'Urshalim' or sName == 'Hierousalem' or sName == 'Urushalim' or sName == 'Al-Quds' or sName == 'Qods'): 
                                city.setName('Jerusalem', False)
                        elif sName == 'Neu Braunfels':
                                city.setName('New Braunfels', False)
                        elif (sName == 'Fort Rouill&#233;' or sName == 'Fort Toronto'):
                                city.setName('Toronto', False)
                        elif (sName == 'Nouvelle-Ib&#233;rie' or sName == 'Nueva Iberia'):
                                city.setName('New Iberia', False)
                        elif (sName == 'Cabo Mesurado'):
                                city.setName('Monrovia', False)
                        elif (sName == 'Fort Rouge'):
                                city.setName('Winnipeg', False)
                        elif (sName == 'Santa F&#233;'):
                                city.setName('Santa Fe', False)
                        elif (sName == 'B&#226;ton Rouge'):
                                city.setName('Baton Rouge', False)
                        elif (sName == 'Guatemala'):
                                city.setName('Guatemala City', False)
                        elif (sName == 'Fort Rosalie'):
                                city.setName('Fort Panmure', False)
                        elif (sName == 'Al-Iskandariya' or sName == 'Alexandreia' or sName == 'Iskenderiye' or sName == 'Eskendereyya'):
                                city.setName('Alexandria', False)
                        elif (sName == 'Al-Hartum' or sName == 'Hartum'):
                                city.setName('Khartoum', False)
                        elif (sName == 'Al-Qahirah' or sName == 'Memphis' or sName == 'Ineb Hedj' or sName == 'Kahire' or sName == 'El-Qahirah'):
                                city.setName('Cairo', False)
                        elif (sName == 'Niwt-Rst' or sName == 'Diospolis Megale' or sName == 'Diospolis Magna' or sName == 'Luksor' or sName == 'Al-Uqsur'):
                                city.setName('Luxor', False)
                        elif sName == 'Al-Basrah':
                                city.setName("Basra", False)
                        elif (sName == "Riyad" or sName == "Ar-Riyad"):
                                city.setName('Riyadh', False)
                        elif sName == 'Bagdat':
                                city.setName('Baghdad', False)
                        elif (sName == "Kuveyt" or sName == "Al-Kuwait"):
                                city.setName('Kuwait City', False)
                        elif (sName == 'Mekke' or sName == 'Makkah'):
                                city.setName('Mecca', False)
                        elif sName == 'Masqat':
                                city.setName('Muscat', False)
                        elif (sName == 'Roodt Eylandt'):
                                city.setName('Rhode Island', False)
                        elif (sName == 'Nieuw Brunswyck'):
                                city.setName('New Brunswick', False)
                        elif (sName == 'Fort Duquesne'):
                                city.setName('Pittsburgh', False)
                        elif (sName == 'Renault'):
                                city.setName('Reno', False)
                        elif (sName == 'San-Francisko' or sName == 'Sanfuranshisuko'):
                                city.setName('San Francisco', False)
                        elif (sName == 'Vankuver' or sName == 'Bankuubaa'):
                                city.setName('Vancouver', False)
                        elif (sName == 'Siehtl' or sName == 'Shiatoru'):
                                city.setName('Seattle', False)
                        elif (sName == 'Rosu' or sName == 'Los-Andzheles'):
                                city.setName('Los Angeles', False)
                        elif (sName == 'Vashington' or sName == 'Washinton'):
                                city.setName('Washington', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexico' or sName == 'Mexiko-Stadt' or sName == 'Mexicopolis' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexico City', False)
                        elif (sName == "Elizavetinskaja Krepost'"):
                                city.setName('Fort Elizabeth', False)
                        elif (sName == "Voskresenskaja"):
                                city.setName('Seward', False)

                elif (iNewOwner == iCeltia and gc.getPlayer(0).isPlayable()): #late start condition 
                        if sName == 'Inverness':
                                city.setName('Inbhir Nis', False)
                        elif sName == 'Belfast':
                                city.setName('B&#233;al Feirste', False)
                        elif (sName == 'Dubh Linn' or sName == 'Dublin'):
                                city.setName('&#193;th Cliath', False)
                elif (iNewOwner == iCeltia and not gc.getPlayer(0).isPlayable()): #late start condition (Byzantium) 
                        if (sName == 'Jerusalem' or sName == 'Yerushalayim' or sName == 'Ierusalim' or sName == 'Aelia Capitolina' or sName == 'Aarru-Hetep' or sName == 'Kud&#252;s' or sName == 'Urshalim' or sName == 'Hierousalem' or sName == 'Urushalim' or sName == 'Al-Quds' or sName == 'Qods'): 
                                city.setName('Hierusalem', False)
                        elif (sName == 'Sin' or sName == 'Sena' or sName == 'Pelusion'):
                                city.setName('Pelusium', False)
                        elif (sName == 'Melpum' or sName == 'Mailand' or sName == 'Mil&#225;n' or sName == 'Milan'):
                                city.setName('Mediolanum', False)
                        elif (sName == 'Lutetia' or sName == 'Paris' or sName == 'Parijs' or sName == 'Par&#237;s'):
                                city.setName('Lutetia Parisiorum', False)
                        elif (sName == 'Burdeos' or sName == 'Bordeaux'):
                                city.setName('Burdigala', False)
                        elif (sName == 'Hippo' or sName == 'Annaba' or sName == 'B&#244;ne'):
                                city.setName('Hippo Regius', False)
                        elif (sName == 'Byzantion' or sName == 'Miklagard' or sName == 'Bizantiya' or sName == 'Konstantinoupolis' or sName == 'Qustantiniyah' or sName == 'Konstantinopel' or sName == "Konstantinopol'" or sName == "Car'grad"):
                                city.setName('Constantinopolis', False) 
                        elif (sName == 'Ziz' or sName == 'Panormos' or sName == 'Balharm' or sName == 'Palermo'):
                                city.setName('Panormus', False)
                        elif sName == 'Iol':
                                city.setName('Iol Caesarea', False)
                        elif sName == 'Lpqy':
                                city.setName('Leptis Magna', False)
                        elif sName == 'Lixos':
                                city.setName('Lixus', False)
                        elif (sName == 'Babil&#251;' or sName == 'Babel' or sName == 'Babil' or sName == 'Babilon' or sName == 'Babirush' or sName == 'Babili' or sName == 'Vavilon'):
                                city.setName('Babylon', False)
                        elif (sName == 'Shushan' or sName == 'Shush' or sName == 'Seleukeia Susiana' or sName == 'Seleucia ad Eulaeum'):
                                city.setName('Susa', False)
                        elif (sName == 'Sur' or sName == 'T&#253;ros' or sName == 'As-Sur'):
                                city.setName('Tyrus', False)
                        elif sName == 'Emporion':
                                city.setName('Emporiae', False)
                        elif sName == 'Odessos':
                                city.setName('Odessus', False)
                        elif sName == 'Naissos':
                                city.setName('Naissus', False)
                        elif (sName == 'Berenikis' or sName == 'Berenice' or sName == 'Bangazi' or sName == 'Bingazi'):
                                city.setName('Hesperides', False)
                        elif sName == 'Ikonion':
                                city.setName('Iconium', False)
                        elif sName == 'Ankyra':
                                city.setName('Ancyra', False)
                        elif sName == 'Antiokeia tes Pisidias':
                                city.setName('Antiochia Pisidiae', False)
                        elif (sName == 'Antiokheia Megale' or sName == 'Antakiyyah' or sName == 'Antakya'):
                                city.setName('Antiochia ad Orontem', False)
                        elif sName == 'Halikarnassos':
                                city.setName('Halikarnassus', False)
                        elif sName == 'Ephesos':
                                city.setName('Ephesus', False)
                        elif sName == 'Ilion':
                                city.setName('Ilium', False)
                        elif (sName == 'Al-Iskandariya' or sName == 'Alexandreia' or sName == 'Iskenderiye' or sName == 'Eskendereyya'):
                                city.setName('Alexandria', False)
                        elif sName == 'Tisfun':
                                city.setName('Ctesiphon', False)
                        elif (sName == 'Massalia' or sName == 'Marseille' or sName == 'Marsella' or sName == 'Marsiliya'):
                                city.setName('Massilia', False)
                        elif sName == 'Epidamnos':
                                city.setName('Dyrrachium', False)
                        elif (sName == 'Athenai' or sName == 'Atina' or sName == 'Athen' or sName == 'Athens' or sName == 'Atenas' or sName == 'Ath&#232;nes'):
                                city.setName('Athenae', False)
                        elif (sName == 'Sparte' or sName == 'Esparta'):
                                city.setName('Sparta', False)
                        elif sName == 'Korinthos':
                                city.setName('Corinthus', False)
                        elif sName == 'Delphoi':
                                city.setName('Delphi', False)
                        elif (sName == 'Lyon' or sName == 'Lugodunon'):
                                city.setName('Lugdunum', False)
                        elif sName == "Pi-Ramesses":
                                city.setName('Avaris', False)
                        elif sName == 'Djanet':
                                city.setName('Tanis', False)
                        elif sName == 'Attaleia':
                                city.setName('Attalea', False)
                        elif (sName == 'Anavarin' or sName == 'Neokastron'):
                                city.setName('Navarino', False)
                        elif (sName == 'Ljubljana' or sName == 'Laibach' or sName == 'Aemona Iulia'):
                                city.setName('Emona', False)
                        elif (sName == 'Karlsburg' or sName == 'Apulon' or sName == 'Balgrad'):
                                city.setName('Apulum', False)
                        elif (sName == 'Napoca' or sName == 'Cluj-Napoca' or sName == 'Klausenburg' or sName == 'Kalosvar'):
                                city.setName('Castrum Clus', False)
                        elif sName == 'Gordion':
                                city.setName('Gordium', False)
                        elif sName == 'Paraitonion':
                                city.setName('Paraetonium', False)
                        elif sName == 'Kyrene':
                                city.setName('Cyrene', False)
                        elif sName == 'Syrakousai':
                                city.setName('Syracusae', False)
                        elif (sName == 'Tyras' or sName == 'Tiraspol' or sName == 'Akkerman' or sName == 'Wei&#223;enburg'):
                                city.setName('Moncastrum', False)
                        elif (sName == 'Trapezon' or sName == 'Tarabizun' or sName == 'Trabzon'):
                                city.setName('Trapezus', False)
                        elif (sName == 'Rome' or sName == 'Rom' or sName == 'Rumiya' or sName == 'Daqin'):
                                city.setName('Roma', False)
                        elif sName == 'Amisos':
                                city.setName('Amisus', False)
                        elif (sName == 'Milid' or sName == 'Malateia' or sName == 'Malatya'):
                                city.setName('Melitene', False)
                        elif (sName == 'Mazaka' or sName == 'Kaisareia' or sName == 'Kayseri'):
                                city.setName('Caesarea Mazaca', False)
                        elif (sName == 'Aix-la-Chapelle' or sName == 'Aachen' or sName == 'Aken'):
                                city.setName('Aquisgranum', False)
                        elif (sName == 'Nijmegen' or sName == 'Nim&#232;gue'):
                                city.setName('Batavodurum', False)
                        elif (sName == 'Konstantia' or sName == 'Konstanca' or sName == 'K&#246;stendsche' or sName == 'Kustendje'):
                                city.setName('Tomis', False)
                        elif (sName == 'Wien' or sName == 'Vena' or sName == 'Vienne' or sName == 'Viyana'):
                                city.setName('Vindobona', False)
                        elif sName == 'Pise':
                                city.setName('Pisae', False)
                        elif (sName == 'Samarkand' or sName == 'Samarqand' or sName == 'Samarkant' or sName == 'Samarcande' or sName == 'Samarcanda' or sName == 'Afrasiyab'):
                                city.setName('Marakanda', False)
                        elif (sName == 'Mainz' or sName == 'Mogontiacum' or sName == 'Mayence'):
                                city.setName('Moguntiacum', False)
                        elif (sName == 'Damasia' or sName == 'Augsburg'):
                                city.setName('Augusta Vindelicorum', False)
                        elif (sName == 'Agley' or sName == 'Oglej' or sName == 'Aquil&#233;e'):
                                city.setName('Aquileia', False)
                        elif (sName == 'Pompeji' or sName == 'Pompeya' or sName == 'Pomp&#233;i'):
                                city.setName('Pompeii', False)
                        elif sName == 'Oea':
                                city.setName('Tripolis', False)
                        elif (sName == 'Alexandreia ad Issum' or sName == 'Al-Iskandarun' or sName == 'Iskenderun'):
                                city.setName('Alexandretta', False)
                        elif sName == 'Mykenai':
                                city.setName('Mycenae', False)
                        elif sName == 'Barbarikon':
                                city.setName('Barbaricum', False)
                        elif (sName == 'Tenochtitl&#225;n' or sName == 'Mexico City' or sName == 'Ciudad de M&#233;xico' or sName == 'Mexiko-Stadt' or sName == 'Mexico' or sName == 'Cidade do M&#233;xico' or sName == 'Mexico-stad' or sName == 'Mekhiko'):
                                city.setName('Mexicopolis', False)
                        elif (sName == 'Chersonesos' or sName == 'Khersones'):
                                city.setName('Chersonesus', False) 
                        elif sName == 'Tiran':
                                city.setName('Tirana', False)
                        elif (sName == 'Frankfurt' or sName == 'Francfort' or sName == 'Frankfort'):
                                city.setName('Bona Mansio', False)
                        elif (sName == 'Venedig' or sName == 'Venise' or sName == 'Venecia' or sName == 'Venice' or sName == 'Veneza' or sName == 'Veneti&#235;' or sName == 'Venecija' or sName == 'Al-Bundukiyya' or sName == 'Venedik'):
                                city.setName('Venetia', False)
                        elif (sName == 'Zantar' or sName == 'Zadar'):
                                city.setName('Iadera', False) 
                        elif (sName == 'Split' or sName == 'Aspalathos'):
                                city.setName('Spalatum', False)
                        elif (sName == 'Beograd' or sName == 'Singidun' or sName == 'Belgrad'):
                                city.setName('Singidunum', False)
                        elif (sName == 'Dimitrof&#231;e' or sName == 'Sirmion' or sName == 'Syrmisch Mitrowitz' or sName == 'Sremska Mitrovica'):
                                city.setName('Sirmium', False)
                        elif (sName == 'Arae' or sName == 'Ras Lanuf'):
                                city.setName('Arae Philaenorum', False)
                        elif (sName == 'Al-Uqaylah' or sName == 'Automala' or sName == 'El Agheila'):
                                city.setName('Anabucis', False)
                        elif (sName == 'Hannover' or sName == 'Hanovre'):
                                city.setName('Hannovera', False)
                        elif (sName == 'Gdansk' or sName == 'Danswijk' or sName == 'Danzig'):
                                city.setName('Gedanum', False)
                        elif (sName == 'K&#246;nigsberg' or sName == 'Kaliningrad'):
                                city.setName('Calininopolis', False)
                        elif (sName == 'Warschau' or sName == 'Varsovia'):
                                city.setName('Warszawa', False)
                        elif (sName == 'Tallinn' or sName == 'Tallin' or sName == 'Revalia'):
                                city.setName('Reval', False)
                        elif (sName == 'Helsinki' or sName == 'Helsingfors' or sName == "Khel'sinki"):
                                city.setName('Helsingia', False)
                        elif (sName == 'Dresde' or sName == 'Dresden'):
                                city.setName('Dresda', False)
                        elif (sName == 'Rostock'):
                                city.setName('Rostochium', False)
                        elif (sName == 'Krakau' or sName == 'Cracovia'):
                                city.setName('Krak&#243;w', False)


                if sName == 'Inbhir Nis' and iNewOwner != iCeltia:
                        city.setName('Inverness', False)
                if sName == 'D&#249;n &#200;ideann' and iNewOwner != iCeltia:
                        city.setName('Edinburgh', False)
                if (sName == 'Aquincum' or sName == 'Ak Ink') and iNewOwner != iRome and iNewOwner != iTurkey:
                        city.setName('Budapest', False)
                if (sName == 'Takao' or sName == 'Gaoxiong') and iNewOwner >= iNumPlayers:
                        city.setName('Kaohsiung', False)
                if sName == 'Momba&#231;a' and iNewOwner != iPortugal:
                        city.setName('Mombasa', False)
                if sName == 'Toranaro' and iNewOwner != iJapan and iNewOwner != iFrance:
                        city.setName('Tolanaro', False)
                if sName == 'Kerimane' and iNewOwner != iJapan:
                        city.setName('Quelimane', False)
                if sName == 'Sofara' and iNewOwner != iJapan:
                        city.setName('Sofala', False)



        def sovietNames(self):
                russianCityList = PyPlayer(iRussia).getCityList()
                for pCity in russianCityList:
                        city = pCity.GetCy()
                        if (city.getName() == 'Caricyn'):
                                city.setName('Stalingrad', False)
                        elif (city.getName() == 'Sankt-Peterburg'):
                                city.setName('Leningrad', False)
                        elif (city.getName() == "Tver'"):
                                city.setName('Kalinin', False)
                        elif (city.getName() == 'Ekaterinburg'):
                                city.setName('Sverdlovsk', False)
                        elif (city.getName() == 'Nizhnij Novgorod'):
                                city.setName('Gorki', False)
                        elif (city.getName() == 'Samara'):
                                city.setName('Kujbyshev', False)
                        elif (city.getName() == "Car'grad"):
                                city.setName("Konstantinopol'", False)
                        elif (city.getName() == 'Bobrujsk'):
                                city.setName('Stalinsk', False)
                        elif (city.getName() == 'Vjatka'):
                                city.setName('Kirov', False)
                        elif (city.getName() == 'Bavly'):
                                city.setName("Oktjabr'skij", False)
                        elif (city.getName() == 'Sumin'):
                                city.setName('Sumy', False)
                        elif (city.getName() == 'Sjangan'):
                                city.setName('Gon Kong', False)




        def onTechAcquired(self, iPlayer):
                era = gc.getPlayer(iPlayer).getCurrentEra()
                if ((iPlayer == iChina or iPlayer == iMongolia or iPlayer == iJapan) and era == con.iMedieval):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == "Chang'an"):
                                        city.setName("Xi'an", False)
                                        break
                if ((iPlayer == iIndia or iPlayer == iArabia or iPlayer == iTurkey) and era >= con.iRenaissance):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == 'Pataliputra'):
                                        city.setName("Patna", False)
                                        break
                if ((iPlayer == iChina or iPlayer == iMongolia or iPlayer == iJapan) and era == con.iRenaissance):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == "Haojing"):
                                        city.setName("Aomen", False)
                                        break
                if (iPlayer == iVikings and era == con.iRenaissance):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == 'Nidaros'):
                                        city.setName('Trondheim', False)
                                        break
                if (iPlayer == iJapan and era == con.iIndustrial):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == 'Edo'):
                                        city.setName('Toukyou', False)
                                        break    
                if ((iPlayer == iEngland or iPlayer == iSpain or iPlayer == iAmerica) and era == con.iIndustrial):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == 'Yax Mutal'):
                                        city.setName('Tikal', False)
                                        break    
                if (iPlayer == iRussia and era >= con.iRenaissance):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == 'Novokholmogory'):
                                        city.setName("Arkhangel'sk", False)
                                elif (city.getName() == 'Spas na Kholmu'):
                                        city.setName('Krasnyj Kholm', False)
                                        break
                if (iPlayer == iRussia and era >= con.iIndustrial):
                        if (gc.getPlayer(iPlayer).getCivics(3) == 18): #state prop
                                self.sovietNames()
                if ((iPlayer == iTurkey or iPlayer == iIndependent or iPlayer == iIndependent2 or iPlayer == iBarbarian) and era == con.iModern):
                        cityList = PyPlayer(iPlayer).getCityList()
                        for pCity in cityList:
                                city = pCity.GetCy()
                                if (city.getName() == 'Angora'):
                                        city.setName('Ankara', False)
                                        break
                                elif (city.getName() == 'Hanseong'):
                                        city.setName('Seoul', False)
                                        break

