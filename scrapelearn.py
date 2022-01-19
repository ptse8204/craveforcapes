import pandas as pd
# from natsort import natsorted # No idea what it is yet
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# from statsmodels.stats.proportion import proportion_confint as ci # No idea what it is yet

print('Opening a browser window...')
driver = webdriver.Firefox()
