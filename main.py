from scraper import Scraper

scraper = Scraper("https://www.ozbargain.com.au/")

print (scraper.count())
print (scraper.nodes[0])
