# from selenium import webdriver
# import unittest

# class PageTest(unittest.TestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()
# 	#def tearDown(self):
# 		#self.browser.quit()
# 	def test_browser_title(self):
# 		self.browser.get('http://localhost:8000')
# 		self.assertIn('Vote Vision',self.browser.title)
# 		#self.fail('Finish the test!')
# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')

from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time


class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(30)
		
	def test_start_list_and_retrieve(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Vote Vision - Feedback', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Feedback Form', headerText)

		GuestName = self.browser.find_element_by_id('UserName')
		self.assertEqual(GuestName.get_attribute('placeholder'),'Name: (Optional)')
		GuestName.send_keys('Oliva Escorial')
		time.sleep(1)

		GuestEmail = self.browser.find_element_by_id('UserEmail')
		self.assertEqual(GuestEmail.get_attribute('placeholder'),'Email Address:')
		GuestEmail.send_keys('olivaescorial3@gmail.com')
		time.sleep(0.5)

		UserConcerns = self.browser.find_element_by_id('UserConcerns')
		self.assertEqual(UserConcerns.get_attribute('placeholder'),'Select your site-related concerns you want to address')
		selectUserConcerns = Select(UserConcerns)
		selectUserConcerns.select_by_visible_text('Other concerns about the website')
		time.sleep(0.5)

		GuestMessage = self.browser.find_element_by_id('UserMessage')
		self.assertEqual(GuestMessage.get_attribute('placeholder'),'Go ahead, we are listening...')
		GuestMessage.send_keys('Helpful Website!')
		time.sleep(0.5)
      		
		submit = self.browser.find_element_by_id('submit')
		submit.click()
		time.sleep(0.5)
		

		# inpName = self.browser.find_element_by_id('userName')
		# self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
		# inpName.click()
		# inpName.send_keys('liba')
		# buttonsubmit=self.browser.find_element_by_id('submit')
		# buttonsubmit.click()
		# time.sleep(1)
		
		# inputbox = self.browser.find_element_by_id('idNewEntry')
		# self.assertEqual(inputbox.get_attribute('placeholder')), 'Persons name you have'
		# inputbox.send_keys('Mickey Mouse')
		# inputbox.send_keys(Keys.ENTER)

		# time.sleep(1)
		table = self.browser.find_element_by_id('registryTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Oliva Escorial, olivaescorial3@gmail.com, Other concerns about the website, Helpful Website!', [row.text for row in rows])


	# def checking_if_in_table_list(self,row_test):
	# 	table = self.browser.find_element_by_id('table')
	# 	rows = table.find_element_by_tag_name('td')
		#self.assertIn(row_text,[rows.text for row in rows])


#-------		
	# if __name__ == '__main__':
	# 	unittest.main(warnings='ignore')

	def test_start_list_and_retrieve_2(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Vote Vision - Feedback', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Feedback Form', headerText)


		GuestName = self.browser.find_element_by_id('UserName')
		self.assertEqual(GuestName.get_attribute('placeholder'),'Name: (Optional)')
		GuestName.send_keys('Dimple Escorial')
		time.sleep(1)

		GuestEmail = self.browser.find_element_by_id('UserEmail')
		self.assertEqual(GuestEmail.get_attribute('placeholder'),'Email Address:')
		GuestEmail.send_keys('dimple@gmail.com')
		time.sleep(0.5)

		UserConcerns = self.browser.find_element_by_id('UserConcerns')
		self.assertEqual(UserConcerns.get_attribute('placeholder'),'Select your site-related concerns you want to address')
		selectUserConcerns = Select(UserConcerns)
		selectUserConcerns.select_by_visible_text('Other concerns about the website')
		time.sleep(0.5)

		GuestMessage = self.browser.find_element_by_id('UserMessage')
		self.assertEqual(GuestMessage.get_attribute('placeholder'),'Go ahead, we are listening...')
		GuestMessage.send_keys('Thank you! :)')
		time.sleep(0.5)
      		
		submit = self.browser.find_element_by_id('submit')
		submit.click()
		time.sleep(0.5)
		
		self.browser.get(self.live_server_url)
		self.assertIn('Vote Vision - Feedback', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Feedback Form', headerText)

		GuestName = self.browser.find_element_by_id('UserName')
		self.assertEqual(GuestName.get_attribute('placeholder'),'Name: (Optional)')
		GuestName.send_keys('Biloy Escorial')
		time.sleep(1)

		GuestEmail = self.browser.find_element_by_id('UserEmail')
		self.assertEqual(GuestEmail.get_attribute('placeholder'),'Email Address:')
		GuestEmail.send_keys('biloy@gmail.com')
		time.sleep(0.5)

		UserConcerns = self.browser.find_element_by_id('UserConcerns')
		self.assertEqual(UserConcerns.get_attribute('placeholder'),'Select your site-related concerns you want to address')
		selectUserConcerns = Select(UserConcerns)
		selectUserConcerns.select_by_visible_text('Other concerns about the website')
		time.sleep(0.5)

		GuestMessage = self.browser.find_element_by_id('UserMessage')
		self.assertEqual(GuestMessage.get_attribute('placeholder'),'Go ahead, we are listening...')
		GuestMessage.send_keys('Informative Website!')
		time.sleep(0.5)
      		
		submit = self.browser.find_element_by_id('submit')
		submit.click()
		time.sleep(0.5)
		
		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Dimple Escorial, dimple@gmail.com, Other concerns about the website, Thank you! :)', [row.text for row in row_data])
		self.assertIn('2: Biloy Escorial, biloy@gmam, Other concerns about the website, Informative Website!', [row.text for row in row_data])

