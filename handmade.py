import phonenumbers
import opencage
number = input('target : ')
import pprint

from phonenumbers import geocoder
pp = phonenumbers.parse(number)
loc = geocoder.description_for_number(pp, "en")

from phonenumbers import carrier
sv = phonenumbers.parse(number)
print(carrier.name_for_number(sv, "en"))

from opencage.geocoder import OpenCageGeocode
key = 'c6456d5bbfa841d5b3f0f65e7608cff2'
geocoder = OpenCageGeocode(key)
qr = str(loc)
rs = geocoder.geocode(qr)
pprint.pprint(rs)
