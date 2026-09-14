#slovarji

slovar = {"ključ" : "vrednost",
        "ključ2" : "vrednost2"}
print(slovar)
#dostop
print(slovar["ključ2"])

#raznoliki slovar
razno =  {"število" : 6,
          "ime" : "Luka",
          "seznam" : [1,2,3,4],
          "slovar" : {"firma" : "Dacia", "moč": "120kw"}}
print(razno["stevilo"] + 10)
print(max(razno["seznam"]))
print(razno["slovar"])
print(razno["slovar"]["firma"])
print(razno["slovar"]["moč"])

#Open Meto API
import requests
base_url = "https://api.open-meteo.com/v1/forecast?latitude=44.5384&longitude=18.6671&daily=rain_sum&forecast_days=1"

call = requests.get(base_url).json()

print(call["daily"])["rain_sum"][0]
