import scrapy
import time
import pymongo

from scrapy.crawler import CrawlerProcess
from pymongo import MongoClient
from selenium import webdriver

#Pymongo initialization
client = MongoClient()
db = client.d3_test_db
collection = db.club_collection
#Information for ManCity MongoDB Document
club = "Manchester City"
id_number = 11

club_data = {
	'club_name': club,
	'club_id': id_number,
	'primary_color': '#6caee0',
	'secondary_color': '#fff'
}

class ManCitySpider(scrapy.Spider):
	name = "cityspider"
	#the mongodb collection we're going to write to, in this case a test database
	#open web driver/window
	driver = webdriver.Chrome()

	def start_requests(self):
		urls = [
	        'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=54', #2016-17 season as of 7/20
			'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=42', #2015-16 season as of 7/26
			'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=27', #2014-15 season as of 7/26
			'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=22', #2013-14 season as of 7/26
			'https://www.premierleague.com/clubs/11/Manchester-City/stats?se=21', #2012-13 season as of 7/26
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		#Start up web driver, sleep for 2.5 seconds to let the page load
		self.driver.get(response.url)
		time.sleep(2.5)
		#Get the season in which these stats are from
		season = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/section/div[1]/div[2]')
		#Get all of the stats
		elements = self.driver.find_elements_by_class_name('allStatContainer')
		# Set up Python dictionary to send to the MongoDB, fill with results from selenium/stats scraped above
		club_data[season.text] = {
			'season': season.text,
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
		}
		#check to see if club data is correct
		print(club_data[season.text])
		#needed for the spider to work, I think.
		print(name)
		for profile in response.css('span.allStatContainer.statgoals'):
			yield {
				'goals': profile.css('span.allStatContainer.statgoals::text').extract(), #_first().strip(),
			}

process = CrawlerProcess({})
process.crawl(ManCitySpider)
process.start()
print(club_data)
#Adds the data to the MongoDB collection specified above
collection.insert_one(club_data)