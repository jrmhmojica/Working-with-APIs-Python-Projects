#IMPORT MODULES
import requests
from plyer import notification
import time


try:
	while(True):
		#CALLING THE API
		url = "https://api.chucknorris.io/jokes/random"
		response = requests.get(url)

		#GETTING A RANDOM JOKE & TURNING IT INTO A NOTIFICATION
		joke_data = response.json()
		notification.notify(title = "Here's a Chuck Norris joke for you.",
							message = joke_data['value'],
							timeout = 15)
		time.sleep(60 * 60 * 2) #notifies every 2 hours

except:
	notification.notify(title = "Chuck does not lose his internet connection, but you do.",
						message = "Check your internet connection. There was an error.",
						timeout = 7)