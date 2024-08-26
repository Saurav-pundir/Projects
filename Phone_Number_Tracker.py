import phonenumbers
from myphone import numbers
from phonenumbers import timezone , geocoder , carrier
from opencage importOpenCageGeocode
number = input("Enter your number with +:")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car =carrier.name_for_number(phone , "en")
reg = geocoder.description_for_valid_number(phone , "en")
key = "8aa0b2b7327a42fab13c52762d320805"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
print (results)
print(number)
print(phone)
print(time)
print(car)
print(reg)
