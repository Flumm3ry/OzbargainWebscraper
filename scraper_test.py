from scraper import Scraper

url = 'https://www.ozbargain.com.au/'


def test_count():
    scraper = Scraper(url)
    assert scraper.count() > 0


def test_does_not_expired():
    scraper = Scraper(url)
    for node in scraper.nodes:
        assert str(node).find("expired") == -1
