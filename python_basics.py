# TEHTÄVÄ_1

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

# TEHTÄVÄ_21: Palautusarvot / return, input, int, float

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