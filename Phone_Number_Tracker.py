import phonenumbers
from phonenumbers import timezone , geocoder , carrier
from opencage.geocoder import OpenCageGeocode
import folium

number = input("Enter your number with +:")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car =carrier.name_for_number(phone , "en")
reg = geocoder.description_for_valid_number(phone , "en")
loc = geocoder.description_for_number(phone , "en")
key = "8aa0b2b7327a42fab13c52762d320805"
geocoder = OpenCageGeocode(key)
query = str(loc)
result = geocoder.geocode(query)
lati = result[0]['geometry']['lat']
long = result[0]['geometry']['lng']

print(number)
print(phone)
print(time)
print(car)
print(reg)
print("Coordinates of ", car, lati,long)
