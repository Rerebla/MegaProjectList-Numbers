from geopy.geocoders import Nominatim
from geopy.distance import great_circle
geolocator = Nominatim(user_agent='my_application')
input1 = input("First city: ")
input2 = input("Second city:  ")
unit = input(
    "Which measurement of lenght would you want? [0]Kilometers, [1]Miles")
location1 = geolocator.geocode(input1)
location2 = geolocator.geocode(input2)
lat1 = location1.raw['lat']
lon1 = location1.raw['lon']
coord1 = (lat1, lon1)
lat2 = location2.raw['lat']
lon2 = location2.raw['lon']
coord2 = (lat2, lon2)
distance = great_circle(coord1, coord2)
if unit == "0":
    print(distance)
elif unit == "1":
    print(distance.miles)
else:
    print("Not existing unit.")
