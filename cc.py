from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
######single match####
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver')
# driver.get(r'https://m.cricbuzz.com/cricket-series/3337/india-tour-of-england-2021/matches')
# p = driver.find_elements_by_id("series-matches")
# p = driver.find_elements_by_class_name("ng-scope")
# p = driver.find_elements_by_xpath("//a[contains(@href,'live-cricket-scores/32058/eng-vs-ind-4th-test-india-tour-of-england-2021')]")
# for i in p:
#     print(i.text.strip())
# ###multi match list###
# driver.get(r'https://www.cricbuzz.com/cricket-team/india/2/results')
# d = driver.find_elements_by_id("series-matches")

# for f in d:
#     print(f.text.strip())

####cricket scorecard###
driver.get(r'https://www.cricbuzz.com/live-cricket-scorecard/32058/eng-vs-ind-4th-test-india-tour-of-england-2021')
y = driver.find_elements_by_id("innings_2")
y = driver.find_elements_by_class_name("ng-scope")
for r in y:
    print(r.text.strip())
driver.quit()