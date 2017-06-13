#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def gps2address(gps):
	try:
		geolocator = Nominatim()
		location = geolocator.reverse(gps)
		return location.address.encode('utf-8')
	except GeocoderTimedOut:
		return gps2address(gps)

def address2gps(address):
	try:
		geolocator = Nominatim()
		location = geolocator.geocode(address)
		return (location.latitude, location.longitude)
	except GeocoderTimedOut:
		return address2gps(address)

def loadFile(path_name):
	with open(path_name) as f:
		content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content]
	return content

def saveResult(row):
	with open('data/result.txt','a') as myfile:
		myfile.write(row+'\n')

if __name__ == '__main__':
	source = 'address'
	if len(sys.argv) > 1:
		source = sys.argv[1]
	directory = 'data/'
	path_name = directory+source+'.txt'
	data_list = loadFile(path_name)
	for row in data_list:
		if source == 'address':
			saveResult(str(address2gps(row)))
		else:
			saveResult(gps2address(row))