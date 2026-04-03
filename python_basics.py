# TEHTÄVÄ_1
"""
luku = int(input('Anna numero'))
print (luku + 10)

#TEHTÄVÄ_2: Kassa-apulainen

Määrä = int(input('Montako pullaa te haluatte?'))
Hinta = int(input('Mikä on pullan hintaa?'))
Summa = (Määrä*Hinta)
print('Yhteensä', Summa, 'euroa')

#TEHTÄVÄ_3: Hyllytys

määrä = int(input('Paljonko pullien kokonaismäärä?'))
laatikko = 3
Summa = määrä // laatikko
yli = määrä % laatikko
print('Yhteensä laatikoita', Summa, 'Yhteensä yli', yli)

#TEHTÄVÄ_4 Parillinen ja pariton

luku = int(input("Anna numero:"))
tulos = luku % 2
print(tulos)

luku = int(input("Anna numero: "))

if luku % 2 == 0:
	print("Parillinen!")
else:
	print("Pariton!")

# TEHTÄVÄ_5: if, else

oikea_salasana = "python123"
syöte = input()

if syöte == oikea_salasana:
	print ('Pääsy sallittu')
else: print('Väärä salasana')

# TEHTÄVÄ_6: elif

t = int(input('Montako astetta on ulkona?'))

if t > 25:
	print ('Helle! Ota aurinkorasvaa')
elif t > 0: 
	print ('Normisää. Nauti ulkoilusta')
else: print ('Kylmää! Pue pipo')  

# TEHTÄVÄ_7: Maksuautomaatti

raha = 10
hinta = int(input('Paljonko tuote maksaa?'))

# Logiikka
if hinta > raha:
	print('Rahat eivät riitä!')
elif hinta == raha:
	print('Kiitos, ei vaihtorahaa.')
else: 
	vaihtoraha = raha -hinta
	print('Vaihtorahaksi',vaihtoraha, 'euroa')

# TEHTÄVÄ_8: Silmukat / Loops

oikea_salasana = "python123"
syöte = input()

if syöte == oikea_salasana:
	print ('Pääsy sallittu')
else: print('Väärä salasana')

kerrat = 0

while syöte != oikea_salasana:
	syöte = input("Anna salasana: ")
	if syöte != oikea_salasana:
		kerrat = kerrat + 1
		print("Väärin! Yritä uudelleen.")
		
print("Pääsy sallittu! Yrityksiä", kerrat)

# TEHTÄVÄ_9: Ostoslista

ostokset = ['leipä', 'maito', 'juusto']
ostokset.append("karkkia")
print(ostokset)

# TEHTÄVÄ_10: For 

ostokset = ["leipä", "maito", "juusto", "karkkia"]

for tuote in ostokset:
	print("Muista ostaa:", tuote)

# TEHTÄVÄ_11:

ostokset = ["leipä", "maito", "juusto", "karkkia"]

if "kahvi" in ostokset:
	print("Kahvi on jo listalla!")
else:
	print("Hups! Kahvi puuttuu. Lisätään se.")
	ostokset.append("kahvi")
	
print("Uusi lista:", ostokset)

# TEHTÄVÄ_12: Lasketaan ruokatarvikkeet / len

ostokset = ["leipä", "maito", "juusto", "karkkia", "kahvi"]
määrä = len(ostokset)
	
print("Listassa on tällä hetkellä", määrä, 'kpl')

# TEHTÄVÄ_13: Poisto listasta / .remove

ostokset = ["leipä", "maito", "juusto", "karkkia", "kahvi"]
ostokset.remove("leipä")
print(len(ostokset))

# TEHTÄVÄ_14: Lajittelu / sort

ostokset = ["leipä", "maito", "juusto", "karkkia", "kahvi"]
ostokset.sort()
print(ostokset)

# TEHTÄVÄ_15: Lukujen summa / sum

hinnat = [10, 5, 2, 8]
yhteensä = sum(hinnat)
print("Yhteensä:", yhteensä, "euroa")

# TEHTÄVÄ_16: Keskiarvo / average

arvosanat = [5, 4, 5, 3, 4]
summa = sum(arvosanat)
määrä = len(arvosanat)
keskiarvo = summa / määrä
print("Keskiarvo on:", keskiarvo)

# TEHTÄVÄ_17: Sanakirjat

opiskelija = {
	"nimi": "Nadja",
	"ikä": 35,
	"koulu": "Metropolia",
	"kaupunki": "Kerava"
}

print("Nimi:", opiskelija["nimi"])
print("Koulu:", opiskelija["koulu"])
print ("Ikä:", opiskelija["ikä"])
print ("Kaupunki:", opiskelija["kaupunki"])

# TEHTÄVÄ_18: Muokkaus,keys ja del-toiminnot

opiskelija = {
	"nimi": "Nadja",
	"ikä": 35,
	"koulu": "Metropolia",
	"kaupunki": "Kerava",
}

opiskelija["ikä"] = 36
opiskelija["kaupunki"] = "Helsinki"

print("Nimi:", opiskelija["nimi"])
print("Uusi ikä:", opiskelija["ikä"])
print("Uusi kaupunki:", opiskelija["kaupunki"])
print("Mitä tietoja meillä on:", opiskelija.keys())

# Poistetaan "koulu"-avain ja sen arvo sanakirjasta
del opiskelija["koulu"]

# Tulostetaan sanakirja poiston jälkeen tarkistusta varten
print("Sanakirja poiston jälkeen:", opiskelija)

# Jos yrität tulostaa poistetun avaimen, Python antaa KeyError-virheen:
# print(opiskelija["koulu"]) <-- Tämä aiheuttaisi virheen!

# TEHTÄVÄ_19: Rekisteri, lista sanakirjoista

kayttajat = [
	{"nimi": "Nadja", "rooli": "admin"},
	{"nimi": "Alex", "rooli": "opiskelija"},
	{"nimi": "Sara", "rooli": "rehtori"}
]

for kayttaja in kayttajat:
	print("Tervetuloa,", kayttaja["nimi"], "! Sinun rooli on:", kayttaja["rooli"])

# TEHTÄVÄ_20: Funktio def

def tervehdi(nimi):
	print("Moi,", nimi + "!")
	print("Tervetuloa koodaamaan.")
	
# Nyt kutsutaan funktiota eri nimillä:
tervehdi("Nadja")
tervehdi("Alex")
tervehdi("Sara")

# TEHTÄVÄ_21: Palautusarvot / return, input, int(1,2,3), float(1.5,9.99)

def laske_ale(hinta):
	ale_hinta = hinta * 0.8
	return ale_hinta

# Käytetään funktiota:
tuote1 = laske_ale(10)
tuote2 = laske_ale(50)

print("Alennusmyynti! 100€ tuote maksaa nyt:", tuote1, "€")
print("50€ tuote maksaa nyt:", tuote2, "€")

def laske_hinta(alkuperainen):
	# 50% (Puoleen hintaan!)
	return alkuperainen * 0.5

# Kysytään hintaa:
kayttajan_hinta = float(input("Mikä on tuotteen hinta? "))

# Kutsutaan funktiota:
tulos = laske_hinta(kayttajan_hinta)

print("Alennuksessa hinta on vain:", tulos, "euroa!")

# TEHTÄVÄ_22: Virheiden hallinta / try, except
try:
	luku = int(input("Anna kokonaisluku: "))
	print("Hienoa! Syötit luvun:", luku)
except:
	print("Hups! Tuo ei ollut numero. Kirjoita vain numeroita!")
	
print("Ohjelma jatkuu tästä, vaikka tuli virhe.")

# TEHTÄVÄ_23: try, except, else (Полная логика)

try:
	ikä = int(input("Kuinka vanha olet? "))
except:
	print("Virhe: Anna ikä numerona!")
else:
	# Tämä suoritetaan VAIN jos int(input) onnistui
	if ikä >= 18:
		print("Olet täysi-ikäinen.")
	else:
		print("Olet alaikäinen.")
		
print("Kiitos tiedosta!")

# TEHTÄVÄ_24: Tiedostojen käsittely / with open, "w", \n

nimi = "Nadja"
paikka = "Kerava"

# "w" tarkoittaa 'write' (kirjoita). Se luo uuden tiedoston.
with open("tervehdys.txt", "w", encoding="utf-8") as tiedosto:
	tiedosto.write("Moi! Nimeni on " + nimi + "\n")
	tiedosto.write("Asun paikassa " + paikka)
	
print("Tiedosto on luotu onnistuneesti!")

# TEHTÄVÄ_25: Tiedoston lukeminen "r"

# "r" tarkoittaa 'read' (lue). Se avaa olemassa olevan tiedoston.
try:
	with open("tervehdys.txt", "r", encoding="utf-8") as tiedosto:
		sisältö = tiedosto.read()
		print("Tiedoston sisältö:")
		print("------------------")
		print(sisältö)
except FileNotFoundError:
	print("Hups! Tiedostoa ei löytynyt.")

# TEHTÄVÄ_26: Tiedoston täydentäminen "a"

merkintä = input("Miten päiväsi meni? ")

# "a" tarkoittaa 'append'. Se lisää tekstin tiedoston loppuun.
with open("paivakirja.txt", "a", encoding="utf-8") as f:
	f.write(merkintä + "\n")
	
print("Merkintä tallennettu päiväkirjaan!")

# TEHTÄVÄ_27: Classes & Objects

class Auto:
	# Luokan rakentaja (Constructor), joka alustaa olion tiedot
	def __init__(self, merkki, malli, vuosi):
		self.merkki = merkki  # Auton merkki (esim. Toyota)
		self.malli = malli    # Auton malli (esim. Corolla)
		self.vuosi = vuosi    # Valmistusvuosi
		
	# Metodi, joka tulostaa auton tiedot
	def nayta_tiedot(self):
		print(f"Auto: {self.merkki} {self.malli}, Vuosi: {self.vuosi}")
		
# Luodaan kaksi eri auto-oliota
auto1 = Auto("Toyota", "Corolla", 2022)
auto2 = Auto("Tesla", "Model 3", 2023)

# Käytetään olion metodia
auto1.nayta_tiedot()
auto2.nayta_tiedot()

# TEHTÄVÄ_28: Decorators

def my_decorator(func):
	def wrapper():
		print("--- Ennen funktion suoritusta ---")
		func()
		print("--- Funktion suorituksen jälkeen ---")
	return wrapper

@my_decorator
def say_hello():
	print("Hello World!!")

say_hello()

# TEHTÄVÄ_29: Decorators with arguments

def logger_decorator(func):
	# *args and **kwargs allow the wrapper to accept any data
	# *args ja **kwargs sallivat wrapperin ottaa vastaan mitä tahansa tietoa
	def wrapper(*args, **kwargs):
		print("--- Calling function: {func.__name__} ---")
		print("--- Kutsutaan funktiota: {func.__name__} ---")
		
		# Execute the original function with its arguments
		# Suoritetaan alkuperäinen funktio sen argumenteilla
		result = func(*args, **kwargs)
		
		print("--- Finished ---")
		print("--- Valmis ---")
		return result
	return wrapper

@logger_decorator
def greet_user(name):
	print("Hello, {name}!")
	
# Now we can call it with a parameter
# Nyt voimme kutsua sitä parametrilla
greet_user("Nadja")

# TEHTÄVÄ_30: List Comprehensions

# Original list of numbers / Alkuperäinen lukulista
numbers = [1, 2, 3, 4, 5, 6]

# 1. Create a list of squares (Power of 2)
# 1. Luodaan lista neliöistä (Potenssiin 2)
# Standard way:
# squares = []
# for x in numbers:
#     squares.append(x**2)

# List comprehension way (The pro way):
# Listanmuodostin (Ammattilaisten tapa):
squares = [x**2 for x in numbers]

# 2. Create a list of even numbers only
# 2. Luodaan lista vain parillisista luvuista
evens = [x for x in numbers if x % 2 == 0]

print("Original:", numbers)
print("Squares:", squares)
print("Evens only:", evens)

# TEHTÄVÄ_31: Importing Modules

import random  # Library for random numbers / Kirjasto satunnaisluvuille
import math    # Library for math operations / Kirjasto matemaattisille operaatioille

# 1. Get a random number between 1 and 100
# 1. Arvotaan luku väliltä 1-100
random_number = random.randint(1, 100)

# 2. Use Pi from math library
# 2. Käytetään Pii-vakiota math-kirjastosta
circle_area = math.pi * (5**2) # Area of circle with radius 5 / Ympyrän pinta-ala säteellä 5

print(f"Random number: {random_number}")
print(f"Circle area: {circle_area:.2f}") # Rounding to 2 decimals / Pyöristys 2 desimaaliin

# TEHTÄVÄ_32: String Formatting (Merkkijonojen muotoilu)

# Kirjoita koodi tähän (Write your code here)
age = 25
print("Olen {} vuotta vanha.".format(age))

# F-Strings

name = "Nadja"
city = "Kerava"
score = 10 / 3

# Basic formatting / Perusmuotoilu
print(f"User: {name}, Location: {city}")
# Käyttäjä: {name}, Sijainti: {city}

# Math inside f-string / Matematiikkaa f-stringin sisällä
print(f"Next year I will be {25 + 1} years old.")
# Ensi vuonna olen {25 + 1} vuotta vanha.

# Formatting numbers (Decimals) / Lukujen muotoilu (Desimaalit)
# .2f means 2 decimal places / .2f tarkoittaa kahta desimaalia
print(f"Your final score is: {score:.1f}")
# Lopullinen pistemääräsi on: {score:.2f}

# TEHTÄVÄ_32: F-Strings

# Kirjoita koodi tähän (Write your code here)
name = "Nadja"
city = "Kerava"
result = 10 / 3

print(f"Name: {name}, City: {city}, Result: {result:.1f}")

# TEHTÄVÄ_33: String alignment

name1 = "Nadja"
name2 = "AI"

# :<10 means left aligned, 10 characters wide
# :<10 tarkoittaa vasemmalle kohdistettua, 10 merkkiä leveä
print(f"|{name1:<10}|") 

# :>10 means right aligned
# :>10 tarkoittaa oikealle kohdistettua
print(f"|{name2:>10}|")

# :^10 means centered
# :^10 tarkoittaa keskitettyä
print(f"|{name1:^10}|")

# TEHTÄVÄ_34: Simple Table / Yksinkertainen taulukko
header_name = "Nimi"
header_sum = "Euro"

print(f"{header_name:<10} | {header_sum:>10}") # Header / Otsikko
print("-" * 23)                                # Separator / Erotin

# Data rows / Tietorivit
print(f"{'Nadja':<10} | {150.50:>10.2f}")
print(f"{'Matti':<10} | {25.00:>10.2f}")
print(f"{'Pekka':<10} | {1200.75:>10.2f}")

# TEHTÄVÄ_35: Harjoitukset sep/end

print("Python", "on", "kivaa", sep='')
print("Pääjohtaja Urho Mikkonen. ", end="Villahousut\n")

label = "Hinta: "
price = 100 
symbol = "€"
print(label, price, symbol, sep='')

# TEHTÄVÄ_36: 

day = "04"
month = "04"
year = "2026"
print(day,month,year, sep=".", end=" Helsinki")

# TEHTÄVÄ_37:

item1 = "Maito"
item2 = "Leipä"
item3 = "Voi"
print(item1, item2, item3, sep=", ", end=".")

# TEHTÄVÄ_38: repr

data = "Nimi:\tNadja"
print(data)
print(repr(data))

# TEHTÄVÄ_39: round

tulos = 10 / 3
pyöre_tulos = tulos
print (round(pyöre_tulos, 3))

# TEHTÄVÄ_40: round

hinta = 19.99
pyöre_hinta = (round(hinta))
print (pyöre_hinta)