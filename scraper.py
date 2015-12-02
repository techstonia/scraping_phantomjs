import platform
from bs4 import BeautifulSoup
from selenium import webdriver

# PhantomJS files have different extensions
# under different operating systems
if platform.system() == 'Windows':
    PHANTOMJS_PATH = './phantomjs.exe'
else:
    PHANTOMJS_PATH = './phantomjs'


# here we'll use pseudo browser PhantomJS,
# but browser can be replaced with browser = webdriver.FireFox(),
# which is good for debugging.
browser = webdriver.PhantomJS(PHANTOMJS_PATH)
browser.get('http://www.scoreboard.com/en/tennis/atp-singles/us-open-2015/results/')

# let's parse our html
soup = BeautifulSoup(browser.page_source, "html.parser")
# get all the games
games = soup.find_all('tr', {'class': 'stage-finished'})

# and print out the html for first game
print(games[0].prettify())