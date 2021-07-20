
#============================================================================
# Weather Bot.                       
#                                                                  05/01/2021
#============================================================================
import json
import urllib2
import tweepy
import requests
from datetime import datetime
import random
import webbrowser
import time
import schedule 

temperature_phrases = False

following = True #Follow everyone following you.

retweet = False
search_rt = "Mallorca weather"
numberofTweets = 3 #Number of tweets you wish to interact with

favorite = False
search_f = "Mallorca weather"
numberOfTweets = 3 #Number of tweets you wish to interact with
 
#codes below are fake: enter details from your Twitter application
CONSUMER_KEY = 'iuCiPMTjb6sixlSVuO9CLwmwd'
CONSUMER_SECRET = '9JsveKvn9yOyQ0YVm9HK1JseEb72T3ecFIFVUfpuupvY7Znfrb'
ACCESS_KEY = '1345328204513501185-lgKjrdxLIHfPvidle8cLLj5AjG4nBF'
ACCESS_SECRET = 'KoS7siPvxeWO38UQlcCtohba9G8jLuQR28SXdKnrQM8Vt'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()
print (user.name)

w_phrases = ["It's beautiful, you could do some cruising today.","Clear as a bell.",
			"Beautiful day, isn't it?","We couldn't ask for a nicer day, could we?","What's the weather like in your city today?", 
			'What a beautiful day!', "We couldn't ask for nicer weather!", "The weather's lovely.", "It's a lovely day.", "Did you order this sunshine?", 
			"It's so nice out today, isn't it?", "The weather's nice today, right?"]

w_rain_phrases = ["Mother nature is on the war path.","Mother nature has lost her temper.","Your wind shield wipers will be on high.",
				"Rain falling in buckets!","Rain falling in sheets!","Atmospheric indigestion.",
				"It will be one of those nights to throw a few logs on the fire and enjoy indoor romance.","It's raining cats and dogs!",
				'Like to dance in the rain?', 'Rainy days are the best time to stay home and read a book.', "Don't forget your umbrella.",
				 "Did you get caught in the rain?", "A curtain of rain beat down from the heavens."]

w_thunderstorms_phrases = ["Mother nature is on the war path.","Mother nature has lost her temper.",'Afraid of thunderstorms?', 'Find lightning beautiful?']

w_fog_phrases = ["Be sure to turn on your headlights when driving through foggy areas.", "Did you have a hard time driving today?",
				 "Pea soup fog.", "It's so foggy you can hardly see your hand in front of your face."]

w_cold_phrases = ["Chilly willy!","It is so cold, polar bears aren't even going outside.","Protect the 3 P's: pets, plants and pipes!",
				"Don't forget your coat; it's cold outside.", "It's freezing outside!", "It's Artic out there!", "It's quite fresh, take a jumper."]

w_warm_phrases = ["On cool days like today, you should be fine with a light jacket."]

w_hot_phrases = ["Pineapple connection.","The three H's outside (hot, hazy and humid).","Like a sauna outside.","Drink plenty of non-alcoholic beverages!",
				"Air conditioner weather!","Try to stay cool weather.","Triple digit heat.","Hot enough to fry eggs on car tops.",
				"It's going to be a scorcher.","Sun screen weather!","Boiling.","Like an oven.","Roasting.","Baking.","Sweltering.","Blistering.",
				"It's boiling hot!", "It's pretty hot, isn't it?", "We're having a heatwave!", "It's positively tropical today.","Did you order this sunshine?"]

w_few_scattered_clouds_phrases = ["The high sunlit clouds drifted across a clear blue sky."]

#web=webbrowser.open("https://openweathermap.org")

now = datetime.now()
dt_string = now.strftime("%H:%M, %b/%d")
time_string = now.strftime("%H:%M")
print("date and time =", dt_string)
 
def getweather():
    """ call openweathermap api"""
    response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Palma de Mallorca&appid=b21cf5ed372fcb4407af676d627294c9&units=metric')
    mydata = response.read()
    return mydata
 
weather = getweather()
print(weather)
w = json.loads(weather)

if w['weather'][0]['description'] == 'light thunderstorm' or w['weather'][0]['description'] == 'thunderstorm' or w['weather'][0]['description'] == 'heavy thunderstorm' or w['weather'][0]['description'] == 'ragged thunderstorm':
    a=u'\U0001F329' #thunderstorm
    f= random.choice(w_thunderstorms_phrases)

if w['weather'][0]['description'] == 'thunderstorm with light rain' or w['weather'][0]['description'] == 'thunderstorm with rain' or w['weather'][0]['description'] == 'thunderstorm with heavy rain' or w['weather'][0]['description'] == 'thunderstorm with heavy drizzle' or w['weather'][0]['description'] == 'thunderstorm with light drizzle' or w['weather'][0]['description'] == 'thunderstorm with drizzle':
    a=u'\U000026C8' #thunderstorm with rain or drizzle
    f= random.choice(w_thunderstorms_phrases + w_rain_phrases)

if w['weather'][0]['description'] == 'light intensity drizzle' or w['weather'][0]['description'] == 'drizzle' or w['weather'][0]['description'] == 'heavy intensity drizzle' or w['weather'][0]['description'] == 'light intensity drizzle rain' or w['weather'][0]['description'] == 'drizzle rain' or w['weather'][0]['description'] == 'heavy intensity drizzle rain' or w['weather'][0]['description'] == 'shower rain and drizzle' or w['weather'][0]['description'] == 'heavy shower rain and drizzle' or w['weather'][0]['description'] == 'shower drizzle':
    a=u'\U0001F326' #drizzle
    f= ''

if w['weather'][0]['description'] == 'light intensity shower rain' or w['weather'][0]['description'] == 'shower rain' or w['weather'][0]['description'] == 'heavy intensity shower rain' or w['weather'][0]['description'] == 'ragged shower rain' or w['weather'][0]['description'] == 'light rain' or w['weather'][0]['description'] == 'moderate rain' or w['weather'][0]['description'] == 'heavy intensity rain' or w['weather'][0]['description'] == 'very heavy rain' or w['weather'][0]['description'] == 'extreme rain':
    a=u'\U0001F327' #rain
    f= random.choice(w_rain_phrases)   

if w['weather'][0]['description'] == 'freezing rain':
    a=u'\U00002744',u'\U0001F327' # freezing rain
    f= random.choice(w_rain_phrases + w_cold_phrases)

if w['weather'][0]['description'] == 'light snow' or w['weather'][0]['description'] == 'snow' or w['weather'][0]['description'] == 'heavy snow' or w['weather'][0]['description'] == 'sleet' or w['weather'][0]['description'] == 'light shower sleet' or w['weather'][0]['description'] == 'shower sleet' or w['weather'][0]['description'] == 'light shower snow' or w['weather'][0]['description'] == 'shower snow' or w['weather'][0]['description'] == 'heavy shower snow':
    a=u'\U0001F328' # snow
    f= random.choice(w_cold_phrases)

if w['weather'][0]['description'] == 'light rain and snow' or w['weather'][0]['description'] == 'rain and snow':
    a=u'\U0001F327',u'\U0001F328' # rain and snow
    f= random.choice(w_rain_phrases + w_cold_phrases)

if time_string < '08:00:00' and w['weather'][0]['description'] == 'clear sky':
    a=u'\U0001F319' #moon
    f= random.choice(w_phrases + w_warm_phrases)

if time_string >= '08:00:00' and time_string <= '18:00:00' and w['weather'][0]['description'] == 'clear sky':
    a=u'\U00002600' #sun
    f= random.choice(w_phrases + w_warm_phrases)

if time_string > '18:00:00' and w['weather'][0]['description'] == 'clear sky':
    a=u'\U0001F319' #moon
    f= random.choice(w_phrases + w_warm_phrases)

if w['weather'][0]['description'] == 'few clouds': 
    a=u'\U0001F324' # sun and little cloud 
    f= random.choice(w_phrases + w_few_scattered_clouds_phrases)

if w['weather'][0]['description'] == 'scattered clouds': 
    a=u'\U000026C5' # big sun and cloud 
    f= random.choice(w_phrases + w_few_scattered_clouds_phrases)

if w['weather'][0]['description'] == 'broken clouds': 
    a=u'\U0001F325' # little sun and cloud 
    f= ''

if w['weather'][0]['description'] == 'overcast clouds': 
    a=u'\U00002601' # cloud
    f= ''

if w['weather'][0]['description'] == 'sand' or w['weather'][0]['description'] == 'dust' or w['weather'][0]['description'] == 'dust whirls': 
    a=u'\U0000231B' # sand 
    f= ''

if w['weather'][0]['description'] == 'mist' or w['weather'][0]['description'] == 'smoke' or w['weather'][0]['description'] == 'fog' or w['weather'][0]['description'] == 'haze': 
    a=u'\U0001F32B' # mist  
    f= random.choice(w_fog_phrases)

if w['weather'][0]['description'] == 'volcanic ash': 
    a=u'\U0001F30B' # volcano 
    f= ''

if w['weather'][0]['description'] == 'tornado': 
    a=u'\U0001F32A' # tornado 
    f= ''

if w['weather'][0]['description'] == 'squalls': 
    a=u'\U0001F32C' # wind  
    f= ''

if w['main']['feels_like'] >= 29:
	b=u'\U0001F525' # fire
	g= random.choice(w_hot_phrases)
    
if w['main']['feels_like'] >= 25 and w['main']['feels_like'] < 29:
	b=u'\U0001F321' # termometer
	g= random.choice(w_hot_phrases)

if w['main']['feels_like'] >= 18 and w['main']['feels_like'] < 25:
	b=u'\U0001F60A' # smiling face
	g= random.choice(w_warm_phrases)

if w['main']['feels_like'] >= 7 and w['main']['feels_like'] < 18:
    b=u'\U0001F633' # flushed face
    g= random.choice(w_cold_phrases)

if w['main']['feels_like'] < 7:
	b=u'\U000026C4' # snowman
	g= random.choice(w_cold_phrases)

c=u'\U0001F32C' # wind

d=u'\U0001F550' # pressure

e=u'\U0001F32B' # humidity

if temperature_phrases == True:
    f=g

wind=w['wind']['speed']*3.6

mylist = [dt_string,' - ','We have',w['weather'][0]['description'], a,'with a temperature of',
       str(w['main']['temp']),u"\u00b0",'C, but feels like',str(w['main']['feels_like']),u"\u00b0",'C',b,'.','\n',f,'\n',
       '\nWind speed',c,':',str(wind),'km/h.','\n', 'Pressure',d,':',
       str(w['main']['pressure']),'hPa.','\n','Humidity',e,':',str(w['main']['humidity']),'%.\n','\n#Mallorca #Baleares #weather #openweather']

#mylist = [dt_string,' - ','We have',w['weather'][0]['description'], a,'with a temperature of',
 #      str(w['main']['temp']),'degrees C, but feels like',str(w['main']['feels_like']),'degrees C',b,'.',
  #     '\nWind speed',c,':',str(w['wind']['speed']),'m/s. Pressure',d,':',
   #    str(w['main']['pressure']),'hPa. Humidity',e,':',str(w['main']['humidity']),'%.\n',f,'\n #Mallorca #Baleares #Aemet #weather #openweather']
    
#Follow everyone following you.
if following == True:
	for follower in tweepy.Cursor(api.followers).items():
		follower.follow()
		print ("Followed everyone that is following " + user.name)

#Retweet a Tweet based on keywords.
if retweet == True:
	for tweet in tweepy.Cursor(api.search, search_rt).items(numberofTweets):
		try:
			tweet.retweet()
			print('Retweeted the tweet')
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			break

#Favorite a Tweet based on keywords.
if favorite == True:
	for tweet in tweepy.Cursor(api.search, search_f).items(numberOfTweets):
		try:
			tweet.favorite()
			print('Favorite the tweet')
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			break

#for status in tweepy.Cursor(api.user_timeline).items():
 #   try:
  #      api.destroy_status(status.id)
   # except:
    #    pass

def job():
	tweet = " ".join(mylist)
	twet=api.update_status(tweet)
	return twet

schedule.every(15).minutes.do(job)
#while True:
#    try: # Add try ... except block to handle exceptions so that you can keep the program running.
#        api.update_status(tweet)
#    except tweepy.TweepError as e:
#            print(e.reason)
#    except StopIteration:
#            break
while True: 
    	schedule.run_pending()
#sleep(1800) #Cada 30min = 1800s, se actualiza. Lo hara indefinidamente, hasta que no lo canceles.
#______________________________________________________________________________
# To do.

#-Anyadir la hora actual al ppio en plan: 11.13pm, Jan5 - We have...
#-Iconos: tanto de la descripcion (scattered clours..), como de la temperatura real 
#(poner icono de un termometro con diferentes colores), humedad, presion y 
#velocidad del viento (estos pueden ser fijos).
#-Anyadir hastags
#-Anyadir un link a OpenWeather.
#-Anyadir una frase como: it's raining cats and dogs! (ver:https://www.fluentu.com/blog/english/talk-about-weather-in-english/, https://www.eslbuzz.com/speaking-about-the-weather-in-english-2/)
#Precipitation will stay in the liquid form but frosty conditions will be the rule tonight as the wind begins to pick up and temperatures fall to just above freezing. It will be one of those nights to throw a few logs on the fire and enjoy indoor romance.

#-Poner un loop de: si se repite el tweet, no actualizar el estado, pero que lo 
# siga haciendo hasta que no se repita. Este loop dentro de 
#otro mas grande que no pare en 6h.


#Hacer para mas sitios de mallorca, y loopear para todos.
# Poner un bot con la temperatura en toda las baleares.
#______________________________________________________________________________
# To run a bot.

# In your directory of the bot, activate python and this file.

# You can stop the bot using Ctrl-C