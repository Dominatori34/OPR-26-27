"""
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
"""

#vaja
import requests
base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m"

call = requests.get(base_url).json()
print(call["current"]["temperature_2m"])

base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
call = requests.get(base_url).json()
print(call["hourly"]["temperature_2m"])

base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min"
call = requests.get(base_url).json()
print(max(call["daily"]["temperature_2m_max"]))
print(min(call["daily"]["temperature_2m_min"]))

base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min"
call = requests.get(base_url).json()
print(max(call["daily"]["temperature_2m_max"]) - min(call["daily"]["temperature_2m_min"]))




