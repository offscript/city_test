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
document = collection.find_one({"club_id": 11})
print(document)

#The spider itself, largely the same as man_city spider 

#After the spider we'll put the data in the database,
#However, we'll be adding to document, not creating an entirely new one. 

#A little test to see if it works before we eventually add to the Man City Document
#process = CrawlerProcess({})
#process.crawl(ManCitySpider)
#process.start()
#print(document)