from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class PoshFollowBot:

# Gets username/password from txt file in same directory.
# Parses information and splits by space
# Assigns values to login variable
	def user_login(self):
		userInfo = open('login.txt','r')
		self.login = userInfo.read().split(' ')
		
# Initializes chrome via Selenium Webdriver. Please enter your own path to chromedriver.exe.
# Selenium targets input field web elements for login and sends the values from user_login function.
# Finally, Selenium clicks the submit button via Xpath. I utlize ChroPath chrome plugin to find relateive Xpath.
	def login_to_poshmark(self):	
		url = "https://poshmark.com/login"
		driver = webdriver.Chrome('/')
		self.driver = driver
		driver.get(url)
		elem = driver.find_element_by_id('login_form_username_email')
		elem.send_keys(self.login[0])
		elem = driver.find_element_by_id('login_form_password')
		elem.send_keys(self.login[1])
		driver.find_element_by_xpath("//button[@class='btn blue btn-primary']").click()

# This function has you enter your search terms via terminal. It creates a list and separates values by space for search.
	def create_search_keywords(self):
		searchVal = input('What would you like to search for? Please separate multpile keywords with a space: ')
		self.searchlist= searchVal.split(" ")

# After getting the list of keywords, I initialize a for loop to go through each search term.
# Selenium directs the webbrowser to a url where the search value gets coded into the URL
# Because more followers populate the more you scroll down, selenium scrolls down 3 times to get more followers. This can be changed.
# After every scroll is a sleep timer for loading. The webpage then scrolls back to top.
# You get a print statement that tells you how many people are available for following.
	def follow_all_users(self):
		for keywords in self.searchlist:
			driver = self.driver
			driver.get('https://poshmark.com/search?query=' + keywords + '&type=people')
			for i in range(3):
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(5)
			driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
			time.sleep(5)
			users_follow_button = driver.find_elements_by_id('follow-user')
			user_count = len(users_follow_button)
			print("There are " + str(user_count) + " users to follow!")

# This part of the script starts clicking the follow button. It then subtracts one from total user count.
# After each click, a random number between 0 and 20 seconds determines how long the scripts sleeps between clicks.
# This is done to simulate a more human interaction.			
			for user in users_follow_button:
				ran_num = random.randrange(0,20)
				user.click()
				user_count = user_count - 1
				print(f"There are now {user_count} users left to click. Will click a new user in {ran_num} seconds.")				
				time.sleep(ran_num)
		print("You have followed all the users.")




p = PoshFollowBot()
p.user_login()
p.login_to_poshmark()
p.create_search_keywords()
p.follow_all_users()
