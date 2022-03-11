import urllib.request, json, sys
from urllib.request import urlopen
<<<<<<< Updated upstream

=======
#from keys import *
>>>>>>> Stashed changes
#from twilio.rest import TwilioRestClient
#from api_keys import *
class weatherGet():
	"""docstring for weatherGet"""
	#need to call it with weatherGet(state, city.replace(' ', '%20')
	def __init__(self, state, city):
		self.state = None
		self.city = None
		self.j = None
		self.string = None
		self.location = None
		self.temperature = None
		self.weather = None
		self.feels = None
		self.last_update = None
		self.current_temp = None
		self.hours_48 = None
		self.hours_24 = None
		self.time_10AM = None
		self.time_1PM = None
		self.time_4PM = None
		self.time_7PM = None
		self.time_10PM = None
		self.getWeather(state, city)
		self.getHourWeather(state, city)
		self.returnWeather(state ,city)
		self.w_ground = ''

	
		#call with self.requestUrl(url) to get json data
	def requestUrl(self, url):
		response = urlopen(url)
		self.string = response.read().decode('utf-8')
		self.j = json.loads(self.string)

		#calls request url to retrieve and organize json data for general conditions resource
	def getWeather(self, state, city):
		self.requestUrl('http://api.wunderground.com/api/' + self.w_ground + '/conditions/q/{0}/{1}.json'.format(state, city))
		self.location = self.j['current_observation']['display_location']['full']
		self.temperature = self.j['current_observation']['temp_f']
		self.weather = self.j['current_observation']['weather']
		self.feels = self.j['current_observation']['feelslike_f']
		self.last_update = self.j['current_observation']['observation_time']

		#get hour to hour weather based of hourly resource
	def getHourWeather(self, state, city):
		self.requestUrl('http://api.wunderground.com/api/' + self.w_ground + '/hourly/q/{0}/{1}.json'.format(state, city))
		self.hours_48 = [f['temp']['english'] for f in self.j['hourly_forecast'] if f["FCTTIME"]['hour'] in ('10', '13', '16', '19', '22')]
		self.hours_24 = self.hours_48[:-1]
		self.time_10AM = self.hours_24[0]
		self.time_1PM = self.hours_24[1]
		self.time_4PM = self.hours_24[2]
		self.time_7PM = self.hours_24[3]
		self.time_10PM = self.hours_24[4]

		#prints weather report in simple readable form
	def returnWeather(self, state, city):
		self.getWeather(state, city)
		self.getHourWeather(state, city)
		#print(self.feels)
		self.current_temp = '```\nThe weather in {0} is {1} at {2}F degrees but feels like {3}F. \n 10AM....{4}F \n 1PM.....{5}F \n 4PM.....{6}F \n 7PM.....{7}F \n 10PM....{8}F \n {9}```'.format(self.location, self.weather, self.temperature, self.feels, self.time_10AM, self.time_1PM, self.time_4PM, self.time_7PM, self.time_10PM, self.last_update)
		#print('test1')

#weatherGet('Pennsylvania', 'State College'.replace(' ', '%20'))