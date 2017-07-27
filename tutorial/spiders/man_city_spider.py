import scrapy
import time
import pymongo

from pymongo import MongoClient
from selenium import webdriver

class ManCitySpider(scrapy.Spider):
	name = "cityspider"
	#the mongodb collection we're going to write to, in this case a test database
	client = MongoClient()
	db = client.d3_test_db
	collection = db.club_collection
	#open web driver/window
	driver = webdriver.Chrome()
	#temporary test data for this particular spider. Includes club name, 
	#season, id_number for the document
	club = "Manchester City"
	season = 2016
	id_number = 11
	start_urls = [
		'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=54', #2016-17 season as of 7/20
		'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=42', #2015-16 season as of 7/26
		'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=27', #2014-15 season as of 7/26
		'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=22', #2013-14 season as of 7/26
		'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=21', #2012-13 season as of 7/26
	]


	def parse(self, response):
		#Start up web driver, sleep for 2.5 seconds to let the page load
		self.driver.get(response.url)
		time.sleep(2.5)
		#Get the season in which these stats are from
		season = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/section/div[1]/div[2]')
		#Get all of the stats
		elements = self.driver.find_elements_by_class_name('allStatContainer')
		# Set up Python dictionary to send to the MongoDB, fill with results from selenium/stats scraped above
		club_data = {
			'club': self.club,
			'season': season.text,
			'stats': {
				'wins': elements[1].text,
				'losses': elements[2].text,
				'goals': elements[6].text,
				'goals_per_match': elements[7].text,
				'shots': elements[8].text,
				'shots_on_target': elements[9].text,
				'shot_accuracy': elements[10].text,
				'penalties_scored': elements[11].text,
				'big_chances_created': elements[12].text,
				'hit_woodwork': elements[13].text,
			},
		}
		#check to see if club data is correct
		print(club_data)
		#Adds the data to the MongoDB collection specified above
		self.collection.insert_one(club_data)
		#needed for the spider to work, I think.
		for profile in response.css('span.allStatContainer.statgoals'):
			yield {
				'goals': profile.css('span.allStatContainer.statgoals::text').extract(), #_first().strip(),
			}