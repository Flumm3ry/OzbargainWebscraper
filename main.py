from scraper import Scraper

scraper = Scraper("https://www.ozbargain.com.au/")

print(scraper.count())
scraper.print_table()
