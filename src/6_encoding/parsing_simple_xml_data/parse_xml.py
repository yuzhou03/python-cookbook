from urllib.request import urlopen
from xml.etree.ElementTree import parse
import logging

# 设置日志记录
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_rss_feed(url):
    try:
        # Download the RSS feed and parse it
        with urlopen(url) as u:
            doc = parse(u)

        # Extract and output tags of interest
        for item in doc.iterfind("channel/item"):
            title = item.findtext("title")
            date = item.findtext("pubDate")
            link = item.findtext("link")

            print(title)
            print(date)
            print(link)
            print()
    except Exception as e:
        logging.error(f"An error occurred while parsing the RSS feed: {e}")


if __name__ == "__main__":
    url = "http://planet.python.org/rss20.xml"
    parse_rss_feed(url)
