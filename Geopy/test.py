import geopy.geocoders as gp

locator = gp.Nominatim(user_agent="myGeocoder")
location = locator.geocode("Islamabad, Pakistan")
loc = str(location.latitude) + "," + str(location.longitude) + ",20km"
print(loc)
# print("Lat{}, Long{}".format(location.latitude, location.longitude))