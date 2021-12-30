# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# inherit TestCase Class and create a new test class
class AAIC(unittest.TestCase):

	# initialization of webdriver
	def setUp(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")
		self.driver = webdriver.Chrome(options=chrome_options) #Firefox()
		

	# Test case method. It should always start with test_
	def test_search_in_appliedaiconsulting(self):
		
		# get driver
		driver = self.driver
		driver.maximize_window()
		
		# get appliedaiconsulting.com using selenium
		driver.get("https://appliedaiconsulting.com/")
		
		# assertion to confirm if web page has Cloud and DevOps keyword in it
		self.assertIn("Digital Engineering | Cloud Native Development | Cloud and DevOps", driver.title)
		#driver.get_screenshot_as_file("ss.jpg")
		#driver.get_screenshot_as_file("report/ss.jpg")
		driver.save_screenshot("ss1.png")
		driver.save_screenshot("report/ss1.png")
		
		#driver.find_element_by_id("hs-eu-confirmation-button").click()
		#time.sleep(1)
		#driver.save_screenshot("report/ss2.png")
		
		driver.find_element_by_id("impliedsubmit").click()
		time.sleep(1)
		driver.save_screenshot("ss2.png")
		driver.save_screenshot("report/ss2.png")

	# cleanup method called after every test performed
	def tearDown(self):
		self.driver.close()

# execute the script
if __name__ == "__main__":
	unittest.main()
