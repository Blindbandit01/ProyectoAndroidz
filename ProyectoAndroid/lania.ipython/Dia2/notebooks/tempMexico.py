import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/0def10027afaebb7/geolookup/conditions/forecast/q/Mexico/Mexico.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_c']
mensaje = "La temperatura actual en %s es: %s C" % (location, temp_f)
print mensaje
f.close()