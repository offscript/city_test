import scrapy
import pymongo
from pymongo import MongoClient

class QuotesSpider(scrapy.Spider): 
	name = "quotes" #name of the spider
	client = MongoClient()
	db = client.spider_test_db
	collection = db.quotes_collection
	start_urls = [
		'http://quotes.toscrape.com/page/1',
		'http://quotes.toscrape.com/page/2',
	]

	#the parse function takes a url and a callback to be executed when the request
	#is fulfilled.
	#I think the % page thing shows how to do the naming convention, yeah it does.
	#NOt sure what the -2 on split is though
	def parse(self, response):
		#client = MongoClient()
		#db = client.spider_test_db
		#collection = db.quotes_collection
		for quote in response.css('div.quote'):
			a_quote = {
				'text': quote.css('span.text::text').extract_first(),
				'author': quote.css('small.author::text').extract_first(),
				'tags': quote.css('div.tags a.tag::text').extract(),
			}
			self.collection.insert_one(a_quote)
			yield {
				'text': quote.css('span.text::text').extract_first(),
				'author': quote.css('small.author::text').extract_first(),
				'tags': quote.css('div.tags a.tag::text').extract(),
			}