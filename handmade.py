import phonenumbers
import opencage
number = input('target : ')

from phonenumbers import geocoder
pp = phonenumbers.parse(number)
loc = geocoder.description_for_number(pp, "en")

from phonenumbers import carrier
sv = phonenumbers.parse(number)
print(carrier.name_for_number(sv, "en"))

from opencage.geocoder import OpenCageGeocode

key = ' '
geocoder = OpenCageGeocode(key)
qr = str(loc)
rs = geocoder.geocode(qr)
print(rs)
