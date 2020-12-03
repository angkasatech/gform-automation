import os

from selenium import webdriver

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))  # Optional argument, if not specified will search path.
driver.get('https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22CHsNNIyH2Ue%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A24%7D');