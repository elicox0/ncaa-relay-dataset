import re
import sys
import requests
from bs4 import BeautifulSoup as bs

def get_tags(url, href_expr=None):
    content = requests.get(url).content
    parser = bs(content, features='html.parser')
    if href_expr:
        pass

    print(parser.find_all('li'))#, {'href':re.compile(r'')}))


if __name__ == "__main__":
    urls = [
    "https://flashresults.ncaa.com/Indoor/2022/010-1_compiled.htm",
    "https://www.tfrrs.org/archives.html",
    ]
    event_dict = {
        "100m"   : "rowMen6",
        "200m"   : "rowMen7",
        "400m"   : "rowMen11",
        "800m"   : "rowMen12",
        "1500m"  : "rowMen13",
        "5000m"  : "rowMen21",
        "10,000m": "rowMen22"
    }
    get_tags(urls[0])

