# standard python libraries
import os
from datetime import datetime

# third-party libraries
import googlemaps
from dotenv import load_dotenv

load_dotenv()

gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_API_KEY", None))

# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print("GEOCODE")
# print(geocode_result)

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# print("\nREVERSE GEOCODE")
# print(reverse_geocode_result)

# Request directions via public transit
# print("\nDIRECTIONS")
now = datetime.now()
origin = "865 Rue de la Frégate, Sainte-Catherine, QC J5C 1Y5, Canada"
destination = "AlayaCare, Montreal, Quebec, Canada"
directions_result = gmaps.directions(
    origin, destination, mode="transit", departure_time=now)
print(directions_result)

origins = ["865 Rue de la Frégate, Sainte-Catherine, QC J5C 1Y5, Canada"]
destinations = ["AlayaCare, Montreal, Canada"]

# matrix = gmaps.distance_matrix(origins, destinations)
# print(matrix)
