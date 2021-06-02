from Bs4 import BeautifulSoup
from requests import get
url = "https://www.wrh.noaa.gov/mesowest/timeseries.php?sid=SFOC1&num=168&wfo=mtr"
soup = BeautifulSoup(url, 'html.parser')