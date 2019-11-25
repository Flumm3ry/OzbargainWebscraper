from scraper import Scraper

url = 'https://www.ozbargain.com.au/'
scraper = Scraper(url)


def test_count():
    assert scraper.count() > 0


def test_all_cells_populated():
    for row in scraper.table:
        assert row.title  # title
        assert row.content  # content
