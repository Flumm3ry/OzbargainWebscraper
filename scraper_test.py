from scraper import Scraper
from bs4 import BeautifulSoup

url = 'https://www.ozbargain.com.au/'
scraper = Scraper(url)


def test_count():
    assert scraper.count() > 0


def test_does_not_expired():
    for node in scraper.nodes:
        assert str(node).find("expired") == -1


def test_all_cells_populated():
    for row in scraper.table:
        assert row[0]  # title
        assert row[1]  # content


def test_not_html_in_content():
    for row in scraper.table:
        for cell in row:
            assert not bool(BeautifulSoup(cell, 'html.parser').find())
